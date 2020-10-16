# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import os
import sys
import requests
import subprocess
import tarfile
import copy
import json
import shutil
import traceback
import concurrent
import tempfile
import docker
import uuid
from queue import Queue, Empty
from time import sleep
from threading import Lock, currentThread, main_thread, Thread, Event
from pathlib import Path
from datetime import datetime
from io import BytesIO

from azureml._model_management._util import write_dir_in_container
from azureml._model_management._util import write_file_in_container
from azureml._model_management._util import get_docker_client
from azure.ml.component._restclients.service_caller_factory import _DesignerServiceCallerFactory
from azureml.core import Datastore, Dataset, Run
from azureml.data.datapath import DataPath
from azureml.data.data_reference import DataReference
from azureml.data.dataset_consumption_config import DatasetConsumptionConfig
from azureml.data import FileDataset
from azureml.core.experiment import Experiment
from azure.ml.component._restclients.designer.models import ErrorResponseException
from ._pipeline_parameters import PipelineParameter
from ._utils import _get_short_path_name, _extract_zip
from ._loggerfactory import _LoggerFactory, track
from ._module_snapshot_cache import ModuleSnapshotCache

PREFIX_PARAMETER = 'AZUREML_PARAMETER_'
PREFIX_DATAREFERENCE = 'AZUREML_DATAREFERENCE_'
OUTPUT_DIR_NAME = 'outputs'
CONTAINER_INPUT_PATH = '/mnt/input'
CONTAINER_OUTPUT_PATH = f'/mnt/{OUTPUT_DIR_NAME}'
CONTAINER_MOUNT_SCRIPTS_PATH = '/mnt/scripts'
SCRIPTE_DIR_NAME = 'scripts'
IMAGE_DIR_NAME = 'image_logs'
EXECUTION_LOGFILE = 'excutionlogs.txt'
SLEEP_INTERVAL = 5
RUN_STATUS = {
    'NotStarted': '0',
    'Preparing': '3',
    'Running': '5',
    'Completed': '8',
    'Failed': '9'
}
STATUS_CODE = {
    'NotStarted': '0',
    'Preparing': '2',
    'Running': '3',
    'Failed': '4',
    'Completed': '5',
}
MOCK_PARALLEL_DRIVER = '_mock_parallel_driver.py'
MODULE_PROPERTY_NAME = 'azureml.moduleid'
PARENT_NODE_ID = '@parent'
NODE_LOG_KEY = '70_driver_log.txt'
PARENT_LOG_KEY = 'logs/azureml/executionlogs.txt'
RUN_PREPARE_LOG = 'Run prepare stage'
RUN_EXEC_LOG = 'Run execute stage'
RUN_RELEASE_LOG = 'Run release stage'
STEP_STATUS = {
    'runStatus': None,
    'startTime': None,
    'endTime': None,
    'status': None,
    'statusCode': None,
    'statusDetail': None,
    'runDetailsUrl': None
}
LOG_FILE = 'log_file'
SHOW_TERMINAL = 'show_terminal'
TRACKER = 'tracker'
STOP_EVENT = 'stop_event'
MESSAGE = 'message'
UPLOAD_THREAD = 'upload_thread'

_logger = None
max_cache_snapshot = 50
max_unused_time = 1000 * 60 * 60 * 6
snapshot_cache_dir = os.path.join(tempfile.gettempdir(), 'azureml_snapshot_cache')
snapshot_cache = ModuleSnapshotCache(snapshot_cache_dir, max_cache_snapshot, max_unused_time)


def _get_logger():
    global _logger
    if _logger is not None:
        return _logger
    _logger = _LoggerFactory.get_logger(__name__)
    return _logger


