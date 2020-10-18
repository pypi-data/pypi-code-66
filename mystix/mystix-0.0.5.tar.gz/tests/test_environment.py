import unittest
from typing import cast

from mystix.language.evaluation.vars import Environment, UndefinedVariableError
from mystix.language.shared.primitives.values import IntegerValue, Value


class EnvironmentTests(unittest.TestCase):

    def test_undefined(self):
        e = Environment()
        try:
            e.get_val("color")
            self.fail()
        except UndefinedVariableError:
            pass

    def test_undefined_undef(self):
        e = Environment()
        try:
            e.undef("color")
            self.fail()
        except UndefinedVariableError:
            pass

    def test_set_no_extend(self):
        e = Environment()
        try:
            e.set_val("width", IntegerValue(5))
            self.fail()
        except UndefinedVariableError:
            pass

    def test_basic(self):
        e = Environment()
        e.extend("width", IntegerValue(3))
        e.extend("height", IntegerValue(4))
        self.assertEqual(3, cast(IntegerValue, e.get_val("width")).value)
        self.assertEqual(4, cast(IntegerValue, e.get_val("height")).value)

    def test_basic_set(self):
        e = Environment()
        e.extend("width", IntegerValue(3))
        self.assertEqual(3, cast(IntegerValue, e.get_val("width")).value)
        e.set_val("width", IntegerValue(8))
        self.assertEqual(8, cast(IntegerValue, e.get_val("width")).value)

    def test_undef(self):
        e = Environment()
        e.extend("width", IntegerValue(3))
        self.assertEqual(3, cast(IntegerValue, e.get_val("width")).value)
        e.undef("width")
        try:
            e.get_val("width")
            self.fail()
        except UndefinedVariableError:
            pass

    def test_multiple_extend(self):
        e = Environment()
        e.extend("width", IntegerValue(3))
        e.extend("width", IntegerValue(6))
        self.assertEqual(6, cast(IntegerValue, e.get_val("width")).value)

    def test_multiple_extend_undef(self):
        e = Environment()
        e.extend("width", IntegerValue(3))
        e.extend("width", IntegerValue(6))
        self.assertEqual(6, cast(IntegerValue, e.get_val("width")).value)
        e.undef("width")
        self.assertEqual(3, cast(IntegerValue, e.get_val("width")).value)
