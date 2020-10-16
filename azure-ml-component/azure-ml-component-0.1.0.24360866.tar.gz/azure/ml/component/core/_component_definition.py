# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
import shutil
from urllib import request
from pathlib import Path
from io import BytesIO
from typing import Sequence, Union, Mapping
from collections import OrderedDict
from tempfile import mkdtemp

from azure.ml.component._api._api import ComponentAPI
from azure.ml.component.core._component_contexts import CreationContext, RegistrationContext
from ruamel import yaml

from azureml.core import Workspace

from ._core import Component
from ._io_definition import _remove_empty_values, InputDefinition, OutputDefinition
from ._environment import Environment
from ._run_settings_definition import RunSettingsDefinition, K8sRunSettingsDefinition
from .._utils import _extract_zip, _is_empty_dir, _sanitize_python_variable_name


# TODO: We should have a shared logger for component package
logger = logging.getLogger(__name__)
logger.propagate = False
logger.setLevel(logging.INFO)


def _to_camel(s, first_lower=False):
    result = s.title().replace('_', '')
    if first_lower and len(result) > 1:
        result = result[0].lower() + result[1:]
    return result


def _to_ordered_dict(data: dict) -> OrderedDict:
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = _to_ordered_dict(value)
    return OrderedDict(data)


class MetaData(dict):
    """The meta data in the component definition."""

    @property
    def annotations(self):
        """Return the annotations in the metadata."""
        return self.get('annotations', {})

    @property
    def tags(self):
        """Return the tags in the metadata."""
        return self.annotations.get('tags')

    @property
    def contact(self):
        """Return the contact in the metadata."""
        return self.annotations.get('contact')

    @property
    def help_document(self):
        """Return the help docuent in the metadata."""
        return self.annotations.get('helpDocument')


