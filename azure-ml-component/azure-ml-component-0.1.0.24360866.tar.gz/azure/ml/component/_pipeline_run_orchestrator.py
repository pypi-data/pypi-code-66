# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import os
import copy
from datetime import datetime
import concurrent.futures

from ._utils import _get_short_path_name
from .component import _OutputBuilder, _InputBuilder
from ._loggerfactory import _LoggerFactory, track
from ._module_run_helper import _module_run, update_visualizer, \
    RUN_STATUS, PARENT_NODE_ID, download_datasets, prepare_nodes_image, \
    EXECUTION_LOGFILE, snapshot_cache


NODE_ID = 'node_id'
STEP_PREFIX = 'prefix'
WORKING_DIR = 'working_dir'
RUN_ID = 'run_id'
EXECUTION_LOG = 'executionlogs.txt'

PIPELINE_STATUS = {
    'runStatus': None,
    'runDetailsUrl': None,
    'statusDetail': None,
    'startTime': None,
    'endTime': None
}

datetime_format = '%Y-%m-%d %H:%M:%S'
submit_log_format = '[{}] Submitting {} runs, first five are: {} \n'
complete_log_format = '[{}] Completing processing {}\n'
failed_log_format = '[{}] Execution of experiment failed, update experiment status and cancel running nodes.'

_logger = None


def _get_logger():
    global _logger
    if _logger is not None:
        return _logger
    _logger = _LoggerFactory.get_logger(__name__)
    return _logger


@track(_get_logger)
def _orchestrate_pipeline_run(pipeline, working_dir, module_node_to_graph_node_mapping, datasource, tracker=None,
                              visualizer=None, pipeline_parameters=None, show_output=False,
                              continue_on_step_failure=None, max_workers=None, use_docker=True):
    """
    Orchestrate pipeline run

    Orchestrating pipeline run to make steps executing in parallel. Firstly will submit no dependency
    steps to start pipeline run, using threadpool to parallel execute steps. When previous steps completed,
    will push no dependency steps to threadpool, until all steps completed.

    :param pipeline: Orchestrated pipeline
    :type pipeline: azure.ml.component.PipelineComponent
    :param working_dir: pipline run data and snapshot store path
    :type working_dir: str
    :param module_node_to_graph_node_mapping: mapping of module node to graph node
    :type module_node_to_graph_node_mapping: dict
    :param datasource: Input datasets of pipeline
    :type datasource: list
    :param tracker: Used for tracking run history.
    :type tracker: RunHistoryTracker
    :param visualizer: To show pipeline graph in notebook
    :type visualizer: azure.ml.component._widgets._visualize
    :param pipeline_parameters: An optional dictionary of pipeline parameter
    :type pipeline_parameters: dict({str:str})
    :param show_output: Indicates whether to show the pipeline run status on sys.stdout.
    :type show_output: bool
    :param continue_on_step_failure: Indicates whether to continue pipeline execution if a step fails.
        If True, only steps that have no dependency on the output of the failed step will continue execution.
    :type continue_on_step_failure: bool
    :param max_workers:  The maximum number of threads that can be used to execute pipeline steps.
        If max_workers is None, it will default to the number of processors on the machine.
    :type max_workers: int
    :param use_docker: If use_docker=True, will pull image from azure and run module in container.
                           If use_docker=False, will directly run module script.
    :type use_docker: bool
    :return: whether pipeline run successful finished
    :rtype: bool
    """
    # prepare for node run
    node_list, module_to_node_mapping = pipeline._expand_pipeline_nodes('', module_node_to_graph_node_mapping)
    node_dict = {node._instance_id: node for node in node_list}
    node_output_dict, begin_exec_node = _prepare_pipeline_run(node_dict)
    executed_nodes = []
    pipeline_run_success = True

    # start downloading node input datset
    input_futures = download_datasets(datasource, pipeline_parameters, pipeline.workspace, working_dir)

    # start getting beginning node images
    image_futures = {}
    if use_docker:
        begin_nodes = [node_dict[node_id] for node_id in begin_exec_node]
        prepare_nodes_image(begin_nodes, image_futures, working_dir)

    # start running node
    if visualizer:
        pipeline_status = update_pipeline_status('Running', run_details_url=tracker.get_run_details_url())
        update_visualizer(visualizer, PARENT_NODE_ID, pipeline_status)

    execution_log_path = os.path.join(working_dir, EXECUTION_LOG)
    with open(execution_log_path, 'w') as execution_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # start nodes execution
            futures = _execute_steps(executor, begin_exec_node, tracker, node_dict, working_dir,
                                     pipeline_parameters, module_to_node_mapping, show_output,
                                     visualizer, input_futures, image_futures,
                                     execution_file, node_output_dict, use_docker)

            current_futures = futures.keys()
            while current_futures:
                done_futures, current_futures = concurrent.futures.wait(
                    current_futures, return_when=concurrent.futures.FIRST_COMPLETED)
                # update running node task list
                next_node_list, pipeline_run_success = _handle_done_futures(
                    done_futures, futures, execution_file, executed_nodes, node_output_dict)
                if not pipeline_run_success and not continue_on_step_failure:
                    concurrent.futures.wait(current_futures, return_when=concurrent.futures.ALL_COMPLETED)
                    break
                else:
                    next_nodes = _find_next_run_node(next_node_list, executed_nodes, node_dict)
                    next_futures = _execute_steps(executor, next_nodes, tracker, node_dict, working_dir,
                                                  pipeline_parameters, module_to_node_mapping, show_output,
                                                  visualizer, input_futures, image_futures,
                                                  execution_file, node_output_dict, use_docker)
                    current_futures.update(next_futures.keys())
                    futures.update(next_futures)
    # upload pipeline log and get log url
    log_file_url = tracker.upload_run_log(EXECUTION_LOG, execution_log_path)
    if visualizer:
        result_status = 'Completed' if pipeline_run_success else 'Failed'
        update_visualizer(
            visualizer,
            PARENT_NODE_ID,
            update_pipeline_status(result_status, status=pipeline_status),
            log_file_url
        )
    # Remove long time no used snapshots in cache
    snapshot_cache.clean_up_snapshot_cache()
    return pipeline_run_success


