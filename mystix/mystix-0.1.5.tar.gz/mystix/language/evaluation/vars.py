from collections import defaultdict
import random

from mystix.language.shared.primitives.values import Value, IntegerValue
from mystix.language.evaluation.errors import LanguageError


class OutOfMemoryError(LanguageError):
    pass


class SegmentationFault(LanguageError):
    pass


def _rand_mem_() -> Value:
    # simulate uninitialized memory
    return IntegerValue(random.randint(0, 100))


class Memory:

    MAX_VALUES = 2000   # memory limit

    def __init__(self):
        self._map_ = defaultdict(
            lambda: _rand_mem_())

    def get_fresh_loc(self) -> int:
        i = 0
        while i < self.MAX_VALUES:
            if i in self._map_:
                i = i + 1
            else:
                return i
        raise OutOfMemoryError()

    def _valid_loc_(self, loc: int) -> bool:
        return 0 <= loc < self.MAX_VALUES

    def write(self, loc: int, val: Value) -> Value:
        if not self._valid_loc_(loc):
            raise SegmentationFault
        else:
            self._map_[loc] = val
            return val

    def read(self, loc: int) -> Value:
        if not self._valid_loc_(loc):
            raise SegmentationFault
        else:
            return self._map_[loc]

    def free(self, loc: int) -> None:
        if not self._valid_loc_(loc):
            raise SegmentationFault
        else:
            self._map_.pop(loc)


class UndefinedVariableError(LanguageError):
    def __init__(self, var_name: str):
        super(LanguageError, self).__init__(
            "Variable '%s' was referenced out of scope!" % var_name)


class Environment:

    def __init__(self):
        self._mem_ = Memory()
        self._map_ = defaultdict(lambda: [])

    def extend(self, name: str, val: Value) -> int:
        l: int = self._mem_.get_fresh_loc()
        self._mem_.write(l, val)
        self._map_[name].append(l)
        return l

    def get_val(self, name: str) -> Value:
        locations = self._map_[name]
        q = len(locations)
        if q == 0:
            raise UndefinedVariableError(name)
        else:
            return self._mem_.read(locations[q-1])

    def set_val(self, name: str, val: Value) -> Value:
        locations = self._map_[name]
        q = len(locations)
        if q == 0:
            raise UndefinedVariableError(name)
        else:
            return self._mem_.write(locations[q-1], val)

    def undef(self, name) -> None:
        locations = self._map_[name]
        q = len(locations)
        if q == 0:
            raise UndefinedVariableError(name)
        else:
            l: int = locations[q-1]
            self._map_[name] = locations[:q-1]
            self._mem_.free(l)
