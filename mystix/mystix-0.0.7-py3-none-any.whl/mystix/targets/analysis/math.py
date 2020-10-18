from mystix.language.shared.primitives.values import (
    NumericalValue, FloatValue, IntegerValue )
from mystix.language.shared.primitives.numerical import NumOp, NumFunction
from mystix.util.errors import NonExhaustiveTypeCaseError
from typing import cast

import math


class MathError(Exception):
    pass


def safe_divide(a, b):
    if b == 0:
        raise MathError("Cannot divide by zero!")
    else:
        return a / b


operations = dict({
    NumOp.PLUS: lambda a, b: a + b,
    NumOp.MINUS: lambda a, b: a - b,
    NumOp.TIMES: lambda a, b: a * b,
    NumOp.DIV: lambda a, b: safe_divide(a,b),
    NumOp.EXP: lambda a, b: a**b
})

functions = dict({
    NumFunction.LOG: lambda x: math.log(x),
    NumFunction.SIN: lambda x: math.sin(x),
    NumFunction.COS: lambda x: math.cos(x),
    NumFunction.EXP: lambda x: math.exp(x)
})

quick_func = dict({
    "inc": lambda x: x + 1,
    "dec": lambda x: x - 1
})


def apply_op(o: NumOp, a: NumericalValue, b: NumericalValue) -> NumericalValue:
    if o in operations:
        result = operations[o](a.value, b.value)
        if type(a) is IntegerValue and type(b) is IntegerValue:
            return cast(NumericalValue, IntegerValue(int(result)))
        else:
            return cast(NumericalValue, FloatValue(float(result)))
    else:
        raise NonExhaustiveTypeCaseError()


def apply_fn(f: NumFunction, x: NumericalValue) -> FloatValue:
    if f in functions:
        try:
            return FloatValue(float(functions[f](x.value)))
        except ValueError:
            raise MathError(
                "Error executing function %s with input %s" % (f,str(x.value)))

    else:
        raise NonExhaustiveTypeCaseError()


def apply_qk(f: str, x: NumericalValue) -> NumericalValue:
    result = quick_func[f](x.value)
    if type(x) is IntegerValue:
        return cast(NumericalValue, IntegerValue(int(result)))
    else:
        return cast(NumericalValue, FloatValue(float(result)))