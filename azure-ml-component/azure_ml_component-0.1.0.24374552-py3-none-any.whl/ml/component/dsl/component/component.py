# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""A wrapper to analyze function annotations, generate component specs, and run component in command line."""
import copy
import types
import inspect
import argparse
import re
import sys
import functools
import contextlib
import multiprocessing
import importlib
from multiprocessing.pool import ThreadPool
from collections import OrderedDict
from enum import EnumMeta
from pathlib import Path
from io import StringIO

from azureml._project.project_manager import _get_tagged_image

from azure.ml.component.dsl._utils import logger, _import_component_with_working_dir, _to_camel_case, \
    _infer_func_relative_path_with_source
from azure.ml.component.dsl._module_spec import BaseModuleSpec, ParallelRunModuleSpec, SPEC_EXT
from ._annotations import _ComponentBaseParam, _ComponentParam, _ComponentOutputPort, _ComponentInputPort, \
    OutputDirectory, _InputFileList, StringParameter, EnumParameter
from ._exceptions import RequiredParamParsingError, TooManyDSLComponentsError


OPENMPI_CPU_IMAGE = _get_tagged_image("mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu16.04")


def component(
    name=None, version=None, namespace=None,
    job_type=None, description=None,
    is_deterministic=None,
    tags=None, contact=None, help_document=None,
    os=None,
    base_image=None, conda_dependencies=None,
    custom_image=None,
    container_registry=None,
    parallel_inputs=None,
    default_compute_target=None, default_datastore=None
):
    """Return a decorator which is used to declare a component with @dsl.component.

    A component is a reusable unit in an Azure Machine Learning workspace.
    With the decorator @dsl.component, a function could be registered as a component in the workspace.
    Then the component could be used to construct an Azure Machine Learning pipeline.
    The parameters of the decorator are the properties of the component spec,
    see https://aka.ms/azureml-component-specs.

    .. remarks::

        The following example shows how to use @dsl.component to declare a simple component.

        .. code-block:: python

            @dsl.component
            def your_component_function(output: OutputDirectory(), input: InputDirectory(), param='str_param'):
                pass

        The following example shows how to declare a component with detailed meta data.

        .. code-block:: python

            @dsl.component(name=name, version=version, namespace=namespace, job_type=job_type, description=description)
            def your_component_function(output: OutputDirectory(), input: InputDirectory(), param='str_param'):
                pass

        An executable component should be in an entry file and could handle command line arguments.
        The following code is a full example of entry.py which could be registered.

        .. code-block:: python

            import sys
            from azure.ml.component import dsl
            from azure.ml.component.dsl.component import ComponentExecutor

            @dsl.component
            def your_component_function(output: OutputDirectory(), input: InputDirectory(), param='str_param'):
                pass

            if __name__ == '__main__':
                ComponentExecutor(your_component_function).execute(sys.argv)

        With the entry.py file, we could build a component specification yaml file.
        For more details of the component spec, see https://aka.ms/azureml-component-specs
        With the yaml file, we could register the component to workspace using az ml cli.
        See https://docs.microsoft.com/en-us/cli/azure/ext/azure-cli-ml/ml?view=azure-cli-latest.
        The command lines are as follows.
        az ml component build --target entry.py
        az ml component register --spec-file entry.spec.yaml


    :param name: The name of the component. If None is set, camel cased function name is used.
    :type name: str
    :param description: The description of the component. If None is set, the doc string is used.
    :type description: str
    :param version: Version of the component.
    :type version: str
    :param namespace: Namespace of the component.
    :type namespace: str
    :param job_type: Job type of the component.
    :type job_type: str
    :param is_deterministic: Specify whether the component will always generate the same result.
    :type is_deterministic: bool
    :param tags: Tags of the component.
    :type tags: builtin.list
    :param contact: Contact of the component.
    :type contact: str
    :param help_document: Help document of the component.
    :type help_document: str
    :param os: OS type of the component.
    :type os: str
    :param base_image: Base image of the component.
    :type base_image: str
    :param conda_dependencies: Dependencies of the component.
    :type conda_dependencies: str
    :param custom_image: User provided docker image, if it is not None, the component will directly run with the image,
                         user should take care of preparing all the required dependent packages in the image.
                         in this case, both base_image and conda_dependencies should be None.
    :type custom_image: str
    :param container_registry: The image registry info when using base_image/custom_image from a private repo.
    :type container_registry: :class:`azureml.core.container_registry.ContainerRegistry`
    :param parallel_inputs: A list of :class:`azure.ml.component.dsl.component.InputDirectory` object.
                            The inputs indicate the data for a parallel run component,
                            these inputs will be converted to a file list to be processed.
    :type parallel_inputs: builtin.list

    :return: An injected function which could be passed to ComponentExecutor
    """
    if os and os.lower() not in {'windows', 'linux'}:
        raise ValueError("Keyword 'os' only support two values: 'windows', 'linux'.")

    # For mpi component, due to some bug, IntelMPI cannot be initialized in linux docker in Windows OS.
    # See https://community.intel.com/t5/Intel-oneAPI-HPC-Toolkit/Intel-MPI-segmentation-fault-bug/td-p/1154073
    # To enable Component.run test in Windows OS for mpi component, we use openmpi base image instead.
    if base_image is None and job_type and job_type.lower() == 'mpi':
        base_image = OPENMPI_CPU_IMAGE
    spec_args = {k: v for k, v in locals().items() if v is not None}
    wrap_callable = False
    if callable(name):
        wrap_callable = True
        spec_args = {}

    def wrapper(func):
        # Indicate the component is generated by dsl.component
        spec_args['annotations'] = {'codegenBy': 'dsl.component'}
        spec_args['name'] = spec_args.get('name', _to_camel_case(func.__name__))
        spec_args['description'] = spec_args.get('description', func.__doc__)
        entry, source_dir = _infer_func_relative_path_with_source(func)
        spec_args['command'] = ['python', entry]
        spec_args['source_directory'] = source_dir
        # Initialize a ComponentExecutor to make sure it works and use it to update the component function.
        executor = ComponentExecutor(func, copy.copy(spec_args))
        executor._update_func(func)
        return func

    return wrapper(name) if wrap_callable else wrapper


