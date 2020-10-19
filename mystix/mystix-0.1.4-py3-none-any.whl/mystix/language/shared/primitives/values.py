from typing import cast


class Value:

    def equals(self, v) -> bool:
        return False


class NumericalValue(Value):

    def __init__(self):
        self.value = 0

    def equals(self, v: Value) -> bool:
        if isinstance(v, NumericalValue):
            return self.value == cast(NumericalValue, v).value
        else:
            return False


class CategoricalValue(Value):

    def __init__(self, val: str = ""):
        self.value = val

    def equals(self, v: Value) -> bool:
        if isinstance(v, CategoricalValue):
            return self.value == cast(CategoricalValue, v).value
        else:
            return False


class BinaryValue(Value):

    def __init__(self, val: bool = False):
        self.value: bool = val

    def equals(self, v: Value) -> bool:
        if isinstance(v, BinaryValue):
            return self.value == cast(BinaryValue, v).value
        else:
            return False


class IntegerValue(NumericalValue):

    def __init__(self, val: int = 0):
        super(NumericalValue, self).__init__()
        self.value = val

    def __repr__(self):
        return "%d" % self.value


class FloatValue(NumericalValue):

    def __init__(self, val: float = 0.0):
        super(NumericalValue, self).__init__()
        self.value = val
