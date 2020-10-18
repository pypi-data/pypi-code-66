# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""A decorator which builds a :class:azure.ml.component.Component."""

from .component import component, ComponentExecutor
from ._annotations import InputDirectory, InputFile, OutputDirectory, OutputFile, \
    StringParameter, EnumParameter, IntParameter, FloatParameter, BoolParameter
from ._exceptions import RequiredParamParsingError, TooManyDSLComponentsError

__all__ = [
    'component',
    'ComponentExecutor',
    'TooManyDSLComponentsError',
    'InputDirectory',
    'InputFile',
    'OutputDirectory',
    'OutputFile',
    'StringParameter',
    'EnumParameter',
    'IntParameter',
    'FloatParameter',
    'BoolParameter',
    'RequiredParamParsingError',
]
