from unittest import TestCase
from mystix.language.shared.primitives.values import (
    NumericalValue, FloatValue, IntegerValue )
from mystix.language.shared.primitives.numerical import NumOp, NumFunction
from mystix.targets.analysis.math import apply_fn, apply_op, MathError
from typing import cast


from math import pi


class MathTests(TestCase):

    def test_plus(self):
        result: NumericalValue = apply_op(
            NumOp.PLUS,
            cast(NumericalValue, IntegerValue(1)),
            cast(NumericalValue, IntegerValue(2)))
        self.assertTrue(type(result) is IntegerValue)
        self.assertTrue(result.equals(IntegerValue(3)))

    def test_minus(self):
        result: NumericalValue = apply_op(
            NumOp.MINUS,
            cast(NumericalValue, IntegerValue(1)),
            cast(NumericalValue, IntegerValue(2)))
        self.assertTrue(type(result) is IntegerValue)
        self.assertTrue(result.equals(IntegerValue(-1)))

    def test_plus_with_float(self):
        result: NumericalValue = apply_op(
            NumOp.PLUS,
            cast(NumericalValue, IntegerValue(1)),
            cast(NumericalValue, FloatValue(2.0)))
        self.assertTrue(type(result) is FloatValue)
        self.assertTrue(result.equals(FloatValue(3.0)))

    def test_divide_zero(self):
        try:
            apply_op(
                NumOp.DIV,
                cast(NumericalValue, IntegerValue(1)),
                cast(NumericalValue, IntegerValue(0)))
            self.fail()
        except MathError:
            pass

    def test_pow(self):
        result: NumericalValue = apply_op(
            NumOp.EXP,
            cast(NumericalValue, IntegerValue(2)),
            cast(NumericalValue, IntegerValue(3)))
        self.assertTrue(type(result) is IntegerValue)
        self.assertTrue(result.equals(IntegerValue(8)))

    def test_sin(self):
        result: FloatValue = apply_fn(
            NumFunction.SIN,
            cast(NumericalValue, FloatValue(pi/2)))
        self.assertTrue(result.equals(FloatValue(1.0)))

    def test_log_domain(self):
        try:
            apply_fn(
                NumFunction.LOG,
                cast(NumericalValue, IntegerValue(-1)))
            self.fail()
        except MathError:
            pass
