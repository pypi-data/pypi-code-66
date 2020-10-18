# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
import os
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

from azureml._base_sdk_common.cli_wrapper._common import get_cli_specific_output, get_workspace_or_default
from azureml._base_sdk_common.common import CLICommandOutput
from azure.ml.component._loggerfactory import _PUBLIC_API, track
from azureml.exceptions import UserErrorException

from azure.ml.component._restclients.exceptions import ComponentAlreadyExistsError
from azure.ml.component._api._api import ComponentAPI

from .transformers import component_definition_to_detail_dict, component_definition_to_summary_dict, \
    component_definition_to_validation_result_dict


def _get_python_executable_of_command(command):
    """Return the version and python executable of the specific command."""
    content = subprocess.run(
        command + ['-c', "import sys;print('Python %s\\n%s' % (sys.version, sys.executable))"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=(os.name == 'nt')
    )
    return content.stdout.decode().strip()


def _get_available_python(possible_python):
    """Get an available python in user environment."""
    use_shell = os.name == 'nt'
    for py_cmd in possible_python:
        ret = subprocess.run(py_cmd + ['--version'], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=use_shell)
        if ret.returncode != 0:
            continue
        # In Python<=3.6, the version is printed in stderr;
        # in Python>=3.7, the version is printed in stdout.
        result = ret.stdout.decode() or ret.stderr.decode()
        if not result.startswith('Python 3'):
            continue
        try:
            minor_version = int(result.split('.')[1])
        except:
            continue
        # Python >= 3.5 is OK.
        if minor_version >= 5:
            return py_cmd


def _get_logger():
    """Get logger for command handler. Used when handler is called directly from CliCommand instead of decorator."""
    try:
        from knack.log import get_logger
        return get_logger(_get_logger.__module__)
    except ImportError:
        return logging.getLogger(_get_logger.__module__)


def _get_cli_args(*args, **kwargs):
    """Generate command line args from function args."""
    args = list(args)
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, list):
                # Converting list types args {'arg_name': [val1, val2]} to ['--arg_name', val1, val2].
                args += ['--' + k] + [str(item) for item in v]
            else:
                args += ['--' + k, str(v)]
    return args


def _run_with_subprocess(entry_module, args, use_shell=os.name == 'nt'):
    """Run entry_module related commands with subprocess.

    :param entry_module: entry module path
    :param args: arguments to run the module
    :param use_shell: If az is running in windows, use shell=True to avoid using python
    of CLI since we need python of user env. Need to investigate why this happens and find a better way.
    :return:
    """
    command = ['python']
    args = ['-m', entry_module] + args
    try:
        return _run_command_in_subprocess(command, args, use_shell)
    except ImportError:
        # For ImportError, we directly raise.
        raise
    except BaseException:
        # For other kinds of errors, it may be caused by python environment problems.
        # We try detecting an available python and use the python to run the command.
        possible_python_commands = [['python'], ['python3'], ['py', '-3']]
        available_python = _get_available_python(possible_python_commands)
        if available_python == command:
            raise
        elif available_python is None:
            msg = "No available python environment is found in user environment, please install python>=3.5 and " + \
                  "install azure-ml-component in your environment before using this command."
            raise RuntimeError(msg)
        else:
            return _run_command_in_subprocess(available_python, args, use_shell)


def _run_command_in_subprocess(command, args, use_shell):
    """Run command in subprocess."""
    content = subprocess.run(
        command + args,
        stderr=subprocess.PIPE, stdout=sys.stderr,
        shell=use_shell, env=os.environ,
    )
    stderr = content.stderr.decode()
    if content.returncode == 0:
        if stderr:
            sys.stderr.write(stderr)
        return {}
    else:
        exception = stderr.strip('\r\n').split('\n')[-1]
        if "No module named 'azureml" in exception:
            # This case is caused by import problems, we hint user to install the package.
            python_executable = _get_python_executable_of_command(command=command)
            from azure.ml.component.dsl._version import VERSION
            msg = "Please install azure-ml-component==%s before using this command." % VERSION
            msg += "\nYour python command: %s" % (' '.join(command))
            if python_executable:
                msg += "\nYour python executable: %s" % python_executable
            raise ImportError(msg)
        else:
            # Otherwise we store error message to tmp file and guide user to read it.
            tmp_file = tempfile.NamedTemporaryFile(suffix='.log', delete=False)
            try:
                tmp_file.write(content.stderr)
            finally:
                tmp_file.close()
            raise RuntimeError(
                'Error: {} happens when executing {}, detailed error messages are here: {}'.format(
                    exception, command + args, tmp_file.name))


