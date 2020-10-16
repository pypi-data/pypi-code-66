import unittest

from json_settings import TerminusSetting

from json_settings import TypeAttributeTypeError
from json_settings import SettingTypeError
from json_settings import TypeAttributeNotImplementedError
from json_settings import SettingCheckError


class Float(TerminusSetting):

    @TerminusSetting.assign
    def __init__(self, value):
        self.type = float

    def check(self):
        pass


class Int(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.type = int

    def check(self):
        pass


class NoType(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.typo = int

    def check(self):
        pass


class NotType(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.type = 1

    def check(self):
        pass


class ValueErrorCheck(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.type = int

    def check(self):
        if self.value == 1:
            raise ValueError("Cannot be equal to 1")


class TypeErrorCheck(TerminusSetting):
    @TerminusSetting.assign
    def __init__(self, value):
        self.type = int

    def check(self):
        if type(self.value) is not int:
            raise TypeError("Not an integer")


class TestTerminusSetting(unittest.TestCase):
    """The unit tests for the :class:`~.TerminusSetting` class.

    """

    def test_type_attribute_not_implemented_error(self):
        with self.assertRaises(TypeAttributeNotImplementedError):
            NoType(1)

    def test_type_attribute_type_error(self):
        with self.assertRaises(TypeAttributeTypeError):
            NotType(1)

    def test_literal_assignment(self):
        setting = Float(1.0)
        self.assertEqual(setting.value, 1.0)
        self.assertEqual(setting.get, 1.0)

    def test_value_check_error(self):
        with self.assertRaises(SettingCheckError):
            ValueErrorCheck(1)

    def test_setting_type_error(self):
        with self.assertRaises(SettingTypeError):
            Int("fish")