def _module_run(module, working_dir, use_docker, tracker, node_id=None, visualizer=None, show_output=True,
                module_to_node_mapping={}, data_dir=None, pipeline_parameters=None,
                input_futures=None, image_futures=None):
    """
    Run module

    _module_run will run module in local environment/container. In prepare state, will download module
    snapshots and input dataste, generate module execute command and pull module image. Then will execute
    command in local environment/container.

    :param module: Executed module
    :type module: azure.ml.component.Component
    :param working_dir: module data and snapshot store path
    :type working_dir: str
    ::param use_docker: If use_docker=True, will pull image from azure and run module in container.
                        If use_docker=False, will directly run module script.
    :type use_docker: bool
    :param tracker: Used for tracking run history.
    :type tracker: RunHistoryTracker
    :param node_id: Node id of module
    :type node_id: str
    :param visualizer: To show pipeline graph in notebook
    :type visualizer: azure.ml.component._widgets._visualize
    :param show_output: Indicates whether to show the pipeline run status on sys.stdout.
    :type show_output: bool
    :param module_to_node_mapping: Mapping of module to node info
    :type module_to_node_mapping: dict{(str, dict)}
    :param data_dir: If module input data in remote, will download to data_dir.
                     If data_dir=None, will set working_dir to data_dir.
    :type data_dir: str
    :param pipeline_parameters: An optional dictionary of pipeline parameter
    :type pipeline_parameters: dict{(str, object)}
    :param input_futures: Download input dataset futures
    :type input_futures: dict{(str, Future)}
    :param image_futures: Get module image futures
    :type image_futures: dict{(str, Future)}
    :return: Module run status
    :rtype: str
    """
    Path(working_dir).mkdir(parents=True, exist_ok=True)
    if not data_dir:
        data_dir = working_dir
    is_main_thread = currentThread() is main_thread()

    status = None
    module_run_success = False
    with Logger(log_path=os.path.join(working_dir, EXECUTION_LOGFILE),
                show_terminal=(show_output and is_main_thread), tracker=tracker) as logger:
        log_file_url = logger.get_log_path()
        try:
            tasks = []
            tracker.print_run_info()

            # Get snapshot directory of module
            snapshot_path = os.path.join(working_dir, SCRIPTE_DIR_NAME)
            get_module_snapshot_task = ThreadWithParent(target=_prepare_module_snapshot, args=(module, snapshot_path))
            get_module_snapshot_task.start()

            module = _prepare_module_run(module, data_dir, pipeline_parameters, module_to_node_mapping, input_futures)

            # visualizer start
            module_run_status = 'Preparing'
            status = update_module_status(module_run_status, run_details_url=tracker.get_run_details_url())
            update_visualizer(visualizer, node_id, status, log_file_url)

            # Genterate command
            command, volumes, environment = _generate_command(module, working_dir, use_docker)
            # create module output file/folder which not exists
            create_module_run_output(module, volumes)
            # For metirc needed environment variables
            if tracker.track_run_history:
                environment.update(_set_environment_variables_for_run(tracker.get_run()))
                _add_new_thread_task(
                    tasks=tasks,
                    target=tracker.add_properties,
                    args=({MODULE_PROPERTY_NAME: module._identifier},))

            if use_docker:
                # Add scripts in volumes
                volumes[snapshot_path] = {'bind': CONTAINER_MOUNT_SCRIPTS_PATH, 'mode': 'rw'}
                # Get module image
                module_image = get_module_image(module, working_dir, image_futures)

            # Start executing module script
            print(f'{RUN_EXEC_LOG}: prepare to call script [ {module._module_dto.entry} ] with command {command}.')
            print(f'{RUN_EXEC_LOG}: run module {module.name} starting....')
            module_run_status = 'Running'
            update_visualizer(visualizer, node_id, update_module_status(module_run_status, status), log_file_url)

            get_module_snapshot_task.join()
            print(f'{RUN_EXEC_LOG}: module execute log\n')
            # Execute module script
            if use_docker:
                module_run_success = execute_module_in_container(
                    command, volumes, environment, module_image.image_name, logger)
            else:
                module_run_success = execute_module_in_local(
                    command, environment, snapshot_path, logger)

            module_run_status = "Completed" if module_run_success else "Failed"
            print(f'{RUN_EXEC_LOG}: finish running module {module.name}, status is {module_run_status}...')
            if not module_run_success:
                print(f'Diagnostic your failed run here:\n'
                      f'\tworking dir: {working_dir}\n'
                      f'\texecution log: {os.path.join(working_dir, EXECUTION_LOGFILE)}\n'
                      f'\toutput dir: {os.path.join(working_dir, OUTPUT_DIR_NAME)}')

            # Upload module outputs/snapshots/log file to portal
            _add_new_thread_task(tasks=tasks, target=tracker.upload_run_output, args=(module, working_dir))
            _add_new_thread_task(tasks=tasks, target=tracker.upload_snapshot, args=(snapshot_path,))
            update_visualizer(visualizer, node_id, update_module_status(module_run_status, status), log_file_url)

            if use_docker and not module_run_success:
                _prepare_debug_config_for_module(
                    module, module_image, command, volumes, environment, snapshot_path)
        except Exception as ex:
            traceback.print_exc()
            update_visualizer(
                visualizer,
                node_id,
                update_module_status('Failed', status, run_details_url=tracker.get_run_details_url()),
                log_file_url)
            raise ex
        finally:
            execution_path = os.path.join(working_dir, EXECUTION_LOGFILE)
            if show_output and not is_main_thread:
                print_logfile(execution_path, logger)
            for task in tasks:
                task.join()
            tracker.update_run_result_status(module_run_success)

    return module_run_status


def _add_new_thread_task(tasks, target, args):
    """
    Create module run child thread which recode parent thread id.
    """
    thread = ThreadWithParent(target=target, args=args)
    tasks.append(thread)
    thread.start()
    return thread


def update_visualizer(visualizer, node_id, status, log=None):
    if not visualizer or not node_id:
        return
    visualizer.send_message(message='status', content={node_id: status})
    if log:
        if node_id != PARENT_NODE_ID:
            visualizer.send_message(message='logs', content={node_id: {NODE_LOG_KEY: log}})
        else:
            visualizer.send_message(message='logs', content={node_id: {PARENT_LOG_KEY: log}})


def update_module_status(module_status, status=None, run_details_url=None):
    if not status:
        status = copy.deepcopy(STEP_STATUS)
    if not run_details_url:
        status['runDetailsUrl'] = run_details_url

    status['status'] = STATUS_CODE[module_status]
    status['statusCode'] = STATUS_CODE[module_status]
    status['runStatus'] = RUN_STATUS[module_status]

    if module_status == 'Running' and not status['startTime']:
        status['startTime'] = datetime.now().isoformat()
    elif module_status == 'Completed' or module_status == 'Failed':
        status['endTime'] = datetime.now().isoformat()
    return status


def create_module_run_output(module, volumes):
    # will create module output file/folder which not exists after module run
    if len(module.outputs) == 0:
        return
    path = Path([key for key, value in volumes.items() if value['bind'] == CONTAINER_OUTPUT_PATH][0])
    for output_name in module.outputs.keys():
        if not (path / output_name).exists():
            if module._output_is_file(output_name):
                (path / output_name).touch()
            else:
                (path / output_name).mkdir(parents=True)


