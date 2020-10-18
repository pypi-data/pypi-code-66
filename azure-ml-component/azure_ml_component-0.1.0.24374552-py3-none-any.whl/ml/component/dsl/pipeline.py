# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""A decorator which builds a :class:azure.ml.component.Pipeline."""
import sys
import uuid

from inspect import signature, Parameter
from functools import wraps
from typing import Callable, Any, TypeVar, Union

from azureml.data.abstract_dataset import AbstractDataset
from azureml.data.data_reference import DataReference

from .. import Component, PipelineComponent
from .._loggerfactory import _LoggerFactory, _PUBLIC_API, track
from .._pipeline_parameters import PipelineParameter
from ._pipeline_stack import _pipeline_stack
from ..component import _InputBuilder, _OutputBuilder
from ._pipeline_definition_stack import _pipeline_definition_stack
from .._pipeline_validator import PipelineValidator, ValidationError
from .._sub_pipeline_info_builder import _build_sub_pipeline_definition, _correct_default_compute_target,\
    _correct_default_data_store
from .._telemetry import WorkspaceTelemetryMixin

_logger = None


def _get_logger():
    global _logger
    if _logger is not None:
        return _logger
    _logger = _LoggerFactory.get_logger(__name__)
    return _logger


def _get_pipeline_parameter(key, value):
    # return value if it's already pipeline parameter
    if isinstance(value, PipelineParameter):
        return value
    return PipelineParameter(key, value)


def _build_sub_pipeline_parameter(func, args, kwargs):
    def all_p(parameters):
        for value in parameters.values():
            yield value

    def wrap_arg_value(arg_name, arg):
        if isinstance(arg, _InputBuilder) or isinstance(arg, _OutputBuilder) \
                or isinstance(arg, AbstractDataset) or isinstance(arg, DataReference) or isinstance(arg,
                                                                                                    PipelineParameter):
            return _InputBuilder(arg, arg_name)
        else:
            return _get_pipeline_parameter(arg_name, arg)

    # transform args
    transformed_args = []
    parameters = all_p(signature(func).parameters)
    for arg in args:
        transformed_args.append(wrap_arg_value(parameters.__next__().name, arg))

    transformed_kwargs = {key: wrap_arg_value(key, value) for key, value in kwargs.items()}
    # transform default values
    for left_args in parameters:
        if left_args.name not in transformed_kwargs.keys() and left_args.default is not Parameter.empty:
            transformed_kwargs[left_args.name] = wrap_arg_value(left_args.name, left_args.default)
    return transformed_args, transformed_kwargs


def _build_pipeline_parameter(is_sub_pipeline, func, args, kwargs):
    # if this is a sub pipeline, we will wrap the arg value with _InputBuilder
    # so that we can keep sub pipeline's ports to inside nodes' ports mapping
    if is_sub_pipeline:
        return _build_sub_pipeline_parameter(func, args, kwargs)

    # transform args
    transformed_args = []

    def all_params(parameters):
        for value in parameters.values():
            yield value

    parameters = all_params(signature(func).parameters)
    for arg in args:
        transformed_args.append(_get_pipeline_parameter(parameters.__next__().name, arg))

    # transform kwargs
    transformed_kwargs = {key: _get_pipeline_parameter(key, value) for key, value in kwargs.items()}

    # transform default values
    for left_args in parameters:
        if left_args.name not in transformed_kwargs.keys() and left_args.default is not Parameter.empty:
            transformed_kwargs[left_args.name] = _get_pipeline_parameter(left_args.name, left_args.default)

    return transformed_args, transformed_kwargs


# hint vscode intellisense
_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])


