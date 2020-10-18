# Module with most used assertions and checks
import numpy as np
from math import isnan


def is_na(var: object) -> bool:
    na = var is None or var is np.nan
    try:
        na = na or isnan(var)
    except TypeError:
        pass
    return na


if __name__ == "__main__":
    print(is_na(None))
    print(is_na(np.nan))
    print(is_na(float('nan')))
    print(is_na('x'))
    print(is_na(''))