def _prepare_debug_config_for_module(module, module_image, command, volumes, environment, snapshot_path):
    from azure.ml.component.debug._module_debug_helper import DebugLocalModuleHelper
    mount_val = "source={},target={},type=bind,consistency=cached"
    mounts = [mount_val.format(key, value['bind'])for key, value in volumes.items()]
    DebugLocalModuleHelper.prepare_dev_container(module_image.image_name,
                                                 name=module.name,
                                                 containerEnv=environment,
                                                 mounts=mounts,
                                                 target=snapshot_path
                                                 )
    DebugLocalModuleHelper.create_launch_config(module._module_dto.entry[:-3], command, snapshot_path, module.job_type)
    from azure.ml.component.dsl._utils import _print_step_info
    _print_step_info([
        f'Module run failed, you can debug module in vscode by steps:',
        '1. Pressing F1, click "Remote-Containers: Reopen in Container".',
        f'2. In Status Bar, selecting python interpreter path "{module_image.python_path}"',
        "3. Pressing F5 to start debugging."])


def _get_snapshot_content(module):
    service_caller = _DesignerServiceCallerFactory.get_instance(module.workspace)
    snapshot_url = service_caller.get_module_snapshot_url_by_id(module_id=module._identifier)
    response = requests.get(snapshot_url, allow_redirects=True)
    return response.content


@track(_get_logger)
def _prepare_module_snapshot(module, target_dir):
    """
    Get module snapshot and move to target_dir. If snapshot exists in cache, will copy it to target_dir.
    If not, will download snapshot to target_dir.

    :param module: module to get snapshot
    :type module: azure.ml.component.Component
    :param target_dir: snapshot store path
    :type target_dir: str
    """
    # Get snapshot dir from cache
    module_id = module._identifier
    if snapshot_cache.prepare_snapshot_from_cache(module_id, target_dir):
        return
    print(f'{RUN_PREPARE_LOG}: download {module.name} snapshot...')
    # If snapshot not exists in cache, download snapshot
    content = _get_snapshot_content(module)
    # extract snapshot to script path
    _extract_zip(BytesIO(content), target_dir)

    if module.job_type.lower().strip() == 'parallel':
        _mock_parallel_driver_file(target_dir)

    # Add snapshot to snapshot cache dir
    snapshot_cache.cache_snapshot(module_id, target_dir)
    print(f'{RUN_PREPARE_LOG}: download {module.name} snapshot completed...')


def _download_snapshot(snapshot_url, script_path):
    # download snapshot to target directory
    response = requests.get(snapshot_url, allow_redirects=True)
    # extract snapshot to script path
    _extract_zip(BytesIO(response.content), script_path)


def _mock_parallel_driver_file(target_dir):
    # For parallel module, we use a mock driver to run the module.
    Path(target_dir).mkdir(parents=True, exist_ok=True)
    target_entry = Path(target_dir) / MOCK_PARALLEL_DRIVER
    if target_entry.exists():
        target_entry.unlink()
    src_entry = Path(__file__).parent / MOCK_PARALLEL_DRIVER
    shutil.copyfile(str(src_entry), str(target_entry))


def _set_environment_variables_for_run(run):
    env = {
        'AZUREML_RUN_ID': run.id,
        'AZUREML_ARM_SUBSCRIPTION': run.experiment.workspace.subscription_id,
        'AZUREML_ARM_RESOURCEGROUP': run.experiment.workspace.resource_group,
        'AZUREML_ARM_WORKSPACE_NAME': run.experiment.workspace.name,
        'AZUREML_ARM_PROJECT_NAME': run.experiment.name,
        'AZUREML_RUN_TOKEN': run._client.run.get_token().token,
        'AZUREML_WORKSPACE_ID': run.experiment.workspace._workspace_id,
        'AZUREML_SERVICE_ENDPOINT': run._client.run.get_cluster_url(),
        'AZUREML_DISCOVERY_SERVICE_ENDPOINT': run.experiment.workspace.discovery_url,
    }
    return env


def _generate_command(
        module, working_dir, use_docker, remove_none_value=True, check_data_exist=True,
        container_input_prefix=CONTAINER_INPUT_PATH, container_output_prefix=CONTAINER_OUTPUT_PATH):
    environment = {}
    volumes = {}
    # Mount input path to container and replace input port value in arguments
    input_path = {}
    for input_name, input_item in module.inputs.items():
        input_is_optional = module._input_is_optional(input_name)
        if isinstance(input_item.dset, str) or isinstance(input_item.dset, Path):
            # Change to absolute path to avoid relative import error when running locally
            input_item_path = Path(input_item.dset).resolve().absolute()
            short_input_item_path = Path(_get_short_path_name(input_item_path))
            port_name = module._pythonic_name_to_input_map[input_name]
            input_data_type = \
                next(input.data_type_ids_list for input in module._interface_inputs if input.name == port_name)
            if ['AnyFile'] == input_data_type:
                if not short_input_item_path.is_file():
                    short_input_item_path = next(
                        filter(lambda item: item.is_file(), short_input_item_path.iterdir()), None)
            if not check_data_exist or short_input_item_path.exists():
                if use_docker:
                    if str(short_input_item_path) in volumes:
                        input_port_path = volumes[str(short_input_item_path)]['bind']
                    else:
                        input_port_path = container_input_prefix + '/' + \
                            os.path.basename(input_name)
                        volumes[str(short_input_item_path)] = {'bind': input_port_path, 'mode': 'ro'}
                else:
                    input_port_path = str(short_input_item_path)
                input_path[input_name] = input_port_path
            else:
                if check_data_exist and not input_is_optional:
                    raise ValueError(
                        f'Local input port path for "{input_name}" does not exist, path: {input_item.dset}')
        else:
            if not input_is_optional:
                raise ValueError(f'Input port "{input_name}" not set')

    # Mount output path to container and replace output port value in arguments
    output_portname_container_path = {}
    for output_port_name in module.outputs.keys():
        if use_docker:
            output_port_path = container_output_prefix + '/' + output_port_name
        else:
            output_port_path = os.path.join(working_dir, OUTPUT_DIR_NAME, output_port_name)
        output_portname_container_path[output_port_name] = output_port_path
    output_path = os.path.join(working_dir, OUTPUT_DIR_NAME)
    if not os.path.exists(output_path) and check_data_exist:
        os.makedirs(output_path)
    volumes[output_path] = {'bind': CONTAINER_OUTPUT_PATH, 'mode': 'rw'}

    # Get module run command
    command = module._get_command(input_path, output_portname_container_path, remove_none_value)
    return command, volumes, environment