class ComponentExecutor:
    """An executor to analyze the spec args of a function and convert it to a runnable component in AzureML."""

    INJECTED_FIELD = '_spec_args'  # The injected field is used to get the component spec args of the function.

    def __init__(self, func: types.FunctionType, spec_args=None):
        """Initialize a ComponentExecutor with a function to enable calling the function with command line args.

        :param func: A function wrapped by dsl.component.
        :type func: types.FunctionType
        """
        if not isinstance(func, types.FunctionType):
            raise TypeError("Only function type is allowed to initialize ComponentExecutor.")
        if spec_args is None:
            spec_args = getattr(func, self.INJECTED_FIELD, None)
            if spec_args is None:
                raise TypeError("You must wrap the function with @dsl.component() before using it.")
        self._raw_spec_args = copy.copy(spec_args)
        self._name = spec_args['name']
        self._job_type = spec_args.get('job_type', 'basic')
        executor_cls = self._get_executor_by_job_type(self.job_type)
        if executor_cls is None:
            raise ValueError("Unrecognized job_type '%s' of dsl.component '%s'." % (self.job_type, func.__name__))
        self._executor = executor_cls(func, spec_args=spec_args)
        self._func = func

    @property
    def name(self):
        """Return the name of the component."""
        return self._name

    @property
    def job_type(self):
        """Return the job type of the component."""
        return self._job_type

    @property
    def spec(self):
        """Return the module spec instance of the component.

        Initialized by the function annotations and the meta data.
        """
        return self._executor.spec

    @property
    def spec_dict(self):
        """Return the component spec data as a python dict."""
        return self._executor.spec.spec_dict

    def to_spec_yaml(self, folder=None, spec_file=None):
        """Generate spec dict object, and dump it as a yaml spec file."""
        pyfile = Path(inspect.getfile(self._func))
        if folder is None:
            # If the folder is not provided, we generate the spec file in the same folder of the function file.
            folder = pyfile.parent
        if spec_file is None:
            # If the spec file name is not provided, get the name from the file name.
            spec_file = pyfile.with_suffix(SPEC_EXT).name
        self.spec.dump_module_spec_to_folder(folder, spec_file)
        return Path(folder) / spec_file

    def get_interface(self):
        """Return the interface of this component.

        :return: A dictionary including the definition of inputs/outputs/params.
        """
        return self._executor.get_interface()

    def execute(self, argv):
        """Execute the component with command line arguments."""
        return self._executor.execute(argv)

    def __call__(self, *args, **kwargs):
        """Directly calling a component executor equals to calling the underlying function directly."""
        return self._func(*args, **kwargs)

    @classmethod
    def collect_component_from_file(cls, py_file, working_dir=None, force_reload=False):
        """Collect single dsl component in a file and return the executors of the components."""
        py_file = Path(py_file).absolute()
        if py_file.suffix != '.py':
            raise ValueError("%s is not a valid py file." % py_file)
        if working_dir is None:
            working_dir = py_file.parent
        working_dir = Path(working_dir).absolute()

        component_path = py_file.relative_to(working_dir).as_posix().split('.')[0].replace('/', '.')

        return cls.collect_component_from_py_module(component_path, working_dir=working_dir, force_reload=force_reload)

    @classmethod
    def collect_component_from_py_module(cls, py_module, working_dir, force_reload=False):
        """Collect single dsl component in a py module and return the executors of the components."""
        components = [component for component in cls.collect_components_from_py_module(py_module,
                                                                                       working_dir,
                                                                                       force_reload)]

        def defined_in_current_file(component):
            entry_file = inspect.getfile(component._func)
            component_path = py_module.replace('.', '/') + '.py'
            return Path(entry_file).resolve().absolute() == (Path(working_dir) / component_path).resolve().absolute()

        components = [component for component in components if defined_in_current_file(component)]
        if len(components) == 0:
            return None
        component = components[0]
        entry_file = inspect.getfile(component._func)
        if len(components) > 1:
            raise TooManyDSLComponentsError(len(components), entry_file)
        component.check_entry_valid(entry_file)
        return component

    @classmethod
    def collect_components_from_py_module(cls, py_module, working_dir=None, force_reload=False):
        """Collect all components in a python module and return the executors of the components."""
        if isinstance(py_module, str):
            try:
                py_module = _import_component_with_working_dir(py_module, working_dir, force_reload)
            except Exception as e:
                raise ImportError("""Error occurs when import component '%s': %s.\n
                Please make sure all requirements inside conda.yaml has been installed.""" % (py_module, e)) from e
        for _, obj in inspect.getmembers(py_module):
            if cls.look_like_component(obj):
                component = ComponentExecutor(obj)
                component.check_py_module_valid(py_module)
                yield component

    @classmethod
    def look_like_component(cls, f):
        """Return True if f looks like a component."""
        if not isinstance(f, types.FunctionType):
            return False
        if not hasattr(f, cls.INJECTED_FIELD):
            return False
        return True

    @classmethod
    def _get_executor_by_job_type(cls, job_type):
        executors = [_BasicComponentExecutor, _ParallelComponentExecutor]
        for executor in executors:
            if executor.is_valid_job_type(job_type):
                return executor
        return None

    def check_entry_valid(self, entry_file):
        """Check whether the entry file is valid to make sure it could be run in AzureML."""
        return self._executor.check_entry_valid(entry_file)

    def check_py_module_valid(self, py_module):
        """Check whether the entry py module is valid to make sure it could be run in AzureML."""
        return self._executor.check_py_module_valid(py_module)

    def _update_func(self, func: types.FunctionType):
        # Set the injected field so the function could be used to initializing with `ComponentExecutor(func)`
        setattr(func, self.INJECTED_FIELD, self._raw_spec_args)
        if hasattr(self._executor, '_update_func'):
            self._executor._update_func(func)