def pipeline(name=None, description=None, default_compute_target=None, default_datastore=None):
    """Build a pipeline which contains all nodes and sub-pipelines defines inside of the function.

    .. remarks::
        The following example shows how to create a pipeline using this decorator.

        .. code-block:: python

            # sub-pipeline defined with decorator
            @dsl.pipeline(name='sub pipeline', description='sub pipeline description')
            def sub_pipeline(pipeline_parameter1, pipeline_parameter2):
                # module1 and module2 will be add into built pipeline
                module1 = xxx
                module2 = xxx
                # Pipeline decorated function need to return outputs, the actual returned pipeline will have this
                # output
                # In this case, sub_pipeline has two outputs: module1's output1 and module2's output1, and renamed
                # them into 'renamed_output1' and 'renamed_output2'
                return {'renamed_output1': module1.outputs.output1, 'renamed_output2': module2.outputs.output1}

            # parent pipeline defined with decorator
            @dsl.pipeline(name='pipeline', description='pipeline description')
            def parent_pipeline(pipeline_parameter1):
                # module3 and sub_pipeline1 will be add into built pipeline
                module3 = xxx
                # sub_pipeline is called inside of a pipeline decorator, param1 and param2 won't be replaced with
                # pipeline parameter, this call returns a pipeline with nodes=[module1, module2] and
                # outputs=module2.outputs
                sub_pipeline1 = sub_pipeline(param1, param2)
                # No return value means the actual returned pipeline won't have outputs

            # sub_pipeline isn't called inside of a pipeline decorator, param1 and param2 will be replaced with
            # pipeline
            # parameter, this call returns a pipeline with nodes=[module1, module2], outputs=module2.outputs and
            # pipeline_parameters={'pipeline_parameter1': param1, 'pipeline_parameter2': param2}
            sub_pipeline2 = sub_pipeline(param1, param2)

            # This call returns a pipeline with nodes=[sub_pipeline1, module3], outputs={} and
            # pipeline_parameters={'pipeline_parameter1': param1}
            pipeline1 = parent_pipeline(param1)

            Parameters defined by in user function will be transformed into
            :class`azureml.pipeline.core.PipelineParameter`.
            If there are nested pipelines decorators, only the parameters of the outermost user function will be
             transformed into PipelineParameter.

    :param name: the name of the built pipeline
    :type: str
    :param description: the description of the built pipeline
    :type: str
    :param default_compute_target: The compute target of built pipeline.
        May be a compute target object or the string name of a compute target on the workspace.
        The priority of compute target assignment goes: module's run config > sub pipeline's default compute target >
        parent pipeline's default compute target.
        Optionally, if the compute target is not available at pipeline creation time, you may specify a tuple of
        ('compute target name', 'compute target type') to avoid fetching the compute target object (AmlCompute
        type is 'AmlCompute' and RemoteCompute type is 'VirtualMachine').
    :type: default_compute_target: azureml.core.compute.DsvmCompute
                        or azureml.core.compute.AmlCompute
                        or azureml.core.compute.RemoteCompute
                        or azureml.core.compute.HDInsightCompute
                        or str
                        or tuple
    :param default_datastore: The default datastore of pipeline.
    :type default_datastore: str or azureml.core.Datastore
    """
    def pipeline_decorator(func: _TFunc) -> _TFunc:
        definition_id = str(uuid.uuid4())
        parent_definition_id = None
        # We use this stack to store the dsl pipeline definition hierarchy
        if not _pipeline_definition_stack.is_empty():
            parent_definition_id = _pipeline_definition_stack.top().id

        # the pipeline definition should be initialized before the pipeline is initialized in dsl case
        # so that we can keep the pipeline's parameters list
        pipeline_definition = _build_sub_pipeline_definition(name=name, description=description,
                                                             default_compute_target=default_compute_target,
                                                             default_data_store=default_datastore, id=definition_id,
                                                             parent_definition_id=parent_definition_id,
                                                             from_module_name=func.__module__,
                                                             parameters=signature(func).parameters.values(),
                                                             func_name=func.__name__)
        pipeline_locals_data = {}

        @wraps(func)
        def wrapper(*args, **kwargs) -> PipelineComponent:
            # check if is sub pipeline
            is_sub_pipeline = not _pipeline_stack.is_empty()

            original_profiler = sys.getprofile()

            def tracer(frame, event, arg):
                if event != 'return':
                    return
                nonlocal pipeline_locals_data
                pipeline_locals_data = frame.f_locals.copy()

            @track(_get_logger, activity_type=_PUBLIC_API, activity_name="pipeline_decorator")
            def construct_top_level_pipeline(*_args, **_kwargs):
                current_pipeline = construct_sub_pipeline(*_args, **_kwargs)
                _LoggerFactory.add_track_dimensions(_get_logger(), current_pipeline._get_telemetry_values(
                    additional_value={
                        'pipeline_parameters_count': len([x for x in args if isinstance(x, PipelineParameter)])
                    },
                    on_create=True))
                return current_pipeline

            # Note: no @track() for construct_sub_pipeline can avoid FatalError. Because:
            # 1.We are using azureml.telemetry to log the pipeline information, @track(_get_logger), which have deeper
            # call stack so it will hit RecursionError, meanwhile, it will catch all exceptions to avoid break the
            # execution of user function, so RecursionError will be caught and ignored;
            # 2.According to Python implementation(https://github.com/python/cpython/blob/master/Include/ceval.h#L48),
            # once RecursionError is raised but caught, then stackoverflow, the interpreter aborts with a FatalError,
            # which is not expected;
            def construct_sub_pipeline(*_args, **_kwargs):
                # add current pipeline into stack
                current_pipeline = PipelineComponent(nodes=[], name=name, description=description,
                                                     default_compute_target=default_compute_target,
                                                     default_datastore=default_datastore, _use_dsl=True)
                _pipeline_stack.push(current_pipeline)
                _pipeline_definition_stack.push(pipeline_definition)
                try:
                    _args, _kwargs = _build_pipeline_parameter(is_sub_pipeline, func, _args, _kwargs)
                    sys.setprofile(tracer)
                    outputs = func(*_args, **_kwargs)
                    sys.setprofile(original_profiler)
                    current_pipeline._save_node_locals(pipeline_locals_data)
                except RecursionError as e:
                    cycles = PipelineValidator.validate_pipeline_cycle(_pipeline_definition_stack)
                    raise ValidationError(message="Detected pipeline recursion, pipelines: {}".format(cycles),
                                          error_type=ValidationError.PIPELINE_RECURSION) from e
                finally:
                    # pop current pipeline out of stack
                    _pipeline_stack.pop()
                    _pipeline_definition_stack.pop()
                    # Nodes are added into the pipeline, we can now extract the workspace info from the pipeline.
                    _LoggerFactory.add_track_dimensions(_get_logger(),
                                                        WorkspaceTelemetryMixin._get_telemetry_value_from_workspace(
                                                            current_pipeline.workspace))

                # update current pipeline's outputs, then return it
                if outputs is None:
                    outputs = {}
                current_pipeline._set_outputs(outputs)
                current_pipeline._set_inputs()
                current_pipeline._build_pipeline_func_parameters(func, args, kwargs)

                # current default compute target with pipeline resolved info
                _correct_default_compute_target(pipeline_definition, current_pipeline._get_default_compute_target())
                _correct_default_data_store(pipeline_definition, current_pipeline.default_datastore)
                # set current pipeline's definition
                current_pipeline._pipeline_definition = pipeline_definition

                return current_pipeline

            if is_sub_pipeline:
                return construct_sub_pipeline(*args, **kwargs)
            return construct_top_level_pipeline(*args, **kwargs)

        return wrapper

    return pipeline_decorator


def _try_to_add_node_to_current_pipeline(node: Union[Component, PipelineComponent]):
    if _pipeline_stack.size() > 0:
        _pipeline_stack.top()._add_node(node)


def _is_pipeline_stack_empty():
    return _pipeline_stack.is_empty()
