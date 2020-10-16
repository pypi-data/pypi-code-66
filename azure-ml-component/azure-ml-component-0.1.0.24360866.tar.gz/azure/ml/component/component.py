# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains classes for creating and managing reusable computational units of an Azure Machine Learning pipeline.

Component allow you to create computational units, which can have inputs, outputs, and rely on parameters
and an environment configuration to operate, e.g. ContainerComponent which runs in a container.

Several component can also composites to form a PipelineComponent.

Component are designed to be reused in different jobs and can evolve to adapt a specific computation logic
to different use cases. Anonymous Component can be used in fast iterations to improve an algorithm,
and once the goal is achieved, the algorithm is usually published as a registered component to enable reuse.
"""

import importlib
import inspect
import json
import os
from pathlib import Path
import tempfile
import time
import types
from typing import Any, List, Callable, Mapping
import uuid

from azure.ml.component._api._api import _dto_2_definition
from azure.ml.component._restclients.service_caller_factory import _DesignerServiceCallerFactory
from azureml.core import Workspace, Datastore, Experiment, ScriptRunConfig
from azureml.core.run import Run
from azureml.core.runconfig import RunConfiguration, Data
from azureml.data.abstract_dataset import AbstractDataset
from azureml.data.tabular_dataset import TabularDataset
from azureml.data.abstract_datastore import AbstractDatastore
from azureml.data.dataset_consumption_config import DatasetConsumptionConfig
from azureml.data.data_reference import DataReference
from azureml.exceptions._azureml_exception import UserErrorException

from .core._component_definition import ContainerComponentDefinition
from .core._run_settings_definition import RunSettingsDefinition, K8sRunSettingsDefinition
from ._attr_dict import _AttrDict
from .debug._constants import DATA_REF_PREFIX
from ._dynamic import KwParameter, create_kw_method_from_parameters
from ._component_func import to_component_func, get_dynamic_input_parameter, get_dynamic_param_parameter
from ._loggerfactory import _LoggerFactory, _PUBLIC_API, track
from ._module_dto import ModuleDto
from ._module_run_helper import _module_run
from ._module_run_helper import _prepare_module_snapshot
from ._module_run_helper import translate_parallel_command_by_module
from ._module_run_helper import translate_mpi_command_by_module
from ._module_run_helper import RunHistoryTracker
from ._module_run_helper import EXECUTION_LOGFILE
from ._module_registration import _load_anonymous_module, _register_module_from_yaml
from ._module_validator import ModuleValidator, ValidationError
from ._telemetry import TelemetryMixin, WorkspaceTelemetryMixin
from ._pipeline_parameters import PipelineParameter
from ._pipeline_data import PipelineData, DatasetRegistration
from ._run_settings import _RunSettings, _K8sRunSettings, set_compute_field
from ._utils import _sanitize_python_variable_name, _get_or_sanitize_python_name, _get_short_path_name

INPUT_TYPES = ['LocalPath', 'Dataset', 'Uri', 'Artifact']
_logger = None


def _get_logger():
    global _logger
    if _logger is not None:
        return _logger
    _logger = _LoggerFactory.get_logger(__name__)
    return _logger


class _InputBuilder(TelemetryMixin):
    """Define the inputs of a Component."""

    AVAILABLE_MODE = ['mount', 'download', 'direct']

    def __init__(self, dset, name: str, mode=None, owner=None):
        super().__init__()
        self._dset = dset
        self._name = name
        self._owner = owner
        mode = 'direct' if isinstance(dset, TabularDataset) else 'mount'
        self._mode = mode

    @track(_get_logger, activity_type=_PUBLIC_API, activity_name="input_configure")
    def configure(self, mode='mount'):
        """
        Use this method to configure the input.

        :param mode: The mode that will be used for this input. Available options are
            'mount' and 'download'.
        :type mode: str
        """
        if mode not in self.AVAILABLE_MODE:
            raise UserErrorException('Invalid mode: {}'.format(mode))

        if self._owner is not None:
            self._owner._specify_input_mode = True
        self._mode = mode

    @property
    def name(self):
        """
        Name of the input.

        :return: Name.
        :rtype: str
        """
        return self._name

    @property
    def mode(self):
        """
        Mode of the input.

        :return: Mode.
        :rtype: str
        """
        return self._mode

    @property
    def dset(self):
        return self._dset

    def _is_dset_data_source(self):
        """Indicate whether the internal dset is a real data source."""
        if isinstance(self.dset, _InputBuilder):
            return self.dset._is_dset_data_source()
        else:
            return self.dset is not None and not isinstance(self.dset, _OutputBuilder) \
                and not isinstance(self.dset, PipelineData)

    def _get_internal_data_source(self):
        """Get the dset iterativly until the dset is not an _InputBuilder."""
        if isinstance(self.dset, _InputBuilder):
            return self.dset._get_internal_data_source()
        else:
            return self.dset

    def build(self):
        from .pipeline_component import PipelineComponent
        if isinstance(self._dset, PipelineParameter):
            return self._dset
        if isinstance(self._dset, AbstractDataset):
            if self._mode == 'mount':
                return self._dset.as_named_input(self._name).as_mount()
            elif self._mode == 'download':
                return self._dset.as_named_input(self._name).as_download()
            elif self._mode == 'direct':
                return self._dset.as_named_input(self._name)
        elif isinstance(self._dset, _OutputBuilder):
            return self._dset.last_build
        elif isinstance(self._dset, _InputBuilder):
            # usually, the _dset should always comes from a source or a output
            # the _dest may be _InputBuilder only to describe that
            # the destination comes from a specific subgraph dummy input port
            return self._dset.build()
        elif isinstance(self._dset, Component) or isinstance(self._dset, PipelineComponent):
            output_len = len(self._dset.outputs.values()) \
                if self._dset.outputs is not None else 0
            if output_len != 1:
                raise UserErrorException('{0} output(s) found of specified module/pipeline "{1}",'
                                         ' exactly 1 output required.'.format(output_len, self._dset.name))
            self._dset = list(self._dset.outputs.values())[0]
            return self._dset.last_build
        elif isinstance(self._dset, _AttrDict):
            output_len = len(self._dset.values())
            if output_len != 1:
                raise UserErrorException('{0} output(s) found of specified outputs,'
                                         ' exactly 1 output required.'.format(output_len))
            self._dset = list(self._dset.values())[0]
            return self._dset.last_build
        else:
            return self._dset

    def _get_telemetry_values(self):
        return self._owner._get_telemetry_values()


class _OutputBuilder(TelemetryMixin):
    """Define the output of a Component."""

    AVAILABLE_MODE = ['mount', 'upload']

    def __init__(self, name: str, datastore=None, output_mode='mount', port_name=None,
                 owner=None):
        super().__init__()
        self._datastore = datastore
        self._name = name
        self._output_mode = output_mode
        self._last_build = None
        self._port_name = port_name
        self._owner = owner
        self._dataset_registration = None

    @track(_get_logger, activity_type=_PUBLIC_API, activity_name="output_configure")
    def configure(self, datastore=None, output_mode='mount'):
        """
        Use this method to configure the output.

        :param datastore: The datastore that will be used to construct PipelineData.
        :type datastore: azureml.core.datastore.Datastore
        :param output_mode: Specifies whether the producing step will use "upload" or "mount"
            method to access the data.
        :type output_mode: str
        """
        if datastore is not None:
            if not isinstance(datastore, AbstractDatastore):
                raise UserErrorException(
                    'Invalid datastore type. Use azureml.core.Datastore for datastore construction.')
            self._datastore = datastore
            if self._owner is not None:
                self._owner._specify_output_datastore = True

        if output_mode != 'mount':
            if output_mode not in self.AVAILABLE_MODE:
                raise UserErrorException('Invalid mode: {}'.format(output_mode))

            self._output_mode = output_mode
            if self._owner is not None:
                self._owner._specify_output_mode = True

    @property
    def datastore(self):
        return self._datastore

    @property
    def output_mode(self):
        """
        Output mode that will be used to construct PipelineData.

        :return: Output mode.
        :rtype: str
        """
        return self._output_mode

    @property
    def port_name(self):
        """Return the output display name."""
        return self._port_name

    @property
    def module_instance_id(self):
        """Specify which module instance build this Output."""
        return self._owner._instance_id

    @property
    def last_build(self):
        return self._last_build

    def build(self, producer=None, default_datastore=None):
        if self._datastore is None:
            self._datastore = default_datastore
        if self._datastore is None:
            raise ValueError("datastore is required")

        self._last_build = PipelineData(self._port_name, datastore=self._datastore, output_mode=self._output_mode,
                                        dataset_registration=self._dataset_registration)
        self._last_build._set_producer(producer)
        self._last_build._set_port_name(self._port_name)
        return self._last_build

    @track(_get_logger, activity_type=_PUBLIC_API)
    def register_as(self, name, create_new_version: bool = True):
        """
        Register the output dataset to the workspace.

        .. remarks::

            Registration can only be applied to output but not input, this means if you only pass the object returned
            by this method to the inputs parameter of a pipline step, nothing will be registered. You must pass the
            object to the outputs parameter of a pipeline step for the registration to happen.

        :param name: The name of the registered dataset once the intermediate data is produced.
        :type name: str
        :param create_new_version: Whether to create a new version of the dataset if the data source changes. Defaults
            to True. By default, all intermediate output will output to a new location when a pipeline runs, so
            it is highly recommended to keep this flag set to True.
        :type create_new_version: bool
        :return:
        """
        self._dataset_registration = DatasetRegistration(name=name, create_new_version=create_new_version)

    def _get_telemetry_values(self):
        return self._owner._get_telemetry_values()


class _ComponentLoadSource(object):
    UNKNOWN = 'unknown'
    REGISTERED = 'registered'
    FROM_YAML = 'from_yaml'
    FROM_FUNC = 'from_func'
    FROM_NOTEBOOK = 'from_notebook'


class Component(WorkspaceTelemetryMixin):
    r"""
    An operational unit that can be used to produce a pipeline.

    A pipeline consists of a series of `azure.ml.component.Component` nodes.

    Note that you should not use the constructor yourself. Use :meth:`azure.ml.component.Component.load`
    and related methods to acquire the needed `azure.ml.component.Component`.

    .. remarks::

        This main functionality of Component class resides at where we call "component function".
        A "component function" is essentially a function that you can call in Python code, which has parameters and
        return value that mimics the component definition in Azure Machine Learning.

        The following example shows how to create a pipeline using publish methods of the
        :class:`azure.ml.component.Component` class:


    For more information about components, see:

    * `What's an azure ml component <https://github.com/Azure/DesignerPrivatePreviewFeatures>`_

    * `Define a component using component specs <https://aka.ms/azureml-component-specs>`_
    """

    def __init__(self, _workspace: Workspace, _module_dto: ModuleDto, _init_params: Mapping[str, str],
                 _module_name: str, _load_source: str):
        """
        Initiate a component.

        :param _workspace: (Internal use only.) The workspace object this component will belong to.
        :type _workspace: azureml.core.Workspace
        :param _module_dto: (Internal use only.) The ModuleDto object.
        :type _module_dto: azure.ml.component._module_dto
        :param _init_params: (Internal use only.) The init params will be used to initialize inputs and parameters.
        :type _init_params: dict
        """
        WorkspaceTelemetryMixin.__init__(self, workspace=_workspace)
        self._module_name = _module_name
        self._workspace = _workspace
        self._module_dto = _module_dto
        self.defintion = None
        self._name_to_argument_name_mapping = _module_dto.module_python_interface.get_param_name_to_argument_name_map()
        # todo: set component definition
        self._component_def = None
        self._load_source = _load_source
        if "://" in self._module_name:
            self._namespace, self._short_name = self._module_name.split("://")
        else:
            self._namespace = self._module_dto.namespace
            self._short_name = self._module_name
        self.__doc__ = self._module_dto.description if self._module_dto.description else ""

        # Generate an id for every component instance
        self._instance_id = str(uuid.uuid4())

        self._init_public_interface(_init_params)

        run_setting_definition = RunSettingsDefinition.from_dto_runsettings(_module_dto.run_setting_parameters)
        self._runsettings = _RunSettings(run_setting_definition, self._module_dto.module_name, self._workspace, self)

        k8s_run_settings_definition = K8sRunSettingsDefinition.from_dto_runsettings(
            self._module_dto.run_setting_parameters,
        )
        self._k8srunsettings = _K8sRunSettings(k8s_run_settings_definition, self) \
            if k8s_run_settings_definition else None

        self._init_dynamic_method()
        self._regenerate_output = None

        # Add current component to global parent pipeline if there is one
        from .dsl.pipeline import _try_to_add_node_to_current_pipeline
        _try_to_add_node_to_current_pipeline(self)

        # Telemetry
        self._specify_input_mode = False
        self._specify_output_mode = False
        self._specify_output_datastore = False
        self._specify_runsettings = False
        self._specify_k8srunsettings = False

    #  region Private Methods

    def _init_public_interface(self, init_params):
        # Inputs
        interface = self._module_dto.module_entity.structured_interface
        self._interface_inputs = interface.inputs
        self._pythonic_name_to_input_map = {
            _get_or_sanitize_python_name(i.name, self._module_dto.module_python_interface.inputs_name_mapping):
                i.name for i in self._interface_inputs
        }

        input_builder_map = {k: _InputBuilder(v, k, owner=self) for k, v in init_params.items()
                             if k in self._pythonic_name_to_input_map.keys()}
        self._inputs = _AttrDict(input_builder_map)

        # Parameters
        self._interface_parameters = interface.parameters
        self._pythonic_name_to_parameter_map = {
            _get_or_sanitize_python_name(
                parameter.name,
                self._module_dto.module_python_interface.parameters_name_mapping):
            parameter.name for parameter in self._interface_parameters
        }

        self._parameter_params = {k: v for k, v in init_params.items()
                                  if k in self._pythonic_name_to_parameter_map.keys()}

        # Outputs
        self._interface_outputs = interface.outputs
        self._pythonic_name_to_output_map = {
            _get_or_sanitize_python_name(i.name, self._module_dto.module_python_interface.outputs_name_mapping):
                i.name for i in self._interface_outputs
        }

        output_builder_map = {k: _OutputBuilder(k, port_name=self._pythonic_name_to_output_map[k], owner=self)
                              for k in self._pythonic_name_to_output_map.keys()}
        self._outputs = _AttrDict(output_builder_map)

    def _init_dynamic_method(self):
        """Update methods set_inputs/set_parameters according to the component input/param definitions."""
        transformed_inputs = self._module_dto.get_transformed_input_params(return_yaml=True)
        self.set_inputs = create_kw_method_from_parameters(
            self.set_inputs, transformed_inputs,
        )
        transformed_parameters = [
            # Here we set all default values as None to avoid overwriting the values by default values.
            KwParameter(name=param.name, default=None, annotation=param.annotation, _type=param._type)
            for param in self._module_dto.get_transformed_parameter_params(return_yaml=True)
        ]
        self.set_parameters = create_kw_method_from_parameters(
            self.set_parameters, transformed_parameters,
        )

    def _build_outputs_map(self, producer=None, default_datastore=None) -> Mapping[str, Any]:
        # output name -> DatasetConsumptionConfig
        _output_map = {}
        for key, val in self._outputs.items():
            if val is None:
                continue
            _output_map[self._pythonic_name_to_output_map[key]] = val.build(producer, default_datastore)

        return _output_map

    def _build_inputs_map(self) -> Mapping[str, Any]:
        # input name -> DatasetConsumptionConfig
        _inputs_map = {}

        for key, val in self._inputs.items():
            if val is None:
                continue
            build = val.build()
            if build is None:
                continue
            _inputs_map[self._pythonic_name_to_input_map[key]] = build

        return _inputs_map

    def _build_params(self) -> Mapping[str, Any]:
        _params = {}

        for key, val in self._parameter_params.items():
            if val is None:
                continue
            if key in self._pythonic_name_to_parameter_map.keys():
                _params[self._pythonic_name_to_parameter_map[key]] = val
        return _params

    def _resolve_compute(self, default_compute, is_local_run=False):
        """
        Resolve compute to tuple.

        :param default_compute: pipeline compute specified.
        :type default_compute: tuple(name, type)
        :param is_local_run: whether component execute in local
        :type is_local_run: bool
        :return: (resolve compute, use_module_compute)
        :rtype: tuple(tuple(name, type), bool)
        """
        if not isinstance(default_compute, tuple):
            raise TypeError("default_compute must be a tuple")

        runsettings = self._runsettings
        target = runsettings.target

        if target is None or target == 'local':
            if default_compute[0] is None and not is_local_run:
                raise UserErrorException("A compute target must be specified")
            return default_compute, False

        if isinstance(target, tuple):
            return target, True
        elif isinstance(target, str):
            default_compute_name, _ = default_compute
            if target == default_compute_name:
                return default_compute, True

            # try to resolve
            _targets = self._workspace.compute_targets
            target_in_workspace = _targets.get(target)
            if target_in_workspace is None:
                print('target={}, not found in workspace, assume this is an AmlCompute'.format(target))
                return (target, "AmlCompute"), True
            else:
                return (target_in_workspace.name, target_in_workspace.type), True
        else:
            return target, True

    def _get_telemetry_values(self, compute_target=None, additional_value=None):
        """
        Get telemetry value out of a Component.

        The telemetry values include the following entries:

        * load_source: The source type which the component node is loaded.
        * specify_input_mode: Whether the input mode is being by users.
        * specify_output_mode: Whether the output mode is being by users.
        * specify_output_datastore: Whether the output datastore is specified by users.
        * specify_runsettings: Whether the runsettings is specified by users.
        * specify_k8srunsettings: Whether the k8srunsettings is specified by users.
        * pipeline_id: the pipeline_id if the component node belongs to some pipeline.
        * specify_node_level_compute: Whether the node level compute is specified by users.
        * compute_type: The compute type that the component uses.

        :param compute_target: The compute target.
        :return: telemetry values.
        :rtype: dict
        """
        telemetry_values = super()._get_telemetry_values()
        telemetry_values.update(self._module_dto._get_telemetry_values())
        telemetry_values['load_source'] = self._load_source
        telemetry_values['specify_input_mode'] = self._specify_input_mode
        telemetry_values['specify_output_mode'] = self._specify_output_mode
        telemetry_values['specify_output_datastore'] = self._specify_output_datastore
        telemetry_values['specify_runsettings'] = self._specify_runsettings
        telemetry_values['specify_k8srunsettings'] = self._specify_k8srunsettings

        node_compute_target, specify_node_level_compute = self._resolve_compute(compute_target) \
            if compute_target is not None else (None, False)

        if hasattr(self, 'pipeline'):
            telemetry_values['pipeline_id'] = self.pipeline._id
        if node_compute_target is not None:
            telemetry_values['specify_node_level_compute'] = specify_node_level_compute
            telemetry_values['compute_type'] = node_compute_target[1]

        telemetry_values.update(additional_value or {})
        return telemetry_values

    def _get_instance_id(self):
        return self._instance_id

    def _get_run_setting(self, name, expected_type, default_value=None):
        """Get run setting with name, returns default_value if didn't find or type did not match expected_type."""
        try:
            val = getattr(self._runsettings, name)
            if not isinstance(val, expected_type):
                raise ValueError("{} should be returned.".format(expected_type))
            else:
                return val
        except (AttributeError, ValueError):
            return default_value

    def _get_default_parameters(self):
        """Get exposed parameters' key-value pairs."""
        interface = self._module_dto.module_entity.structured_interface
        return {p.name: p.default_value for p in interface.parameters}

    def _populate_runconfig(self, use_local_compute=False):
        """Populate runconfig from component."""
        raw_conf = json.loads(self._module_dto.module_entity.runconfig)
        run_config = RunConfiguration._get_runconfig_using_dict(raw_conf)
        run_config._target, compute_type = ('local', None) if use_local_compute else self._runsettings.target

        set_compute_field(self._k8srunsettings, compute_type, run_config)

        if hasattr(self._runsettings, 'process_count_per_node'):
            if use_local_compute:
                # When running in local, process count per node can be absent, we will set 1 for it.
                if self.job_type.lower() == 'mpi':
                    run_config.mpi.process_count_per_node = self._get_run_setting('process_count_per_node', int, 1)
            else:
                run_config.mpi.process_count_per_node = self._runsettings.process_count_per_node
        if hasattr(self._runsettings, 'node_count'):
            if use_local_compute:
                # When running in local, node count is always 1
                run_config.node_count = 1
            else:
                run_config.node_count = self._runsettings.node_count

        return run_config

    def _replace(self, new_module):
        """Replace component in pipeline. Use it cautiously."""
        self._module_name = new_module._module_name
        self._namespace = new_module._namespace
        self._module_dto = new_module._module_dto
        self._workspace = new_module._workspace

    def _is_replace_target(self, target):
        """
        Provide for replace a component in pipeline.

        Check if current node(component) is the target one we want

        :return: Result of comparision between two components
        :rtype: bool
        """
        if target.name != self.name:
            return False
        if target._namespace != self._namespace:
            return False
        if target._module_dto != self._module_dto:
            return False
        return True

    @staticmethod
    def _from_func(
            workspace: Workspace,
            func: types.FunctionType,
            force_reload=True,
            load_source=_ComponentLoadSource.UNKNOWN
    ):
        def _reload_func(f: types.FunctionType):
            """Reload the function to make sure the latest code is used to generate yaml."""
            module = importlib.import_module(f.__module__)
            # if f.__name__ == '__main__', reload will throw an exception
            if f.__module__ != '__main__':
                from azure.ml.component.dsl._utils import _force_reload_module
                _force_reload_module(module)
            return getattr(module, f.__name__)

        if force_reload:
            func = _reload_func(func)
        # Import here to avoid circular import.
        from azure.ml.component.dsl.component import ComponentExecutor
        from azure.ml.component.dsl._module_spec import SPEC_EXT
        from azure.ml.component.dsl._utils import _temporarily_remove_file
        # If a ComponentExecutor instance is passed, we directly use it,
        # otherwise we construct a ComponentExecutor with the function
        executor = func if isinstance(func, ComponentExecutor) else ComponentExecutor(func)
        # Use a temp spec file to register.
        temp_spec_file = Path(inspect.getfile(func)).absolute().with_suffix(SPEC_EXT)
        temp_conda_file = temp_spec_file.parent / 'conda.yaml'
        conda_exists = Path(temp_conda_file).is_file()
        # the conda may be the notebook gen conda, cannot temporarily remove if exists
        with _temporarily_remove_file(temp_spec_file):
            try:
                temp_spec_file = executor.to_spec_yaml(
                    folder=temp_spec_file.parent,
                    spec_file=temp_spec_file.name)
                return Component._from_module_spec(workspace=workspace, yaml_file=str(temp_spec_file),
                                                   load_source=load_source)
            finally:
                if not conda_exists and Path(temp_conda_file).is_file():
                    Path(temp_conda_file).unlink()

    @staticmethod
    def _from_module_spec(
            workspace: Workspace,
            yaml_file: str,
            load_source: str
    ):
        module_dto = _load_anonymous_module(workspace, yaml_file)

        # build module func with module version
        module_dto.correct_module_dto()
        return Component._component_func(workspace, module_dto, load_source)

    @staticmethod
    def _component_func(
            workspace: Workspace,
            module_dto: ModuleDto,
            load_source: str = _ComponentLoadSource.UNKNOWN,
            return_yaml=True
    ) -> Callable[..., 'Component']:
        """
        Get component func from ModuleDto.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param module_dto: ModuleDto instance
        :type module_dto: azure.ml.component._module_dto
        :param name: The name of component
        :type name: str
        :param _load_source: The source which the component is loaded.
        :type _load_source: str
        :return: a function that can be called with parameters to get a `azure.ml.component.Component`
        :rtype: function
        """
        def create_component_func(**kwargs) -> 'Component':
            if module_dto.yaml_str:
                definition = _dto_2_definition(module_dto, workspace)
                definition._load_source = load_source  # TODO: Set the source when initialize the definition.
                return _Component(definition, _init_params=kwargs)
            return Component(workspace, module_dto, kwargs, module_dto.module_name, load_source)

        return to_component_func(ws=workspace, module_dto=module_dto, return_yaml=return_yaml,
                                 component_creation_func=create_component_func)

    # endregion

    # region Local run

    def _transfer_params(self, run_id, params, runconfig):
        """Transfer params from DataReference to runconfig's setting."""
        transfered_params = {}
        for key, value in params.items():
            # Use command line option from module dto
            k = self.get_argument_name_by_name(key)
            v = "{}{}".format(DATA_REF_PREFIX, key)
            if isinstance(value, DataReference):
                runconfig.data_references[key] = value.to_config()
            elif isinstance(value, DatasetConsumptionConfig):
                value.dataset._ensure_saved(self._workspace)
                runconfig.data[key] = Data.create(value)
            elif isinstance(value, PipelineData):
                # ScriptRunConfig can't use DataReference directly
                out_key = "outputs"
                # This path will be showed on portal's outputs if datastore is workspaceblobstore
                path = "{}/{}/{}/{}".format("azureml", run_id, out_key, key)
                data_ref = value.datastore.path(path)
                runconfig.data_references[key] = data_ref.to_config()
            else:
                v = value
            transfered_params[k] = v
        return transfered_params

    def _get_input_config_by_argument_name(self, argument_name):
        inputs_config = self._module_dto.module_entity.structured_interface.inputs
        input_interface = self._module_dto.module_python_interface.get_input_by_argument_name(argument_name)
        if input_interface:
            input_name = input_interface.name
        else:
            input_name = self._pythonic_name_to_input_map[argument_name]
        input_config = next(filter(lambda input: input.name == input_name, inputs_config), None)
        return input_config

    def _input_is_optional(self, argument_name):
        return self._get_input_config_by_argument_name(argument_name).is_optional

    def _get_input_name_by_argument_name(self, argument_name):
        return self._get_input_config_by_argument_name(argument_name).name

    def _get_output_config_by_argument_name(self, argument_name):
        outputs_config = self._module_dto.module_entity.structured_interface.outputs
        output_interface = self._module_dto.module_python_interface.get_output_by_argument_name(argument_name)
        if output_interface:
            output_name = output_interface.name
        else:
            output_name = self._pythonic_name_to_output_map[argument_name]
        output_config = next(filter(lambda output: output.name == output_name, outputs_config), None)
        return output_config

    def _output_is_file(self, argument_name):
        return self._get_output_config_by_argument_name(argument_name).data_type_id == 'AnyFile'

    def _build_arguments_for_run_config(self, run_config, run_id):
        """Build argument for run config and fill data reference in it."""
        arguments = []
        default_datastore = Datastore.get(self._workspace, 'workspaceblobstore')
        input_params = self._transfer_params(run_id, self._build_inputs_map(), run_config)
        output_params = self._transfer_params(
            run_id,
            self._build_outputs_map(default_datastore=default_datastore),
            run_config)
        arguments = self._get_arguments(input_params, output_params)
        return arguments

    def _get_command(self, input_path, output_path, remove_none_value=True):
        """
        Get component execute command.

        :param input_path: Replace input port value
        :type input_path: dict
        :param output_path: Replace output port value
        :type output_path: dict
        :return: a list that contains component arguments, and a dict contains environment variables component needed
        :rtype: list
        """
        ret = self._get_arguments(input_path, output_path, remove_none_value)
        runconfig = json.loads(self._module_dto.module_entity.runconfig)
        framework = None if 'Framework' not in runconfig else runconfig['Framework']
        if framework and framework.lower() == 'python':
            ret.insert(0, 'python')
        elif not framework:
            raise Exception('Framework in runconfig is None')
        else:
            raise NotImplementedError('Unsupported framework {}, only Python is supported now.'.format(framework))
        script = None if 'Script' not in runconfig else runconfig['Script']
        if script:
            ret.insert(1, script)
        else:
            raise Exception('Script in runconfig is None')

        if self.job_type.lower() == 'mpi':
            ret = translate_mpi_command_by_module(ret, self)
        elif self.job_type.lower() == 'parallel':
            ret = translate_parallel_command_by_module(ret, self, input_path)
        return ret

    def _get_arguments(self, input_path, output_path, remove_none_value=True):
        """
        Get component arguments.

        :param input_path: Replace input port value
        :type input_path: dict
        :param output_path: Replace output port value
        :type output_path: dict
        :return: a list that contains component arguments, and a dict contains environment variables component needed
        :rtype: list
        """
        def _get_argument_value(argument, parameter_params, input_path, output_path):
            arg_value = None

            if argument.value_type == '0':
                # Handle anonymous_module output
                output_prefix = 'DatasetOutputConfig:'
                if argument.value.startswith(output_prefix):
                    arg_value_key = _get_or_sanitize_python_name(argument.value[len(output_prefix):],
                                                                 self._module_dto.module_python_interface
                                                                 .outputs_name_mapping)
                    if arg_value_key in output_path:
                        return output_path[arg_value_key]
                return argument.value
            elif argument.value_type == '1':
                # Get parameter argument value
                arg_value_key = self._module_dto\
                    .module_python_interface.parameters_name_mapping.get(argument.value)
                if arg_value_key is None:
                    arg_value_key = _sanitize_python_variable_name(argument.value)
                if arg_value_key in parameter_params:
                    if parameter_params[arg_value_key] is not None:
                        arg_value = str(parameter_params[arg_value_key])
                    else:
                        arg_value = parameter_params[arg_value_key]
                else:
                    arg_value = argument.value
            elif argument.value_type == '2':
                # Get input argument value
                arg_value_key = self._module_dto\
                    .module_python_interface.inputs_name_mapping.get(argument.value)
                if arg_value_key is None:
                    arg_value_key = _sanitize_python_variable_name(argument.value)
                if arg_value_key in input_path:
                    arg_value = input_path[arg_value_key]
                else:
                    arg_value = None
            elif argument.value_type == '3':
                # Get output argument value
                arg_value_key = self._module_dto\
                    .module_python_interface.outputs_name_mapping.get(argument.value)
                if arg_value_key is None:
                    arg_value_key = _sanitize_python_variable_name(argument.value)
                if arg_value_key in output_path:
                    arg_value = output_path[arg_value_key]
            elif argument.value_type == '4':
                # Get nestedList argument value
                arg_value = []
                for sub_arg in argument.nested_argument_list:
                    sub_arg_value = _get_argument_value(
                        sub_arg, parameter_params, input_path, output_path)
                    arg_value.append(sub_arg_value)
            return arg_value

        arguments = self._module_dto.module_entity.structured_interface.arguments
        parameter_params = self._parameter_params
        ret = []

        for arg in arguments:
            arg_value = _get_argument_value(arg, parameter_params, input_path, output_path)
            ret.append(arg_value)

        def flatten(arr):
            for element in arr:
                if hasattr(element, "__iter__") and not isinstance(element, str):
                    for sub in flatten(element):
                        yield sub
                else:
                    yield element

        ret = list(flatten(ret))
        if remove_none_value:
            # Remove None value and its flag in arguments
            ret = [x[0] for x in zip(ret, ret[1:] + ret[-1::]) if (x[0] and x[1])]

        return ret

    # endregion

    # region Public Methods

    @property
    def name(self):
        """
        Get the name of the Component.

        :return: The name.
        :rtype: str
        """
        return self._module_name

    @property
    def _version_id(self):
        """
        Get the version id of the Component.

        :return: The version id.
        :rtype: str
        """
        return self._module_dto.module_version_id

    @property
    def namespace(self):
        """
        Get the namespace of the Component.

        :return: The namespace.
        :rtype: str
        """
        return self._namespace

    @property
    def inputs(self) -> _AttrDict[str, _InputBuilder]:
        """Get the inputs of the Component."""
        return self._inputs

    @property
    def outputs(self) -> _AttrDict[str, _OutputBuilder]:
        """Get the outputs of the Component."""
        return self._outputs

    @property
    def runsettings(self):
        """
        Get run settings for Component.

        :return: the run settings.
        :rtype: _RunSettings
        """
        return self._runsettings

    @property
    def k8srunsettings(self):
        """
        Get compute run settings for Component.

        TODO: move to runsettings

        :return the compute run settings
        :rtype _K8sRunSettings
        """
        return self._k8srunsettings

    @property
    def workspace(self):
        """
        Get the workspace of the Componnet.

        :return: the Workspace.
        :rtype: azureml.core.Workspace
        """
        return self._workspace

    @property
    def regenerate_output(self):
        """
        Return flag whether the component should be run again.

        Set to True to force a new run (disallows component/datasource reuse).

        :return: the regenerate_output value.
        :rtype: bool
        """
        return self._regenerate_output

    @regenerate_output.setter
    def regenerate_output(self, regenerate_output):
        self._regenerate_output = regenerate_output

    @property
    def job_type(self):
        """
        Return the job type of the component.

        :return: the job_type value.
        :rtype: str
        """
        return self._module_dto.job_type

    @property
    def _identifier(self):
        """Return the identifier of the component."""
        return self._module_dto.module_version_id

    @property
    def version(self):
        """Return the version of the component."""
        return self._module_dto.module_version

    @property
    def registered_by(self):
        """Return who created the component definition."""
        return self._module_dto.registered_by

    @property
    def created_date(self):
        """Return the created date of the corresponding component definition."""
        return self._module_dto.created_date

    def get_argument_name_by_name(self, name):
        """Return the argument name of an input/output according its name."""
        return self._name_to_argument_name_mapping.get(name)

    def set_inputs(self, *args, **kwargs) -> 'Component':
        """Update the inputs of the module."""
        # Note that the argument list must be "*args, **kwargs" to make sure
        # vscode intelligence works when the signature is updated.
        # https://github.com/microsoft/vscode-python/blob/master/src/client/datascience/interactive-common/intellisense/intellisenseProvider.ts#L79
        self.inputs.update({k: _InputBuilder(v, k, owner=self) for k, v in kwargs.items() if v is not None})
        return self

    def set_parameters(self, *args, **kwargs) -> 'Component':
        """Update the parameters of the module."""
        # Note that the argument list must be "*args, **kwargs" to make sure
        # vscode intelligence works when the signature is updated.
        # https://github.com/microsoft/vscode-python/blob/master/src/client/datascience/interactive-common/intellisense/intellisenseProvider.ts#L79
        self._parameter_params.update({k: v for k, v in kwargs.items() if v is not None})
        return self

    def validate(self, raise_error=False, pipeline_parameters=None):
        """
        Validate that all the inputs and parameters are in fact valid.

        :return: the errors found during validation.
        :rtype: list
        """
        # Validate inputs
        errors = []

        def process_error(e: Exception, error_type):
            ve = ValidationError(str(e), e, error_type)
            if raise_error:
                raise ve
            else:
                errors.append({'message': ve.message, 'type': ve.error_type})

        def update_provided_inputs(provided_inputs, pipeline_parameters):
            if pipeline_parameters is None:
                return provided_inputs
            _provided_inputs = {}
            for k, v in provided_inputs.items():
                _input = v._get_internal_data_source()
                if not isinstance(_input, PipelineParameter) or _input.name not in pipeline_parameters.keys():
                    _provided_inputs[k] = v
                else:
                    _provided_inputs[k] = (_InputBuilder(PipelineParameter(
                        name=_input.name, default_value=pipeline_parameters[_input.name]),
                        name=v.name, mode=v.mode, owner=v._owner))
            return _provided_inputs

        def update_provided_parameters(provided_parameters, pipeline_parameters):
            _params = {}
            for k, v in provided_parameters.items():
                _input = v._get_internal_data_source() if isinstance(v, _InputBuilder) else v
                if not isinstance(_input, PipelineParameter) or \
                        pipeline_parameters is None or \
                        _input.name not in pipeline_parameters.keys():
                    _params[k] = _input
                else:
                    _params[k] = pipeline_parameters[_input.name]
            return _params

        provided_inputs = update_provided_inputs(self._inputs, pipeline_parameters)
        ModuleValidator.validate_module_inputs(provided_inputs=provided_inputs,
                                               interface_inputs=self._interface_inputs,
                                               param_python_name_dict=self._module_dto.module_python_interface
                                               .inputs_name_mapping,
                                               process_error=process_error)

        provided_parameters = update_provided_parameters(self._parameter_params, pipeline_parameters)
        ModuleValidator.validate_module_parameters(provided_parameters=provided_parameters,
                                                   interface_parameters=self._interface_parameters,
                                                   param_python_name_dict=self._module_dto.module_python_interface
                                                   .parameters_name_mapping,
                                                   process_error=process_error)

        ModuleValidator.validate_runsettings(runsettings=self._runsettings,
                                             process_error=process_error)

        ModuleValidator.validate_k8srunsettings(k8srunsettings=self._k8srunsettings,
                                                process_error=process_error)

        return errors

    @track(_get_logger, activity_type=_PUBLIC_API)
    def run(self, working_dir=None, experiment_name=None, use_docker=True, track_run_history=True):
        """Run component in local container.

        .. remarks::

            After executing this method, scripts, output dirs and log file will be created in working dir.

            .. code-block:: python

                # Suppose we have a workspace as 'ws'
                # First, load a component, and set parameters of module
                ejoin = Component.load(ws, namespace='microsoft.com/bing', name='ejoin')
                component = ejoin(leftcolumns='m:name;age', rightcolumns='income',
                    leftkeys='m:name', rightkeys='m:name', jointype='HashInner')
                # Second, set prepared input path and output path to run component in local. If not set working_dir,
                # will create it in temp dir. In this example, left_input and right_input are input port of ejoin.
                # And after running, output data and log will write in working_dir
                component.set_inputs(left_input=your_prepare_data_path)
                component.set_inputs(right_input=your_prepare_data_path)
                component.run(working_dir=dataset_output_path)

        :param working_dir: The output path for component output info
        :type working_dir: str
        :param experiment_name: The experiment_name will show in portal. If not set, will use component name.
        :type experiment_name: str
        :param use_docker: If use_docker=True, will pull image from azure and run component in container.
                           If use_docker=False, will directly run component script.
        :type use_docker: bool
        :param track_run_history: If track_run_history=True, will create azureml.Run and upload component output
                                  and log file to portal.
                                  If track_run_history=False, will not create azureml.Run to upload outputs
                                  and log file.
        :type track_run_history: bool
        :return: component run status
        :rtype: str
        """
        if not self.job_type or self.job_type.lower().strip() not in ['basic', 'mpi', 'parallel']:
            raise UserErrorException(
                'Unsupported component job type {}, " \
                "only basic/mpi/parallel component is supported now.'.format(self.job_type))
        if not working_dir:
            working_dir = os.path.join(tempfile.gettempdir(), self._identifier)
        short_working_dir = _get_short_path_name(working_dir, create_dir=True)
        print('working dir is {}'.format(working_dir))

        experiment_name = experiment_name if experiment_name else _sanitize_python_variable_name(self._short_name)
        tracker = RunHistoryTracker.with_definition(
            experiment_name=experiment_name,
            track_run_history=track_run_history,
            module=self,
            working_dir=short_working_dir,
            path=EXECUTION_LOGFILE)
        return _module_run(self, short_working_dir, use_docker, tracker=tracker)

    @track(_get_logger, activity_type=_PUBLIC_API)
    def submit(self, experiment_name=None, source_dir=None, tags=None) -> Run:
        """Submit component to remote compute target.

        .. remarks::

            Submit is an asynchronous call to the Azure Machine Learning platform to execute a trial on
            remote hardware.  Depending on the configuration, submit will automatically prepare
            your execution environments, execute your code, and capture your source code and results
            into the experiment's run history.
            An example of how to submit an experiment from your local machine is as follows:

            .. code-block:: python

                # Suppose we have a workspace as 'ws'
                # First, load a module, and set parameters of module
                train_module_func = Component.load(ws, namespace='microsoft.com/aml/samples', name='Train')
                train_data = Dataset.get_by_name(ws, 'training_data')
                train = train_module_func(training_data=train_data, max_epochs=5, learning_rate=0.01)
                # Second, set compute target for component then add compute running settings.
                # After running finish, the output data will be in outputs/$output_file
                train.runsettings.configure(target="k80-16-c")
                train.runsettings.resourceconfiguration.configure(gpu_count=1, is_preemptible=True)
                run = train.submit(experiment_name="module-submit-test")
                print(run.get_portal_url())
                run.wait_for_completion()

        :param experiment_name: experiment name
        :type experiment_name: str
        :param source_dir: source dir is where the machine learning scripts locate
        :type source_dir: str
        :param tags: Tags to be added to the submitted run, {"tag": "value"}
        :type tags: dict

        :return run
        :rtype: azureml.core.Run
        """
        if self._runsettings.target is None:
            raise UserErrorException("Submit require a remote compute configured.")
        if experiment_name is None:
            experiment_name = _sanitize_python_variable_name(self._short_name)
        if source_dir is None:
            source_dir = os.path.join(tempfile.gettempdir(), self._identifier)
            print("[Warning] script_dir is None, create tempdir: {}".format(source_dir))
        experiment = Experiment(self._workspace, experiment_name)
        run_config = self._populate_runconfig()

        script = run_config.script
        if not os.path.isfile("{}/{}".format(source_dir, script)):
            print("[Warning] Can't find {} from {}, will download from remote".format(script, source_dir))
            _prepare_module_snapshot(self, source_dir)

        run_id = experiment_name + "_" + str(int(time.time())) + "_" + str(uuid.uuid4())[:8]
        arguments = self._build_arguments_for_run_config(run_config, run_id)

        src = ScriptRunConfig(source_directory=source_dir, script=script, arguments=arguments, run_config=run_config)
        run = experiment.submit(config=src, tags=tags, run_id=run_id)
        print('Link to Azure Machine Learning Portal:', run.get_portal_url())
        return run

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def batch_load(workspace: Workspace, ids: List[str] = None, identifiers: List[tuple] = None) -> \
            List[Callable[..., 'Component']]:
        """
        Batch load components by identifier list.

        If there is an exception with any component, the batch load will fail. Partial success is not allowed.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param ids: component version ids
        :type ids: list[str]
        :param identifiers: list of tuple(name, namespace, version)
        :type identifiers: list[tuple]

        :return: a tuple of component functions
        :rtype: tuple(function)
        """
        service_caller = _DesignerServiceCallerFactory.get_instance(workspace)
        refined_module_dtos = \
            service_caller.batch_get_modules(module_version_ids=ids,
                                             name_identifiers=identifiers)
        module_number = len(refined_module_dtos)
        module_dtos = [ModuleDto(item) for item in refined_module_dtos]
        telemetry_values = WorkspaceTelemetryMixin._get_telemetry_value_from_workspace(workspace)
        telemetry_values.update({
            'count': module_number,
        })
        _LoggerFactory.add_track_dimensions(_get_logger(), telemetry_values)
        module_funcs = (Component._component_func(workspace=workspace,
                                                  module_dto=module_dto,
                                                  load_source=_ComponentLoadSource.REGISTERED,
                                                  return_yaml=False
                                                  )
                        for module_dto in module_dtos)
        if module_number == 1:
            module_funcs = next(module_funcs)
        return module_funcs

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def load(workspace: Workspace, namespace: str = None, name: str = None,
             version: str = None, id: str = None) -> Callable[..., 'Component']:
        """
        Get component function from workspace.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param namespace: Namespace
        :type namespace: str
        :param name: The name of component
        :type name: str
        :param version: Version
        :type version: str
        :param id: str : The component version id of an existing component
        :type id: str
        :return: a function that can be called with parameters to get a `azure.ml.component.Component`
        :rtype: function
        """
        service_caller = _DesignerServiceCallerFactory.get_instance(workspace)
        if id is None:
            module_dto = ModuleDto(service_caller.get_module(
                module_namespace=namespace,
                module_name=name,
                version=version,  # If version is None, this will get the default version
                include_run_setting_params=False
            ))
        else:
            module_dto = ModuleDto(service_caller.get_module_by_id(module_id=id, include_run_setting_params=False))

        module_dto.correct_module_dto()

        return Component._component_func(workspace,
                                         module_dto,
                                         _ComponentLoadSource.REGISTERED,
                                         return_yaml=True)

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def from_notebook(workspace: Workspace, notebook_file: str, source_dir=None) -> Callable[..., 'Component']:
        """Register an anonymous component from a jupyter notebook file and return the registered component func.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param notebook_file: The jupyter notebook file run in module.
        :type notebook_file: str
        :param source_dir: The source directory of the module.
        :type source_dir: str

        :return: a function that can be called with parameters to get a `azure.ml.component.Component`
        :rtype: function
        """
        from azure.ml.component.dsl._component_from_notebook import gen_component_by_notebook
        if source_dir is None:
            source_dir = Path(notebook_file).parent
            notebook_file = Path(notebook_file).name
        if not notebook_file.endswith('.ipynb'):
            raise UserErrorException("'%s' is not a jupyter notebook file" % notebook_file)
        temp_target_file = '_' + Path(notebook_file).with_suffix('.py').name
        temp_target_path = Path(source_dir) / Path(temp_target_file)
        conda_file = temp_target_path.parent / 'conda.yaml'

        from azure.ml.component.dsl._utils import _temporarily_remove_file, _change_working_dir
        with _temporarily_remove_file(temp_target_path), _temporarily_remove_file(conda_file):
            generator = gen_component_by_notebook(
                notebook_file,
                working_dir=source_dir,
                target_file=temp_target_file,
                force=True)

            with _change_working_dir(source_dir):
                from runpy import run_path
                notebook_module = run_path(temp_target_file)
                notebook_func = notebook_module[generator.func_name]
                return Component._from_func(workspace=workspace, func=notebook_func,
                                            force_reload=False, load_source=_ComponentLoadSource.FROM_NOTEBOOK)

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def from_func(workspace: Workspace, func: types.FunctionType, force_reload=True) -> Callable[..., 'Component']:
        """Register an anonymous component from a wrapped python function and return the registered component func.

        :param workspace: The workspace object this module will belong to.
        :type workspace: azureml.core.Workspace
        :param func: A wrapped function to be loaded or a ComponentExecutor instance.
        :type func: types.FunctionType
        :param force_reload: Whether reload the function to make sure the code is the latest.
        :type force_reload: bool
        """
        return Component._from_func(workspace=workspace, func=func,
                                    force_reload=force_reload, load_source=_ComponentLoadSource.FROM_FUNC)

    @track(_get_logger, activity_type=_PUBLIC_API)
    def export_yaml(self, directory=None):
        """
        Export component to yaml files.

        This is an experimental function, will be changed anytime.

        :param directory: target directory path. Default current working directory
            path will be used if not provided.
        :type directory: str
        :return: directory path
        :rtype: str
        """
        pass

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def from_yaml(workspace: Workspace, yaml_file: str) -> Callable[..., 'Component']:
        """Register an anonymous component from yaml file to workspace and return the registered component func.

        Assumes source code is in the same directory with yaml file. Then return the registered component func.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param yaml_file: Module spec file. The spec file could be located in local or Github.
                          For example:

                          * "custom_module/module_spec.yaml"
                          * "https://github.com/zzn2/sample_modules/blob/master/3_basic_module/basic_module.yaml"
        :type yaml_file: str
        :return: a function that can be called with parameters to get a `azure.ml.component.Component`
        :rtype: function
        """
        return Component._from_module_spec(workspace=workspace, yaml_file=yaml_file,
                                           load_source=_ComponentLoadSource.FROM_YAML)

    @staticmethod
    @track(_get_logger, activity_type=_PUBLIC_API)
    def register(workspace: Workspace, yaml_file: str, amlignore_file: str = None, set_as_default: bool = False,
                 version: str = None) -> \
            Callable[..., 'Component']:
        """
        Register an component from yaml file to workspace.

        TODO: rename to same as CLI

        Assumes source code is in the same directory with yaml file. Then return the registered component func.

        :param workspace: The workspace object this component will belong to.
        :type workspace: azureml.core.Workspace
        :param yaml_file: Module spec file. The spec file could be located in local or Github.
                          For example:

                          * "custom_module/module_spec.yaml"
                          * "https://github.com/zzn2/sample_modules/blob/master/3_basic_module/basic_module.yaml"
        :type yaml_file: str
        :param amlignore_file: The .amlignore or .gitignore file path used to exclude files/directories in the snapshot
        :type amlignore_file: str
        :param set_as_default: By default false, default version of the component will not be updated
                                when registering a new version of module. Specify this flag to set
                                the new version as the module's default version.
        :type set_as_default: bool
        :param version: If specified, registered component will use specified value as version
                                            instead of the version in the yaml.
        :type version: str
        :return: a function that can be called with parameters to get a `azure.ml.component.Component`
        :rtype: function
        """
        if version is not None:
            if not isinstance(version, str):
                raise UserErrorException('Only string type of supported for param version.')
            elif version == "":
                # Hint user when accidentally set empty string to set_version
                raise UserErrorException('Param version does not allow empty value.')
        module_dto = _register_module_from_yaml(workspace, yaml_file, amlignore_file=amlignore_file,
                                                set_as_default=set_as_default,
                                                version=version)

        # build component func with module dto
        return Component._component_func(workspace, module_dto, _ComponentLoadSource.FROM_YAML)

    # endregion


