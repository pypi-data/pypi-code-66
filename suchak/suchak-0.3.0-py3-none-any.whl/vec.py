import numpy as np
from numba import typeof, types

from suchak.jitclass import jitclass

_series_vtable = {}


def series_factory(dtype: np.dtype):
    try:
        return _series_vtable[dtype]
    except KeyError:
        pass

    @jitclass
    class Series:
        buf: typeof(np.empty(0, dtype=dtype))
        idx: types.int32

        def __init__(self, capacity: int):
            self.buf = np.empty(capacity, dtype=dtype)
            self.idx = len(self.buf)

        def array(self) -> np.ndarray:
            return self.buf[self.idx :]

        def next(self):
            self.idx -= 1

            # perform array-doubling if needed
            if self.idx < 0:
                old = self.buf
                new = np.empty(len(old) * 2, dtype=old.dtype)
                new[-len(old) :] = old
                self.buf = new
                self.idx = len(old) - 1

        def push(self, value):
            self.next()
            self[0] = value

        def __getitem__(self, idx: int):
            return self.buf[self.idx + idx]

        def __setitem__(self, idx: int, value):
            self.buf[self.idx + idx] = value

    _series_vtable[dtype] = Series
    return Series


FloatSeries = series_factory(np.dtype("float"))