def get_node_input_dset(input_dset):
    if isinstance(input_dset, _InputBuilder):
        return get_node_input_dset(input_dset.dset)
    else:
        return input_dset


def _prepare_pipeline_run(node_dict):
    node_output_dict = {}
    begin_exec_node = []
    for node in node_dict.values():
        pre_input_list = []
        for input in node.inputs.values():
            dset = get_node_input_dset(input.dset)
            if isinstance(dset, _OutputBuilder):
                pre_input_list.append(dset)
        if len(pre_input_list) == 0:
            begin_exec_node.append(node._instance_id)
        for input in pre_input_list:
            if input.module_instance_id not in node_output_dict.keys():
                node_output_dict[input.module_instance_id] = []
            node_output_dict[input.module_instance_id].append(node._instance_id)

    return node_output_dict, begin_exec_node


def _execute_steps(executor, steps, tracker, node_dict, working_dir, pipeline_parameters,
                   module_to_node_mapping, show_output, visualizer, input_futures,
                   image_futures, execution_file, node_output_dict, use_docker):
    futures = {}
    next_node_list = set()
    for node in steps:
        child_tracker = tracker.get_child_tracker(name=node_dict[node].name, path=EXECUTION_LOGFILE)
        submit_future = executor.submit(
            exec_node, node_dict[node], child_tracker, working_dir, pipeline_parameters,
            module_to_node_mapping, show_output, visualizer, input_futures, image_futures,
            node, use_docker)
        futures[submit_future] = {
            NODE_ID: node,
            RUN_ID: child_tracker.get_run_id()
        }
        if node in node_output_dict:
            next_node_list.update(node_output_dict[node])
    if len(steps) > 0:
        run_id_list = [value[RUN_ID] or value[NODE_ID] for value in futures.values()]
        execution_file.write(
            submit_log_format.format(datetime.now().strftime(datetime_format),
                                     len(steps),
                                     ','.join(run_id_list[0:5])))
    if use_docker:
        # prepare for getting next nodes image
        next_nodes = [node_dict[node_id] for node_id in next_node_list]
        prepare_nodes_image(next_nodes, image_futures, working_dir)
    return futures


def _find_next_run_node(next_node_list, executed_nodes, node_dict):
    next_nodes = set()
    for node_id in next_node_list:
        node = node_dict[node_id]
        node_inputs = [get_node_input_dset(input) for input in node.inputs.values()]
        if all([input.module_instance_id in executed_nodes
                for input in node_inputs if isinstance(input, _OutputBuilder)]):
            next_nodes.add(node._instance_id)
    return next_nodes


def _handle_done_futures(done_futures, futures, execution_file, executed_nodes, node_output_dict):
    # check and log step run status
    # if step completed get next executing node list
    next_node_list = set()
    pipeline_run_success = True
    for future in done_futures:
        if future.result() != 'Completed':
            pipeline_run_success = False
            execution_file.write(failed_log_format.format(datetime.now().strftime(datetime_format)))
            continue
        node_id = futures[future][NODE_ID]
        execution_file.write(
            complete_log_format.format(
                datetime.now().strftime(datetime_format),
                f'run id {futures[future][RUN_ID]}' if futures[future][RUN_ID] else f'node id {node_id}'))
        executed_nodes.append(node_id)
        if node_id in node_output_dict:
            next_node_list.update(node_output_dict[node_id])
    return next_node_list, pipeline_run_success


def update_pipeline_status(pipeline_status, status=None, run_details_url=None):
    if not status:
        status = copy.deepcopy(PIPELINE_STATUS)
    if run_details_url:
        status['runDetailsUrl'] = run_details_url

    status['runStatus'] = RUN_STATUS[pipeline_status]

    if pipeline_status == 'Running' and not status['startTime']:
        status['startTime'] = datetime.now().isoformat()
    elif pipeline_status == 'Completed' or pipeline_status == 'Failed':
        status['endTime'] = datetime.now().isoformat()
    return status


def trans_node_name(node_name, node_id=None):
    if node_id:
        return f'{node_name.strip()}_{node_id}'
    else:
        return f'{node_name.strip()}'


def exec_node(node, tracker, working_dir, pipeline_parameters, module_to_node_mapping,
              show_output, visualizer, input_futures, image_futures, node_id, use_docker):
    try:
        node_run_filename = trans_node_name(node.name, tracker.get_run_id() or node_id)
        node_working_dir = _get_short_path_name(
            os.path.join(working_dir, module_to_node_mapping[node._instance_id][STEP_PREFIX], node_run_filename),
            create_dir=True)
        status = _module_run(
            module=node,
            working_dir=node_working_dir,
            tracker=tracker,
            use_docker=use_docker,
            node_id=module_to_node_mapping[node._instance_id][NODE_ID],
            visualizer=visualizer,
            show_output=show_output,
            module_to_node_mapping=module_to_node_mapping,
            data_dir=working_dir,
            pipeline_parameters=pipeline_parameters,
            input_futures=input_futures,
            image_futures=image_futures)
        if status != 'Completed':
            raise RuntimeError(f'Step "{node_run_filename}" run failed.')
        module_to_node_mapping[node._instance_id][WORKING_DIR] = node_working_dir
    except Exception as e:
        print(e)
        print(f'{node.name} run failed, exception: {str(e)}')
        return 'Failed'
    return status