class _Component(Component):
    """This is a Component class which is initialized by ComponentDefinition.

    It will replace the original Component once all dependencies on ModuleDto is removed.
    """

    def __init__(self, definition: ContainerComponentDefinition, _init_params: Mapping[str, str]):
        """Initialize a component with a component definition.

        :param definition: The ContainerComponentDefinition object which describe the interface of the component.
        :type definition: azure.ml.component.core._component_definition.ContainerComponentDefinition
        :param _init_params: (Internal use only.) The init params will be used to initialize inputs and parameters.
        :type _init_params: dict
        """
        WorkspaceTelemetryMixin.__init__(self, definition.workspace)
        # TODO: Impelment the logic according to Definition and remove backward compatibility logic.
        # 1. Change the interface of __init__ with ContainerComponentDefinition instead of current params
        #    and adjust the creation methods like Component.load;
        # 2. Update the initialization logic to use component_definition to initialize instead of _module_dto;
        #   2.1 Initialize the inputs/outputs with InputDefinition/OutputDefinition in component_definition;
        #   2.2 Add runsetting for component_definition and initialize the runsettings here with that;
        #   2.3 Initialize other meta information with component_definition
        # 3. Replace current Container class with this class
        # 4. Align PipelineComponent and ContainerComponent

        self._definition = definition
        self._name_to_argument_name_mapping = {
            **{self._get_name_by_display_name(p.name): arg for arg, p in definition.inputs.items()},
            **{self._get_name_by_display_name(p.name): arg for arg, p in definition.outputs.items()},
        }

        # Generate an id for every component instance
        self._instance_id = str(uuid.uuid4())

        # Telemetry
        self._specify_input_mode = False
        self._specify_output_mode = False
        self._specify_output_datastore = False
        self._specify_runsettings = False
        self._specify_k8srunsettings = False

        self._init_public_interface(_init_params)

        self._runsettings = _RunSettings(definition.runsettings, self._module_dto.module_name, self._workspace, self)
        self._k8srunsettings = _K8sRunSettings(definition.k8srunsettings, self) if definition.k8srunsettings else None

        self._init_dynamic_method()
        self._regenerate_output = None

        # Add current component to global parent pipeline if there is one
        from .dsl.pipeline import _try_to_add_node_to_current_pipeline
        _try_to_add_node_to_current_pipeline(self)

    @property
    def definition(self) -> ContainerComponentDefinition:
        return self._definition

    @property
    def _workspace(self):
        return self.definition.workspace

    @property
    def _module_name(self):
        """Return the module name."""
        return self.definition.name

    @property
    def _short_name(self):
        """Return the name of the component."""
        return self.definition.name

    @property
    def _module_dto(self):
        return self.definition._module_dto

    @property
    def _namespace(self):
        return self.definition.namespace

    @property
    def _load_source(self):
        return self.definition._load_source

    @property
    def job_type(self):
        """
        Return the job type of the component.

        :return: the job_type value.
        :rtype: str
        """
        return self.definition.job_type

    @property
    def _identifier(self):
        """Return the identifier of the component."""
        return self.definition.identifier

    @property
    def version(self):
        """Return the version of the component."""
        return self.definition.version

    @property
    def registered_by(self):
        """Return who created the component definition."""
        return self.definition.creation_context.registered_by

    @property
    def created_date(self):
        """Return the created date of the corresponding component definition."""
        return self.definition.creation_context.created_date

    def _replace(self, new_module):
        if not isinstance(new_module, _Component):
            raise TypeError("Can only replaced by a _Componet object, got %r" % type(new_module))
        self._definition = new_module.definition

    def _init_public_interface(self, init_params):
        input_builder_map = {
            name: _InputBuilder(value, name=name, owner=self) for name, value in init_params.items()
            if name in self.definition.inputs and not self.definition.inputs[name].is_param()
        }
        self._inputs = _AttrDict(input_builder_map)

        self._parameter_params = {
            name: value for name, value in init_params.items()
            if name in self.definition.inputs and self.definition.inputs[name].is_param()
        }

        output_builder_map = {
            name: _OutputBuilder(name, port_name=self._get_name_by_display_name(output.name), owner=self)
            for name, output in self.definition.outputs.items()
        }
        self._outputs = _AttrDict(output_builder_map)

        self._pythonic_name_to_input_map = {
            name: self._get_name_by_display_name(input.name)
            for name, input in self.definition.inputs.items() if not input.is_param()
        }
        self._pythonic_name_to_output_map = {
            name: self._get_name_by_display_name(output.name)
            for name, output in self.definition.outputs.items()
        }

        # TODO: Remove the following properties once the validation logic is refined
        interface = self._module_dto.module_entity.structured_interface
        self._interface_inputs = interface.inputs
        self._interface_parameters = interface.parameters
        self._interface_outputs = interface.outputs

    def _get_name_by_display_name(self, display_name):
        return self.definition._display_name_to_name.get(display_name, display_name)

    def _init_dynamic_method(self):
        """Update methods set_inputs/set_parameters according to the component input/param definitions."""
        self.set_inputs = create_kw_method_from_parameters(
            self.set_inputs, get_dynamic_input_parameter(self.definition),
        )
        self.set_parameters = create_kw_method_from_parameters(
            self.set_parameters, get_dynamic_param_parameter(self.definition),
        )

    def _build_outputs_map(self, producer=None, default_datastore=None) -> Mapping[str, Any]:
        # output name -> DatasetConsumptionConfig
        return {
            # This is a workaround that the backend required name is currently not the name in definition,
            # we need to use such a mapping to get the required name.
            self._get_name_by_display_name(output.name): self._outputs[name].build(producer, default_datastore)
            for name, output in self.definition.outputs.items()
        }

    def _build_inputs_map(self) -> Mapping[str, Any]:
        # input name -> DatasetConsumptionConfig
        _inputs_map = {}

        for name, input in self.definition.inputs.items():
            value = self._inputs.get(name)
            if value is None:
                continue
            value = value.build()
            if value is not None:
                # This is a workaround that the backend required name is currently not the name in definition,
                # we need to use such a mapping to get the required name.
                name = self._get_name_by_display_name(input.name)
                _inputs_map[name] = value

        return _inputs_map

    def _build_params(self) -> Mapping[str, Any]:
        # input param name -> input param value
        return {
            param.name: self._parameter_params[name] for name, param in self.definition.inputs.items()
            if self._parameter_params.get(name) is not None
        }

    def _output_is_file(self, argument_name):
        """Return True if the output is expected to be a file instead of a directory.

        This is only used in Component.run, will be refined in the future.
        """
        return self.definition.outputs[argument_name].type == 'AnyFile'

    def _input_is_optional(self, argument_name):
        return self.definition.inputs[argument_name].optional

    def _get_input_name_by_argument_name(self, argument_name):
        return self._get_name_by_display_name(self.definition.inputs[argument_name].name)

    def _get_default_parameters(self):
        """Get exposed parameters' key-value pairs."""
        return {
            self._get_name_by_display_name(v.name): v.default
            for v in self.definition.inputs.values()
            if v.is_param()
        }
