# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Sequence, Optional, Union


def _remove_empty_values(data):
    if not isinstance(data, dict):
        return data
    return {k: _remove_empty_values(v) for k, v in data.items() if v is not None}


class InputDefinition:

    _PARAM_VALIDATORS = {
        'String': None,
        'Float': None,
        'Integer': None,
        'Boolean': None,
        'Enum': None,

        # The following types are internal usage for built-in modules.
        'Script': None,
        'ColumnPicker': None,
        'Credential': None,
        'ParameterRange	': None
    }  # These validators are used to validate input parameter values.

    def __init__(self, name, type, description=None, default=None, optional=False, enum=None, min=None, max=None):
        """Define an input for the component."""
        self._name = name
        self._type = type
        self._description = description
        self._optional = optional
        self._default = default
        self._enum = enum
        self._min = min
        self._max = max

    @property
    def name(self) -> str:
        """"Return the name of the input."""
        return self._name

    @property
    def type(self) -> str:
        """"Return the type of the input."""
        return self._type

    @property
    def optional(self) -> bool:
        """"Return whether the input is optional."""
        return self._optional

    @property
    def default(self) -> Optional[Union[str, int, float]]:
        """"Return the default value of the input."""
        return self._default

    @property
    def description(self) -> Optional[str]:
        """"Return the description of the input."""
        return self._description

    @property
    def enum(self) -> Optional[Sequence[str]]:
        """"Return the enum values of the input for an enum input."""
        return self._enum

    @property
    def max(self) -> Optional[Union[int, float]]:
        """"Return the maximum value of the input for a numeric input."""
        return self._max

    @property
    def min(self) -> Optional[Union[int, float]]:
        """"Return the minimum value of the input for a numeric input."""
        return self._min

    def to_dict(self) -> dict:
        """Convert the InputDefinition object to a dict."""
        keys = ['name', 'type', 'description', 'min', 'max', 'enum', 'default', 'optional']
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    @classmethod
    def from_dict(cls, dct: dict):
        """Convert a dict to an InputDefinition object."""
        return cls(**dct)

    @classmethod
    def load(cls, data):
        """Load an InputDefinition according to the input data type."""
        if isinstance(data, InputDefinition):
            return data
        elif isinstance(data, dict):
            return cls.from_dict(data)
        raise NotImplementedError("The conversion from %s to %s is not implemented." % (type(data), cls))

    def is_param(self):
        """Return True if this input is a parameter, otherwise(it is an input port) return False."""
        return isinstance(self.type, str) and self.type in self._PARAM_VALIDATORS

    def validate(self, value):
        """Validate whether the value is OK as the input."""
        validator = self._PARAM_VALIDATORS.get(str(self.type))
        if validator is None:
            return
        # TODO: Validate logic goes here


class OutputDefinition:

    def __init__(self, name, type, description=None):
        """Define an output definition for the component."""
        self._name = name
        self._type = type
        self._description = description

    @property
    def name(self) -> str:
        """"Return the name of the output."""
        return self._name

    @property
    def type(self) -> str:
        """"Return the type of the output."""
        return self._type

    @property
    def description(self) -> str:
        """"Return the description of the output."""
        return self._description

    @classmethod
    def from_dict(cls, dct: dict):
        """Convert a dict to an OutputDefinition object."""
        return cls(**dct)

    def to_dict(self):
        """Convert the OutputDefinition object to a dict."""
        keys = ['name', 'type', 'description']
        result = {key: getattr(self, key) for key in keys}
        return _remove_empty_values(result)

    @classmethod
    def load(cls, data):
        """Load an OutputDefinition according to the output data type."""
        if isinstance(data, OutputDefinition):
            return data
        elif isinstance(data, dict):
            return cls.from_dict(data)
        raise NotImplementedError("The conversion from %s to %s is not implemented." % (type(data), cls))
