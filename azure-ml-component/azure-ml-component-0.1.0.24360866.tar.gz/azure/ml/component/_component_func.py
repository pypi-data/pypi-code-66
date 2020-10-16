# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import Callable
import warnings

from azure.ml.component._restclients.service_caller_factory import _DesignerServiceCallerFactory
from azureml.core import Workspace
from ._module_dto import ModuleDto

from .core._component_definition import ComponentDefinition
from ._dynamic import create_kw_function_from_parameters, KwParameter
from ._utils import _get_or_sanitize_python_name


def _get_module_yaml(workspace: Workspace, module_version_id: str):
    """
    Display yaml of module.

    :return: yaml of module
    :rtype: str
    """
    try:
        service_caller = _DesignerServiceCallerFactory.get_instance(workspace)
        result = service_caller.get_module_yaml_by_id(module_version_id)
        return str(result)
    except Exception as e:
        warnings.warn("get module yaml meet exception : %s" % str(e))
        return None


def to_component_func(ws: Workspace, module_dto: ModuleDto, return_yaml: bool,
                      component_creation_func) -> Callable:
    func_docstring_lines = []
    module_description = module_dto.description.strip() if module_dto.description else ""
    func_docstring_lines.append(module_description)

    transformed_inputs, transformed_parameters, all_outputs = module_dto.get_module_inputs_outputs(
        return_yaml)
    all_params = transformed_inputs + transformed_parameters

    namespace = module_dto.namespace
    if namespace is None:
        func_name = "[module] {}".format(module_dto.module_name)
    else:
        func_name = "[module] {} (namespace: {})".format(
            module_dto.module_name, namespace)

    # TODO: remove this when SMT added yaml on register module
    if module_dto.yaml_str is None:
        module_dto.yaml_str = _get_module_yaml(
            ws, module_dto.module_version_id)

    yaml = module_dto.yaml_str if return_yaml else None
    if yaml:
        # Use ```yaml\n{1}\n``` to make the yaml part readable in markdown.
        doc_string = '{0}\n\nModule yaml:\n```yaml\n{1}\n```'.format(
            module_description, yaml)
    else:
        doc_string = '{0}\n\n{1}'.format(
            module_description,
            '\n'.join(_get_docstring_lines(all_params, all_outputs,
                                           module_dto.module_python_interface.outputs_name_mapping)))
    dynamic_func = create_kw_function_from_parameters(
        component_creation_func,
        documentation=doc_string,
        parameters=all_params,
        func_name=func_name,
    )

    return dynamic_func


def get_dynamic_input_parameter(self: ComponentDefinition):
    """Return the dynamic parameter of the definition's input ports."""
    return [KwParameter(name=name, annotation=str(input.type), default=None, _type=str(input.type))
            for name, input in self.inputs.items() if not input.is_param()]


def get_dynamic_param_parameter(self: ComponentDefinition):
    """Return the dynamic parameter of the definition's input parameters."""
    return [KwParameter(name=name, annotation=str(param.type), default=None, _type=str(param.type))
            for name, param in self.inputs.items() if param.is_param()]


def _get_docstring_lines(all_params, all_outputs, param_name_dict):
    docstring_lines = []
    if len(all_params) > 0:
        docstring_lines.append("\n")
    for param in all_params:
        if param.default is None or (isinstance(param.default, str) and len(param.default.strip()) == 0):
            docstring_lines.append(":param {}: {}".format(param.name, param.annotation))
        else:
            docstring_lines.append(":param {}: {}. (optional, default value is {}.)"
                                   .format(param.name, param.annotation, param.default))
        docstring_lines.append(":type {}: {}".format(param.name, param._type))

    if len(all_outputs) > 0:
        docstring_lines.append("\n")
    for o in all_outputs:
        output_name = \
            _get_or_sanitize_python_name(o.name, param_name_dict)
        docstring_lines.append(":output {}: {}".format(output_name,
                                                       o.description if o.description is not None else o.name))
        docstring_lines.append(":type: {}: {}".format(
            output_name, str(o.data_type_id)))
    return docstring_lines