def translate_mpi_command_by_module(command, module):
    # Get process_count_per_node param from run settings, will be 1 if did not find
    process_count_per_node = module._get_run_setting('process_count_per_node', int, 1)
    # Setting --oversubscribe allowed to be oversubscribed and overload of processing elements.
    # https://www.open-mpi.org/faq/?category=running#oversubscribing
    command[0:0] = ['mpiexec', '-n', str(process_count_per_node), '--allow-run-as-root', '--oversubscribe']

    node_count_argument = module._module_dto.get_run_setting_parameter_by_argument_name('node_count')
    if node_count_argument and node_count_argument.default_value:
        from azure.ml.component.dsl._utils import logger as dsl_logger
        dsl_logger.warning(f'Ignore {module.name} setting node_count = {node_count_argument.default_value}, '
                           'module.run only supports executing node on single node')

    return command


def translate_parallel_command_by_module(command, module, input_paths):
    # translate key of input_paths from input argument name to input name
    command[1] = MOCK_PARALLEL_DRIVER
    port_arg_map = {}
    for input_arg_name, input_path in input_paths.items():
        input_name = module._get_input_name_by_argument_name(input_arg_name)
        port_arg_map[input_name] = input_path
    return translate_parallel_command(command, port_arg_map)


def translate_parallel_command(command, port_arg_map):
    # In parallel module, input value is input_name, and input param name starts with '--input_fds'.
    # This function will translate input name to input path.
    # https://msdata.visualstudio.com/Vienna/_git/AzureMlCli?path=%2Fsrc%2Fazureml-parallel-run%2Fazureml_sys%2Fazureml_sys%2Fparallel_run%2Fjob_args.py&version=GBmaster
    for index, item in enumerate(command):
        if item.startswith('--input_fds_') and index + 1 < len(command) and \
                command[index + 1] in port_arg_map:
            command[index + 1] = port_arg_map[command[index + 1]]
    return command


@track(_get_logger)
def _prepare_module_run(node, working_dir, pipeline_parameters, module_to_node_mapping, input_futures=None):
    # Replace node inputs and parameters
    copy_node = copy.deepcopy(node)
    input_path = {}
    for input_name, input_value in copy_node.inputs.items():
        input_path[input_name] = _prepare_module_inputs(
            node.workspace, input_name, input_value.dset, working_dir,
            pipeline_parameters, module_to_node_mapping, input_futures)
    copy_node.set_inputs(**input_path)

    params_value = {}
    for param_name, param_value in copy_node._parameter_params.items():
        params_value[param_name] = _get_module_parameter(param_name, param_value, pipeline_parameters)
    copy_node.set_parameters(**params_value)
    return copy_node


def _get_module_parameter(param_name, param_value, pipeline_parameters):
    from .component import _InputBuilder
    if isinstance(param_value, PipelineParameter):
        return get_pipeline_param(param_name, param_value, pipeline_parameters)
    elif isinstance(param_value, _InputBuilder):
        return _get_module_parameter(param_name, param_value.dset, pipeline_parameters)


def _prepare_module_inputs(workspace, input_name, dset, working_dir,
                           pipeline_parameters, module_to_node_mapping, input_futures=None):
    if input_futures and dset in input_futures:
        if not input_futures[dset].done():
            print(f'{RUN_PREPARE_LOG}: download input dataset [ {input_name} ] starting...')
            input_futures[dset].result()
            print(f'{RUN_PREPARE_LOG}: download input dataset [ {input_name} ] completed...')
        return input_futures[dset].result()
    # Download dataset and replace node inputs to local data path
    from ._pipeline_run_orchestrator import WORKING_DIR
    from .component import _OutputBuilder, _InputBuilder
    if isinstance(dset, _InputBuilder):
        return _prepare_module_inputs(
            workspace, input_name, dset.dset, working_dir,
            pipeline_parameters, module_to_node_mapping, input_futures)
    if isinstance(dset, _OutputBuilder):
        return os.path.join(module_to_node_mapping[dset.module_instance_id][WORKING_DIR], OUTPUT_DIR_NAME, dset._name)
    elif isinstance(dset, DataReference) or isinstance(dset, FileDataset) or \
            isinstance(dset, DataPath) or isinstance(dset, DatasetConsumptionConfig) or \
            isinstance(dset, PipelineParameter):
        return _download_input_data(workspace, dset, working_dir, pipeline_parameters)
    elif isinstance(dset, str) or not dset:
        return dset
    else:
        raise ValueError(f"Unknown type {type(dset)} for node input dataset {input_name}")