class ComponentDefinition(Component):
    r"""represents a Component asset version.

    ComponentDefinition is immutable class.
    """
    def __init__(
        self, name, type, version=None, namespace=None,
        description=None, metadata=None, is_deterministic=False,
        inputs=None, outputs=None,
        runsettings: RunSettingsDefinition = None,
        workspace=None,
        creation_context=None,
        registration_context=None
    ):
        """Initialize the component."""
        self._name = name
        self._type = type
        self._version = version
        self._namespace = namespace
        self._description = description
        self._metadata = MetaData(metadata or {})
        self._is_deterministic = is_deterministic
        inputs = inputs or {}
        outputs = outputs or {}
        self._inputs = {key: InputDefinition.load(data) for key, data in inputs.items()}
        self._outputs = {key: OutputDefinition.load(data) for key, data in outputs.items()}
        self._runsettings = runsettings
        self._k8srunsettings = None
        self._workspace = workspace
        self._creation_context = creation_context
        self._registration_context = registration_context

    @property
    def name(self) -> str:
        """Return the name of the component."""
        return self._name

    @property
    def namespace(self) -> str:
        """Return the namespace of the component."""
        return self._namespace

    @property
    def version(self) -> str:
        """Return the version of the component."""
        return self._version

    @property
    def type(self) -> str:
        """Return the type of the component."""
        return self._type

    @property
    def inputs(self) -> Mapping[str, InputDefinition]:
        """Return the inputs of the component."""
        return self._inputs

    @property
    def outputs(self) -> Mapping[str, OutputDefinition]:
        """Return the outputs of the component."""
        return self._outputs

    @property
    def description(self):
        """Return the description of the component."""
        return self._description

    @property
    def metadata(self) -> MetaData:
        """Return the metadata of the component."""
        return self._metadata

    @property
    def tags(self):
        """Return the tags of the component."""
        return self.metadata.tags

    @property
    def contact(self):
        """Return the contact of the component."""
        return self.metadata.contact

    @property
    def help_document(self):
        """Return the help document of the component."""
        return self.metadata.help_document

    @property
    def is_deterministic(self) -> bool:
        """Return whether the component is deterministic."""
        return self._is_deterministic

    @property
    def workspace(self) -> Workspace:
        """Return the workspace of the component."""
        return self._workspace

    @property
    def creation_context(self):
        # If component is not initialized from module dto, create an empty CreationContext.
        if self._creation_context is None:
            self._creation_context = CreationContext({})
        return self._creation_context

    @creation_context.setter
    def creation_context(self, val):
        """Set creation context for ComponentDefinition."""
        self._creation_context = val

    @property
    def registration_context(self):
        # If component is not initialized from module dto, create an empty RegistrationContext.
        if self._registration_context is None:
            self._registration_context = RegistrationContext({})
        return self._registration_context

    @registration_context.setter
    def registration_context(self, val):
        """Set registration context for ComponentDefinition."""
        self._registration_context = val

    @property
    def identifier(self):
        """Return the identifier of the component(unique in one workspace)."""
        return self.registration_context.id

    @property
    def runsettings(self) -> RunSettingsDefinition:
        """Return the run settings definition of the component."""
        return self._runsettings

    @property
    def k8srunsettings(self) -> K8sRunSettingsDefinition:
        """Return the k8s run settings definition of the component."""
        return self._k8srunsettings

    @staticmethod
    def list(workspace, include_disabled=False) -> Sequence['ComponentDefinition']:
        """Return a list of components in the workspace.

        :param workspace: The workspace from which to list component definitions.
        :type workspace: azureml.core.workspace.Workspace
        :param include_disabled: Include disabled modules in list result
        :type include_disabled: bool
        :return: A list of module objects.
        :rtype: Sequence['ComponentDefinition']
        """
        raise NotImplementedError

    @staticmethod
    def get(workspace, name, namespace=None, version=None):
        """Get the component definition object from the workspace.

        :param workspace: The workspace that contains the component.
        :type workspace: azureml.core.workspace.Workspace
        :param name: The name of the component to return.
        :type name: str
        :param namespace: The namespace of the component to return.
        :type namespace: str
        :param version: The version of the component to return.
        :type version: str
        :return: The module object.
        :rtype: ComponentDefinition
        """
        raise NotImplementedError

    def register(self, workspace, set_as_default_version=True, overwrite_module_version=None):
        """Register the component definition to a workspace.

        :param workspace: The workspace
        :type workspace: azureml.core.workspace.Workspace
        :param set_as_default_version: Whether to update the default version.
        :type set_as_default_version: bool.
        :param overwrite_module_version: If specified, registered component will use specified value as version
                                            instead of the version in the yaml.
        :type overwrite_module_version: str
        :return: Returns the component definition object
        :rtype: ComponentDefinition
        """
        raise NotImplementedError

    def validate(self):
        """Validate whether the component is valid."""
        raise NotImplementedError

    def enable(self):
        """Enable a component in the workspace.

        :return: The updated component object.
        :rtype: ComponentDefinition
        """
        raise NotImplementedError

    def disable(self):
        """Disable a component in the workspace.

        :return: The updated component object.
        :rtype: ComponentDefinition
        """
        raise NotImplementedError

    @classmethod
    def load(cls, yaml_file) -> 'ComponentDefinition':
        """Load a component definition from a component yaml file."""
        with open(yaml_file) as fin:
            return cls._from_dict(yaml.safe_load(fin))

    def save(self, yaml_file):
        """Dump the component definition to a component yaml file."""
        _setup_yaml(yaml)
        data = _to_ordered_dict(self._to_dict())
        with open(yaml_file, 'w') as fout:
            yaml.dump(data, fout, default_flow_style=False)

    @classmethod
    def _from_dict(cls, dct) -> 'ComponentDefinition':
        """Load a component definition from a component yaml dict."""
        raise NotImplementedError

    def _to_dict(self):
        """Convert the component definition to a python dict."""
        result = {
            'name': self.name,
            'version': self.version,
            'namespace': self.namespace,
            'type': self.type,
            'description': self.description,
            'isDeterministic': self.is_deterministic,
            'metadata': self.metadata if self.metadata else None,
            'inputs': {key: val.to_dict() for key, val in self.inputs.items()},
            'outputs': {key: val.to_dict() for key, val in self.outputs.items()},
        }
        result = _remove_empty_values(result)
        return result