class _BasicComponentExecutor:
    SPEC_CLASS = BaseModuleSpec  # This class is used to initialize a component spec instance.
    SPECIAL_FUNC_CHECKERS = {
        'Coroutine': inspect.iscoroutinefunction,
        'Async generator': inspect.isasyncgenfunction,
        'Generator': inspect.isgeneratorfunction,
    }
    VALID_SPECIAL_FUNCS = set()

    def __init__(self, func: types.FunctionType, spec_args=None):
        """Initialize a ComponentExecutor with a function."""
        if spec_args is None:
            spec_args = getattr(func, ComponentExecutor.INJECTED_FIELD)
        self._spec_args = copy.deepcopy(spec_args)
        self._assert_job_type(self.job_type)
        self._assert_valid_func(func)
        self._func = func
        self._arg_mapping = self._analyze_annotations(func)
        self._parallel_inputs = None
        if 'parallel_inputs' in spec_args:
            self._parallel_inputs = _InputFileList(self._spec_args.pop('parallel_inputs'))

    @property
    def job_type(self):
        return self._spec_args.get('job_type', 'basic')

    @property
    def spec(self):
        """
        Return the module spec instance of the component.

        Initialized by the function annotations and the meta data.
        """
        io_properties = self._generate_spec_io_properties(self._arg_mapping, self._parallel_inputs)
        return self.SPEC_CLASS(**self._spec_args, **io_properties)

    def get_interface(self):
        """Return the interface of this component.

        :return: A dictionary including the definition of inputs/outputs/params.
        """
        properties = self._generate_spec_io_properties(self._arg_mapping, self._parallel_inputs)
        properties.pop('args')
        return properties

    def execute(self, argv):
        """Execute the component with command line arguments."""
        args = self._parse(argv)
        run = self._func(**args)
        if self._parallel_inputs is not None:
            run(self._parallel_inputs.load_from_argv(argv))

    def __call__(self, *args, **kwargs):
        """Directly calling a component executor equals to calling the underlying function directly."""
        return self._func(*args, **kwargs)

    @classmethod
    def is_valid_job_type(cls, job_type):
        return job_type in {None, 'mpi', 'basic'}

    @classmethod
    def _assert_job_type(cls, job_type):
        if not cls.is_valid_job_type(job_type):
            raise ValueError("Job type '%s' is invalid for '%s'" % (job_type, cls.__name__))

    def _assert_valid_func(self, func):
        """Check whether the function is valid, if it is not valid, raise."""
        for k, checker in self.SPECIAL_FUNC_CHECKERS.items():
            if k not in self.VALID_SPECIAL_FUNCS:
                if checker(func):
                    raise NotImplementedError("%s function is not supported for %s component now." % (k,
                                                                                                      self.job_type))

    def check_entry_valid(self, entry_file):
        """Check whether the entry file call .execute(sys.argv) to make sure it could be run in AzureML."""
        # Now we simply use string search, will be refined in the future.
        main_code = """if __name__ == '__main__':\n    %sExecutor(%s).execute(sys.argv)""" % (
            'Component', self._func.__name__)
        module_main_code = """if __name__ == '__main__':\n    %sExecutor(%s).execute(sys.argv)""" % (
            'Module', self._func.__name__)
        with open(entry_file) as fin:
            content = fin.read()
            if main_code not in content and module_main_code not in content:
                msg = "The following code doesn't exist in the entry file, it may not run correctly.\n%s" % main_code
                logger.warning(msg)

    def check_py_module_valid(self, py_module):
        pass

    @classmethod
    def _parse_with_mapping(cls, argv, arg_mapping):
        """Use the parameters info in arg_mapping to parse commandline params.

        :param argv: Command line arguments like ['--param-name', 'param-value']
        :param arg_mapping: A dict contains the mapping from param key 'param_name' to _ComponentBaseParam
        :return: params: The parsed params used for calling the user function.
        """
        parser = argparse.ArgumentParser()
        for param in arg_mapping.values():
            param.add_to_arg_parser(parser)
        args, _ = parser.parse_known_args(argv)

        # Convert the string values to real params of the function.
        params = {}
        for name, param in arg_mapping.items():
            val = getattr(args, param.to_var_name())
            if val is None:
                if isinstance(param, _ComponentOutputPort) or not param.optional:
                    raise RequiredParamParsingError(name=param.name, arg_string=param.arg_string)
                continue
            # If it is a parameter, we help the user to parse the parameter,
            # if it is an input port, we use load to get the param value of the port,
            # otherwise we just pass the raw value as the param value.
            param_value = val
            if isinstance(param, _ComponentParam):
                param_value = param.parse_and_validate(val)
            elif isinstance(param, _ComponentInputPort):
                param_value = param.load(val)
            params[name] = param_value
            # For OutputDirectory, we will create a folder for it.
            if isinstance(param, OutputDirectory) and not Path(val).exists():
                Path(val).mkdir(parents=True, exist_ok=True)
        return params

    def _parse(self, argv):
        return self._parse_with_mapping(argv, self._arg_mapping)

    @classmethod
    def _generate_spec_outputs(cls, arg_mapping):
        """Generate output ports of a component, from the return annotation and the arg annotations.

        The outputs including the return values and the special PathOutputPort in args.
        """
        return [val for val in arg_mapping.values() if isinstance(val, _ComponentOutputPort)]

    @classmethod
    def _generate_spec_inputs(cls, arg_mapping, parallel_inputs: _InputFileList = None):
        """Generate input ports of the component according to the analyzed argument mapping."""
        input_ports = [val for val in arg_mapping.values() if isinstance(val, _ComponentInputPort)]
        if parallel_inputs:
            input_ports = [port for port in parallel_inputs.inputs] + input_ports
        return input_ports

    @classmethod
    def _generate_spec_params(cls, arg_mapping):
        """Generate parameters of the component according to the analyzed argument mapping."""
        return [val for val in arg_mapping.values() if isinstance(val, _ComponentParam)]

    @classmethod
    def _generate_spec_io_properties(cls, arg_mapping, parallel_inputs=None):
        """Generate the required properties for a component spec according to the annotation of a function."""
        inputs = cls._generate_spec_inputs(arg_mapping, parallel_inputs)
        outputs = cls._generate_spec_outputs(arg_mapping)
        params = cls._generate_spec_params(arg_mapping)
        args = []
        for val in inputs + params + outputs:
            if isinstance(val, (_ComponentInputPort, _ComponentParam)) and val.optional:
                args.append(val.arg_group())
            else:
                args += val.arg_group()
        return {'inputs': inputs, 'outputs': outputs, 'params': params, 'args': args}

    @classmethod
    def _analyze_annotations(cls, func):
        """Analyze the annotation of the function to get the parameter mapping dict and the output port list.

        :param func:
        :return: (param_mapping, output_list)
            param_mapping: The mapping from function param names to input ports/component parameters;
            output_list: The output port list analyzed from return annotations.
        """
        mapping = OrderedDict()
        sig = inspect.signature(func)
        for param_name, param_attr in sig.parameters.items():
            annotation = cls._generate_parameter_annotation(param_attr)
            if annotation.name is None:
                annotation.update_name(_to_camel_case(param_name))
            annotation.arg_name = param_name
            mapping[param_name] = annotation

        return mapping

    @classmethod
    def _generate_parameter_annotation(cls, param_attr):
        """Generate an input port/parameter according to a param annotation of the function."""
        annotation = param_attr.annotation

        # If the user forgot to initialize an instance, help him to initalize.
        if isinstance(annotation, type) and issubclass(annotation, _ComponentBaseParam):
            annotation = annotation()

        # If the param doesn't have annotation, we get the annotation from the default value.
        # If the default value is None or no default value, it is treated as str.
        if annotation is param_attr.empty:
            default = param_attr.default
            annotation = str if default is None or default is param_attr.empty else type(param_attr.default)

        # An enum type will be converted to EnumParameter
        if isinstance(annotation, EnumMeta):
            annotation = EnumParameter(enum=annotation)

        # If the annotation is not one of _ComponentParam/ComponentInputPort/ComponentPort,
        # we use DATA_TYPE_MAPPING to get the corresponding class according to the type of annotation.
        if not isinstance(annotation, (_ComponentParam, _ComponentInputPort, _ComponentOutputPort)):
            param_cls = _ComponentParam.DATA_TYPE_MAPPING.get(annotation)
            if param_cls is None:
                # If the type is still unrecognized, we treat is as string.
                param_cls = StringParameter
            annotation = param_cls()
        annotation = copy.copy(annotation)

        # If the default value of a parameter is set, set the port/param optional,
        # and set the default value of a parameter.
        # Note that output port cannot be optional.
        if not isinstance(param_attr, _ComponentOutputPort) and param_attr.default is not param_attr.empty:
            annotation.set_optional()
            # Only parameter support default value in yaml.
            if isinstance(annotation, _ComponentParam):
                annotation.update_default(param_attr.default)

        return annotation

    def _update_func(self, func):
        pass