def _download_input_data(workspace, dset, working_dir, pipeline_parameters=None, is_download=True):
    # Download module input dataset to local
    if isinstance(dset, PipelineParameter):
        default_value = dset.default_value if not pipeline_parameters or \
            (dset.name not in pipeline_parameters.keys()) else pipeline_parameters[dset.name]
        return _download_input_data(workspace, default_value, working_dir, pipeline_parameters)
    elif isinstance(dset, DataReference):
        data_store_name = dset.data_store_name
        path_on_data_store = dset.path_on_datastore
        blob_data_store = Datastore.get(workspace, data_store_name)
        target_path = Path(working_dir) / path_on_data_store
        if not is_download:
            return str(target_path)
        if target_path.exists():
            return str(target_path)
        blob_data_store.download(
            target_path=working_dir, prefix=path_on_data_store, overwrite=False)
        target_path.mkdir(exist_ok=True, parents=True)
        return str(target_path)
    elif isinstance(dset, FileDataset):
        dataset_id = dset.id
        dataset_name = dset.name
        target_path = Path(working_dir, dataset_name if dataset_name else dataset_id)
        if not is_download:
            return str(target_path)
        if target_path.exists():
            return str(target_path)
        dataset = Dataset.get_by_id(workspace, dataset_id)
        dataset.download(target_path=str(target_path), overwrite=False)
        return str(target_path)
    elif isinstance(dset, DataPath):
        path_on_data_store = dset._path_on_datastore
        target_path = Path(working_dir) / path_on_data_store
        if not is_download:
            return str(target_path)
        if target_path.exists():
            return str(target_path)
        dset._datastore.download(
            target_path=working_dir, prefix=path_on_data_store, overwrite=False)
        target_path.mkdir(exist_ok=True, parents=True)
        return str(target_path)
    elif isinstance(dset, DatasetConsumptionConfig):
        return _download_input_data(workspace, dset.dataset, working_dir, pipeline_parameters)
    elif isinstance(dset, str) or isinstance(dset, Path):
        # When generate command will check dset existence
        return dset
    else:
        raise ValueError('Input dataset is of unsupported type: {0}'.format(type(dset).__name__))


def get_pipeline_param(param_name, param_value, pipeline_parameters):
    default_value = pipeline_parameters[param_value.name] if pipeline_parameters and \
        param_value.name in pipeline_parameters.keys() else param_value.default_value
    if isinstance(default_value, int) or isinstance(default_value, str) or \
            isinstance(default_value, bool) or isinstance(default_value, float):
        return default_value
    else:
        raise ValueError('Node parameter is of unsupported type: {0}'.format(type(default_value).__name__))


@track(_get_logger)
def get_module_image(module, working_dir, image_futures):
    """
    Get module image to local

    If module image exists in image_futures, will wait for task of getting image completed.
    If not will execute getting module image.

    :param module: module
    :type module: azure.ml.component.Component
    :param working_dir: module image log store path
    :type working_dir: str
    :param image_futures: Dict of getting module image tasks
    :type image_futures: dict{(str, Future)}
    :return: module image info
    :rtype: azure.ml.component.debug._image.ModuleImage
    """
    from azure.ml.component.debug._image import ModuleImage
    module_image = ModuleImage(module, os.path.join(working_dir, IMAGE_DIR_NAME))
    image_name = module_image.image_details['dockerImage']['name']
    if image_futures and image_name in image_futures:
        if image_futures[image_name].running():
            print(f'{RUN_PREPARE_LOG}: get {module.name} image {image_name} starting...')
            image_name = image_futures[image_name].result()
        else:
            image_name = image_futures[image_name].result()
    else:
        print(f'{RUN_PREPARE_LOG}: get {module.name} image {image_name} starting...')
        image_name = module_image.get_module_image()
    module_image.image_name = image_name
    print(f'{RUN_PREPARE_LOG}: get {module.name} image {image_name} completed...')
    return module_image


@track(_get_logger)
def execute_module_in_local(command, environment, cwd, logger):
    """
    Execute command in subprocess and streaming log output in logger.

    :param command: execute command in container
    :type command: list
    :param environment: the environment variables for the new process
    :type environment: dict
    :param cwd: current directory when execute command
    :type cwd: str
    :param logger: log container output
    :type logger: azure.ml.component._module_run_helper.Logger
    :return command_result: is command execute success
    :rtype bool
    """
    environment.update(os.environ)
    process = subprocess.Popen(command, env=environment, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               bufsize=1, universal_newlines=True, encoding='utf-8')
    while True:
        exec_output = process.stdout.readline()
        if not exec_output and process.poll() is not None:
            break
        if exec_output:
            logger.write_message(exec_output)
        else:
            sleep(SLEEP_INTERVAL)
    logger.write_message('\n')
    return process.returncode == 0


@track(_get_logger)
def execute_module_in_container(command, volumes, environment, image, logger):
    """
    Execute command in container and streaming log container output to logger.

    :param image: the image to exec
    :type image: str
    :param command: execute command in container
    :type command: list
    :param volumes: volumes need to mount in container
    :type volumes: dict
    :param environment: Environment variables to set inside the container
    :type environment: dict
    :param logger: log container output
    :type logger: azure.ml.component._module_run_helper.Logger
    :return command_result: is command execute success
    :rtype bool
    """
    docker_client = get_docker_client()
    is_wsl_or_container = is_in_container() or is_in_wsl1()
    if is_wsl_or_container:
        container = docker_client.containers.create(
            image, working_dir=CONTAINER_MOUNT_SCRIPTS_PATH, environment=environment,
            stdin_open=True, privileged=True, tty=True)
    else:
        container = docker_client.containers.create(
            image, working_dir=CONTAINER_MOUNT_SCRIPTS_PATH, environment=environment,
            volumes=volumes, stdin_open=True, privileged=True, tty=True)
    try:
        container.start()
        if is_wsl_or_container:
            command_result, stdout = exec_command_in_wsl1_container(container, command, volumes, logger)
        else:
            command_result, stdout = container_exec_run(container, command, logger)
    except Exception:
        traceback.print_exc()
        return False
    finally:
        container.stop()
        if command_result == 0:
            container.remove()
    return command_result == 0