class ContainerComponentDefinition(ComponentDefinition):
    r"""represents a Component asset version.

    ComponentDefinition is immutable class.
    """
    TYPE_NAME = 'ContainerComponent'

    def __init__(self, name, version=None, namespace=None,
                 description=None, job_type=None, metadata=None, is_deterministic=False,
                 inputs=None, outputs=None,
                 runsettings: RunSettingsDefinition = None,
                 command=None, environment=None,
                 source_directory=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None
                 ):
        """Initialize a ContainerComponentDefinition from the args."""
        super().__init__(
            name=name, version=version, namespace=namespace, type=self.TYPE_NAME,
            description=description,
            metadata=metadata,
            is_deterministic=is_deterministic,
            inputs=inputs, outputs=outputs,
            runsettings=runsettings,
            workspace=workspace,
            creation_context=creation_context,
            registration_context=registration_context
        )
        self._job_type = job_type
        self._command = command
        if isinstance(environment, dict):
            environment = Environment._from_dict(environment)
        self._environment = environment
        self._source_directory = source_directory
        self._snapshot_local_cache = None
        self._api_caller = None

        # This field is used for telemetry when loading the component from a workspace,
        # a new name may be required since the interface has been changed to `get` instead of `load`
        self._load_source = None

        # This property is a workaround to unblock the implementation of Component,
        # will be removed after all the implementations are ready.
        self._module_dto = None

        # This property is a workaround that there is a name and a 'display name',
        # where the yaml is using display name, but the backend uses 'name',
        # we need to store such a mapping to get the backend name
        self._display_name_to_name = {}

    @property
    def job_type(self):
        """Return the job type of the ContainerComponentDefinition."""
        return self._job_type

    @property
    def command(self):
        """Return the command of the ContainerComponentDefinition."""
        return self._command

    @property
    def environment(self) -> Environment:
        """Return the environment of the ContainerComponentDefinition."""
        if self._environment is None:
            self._environment = Environment()
        return self._environment

    @property
    def source_directory(self):
        """Return the source directory of the ContainerComponentDefinition."""
        return self._source_directory or '.'

    @property
    def _registered(self) -> bool:
        """Return whether the ContainerComponentDefinition is registered in the workspace."""
        return self.workspace is not None and self.identifier is not None

    @property
    def api_caller(self):
        """CRUD layer to call rest APIs."""
        if self._api_caller is None:
            self._api_caller = ComponentAPI(self.workspace)
        return self._api_caller

    @api_caller.setter
    def api_caller(self, api_caller):
        """Setter for api caller."""
        self._api_caller = api_caller

    def _to_dict(self) -> dict:
        """Convert the component definition to a python dict."""
        result = super()._to_dict()
        result.update({
            'jobType': self.job_type,
            'command': self._reformat_command(self.command),
            'environment': self.environment._to_dict(),
            'source_directory': self.source_directory if self.source_directory != '.' else None,
        })
        return _remove_empty_values(result)

    @property
    def snapshot_url(self) -> str:
        """Return the snapshot url for a registered ContainerComponentDefinition."""
        if not self._registered:
            raise ValueError("Only registered ContainerComponent has a snapshot url.")
        return self.api_caller.get_snapshot_url_by_id(component_id=self.identifier)

    def get_snapshot(self, target=None, overwrite=False) -> Path:
        """Get the snapshot in target folder, if target is None, the snapshot folder is returned."""
        if target is not None:
            target = Path(target)
            if target.exists() and not _is_empty_dir(target) and not overwrite:
                raise FileExistsError("Target '%s' can only be an empty folder when overwrite=False." % target)
            if target.exists():
                shutil.rmtree(target)  # Remove the empty folder to store snapshot.
            target.parent.mkdir(exist_ok=True, parents=True)  # Make sure the parent folder exists.
        if self._snapshot_local_cache:
            if target is None:
                return self._snapshot_local_cache
            shutil.copytree(str(self._snapshot_local_cache), str(target))
        else:
            if target is None:
                target = mkdtemp()
            self._download_snapshot(target)
            self._snapshot_local_cache = target
            return target

    def _download_snapshot(self, target: Union[str, Path]):
        """Download the snapshot in the target folder."""
        snapshot_url = self.snapshot_url
        response = request.urlopen(snapshot_url)
        _extract_zip(BytesIO(response.read()), target)

    @staticmethod
    def get(
            workspace: Workspace, name: str, namespace: str = None, version: str = None,
    ) -> 'ContainerComponentDefinition':
        """Get the component definition object from the workspace."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        component = api_caller.get(
            name=name,
            namespace=namespace,
            version=version,  # If version is None, this will get the default version
        )
        component.api_caller = api_caller
        return component

    @staticmethod
    def list(workspace, include_disabled=False) -> Sequence['ContainerComponentDefinition']:
        """Return a list of components in the workspace."""
        api_caller = ComponentAPI(workspace=workspace, logger=logger)
        return api_caller.list(include_disabled=include_disabled)

    @classmethod
    def load(cls, yaml_file) -> 'ContainerComponentDefinition':
        result = super(ContainerComponentDefinition, cls).load(yaml_file)
        result._snapshot_local_cache = Path(Path(yaml_file).parent / result.source_directory)
        return result

    @classmethod
    def _from_dict(cls, dct) -> 'ContainerComponentDefinition':
        """Load a component definition from a component yaml dict."""
        if 'type' in dct:
            if dct.pop('type') != cls.TYPE_NAME:
                raise TypeError("The type must be %r." % cls.TYPE_NAME)
        keys_to_update = ['job_type', 'source_directory', 'is_deterministic']
        for key in keys_to_update:
            camel = _to_camel(key, first_lower=True)
            if camel in dct:
                dct[key] = dct.pop(camel)
        return cls(**dct)

    @staticmethod
    def _reformat_command(command):
        """Reformat the command to make the output yaml clear."""
        if not command:
            return []
        # Here we call _YamlFlowList and _YamlFlowDict to have better representation when dumping args to yaml.
        result = []
        for arg in command:
            if isinstance(arg, list):
                arg = [_YamlFlowDict(item) if isinstance(item, dict) else item for item in arg]
                arg = _YamlFlowList(arg)
            result.append(arg)
        return result

    @classmethod
    def _module_yaml_convert_arg_item(cls, arg, inputs, outputs):
        """Convert one arg item in old style yaml to new style."""
        if isinstance(arg, (str, int, float)):
            return arg
        if isinstance(arg, list):
            return cls._module_yaml_convert_args(arg, inputs, outputs)
        if not isinstance(arg, dict) or len(arg) != 1:
            raise ValueError("Arg item is not valid: %r" % arg)
        key, value = list(arg.items())[0]
        key = '$' + key
        for value_key in ['inputs', 'outputs']:
            items = locals()[value_key]
            for item in items:
                if item['name'] == value:
                    return {key: value_key + '.' + item['argumentName']}
        raise ValueError("%r is not in inputs and outputs." % value)

    @classmethod
    def _module_yaml_convert_args(cls, args, inputs, outputs):
        """Convert the args in old style yaml to new style."""
        return [cls._module_yaml_convert_arg_item(arg, inputs, outputs) for arg in args] if args else []

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        """Construct the component dict from an old style ModuleDefinition."""
        inputs, outputs = module.input_ports + module.params, module.output_ports
        for item in inputs + outputs:
            if 'argumentName' not in item:
                item['argumentName'] = _sanitize_python_variable_name(item['name'])

        command = module.command or []
        command += cls._module_yaml_convert_args(module.args, inputs, outputs)
        # Convert options to enum
        for i in inputs:
            if 'options' in i:
                i['enum'] = i.pop('options')

        input_pairs = [(item.pop('argumentName'), item) for item in inputs]
        output_pairs = [(item.pop('argumentName'), item) for item in outputs]
        new_dct = {
            'name': module.name,
            'version': module.version,
            'namespace': module.namespace,
            'jobType': module.job_type,
            'isDeterministic': module.is_deterministic,
            'description': module.description,
            'metadata': module.metadata,
            'type': cls.TYPE_NAME,
            'inputs': {key: value for key, value in input_pairs},
            'outputs': {key: value for key, value in output_pairs},
            'command': command,
            'environment': module.aml_environment,
        }
        return new_dct

    @staticmethod
    def _from_module_yaml_dict(dct) -> 'ContainerComponentDefinition':
        """Load the component from the old style module yaml dict."""
        from ..dsl._module_spec import _YamlModuleDefinition, _YamlParallelModuleDefinition, \
            _YamlHDInsightModuleDefinition
        definition_cls, cls = _YamlModuleDefinition, ContainerComponentDefinition
        job_type = dct.get('jobType')
        if job_type is not None:
            if job_type.lower() == 'parallel':
                definition_cls, cls = _YamlParallelModuleDefinition, ParallelContainerComponentDefinition
            elif job_type.lower() == 'hdinsight':
                definition_cls, cls = _YamlHDInsightModuleDefinition, HDInsightContainerComponentDefinition
        return cls._from_dict(cls._construct_dict_from_module_definition(definition_cls(dct)))


class ParallelContainerComponentDefinition(ContainerComponentDefinition):
    """The component definition of a parallel component."""

    def __init__(self, name, version=None, namespace=None,
                 description=None, metadata=None, is_deterministic=False,
                 inputs=None, outputs=None,
                 input_data=None, output_data=None,
                 entry=None,
                 command=None, environment=None,
                 source_directory=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None):
        super().__init__(
            name=name, version=version, namespace=namespace, description=description, metadata=metadata,
            is_deterministic=is_deterministic, inputs=inputs, outputs=outputs,
            command=command, environment=environment,
            source_directory=source_directory,
            workspace=workspace, creation_context=creation_context, registration_context=registration_context,
        )
        # Here we support multiple input_data as an input list.
        self._input_data = input_data if isinstance(input_data, list) else [input_data]
        self._output_data = output_data
        self._entry = entry
        self._job_type = 'parallel'

    @property
    def input_data(self) -> Sequence[str]:
        return self._input_data

    @property
    def output_data(self) -> str:
        return self._output_data

    @property
    def entry(self) -> str:
        return self._entry

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        dct = super()._construct_dict_from_module_definition(module)
        dct['parallel'] = {
            'inputData': module.input_data,
            'outputData': module.output_data,
            'entry': module.entry,
        }
        return dct

    @classmethod
    def _from_dict(cls, dct) -> 'ParallelContainerComponentDefinition':
        job_type = None if 'jobType' not in dct else dct.pop('jobType')
        if job_type is None or job_type.lower() != 'parallel':
            raise ValueError("The job type must be parallel, got '%s'." % job_type)
        if 'parallel' not in dct:
            raise KeyError("The dict for the parallel component must contain 'parallel' section.")
        parallel = dct.pop('parallel')
        dct['input_data'] = parallel['inputData']
        dct['output_data'] = parallel['outputData']
        dct['entry'] = parallel['entry']
        return super()._from_dict(dct)

    def _to_dict(self) -> dict:
        result = super()._to_dict()
        result['parallel'] = {
            'inputData': self.input_data,
            'outputData': self.output_data,
            'entry': self.entry
        }
        return _remove_empty_values(result)


class HDInsightContainerComponentDefinition(ContainerComponentDefinition):
    """The component definition of a HDInsight component."""

    def __init__(self, name, version=None, namespace=None,
                 description=None, metadata=None, is_deterministic=False,
                 inputs=None, outputs=None,
                 file=None, jars=None,
                 py_files=None,
                 command=None, environment=None,
                 source_directory=None,
                 workspace=None,
                 creation_context=None,
                 registration_context=None):
        super().__init__(
            name=name, version=version, namespace=namespace, description=description, metadata=metadata,
            is_deterministic=is_deterministic, inputs=inputs, outputs=outputs,
            command=command, environment=environment,
            source_directory=source_directory,
            workspace=workspace, creation_context=creation_context, registration_context=registration_context,
        )
        self._file = file
        self._jars = jars
        self._py_files = py_files

    @property
    def file(self) -> str:
        return self._file

    @property
    def jars(self) -> Sequence[str]:
        return self._jars

    @property
    def py_files(self) -> Sequence[str]:
        return self._py_files

    @classmethod
    def _construct_dict_from_module_definition(cls, module):
        dct = super()._construct_dict_from_module_definition(module)
        dct['hdinsight'] = {
            'file': module.file,
            'jars': module.jars,
            'pyFiles': module.py_files,
        }
        return dct

    @classmethod
    def _from_dict(cls, dct) -> 'HDInsightContainerComponentDefinition':
        job_type = None if 'jobType' not in dct else dct.pop('jobType')
        if job_type is None or job_type.lower() != 'hdinsight':
            raise ValueError("The job type must be hdinsight, got '%s'." % job_type)
        if 'hdinsight' not in dct:
            raise KeyError("The dict for the hdinsight component must contain 'hdinsight' section.")
        hdinsight = dct.pop('hdinsight')
        dct['file'] = hdinsight['file']
        dct['jars'] = hdinsight['jars']
        dct['py_files'] = hdinsight['pyFiles']
        return super()._from_dict(dct)

    def _to_dict(self) -> dict:
        result = super()._to_dict()
        result['hdinsight'] = {
            'file': self._file,
            'jars': self._jars,
            'pyFiles': self._pyFiles
        }
        return _remove_empty_values(result)


class _Environment:

    def __init__(self, docker, python, os='linux'):
        self._os = os
        self._docker = docker,
        self._python = python

    @property
    def os(self):
        return self._os

    @property
    def docker(self):
        return self._docker

    @property
    def python(self):
        return self._python


class _YamlFlowDict(dict):
    """This class is used to dump dict data with flow_style."""

    @classmethod
    def representer(cls, dumper: yaml.dumper.Dumper, data):
        return dumper.represent_mapping('tag:yaml.org,2002:map', data, flow_style=True)


class _YamlFlowList(list):
    """This class is used to dump list data with flow_style."""

    @classmethod
    def representer(cls, dumper: yaml.dumper.Dumper, data):
        return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)


def _str_representer(dumper: yaml.dumper.Dumper, data):
    """Dump a string with normal style or '|' style according to whether it has multiple lines."""
    style = ''
    if '\n' in data:
        style = '|'
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style=style)


def _setup_yaml(yaml):
    yaml.add_representer(_YamlFlowDict, _YamlFlowDict.representer)
    yaml.add_representer(_YamlFlowList, _YamlFlowList.representer)
    yaml.add_representer(str, _str_representer)

    # Setup to preserve order in yaml.dump, see https://stackoverflow.com/a/8661021
    def _represent_dict_order(self, data):
        return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    yaml.add_representer(OrderedDict, _represent_dict_order)