class _ParallelComponentExecutor(_BasicComponentExecutor):
    """This executor handle parallel component specific operations to enable parallel component."""

    SPEC_CLASS = ParallelRunModuleSpec
    JOB_TYPE = 'parallel'
    FIELDS = {'init', 'run', 'shutdown'}
    CONFLICT_ERROR_TPL = "It is not allowed to declare {}() once a parallel component is defined."
    VALID_SPECIAL_FUNCS = {'Generator'}

    def __init__(self, func: callable, spec_args=None):
        """Initialize a ParallelComponentExecutor with a provided function."""
        super().__init__(func, spec_args)
        if not self._parallel_inputs:
            raise ValueError(
                "Parallel component should have at lease one parallel input, got 0.",
            )
        self._output_keys = [key for key, val in self._arg_mapping.items() if isinstance(val, OutputDirectory)]
        if len(self._output_keys) == 0:
            raise ValueError(
                "Parallel component should have at least one OutputDirectory, got %d." % len(self._output_keys)
            )
        self._args = {}
        self._spec_args.update({
            'input_data': [port.name for port in self._parallel_inputs.inputs],
            # We use the first output as the parallel output data.
            # This is only a workaround according to current parallel run design, picking any output port is OK.
            'output_data': self._arg_mapping[self._output_keys[0]].name,
        })
        command = self._spec_args.pop('command')
        self._spec_args['entry'] = command[-1]
        self._spec_args.pop('job_type')
        self._run_func = None
        self._generator = None

    def execute(self, argv, batch_size=4):
        """Execute the component using parallel run style. This is used for local debugging."""
        self.init_argv(argv)

        files = self._parallel_inputs.load_from_argv(argv)
        # Use multiprocessing to run batches.
        count = len(files)
        batches = (count + batch_size - 1) // batch_size
        nprocess = min(max(batches, 1), multiprocessing.cpu_count())
        logger.info("Run %d batches to process %d files." % (batches, count))
        batch_files = [files[i * batch_size: (i + 1) * batch_size] for i in range(batches)]
        with ThreadPool(nprocess) as pool:
            batch_results = pool.map(self.run, batch_files)
        results = []
        for result in batch_results:
            results += result
        shutdown_result = self.shutdown()
        return shutdown_result if shutdown_result is not None else results

    @staticmethod
    def _remove_ambiguous_option_in_argv(argv: list, parse_method):
        """Remove ambiguous options in argv for an argparser method.

        This is a workaround to solve the issue that parallel run will add some other command options
        which will cause the problem 'ambiguous option'.
        """
        pattern = re.compile(r"error: ambiguous option: (\S+) could match")
        while True:
            stderr = StringIO()
            with contextlib.redirect_stderr(stderr):
                try:
                    parse_method(argv)
                except SystemExit:
                    stderr_value = stderr.getvalue()
                    match = pattern.search(stderr_value)
                    if not match:
                        # If we cannot found such pattern, which means other problems is raised, we directly raise.
                        sys.stdout.write(stderr_value)
                        raise
                    # Remove the option_str and the value of it.
                    option_str = match.group(1)
                    logger.debug("Ambiguous option '%s' is found in argv, remove it." % option_str)
                    idx = argv.index(option_str)
                    argv = argv[:idx] + argv[idx + 2:]
                else:
                    # If no exception is raised, return the ready args.
                    return argv

    def init(self):
        """Init params except for the InputFiles with the sys args when initializing parallel component.

        This method will only be called once in one process.
        """
        return self.init_argv(sys.argv)

    def init_argv(self, argv=None):
        """Init params except for the InputFiles with argv."""
        if argv is None:
            argv = sys.argv
        logger.info("Initializing parallel component, argv = %s" % argv)
        mapping = copy.copy(self._arg_mapping)
        argv = self._remove_ambiguous_option_in_argv(
            argv, functools.partial(self._parse_with_mapping, arg_mapping=mapping),
        )
        args = self._parse_with_mapping(argv, mapping)
        logger.info("Parallel component initialized, args = %s" % args)
        ret = self._func(**args)
        # If the init function is a generator, the first yielded result is the run function.
        if isinstance(ret, types.GeneratorType):
            self._generator = ret
            ret = next(ret)

        # Make sure the return result is a callable.
        if callable(ret):
            self._run_func = ret
        else:
            raise TypeError("Return/Yield result of the function must be a callable, got '%s'." % (type(ret)))

        sig = inspect.signature(self._run_func)
        if len(sig.parameters) != 1:
            raise ValueError(
                "The method {}() returned by {}() has incorrect signature {}."
                " It should have exact one parameter.".format(ret.__name__, self._func.__name__, sig)
            )
        return self._run_func

    def run(self, files):
        results = self._run_func(files)
        if results is not None:
            return files
        return results

    def shutdown(self):
        if self._generator:
            # If the function is using yield, call next to run the codes after yield.
            while True:
                try:
                    next(self._generator)
                except StopIteration as e:
                    return e.value

    def check_entry_valid(self, entry_file):
        pass

    def check_py_module_valid(self, py_module):
        # For parallel component, the init/run/shutdown in py_module should be
        # _ParallelComponentExecutor.init/run/shutdown
        for attr in self.FIELDS:
            func = getattr(py_module, attr)
            if not self.is_valid_init_run_shutdown(func, attr):
                raise AttributeError(self.CONFLICT_ERROR_TPL.format(attr))

    def _update_func(self, func: types.FunctionType):
        # For a parallel component, we should update init/run/shutdown for the script.
        # See "Write your inference script" in the following link.
        # https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-parallel-run-step
        py_module = importlib.import_module(func.__module__)
        for attr in self.FIELDS:
            func = getattr(py_module, attr, None)
            # We don't allow other init/run/shutdown in the script.
            if func is not None and not self.is_valid_init_run_shutdown(func, attr):
                raise AttributeError(self.CONFLICT_ERROR_TPL.format(attr))
            setattr(py_module, attr, getattr(self, attr))

    @classmethod
    def is_valid_init_run_shutdown(cls, func, attr):
        return isinstance(func, types.MethodType) and func.__func__ == getattr(_ParallelComponentExecutor, attr)

    @classmethod
    def _generate_spec_io_properties(cls, arg_mapping, parallel_inputs=None):
        """Generate the required properties for a component spec according to the annotation of a function.

        For parallel component, we need to remove InputFiles and --output in args.
        """
        properties = super()._generate_spec_io_properties(arg_mapping, parallel_inputs)
        args_to_remove = []
        for k, v in arg_mapping.items():
            # InputFiles and the output named --output need to be removed in the arguments.
            # For InputFiles: the control script will handle it and pass the files to run();
            # For the output, the control script will add an arg item --output so we should not define it again.
            if v.to_cli_option_str() == '--output':
                args_to_remove.append(v)
        if parallel_inputs:
            args_to_remove += [port for port in parallel_inputs.inputs]
        args = properties['args']
        for arg in args_to_remove:
            if isinstance(arg, _ComponentInputPort) and arg.optional:
                args.remove(arg.arg_group())
            else:
                idx = args.index(arg.arg_string)
                args.remove(arg.arg_string)
                args.remove(args[idx])
        return properties

    @classmethod
    def is_valid_job_type(cls, job_type):
        return job_type == cls.JOB_TYPE