def _copy_from_docker(container, source, target):
    try:
        data_stream, _ = container.get_archive(source)
        tar_file = target + '.tar'
        with open(tar_file, 'wb') as f:
            for chunk in data_stream:
                f.write(chunk)
        with tarfile.open(tar_file, mode='r') as tar:
            for file_name in tar.getnames():
                tar.extract(file_name, os.path.dirname(target))
    except Exception as e:
        raise RuntimeError(e)
    finally:
        os.remove(tar_file)


def is_in_container():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )


def is_in_wsl1():
    process = subprocess.run("systemd-detect-virt -c", shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)
    return 'wsl' in process.stdout


def exec_command_in_wsl1_container(container, command, volumes, logger):
    """
        In WSL1 and container, will execute docker command in host machine, so folder in WSL1/container
        cannot mount in docker container. Using docker cp to replace mounting.
        :param container: container
        :type container: docker.container
        :param command: execute command in container
        :type command: list
        :param volumes: volumes need to mount in container
        :type volumes: dict
        :param logger: log container output
        :type logger: azure.ml.component._module_run_helper.Logger
        :return command_result: command run result, if not 0, may some error when execute
                stdout: log of executing command
        :rtype int, bytes
    """
    print('Warning: Running in WSL1 or container')
    # copy code and data to container
    for key, item in volumes.items():
        if not os.path.exists(key):
            continue
        if os.path.isdir(key):
            write_dir_in_container(container, item['bind'], key)
        else:
            with open(key, 'rb') as f:
                write_file_in_container(container, item['bind'], f.read())

    # execute command
    command_result, exec_output = container_exec_run(container, command, logger=logger)

    # copy reuslt to local
    for key, item in volumes.items():
        if item['bind'].startswith(CONTAINER_OUTPUT_PATH):
            _copy_from_docker(container, item['bind'], key)
    return command_result, exec_output


def container_exec_run(container, command, logger):
    # Create and start a container execution
    container_exec = docker.APIClient().exec_create(container.id, command)
    exec_output = docker.APIClient().exec_start(container_exec['Id'], stream=True)

    for line in exec_output:
        line = line.decode('utf-8')
        logger.write_message(line)
    logger.write_message('\n')
    # Get command exit code in container
    container_inspect = docker.APIClient().exec_inspect(container_exec['Id'])
    command_result = container_inspect['ExitCode']
    return command_result, exec_output


def download_datasets(datasource, pipeline_parameters, workspace, working_dir):
    input_dataset_futures = {}
    dataset_path_futures = {}
    executor = concurrent.futures.ThreadPoolExecutor()
    for item in datasource:
        if not isinstance(item, str):
            dataset_path = _download_input_data(workspace, item, working_dir, pipeline_parameters, is_download=False)
            if dataset_path not in dataset_path_futures:
                dataset_path_futures[dataset_path] = \
                    executor.submit(_download_input_data, workspace, item, working_dir, pipeline_parameters)
                input_dataset_futures[item] = dataset_path_futures[dataset_path]
    return input_dataset_futures


def prepare_nodes_image(node_list, image_future_dict, working_dir):
    from azure.ml.component.debug._image import ModuleImage
    executor = concurrent.futures.ThreadPoolExecutor()
    for module in node_list:
        module_image = ModuleImage(module, os.path.join(working_dir, IMAGE_DIR_NAME))
        image_name = module_image.image_details['dockerImage']['name']
        if image_name not in image_future_dict:
            image_future_dict[image_name] = executor.submit(module_image.get_module_image)
    return image_future_dict


def print_logfile(log_path, logger):
    if os.path.exists(log_path):
        # Convert log path to long path
        long_name = Path(log_path).resolve().absolute().as_posix()
        print_str = f"\n{long_name}\n{'=' * len(long_name)}\n"
        with open(log_path) as f:
            for line in f.readlines():
                print_str += line
        logger.print_to_terminal(print_str)