def _run_step_run_debugger(args):
    """Run step run debugger related commands with subprocess since it requires dataprep to download dataset.
    It would be easier for user to install it in their own environment."""
    entry_module = 'azure.ml.component.debug._step_run_debugger'
    _run_with_subprocess(entry_module, args)


def _run_pipeline_project(args):
    """Run module project related commands with subprocess since az uses a separated python environment,
    while we need to use user's environment to build his project to avoid dependency issues.
    """
    entry_module = 'azure.ml.component.dsl._pipeline_project'
    _run_with_subprocess(entry_module, args)


def _get_component_api_instance(workspace, logger):
    """Get an instance to call component APIs.

    :param workspace: workspace
    :return: azure.ml.component._api.ComponentAPI
    """
    return ComponentAPI(workspace, logger=logger, from_cli=True)


def _register_component(workspace_name, resource_group_name, subscription_id, spec_file, package_zip, set_as_default,
                        amlignore_file, fail_if_exists, version, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __register_component(workspace=workspace, spec_file=spec_file, package_zip=package_zip,
                                set_as_default=set_as_default, amlignore_file=amlignore_file,
                                fail_if_exists=fail_if_exists, version=version, logger=logger)


@track(activity_name="CLI_Component_register", activity_type=_PUBLIC_API)
def __register_component(workspace, spec_file, package_zip, set_as_default, amlignore_file, fail_if_exists,
                         version, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _register(
        workspace, spec_file, package_zip, set_as_default, amlignore_file, fail_if_exists, version, logger)


@track(activity_name="CLI_Module_register", activity_type=_PUBLIC_API)
def _register_module(
        workspace, spec_file, package_zip, set_as_default, amlignore_file, fail_if_exists, version, logger):
    return _register(
        workspace, spec_file, package_zip, set_as_default, amlignore_file, fail_if_exists, version, logger)


def _register(workspace, spec_file, package_zip, set_as_default, amlignore_file, fail_if_exists, version, logger):
    # If user passed a module project via spec_file, batch register it
    # NOTE: We assumes all modules inside .moduleporj can be built in same environment
    from azure.ml.component.dsl._pipeline_project import PipelineProject
    if spec_file is not None and PipelineProject.is_project(Path(spec_file)):
        unsupported_args = ['package_zip', 'set_as_default', 'amlignore_file', 'fail_if_exists']
        for arg_name, val in locals().items():
            if arg_name in unsupported_args and val:
                raise UserErrorException(f'{arg_name} is not supported for batch register.')
        # we should use subprocess to make sure dsl.modules could be loaded correctly.
        with redirect_stdout(sys.stderr):
            _run_pipeline_project(_get_cli_args(
                'register', target=spec_file, workspace_name=workspace.name,
                resource_group=workspace.resource_group, subscription_id=workspace.subscription_id, version=version
            ))
            return {}

    try:
        componentAPI = _get_component_api_instance(workspace, logger)
        component = componentAPI.register(
            spec_file=spec_file,
            package_zip=package_zip,
            set_as_default=set_as_default,
            amlignore_file=amlignore_file,
            version=version
        )
        if not component._module_dto.is_default_module_version:
            # TODO: module -> component here
            logger.warning(
                'Registered new version %s, but the module default version kept to be %s.\n'
                'Use "az ml module set-default-version" or "az ml module register --set-as-default-version" '
                'to set default version.', component._module_dto.module_version, component._module_dto.default_version)
    except ComponentAlreadyExistsError as e:
        if fail_if_exists:
            raise e
        else:
            logger.warning(e.message)
            return {}

    return component_definition_to_detail_dict(component)


def _validate_component(workspace_name, resource_group_name, subscription_id, spec_file, package_zip, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)

    return __validate_component(workspace=workspace, spec_file=spec_file, package_zip=package_zip,
                                logger=logger)


@track(activity_name="CLI_Component_validate", activity_type=_PUBLIC_API)
def __validate_component(workspace, spec_file, package_zip, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _validate(workspace, spec_file, package_zip, logger)


@track(activity_name="CLI_Module_validate", activity_type=_PUBLIC_API)
def _validate_module(workspace, spec_file, package_zip, logger):
    return _validate(workspace, spec_file, package_zip, logger)


def _validate(workspace, spec_file, package_zip, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    module = componentAPI.validate(spec_file, package_zip)
    return component_definition_to_validation_result_dict(module)


def _list_component(workspace_name, resource_group_name, subscription_id, include_disabled, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __list_component(workspace=workspace, include_disabled=include_disabled, logger=logger)


@track(activity_name="CLI_Component_list", activity_type=_PUBLIC_API)
def __list_component(workspace, include_disabled, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _list(workspace, include_disabled, logger)


@track(activity_name="CLI_Module_list", activity_type=_PUBLIC_API)
def _list_module(workspace, include_disabled, logger):
    return _list(workspace, include_disabled, logger)


def _list(workspace, include_disabled, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    components = componentAPI.list(include_disabled=include_disabled)
    return [component_definition_to_summary_dict(m) for m in components]


def _show_component(workspace_name, resource_group_name, subscription_id, namespace, component_name, component_version,
                    logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)

    return __show_component(workspace=workspace, namespace=namespace, component_name=component_name,
                            component_version=component_version, logger=logger)


@track(activity_name="CLI_Component_show", activity_type=_PUBLIC_API)
def __show_component(workspace, namespace, component_name, component_version, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _show(workspace, namespace, component_name, component_version, logger)


@track(activity_name="CLI_Module_show", activity_type=_PUBLIC_API)
def _show_module(workspace, namespace, module_name, component_version, logger):
    return _show(workspace, namespace, module_name, component_version, logger)


def _show(workspace, namespace, module_name, component_version, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    component = componentAPI.get(name=module_name, namespace=namespace, version=component_version)
    return component_definition_to_detail_dict(component)


def _enable_component(workspace_name, resource_group_name, subscription_id, namespace, component_name, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __enable_component(workspace=workspace, namespace=namespace, component_name=component_name,
                              logger=logger)


@track(activity_name="CLI_Component_enable", activity_type=_PUBLIC_API)
def __enable_component(workspace, namespace, component_name, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _enable(workspace, namespace, component_name, logger)


@track(activity_name="CLI_Module_enable", activity_type=_PUBLIC_API)
def _enable_module(workspace, namespace, module_name, logger):
    return _enable(workspace, namespace, module_name, logger)


def _enable(workspace, namespace, module_name, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    component = componentAPI.enable(name=module_name, namespace=namespace)
    return component_definition_to_detail_dict(component)


def _disable_component(workspace_name, resource_group_name, subscription_id, namespace, component_name, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __disable_component(workspace=workspace, namespace=namespace, component_name=component_name,
                               logger=logger)


@track(activity_name="CLI_Component_disable", activity_type=_PUBLIC_API)
def __disable_component(workspace, namespace, component_name, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _disable(workspace, namespace, component_name, logger)


@track(activity_name="CLI_Module_disable", activity_type=_PUBLIC_API)
def _disable_module(workspace, namespace, module_name, logger):
    return _disable(workspace, namespace, module_name, logger)


def _disable(workspace, namespace, module_name, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    component = componentAPI.disable(name=module_name, namespace=namespace)
    return component_definition_to_detail_dict(component)


def _component_set_default_version(workspace_name, resource_group_name, subscription_id, namespace, component_name,
                                   component_version, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __component_set_default_version(workspace=workspace, namespace=namespace,
                                           component_name=component_name, component_version=component_version,
                                           logger=logger)


@track(activity_name="CLI_Component_set_default_version", activity_type=_PUBLIC_API)
def __component_set_default_version(workspace, namespace, component_name, component_version, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _set_default_version(workspace, namespace, component_name, component_version, logger)


@track(activity_name="CLI_Module_set_default_version", activity_type=_PUBLIC_API)
def _module_set_default_version(workspace, namespace, module_name, component_version, logger):
    return _set_default_version(workspace, namespace, module_name, component_version, logger)


def _set_default_version(workspace, namespace, module_name, component_version, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    component = componentAPI.set_default_version(
        name=module_name,
        namespace=namespace,
        version=component_version
    )
    return component_definition_to_detail_dict(component)


@track(activity_name="CLI_Component_download", activity_type=_PUBLIC_API)
def _download_component(workspace_name, resource_group_name, subscription_id, namespace, component_name,
                        component_version, target_dir, overwrite, logger=None):
    if logger is None:
        logger = _get_logger()
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __download_component(workspace=workspace, namespace=namespace, component_name=component_name,
                                component_version=component_version,
                                target_dir=target_dir, overwrite=overwrite,
                                logger=logger)


def __download_component(workspace, namespace, component_name, component_version, target_dir, overwrite, logger):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _download(workspace, namespace, component_name, component_version, target_dir, overwrite, logger)


@track(activity_name="CLI_Module_download", activity_type=_PUBLIC_API)
def _download_module(workspace, namespace, module_name, component_version, target_dir, overwrite, logger):
    return _download(workspace, namespace, module_name, component_version, target_dir, overwrite, logger)


def _download(workspace, namespace, module_name, component_version, target_dir, overwrite, logger):
    componentAPI = _get_component_api_instance(workspace, logger)
    file_path = componentAPI.download(
        name=module_name, namespace=namespace, version=component_version,
        target_dir=target_dir, overwrite=overwrite
    )
    # TODO: module -> component
    logger.warning(
        f"Downloaded spec file: {file_path['module_spec']} is the actual spec used for the module. "
        f"Compared to the spec inside snapshot, it contains backend processing logic on additional-includes."
    )
    return file_path


@track(activity_name="CLI_Component_init", activity_type=_PUBLIC_API)
def _init_component(source, component_name, job_type, source_dir, inputs, outputs, entry_only, logger=None):
    return _init(source, component_name, job_type, source_dir, inputs, outputs, entry_only, logger)


@track(activity_name="CLI_Module_init", activity_type=_PUBLIC_API)
def _init_module(source, component_name, job_type, source_dir, inputs, outputs, entry_only, logger=None):
    return _init(source, component_name, job_type, source_dir, inputs, outputs, entry_only, logger)


def _init(source, component_name, job_type, source_dir, inputs, outputs, entry_only, logger=None):
    if logger is None:
        logger = _get_logger()
    if source is None:
        # Init a module from template
        # Here we directly call ModuleProject.init since azure-ml-component is put in the dependency of
        # azureml-cli. There won't be any dependency issue since sample modules don't have special requirements.
        from azure.ml.component.dsl._pipeline_project import PipelineProject
        PipelineProject.init(
            source=source, name=component_name, job_type=job_type, source_dir=source_dir, entry_only=entry_only)
    else:
        # If init from function/dslmodule,
        # we should use subprocess to make sure user function could be loaded correctly.
        return _run_pipeline_project(_get_cli_args(
            'init', source=source, name=component_name,
            type=job_type, source_dir=source_dir,
            inputs=inputs, outputs=outputs,
            entry_only=entry_only
        ))
    return {}


@track(activity_name="CLI_Module_build", activity_type=_PUBLIC_API)
def _build_module(target, source_dir, logger=None):
    _build(target, source_dir, logger)


@track(activity_name="CLI_Component_build", activity_type=_PUBLIC_API)
def _build_component(target, source_dir, logger=None):
    _build(target, source_dir, logger)


def _build(target, source_dir, logger=None):
    """Build module from an existing dsl.module."""
    if logger is None:
        logger = _get_logger()
    args = _get_cli_args('build', target=target, source_dir=source_dir)
    # We should use subprocess to make sure user dependencies could be loaded correctly.
    return _run_pipeline_project(args)


def _parse_experiment_url(url):
    """Parse workspace and run info from experiment url."""
    try:
        from azure.ml.component.debug._step_run_debug_helper import DebugOnlineStepRunHelper
    except ImportError:
        raise ImportError("Could not import azure ml component debug utility. \
                          Please make sure azure-ml-component is installed.")
    return DebugOnlineStepRunHelper.parse_designer_url(url)


def _debug_component(run_id=None,
                     experiment_name=None,
                     url=None,
                     target=None,
                     spec_file=None,
                     dry_run=None,
                     subscription_id=None, resource_group_name=None, workspace_name=None):
    """Entrance of component debug."""
    # parse workspace
    if url is not None:
        run_id, experiment_name, workspace_name, resource_group_name, subscription_id = _parse_experiment_url(url)
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __debug_component(workspace, run_id, experiment_name, target, spec_file, dry_run)


def _debug_module(run_id=None,
                  experiment_name=None,
                  url=None,
                  target=None,
                  spec_file=None,
                  dry_run=None,
                  subscription_id=None, resource_group_name=None, workspace_name=None):
    """Entrance of module debug."""
    # parse workspace
    if url is not None:
        run_id, experiment_name, workspace_name, resource_group_name, subscription_id = _parse_experiment_url(url)
    workspace = get_workspace_or_default(subscription_id=subscription_id, resource_group=resource_group_name,
                                         workspace_name=workspace_name)
    return __debug_module(workspace, run_id, experiment_name, target, spec_file, dry_run)


@track(activity_name="CLI_Component_debug", activity_type=_PUBLIC_API)
def __debug_component(workspace,
                      run_id=None,
                      experiment_name=None,
                      target=None,
                      spec_file=None,
                      dry_run=None):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _debug(workspace, run_id, experiment_name, target, spec_file, dry_run)


@track(activity_name="CLI_Module_debug", activity_type=_PUBLIC_API)
def __debug_module(workspace,
                   run_id=None,
                   experiment_name=None,
                   target=None,
                   spec_file=None,
                   dry_run=None):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    return _debug(workspace, run_id, experiment_name, target, spec_file, dry_run)


def _debug(
        workspace,
        run_id=None,
        experiment_name=None,
        target=None,
        spec_file=None,
        dry_run=None):
    """Debug an existing step run or a spec."""
    with redirect_stdout(sys.stderr):
        if spec_file is not None:
            # debug module
            try:
                from azure.ml.component.debug._module_debugger import LocalModuleDebugger
            except ModuleNotFoundError as e:
                raise ImportError(
                    f"Please install azure-ml-component before using az ml module debug.") from e
            debugger = LocalModuleDebugger(workspace_name=workspace.name,
                                           resource_group=workspace.resource_group,
                                           subscription_id=workspace.subscription_id,
                                           yaml_file=spec_file)
            debugger.run()
        else:
            # debug step run with workspace
            _run_step_run_debugger(
                _get_cli_args('debug', run_id=run_id, experiment_name=experiment_name,
                              workspace_name=workspace.name,
                              resource_group_name=workspace.resource_group,
                              subscription_id=workspace.subscription_id,
                              target=target, dry_run=dry_run))

        return {}


def _export(url, draft_id, run_id, path, export_format,
            subscription_id=None, resource_group_name=None, workspace_name=None):
    """Export pipeline draft or pipeline run as sdk code."""
    # Note: put export to module_commands because cli requires all handler function in same package
    # TODO: keep one _export (remove export_pipeline from cmd_pipeline)
    try:
        from azure.ml.component._graph_to_code import _parse_designer_url
    except ImportError:
        raise ImportError("Could not import azure ml component graph-to-code utility. \
                          Please make sure azure-ml-component is installed.")

    if url is not None:
        subscription_id, resource_group_name, workspace_name, draft_id, run_id = _parse_designer_url(url)

    workspace_object = get_workspace_or_default(subscription_id=subscription_id,
                                                resource_group=resource_group_name,
                                                workspace_name=workspace_name)
    return __export(
        workspace=workspace_object, draft_id=draft_id, run_id=run_id, path=path, export_format=export_format)


@track(activity_name="CLI_Component_export", activity_type=_PUBLIC_API)
def __export(workspace, draft_id, run_id, path, export_format):
    """This function has workspace object in params. Use it as an intermediate so we can log workspace in telemetry."""
    try:
        from azure.ml.component._graph_to_code import _export_pipeline_draft_to_code, _export_pipeline_run_to_code
        from azureml.pipeline.core import PipelineRun
    except ImportError:
        raise ImportError("Could not import azure ml component graph-to-code utility. \
                          Please make sure azure-ml-component is installed.")

    if draft_id is None and run_id is None:
        raise ValueError("One of --draft-id or --run-id should be specified")

    if draft_id is not None and run_id is not None:
        raise ValueError("Cannot specify both --draft-id and --run-id at the same time")

    format_mapping = {
        "python": "Python",
        "py": "Python",
        "jupyternotebook": "JupyterNotebook",
        "ipynb": "JupyterNotebook"
    }
    normallized_export_format = format_mapping.get(export_format.lower())
    if normallized_export_format is None:
        raise ValueError(
            "The specified export_format: {} is not supported. Use python or jupyternotebook".format(export_format))

    if path is None:
        path = os.getcwd()
    if not os.path.exists(path):
        raise ValueError("The specified path: {} does not exist.".format(path))

    saved_to = None
    if draft_id is not None:
        saved_to = _export_pipeline_draft_to_code(workspace=workspace,
                                                  draft_id=draft_id,
                                                  path=path,
                                                  export_format=normallized_export_format)
        command_output = CLICommandOutput("Successfully export pipeline draft {} to {}".format(draft_id, saved_to))

    if run_id is not None:
        pipeline_run = PipelineRun.get(workspace=workspace, run_id=run_id)
        saved_to = _export_pipeline_run_to_code(workspace=workspace,
                                                pipeline_run_id=run_id,
                                                path=path,
                                                export_format=normallized_export_format,
                                                experiment_name=pipeline_run.experiment.name,
                                                experiment_id=pipeline_run.experiment.id)
        command_output = CLICommandOutput("Successfully export pipeline run {} to {}".format(run_id, saved_to))

    command_output.set_do_not_print_dict()
    return get_cli_specific_output(command_output)