class Logger(object):
    _instance_lock = Lock()
    tid_to_loginfo = {}
    _instance = None

    def __new__(cls, *args, **kwargs):
        with Logger._instance_lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(Logger)
                cls._sys_stdout = sys.stdout
                cls._sys_stderr = sys.stderr
        return cls._instance

    def __init__(self, log_path, show_terminal=False, tracker=None):
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        tid = currentThread().ident
        loginfo = {
            # define logger file encoding using 'utf-8', else default encoding will be 'cp1252'
            LOG_FILE: open(log_path, "a", encoding='utf-8'),
            SHOW_TERMINAL: show_terminal,
            TRACKER: tracker,
            STOP_EVENT: Event(),
            MESSAGE: None
        }
        self.tid_to_loginfo[tid] = loginfo
        if tracker and tracker.track_run_history:
            loginfo[MESSAGE] = Queue()
            loginfo[UPLOAD_THREAD] = Thread(target=self._upload_logger_message, args=(tid,))
            loginfo[UPLOAD_THREAD].start()
        if sys.stdout != self:
            sys.stdout = self
        if sys.stderr != self:
            sys.stderr = self

    def set_show_terminal(self, show_terminal):
        tid = currentThread().ident
        self.tid_to_loginfo[tid][SHOW_TERMINAL] = show_terminal

    def get_log_path(self):
        tid = currentThread().ident
        return self.tid_to_loginfo[tid][LOG_FILE].name

    def write(self, message):
        if message and message != '\n':
            message = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {message} \n'
        else:
            return
        self.write_message(message)

    def write_message(self, message='\n'):
        tid = currentThread().ident
        if tid not in self.tid_to_loginfo:
            if hasattr(currentThread(), 'parent') and currentThread().parent.ident in self.tid_to_loginfo:
                tid = currentThread().parent.ident
            else:
                return
        if self.tid_to_loginfo[tid][SHOW_TERMINAL]:
            self._sys_stdout.write(message)
            self._sys_stdout.flush()
        self.tid_to_loginfo[tid][LOG_FILE].write(message)
        self.tid_to_loginfo[tid][LOG_FILE].flush()
        if self.tid_to_loginfo[tid][MESSAGE]:
            self.tid_to_loginfo[tid][MESSAGE].put(message)

    def flush(self):
        tid = currentThread().ident
        if tid in self.tid_to_loginfo:
            if self.tid_to_loginfo[tid][SHOW_TERMINAL]:
                self._sys_stdout.flush()
            self.tid_to_loginfo[tid][LOG_FILE].flush()

    def remove_current_thread(self):
        log_info = self.tid_to_loginfo.pop(currentThread().ident, None)
        if log_info:
            log_info[LOG_FILE].close()
            if log_info[MESSAGE]:
                log_info[MESSAGE].join()
            log_info[STOP_EVENT].set()
            if UPLOAD_THREAD in log_info:
                log_info[UPLOAD_THREAD].join()

        if len(self.tid_to_loginfo) == 0:
            sys.stdout = self._sys_stdout
            sys.stderr = self._sys_stderr

    def fileno(self):
        tid = currentThread().ident
        if tid in self.tid_to_loginfo.keys():
            return self.tid_to_loginfo[tid][LOG_FILE].fileno()
        else:
            raise ValueError(f'Cannot find thread_id: {tid} in Logger.')

    def print_to_terminal(self, message):
        # only print message on terminal
        self._sys_stdout.write(message)
        self._sys_stdout.flush()

    def _upload_logger_message(self, tid):
        queue = self.tid_to_loginfo[tid][MESSAGE]
        tracker = self.tid_to_loginfo[tid][TRACKER]
        stop_event = self.tid_to_loginfo[tid][STOP_EVENT]
        while True and not stop_event.isSet():
            try:
                upload_message = ''
                while not queue.empty():
                    upload_message = upload_message + queue.get(block=False)
                    queue.task_done()
            except Empty:
                pass
            except Exception as e:
                raise ValueError(f'Failed to upload execution info to run history log: {e}')
            finally:
                if upload_message:
                    tracker.append_run_history_log(upload_message)
                sleep(SLEEP_INTERVAL)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            traceback.print_exc()
        self.remove_current_thread()


def _get_and_start_run_with_definition(module, experiment, working_dir) -> Run:
    """ Starts a run with definition.

    :param module: Executed module
    :type module: azure.ml.component.Component
    :param experiment: Experiment
    :type azuerml.core.Experiment
    :param working_dir: The output path for module output info
    :type working_dir: str
    """
    # TODO: we may need to reuse the code from _commands in the future
    # Prepare run config
    run_id = str(uuid.uuid4())
    run_config = module._populate_runconfig(use_local_compute=True)
    arguments = module._build_arguments_for_run_config(run_config, run_id)
    run_config.arguments = copy.deepcopy(arguments)
    # Mount is not allowed with local compute
    for data_ref in run_config.data_references.values():
        data_ref.mode = 'download'
    for data in run_config.data.values():
        data.mechanism = 'download'

    try:
        return _submit_local_run_2_execution_service(module, experiment, run_config, run_id, working_dir)
    except BaseException:
        # If execution service doesn't support this kind of run, just submit an empty one.
        return Run._start_logging(experiment, outputs=working_dir, snapshot_directory=None)


def _submit_local_run_2_execution_service(module, experiment, run_config, run_id, working_dir) -> Run:
    import urllib3

    from azureml._restclient import RunClient
    from azureml._restclient.models import CreateRunDto
    from azureml._restclient.clientbase import ClientBase
    from azureml._execution._commands import _raise_request_error, _get_common_headers, _serialize_run_config_to_dict

    service_context = module.workspace.service_context
    service_arm_scope = "{}/experiments/{}".format(service_context._get_workspace_scope(), experiment.name)
    service_address = service_context._get_execution_url()

    definition = {
        'Configuration': _serialize_run_config_to_dict(run_config)
    }

    files = [
        ("files", ("definition.json", json.dumps(definition, indent=4, sort_keys=True)))
    ]

    headers = _get_common_headers()
    auth_header = module.workspace._auth_object.get_authentication_header()
    headers.update(auth_header)

    uri = service_address + "/execution/v1.0" + service_arm_scope + "/localrun"

    # Unfortunately, requests library does not take Queryparams nicely.
    # Appending run_id_query to the url for service to extract from it.

    run_id_query = urllib3.request.urlencode({"runId": run_id})
    uri += "?" + run_id_query

    response = ClientBase._execute_func(requests.post, uri, files=files, headers=headers)
    _raise_request_error(response, "starting run")

    # set run name with run client
    client = RunClient(service_context, experiment.name, run_id,
                       experiment_id=experiment.id)
    create_run_dto = CreateRunDto(run_id, name=module.name)
    run_dto = client.patch_run(create_run_dto)
    return Run(experiment=experiment, run_id=run_id, outputs=working_dir, _run_dto=run_dto)


class RunHistoryTracker:
    def __init__(self, run, track_run_history=True, path=None):
        self.run = run
        self.track_run_history = track_run_history
        if path and track_run_history:
            self.create_run_history_log(path)

    @classmethod
    @track(_get_logger)
    def from_run(cls, run, track_run_history, path=None):
        return cls(run, track_run_history, path)

    @classmethod
    @track(_get_logger)
    def with_definition(cls, experiment_name, module, working_dir, track_run_history, path=None):
        run = None
        if track_run_history:
            experiment = Experiment(module.workspace, experiment_name)
            run = _get_and_start_run_with_definition(module, experiment, working_dir)
        return cls(run, track_run_history, path)

    @classmethod
    def without_definition(cls, workspace, experiment_name, track_run_history, path=None):
        run = None
        if track_run_history:
            experiment = Experiment(workspace, experiment_name)
            run = Run._start_logging(experiment, snapshot_directory=None)
        return cls(run, track_run_history, path)

    def update_run_result_status(self, run_success, error_details=None):
        if self.run:
            if run_success:
                self.run.complete()
            else:
                self.run.fail(error_details=error_details)
            print('Finish uploading run status to run history')

    def get_run(self):
        return self.run

    def get_run_details_url(self):
        if self.run:
            return self.run._run_details_url

    def get_run_id(self):
        if self.run:
            return self.run.id

    def print_run_info(self):
        if self.run:
            print(f'RunId: {self.run.id}')
            print(f'Link to Azure Machine Learning Portal: {self.run.get_portal_url()}')

    def add_properties(self, properties):
        """
        Add immutable properties to the run.
        :param properties: The hidden properties stored in the run object.
        :type properties: dict
        """
        if self.run:
            self.run.add_properties(properties)

    def upload_run_output(self, module, working_dir):
        if self.run:
            print(f'{RUN_RELEASE_LOG}: upload {module.name} outputs to run history starting...')
            # Upload output to experiment
            for output_port_name in module.outputs.keys():
                output_port_path = os.path.join(working_dir, OUTPUT_DIR_NAME, output_port_name)
                if os.path.exists(output_port_path):
                    if os.path.isdir(output_port_path):
                        self.run.upload_folder(output_port_name, output_port_path)
                    else:
                        self.run.upload_file(output_port_name, output_port_path)
            print(f'{RUN_RELEASE_LOG}: upload {module.name} outputs to run history completed...')

    def upload_snapshot(self, snapshot_path):
        if self.track_run_history:
            print(f'{RUN_RELEASE_LOG}: upload snapshot to run history starting...')
            self.run.take_snapshot(snapshot_path)
            print(f'{RUN_RELEASE_LOG}: upload snapshot to run history completed...')

    @track(_get_logger)
    def upload_run_log(self, log_file_name, log_file_path):
        log_file_url = None
        if self.run:
            upload_log_file = self.run.upload_file(log_file_name, log_file_path)
            log_file_url = upload_log_file.artifact_content_information[log_file_name].content_uri
        return log_file_url

    def append_run_history_log(self, message):
        if self.run and hasattr(self, 'run_history_log_info'):
            run = self.run
            _run_artifacts_client = run._experiment.workspace.service_context._get_artifacts_restclient().artifact
            url = _run_artifacts_client.upload.metadata['url']
            path_format_arguments = {
                'subscriptionId': run._experiment.workspace.subscription_id,
                'resourceGroupName': run._experiment.workspace.resource_group,
                'workspaceName': run._experiment.workspace.name,
                'origin': 'ExperimentRun',
                'container': run._container,
                'path': self.run_history_log_info.path
            }
            url = _run_artifacts_client._client.format_url(url, **path_format_arguments)
            query_parameters = {'append': True}
            header_parameters = {'Content-Type': 'application/octet-stream'}
            request = _run_artifacts_client._client.post(url, query_parameters)
            response = _run_artifacts_client._client.send(
                request, header_parameters, message.encode('utf-8'), stream=False)

            if response.status_code not in [200]:
                raise ErrorResponseException(_run_artifacts_client._serialize, response)

    @track(_get_logger)
    def create_run_history_log(self, path):
        if self.run:
            run = self.run
            from azureml._restclient.models.artifact_dto import ArtifactDto
            _run_artifacts_client = run._experiment.workspace.service_context._get_artifacts_restclient().artifact
            artifact_dto = ArtifactDto(origin='ExperimentRun', container=run._container, path=path)
            # Create run artifact
            _run_artifacts_client.create(
                subscription_id=run._experiment.workspace.subscription_id,
                resource_group_name=run._experiment.workspace.resource_group,
                workspace_name=run._experiment.workspace.name,
                artifact_dto=artifact_dto)
            # Get run artifact info
            result = _run_artifacts_client.get_content_information(
                subscription_id=run._experiment.workspace.subscription_id,
                resource_group_name=run._experiment.workspace.resource_group,
                workspace_name=run._experiment.workspace.name,
                origin='ExperimentRun',
                container=run._container,
                path=path,
                raw=True
            )
            self.run_history_log_info = result.output

    def get_run_history_log_url(self):
        if hasattr(self, 'run_history_log_info'):
            return self.run_history_log_info.content_uri
        return None

    def get_child_tracker(self, name, path=None):
        if self.track_run_history:
            return RunHistoryTracker.from_run(
                run=self.run.child_run(name=name),
                track_run_history=self.track_run_history,
                path=path)
        else:
            return RunHistoryTracker(None, track_run_history=False)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.update_run_result_status(False, error_details=exc_val)


class ThreadWithParent(Thread):

    def __init__(self, *args, **kwargs):
        self.parent = currentThread()
        Thread.__init__(self, *args, **kwargs)
