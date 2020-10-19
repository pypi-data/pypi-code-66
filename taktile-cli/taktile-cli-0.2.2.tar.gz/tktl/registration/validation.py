import warnings
from typing import Iterator, Sequence, Union

import pandas
import pandas.api.types as ptypes

from tktl.core.exceptions import exceptions
from tktl.core.loggers import CliLogger

logger = CliLogger()


def validate_outputs(preds) -> Union[bool, Iterator]:
    if not isinstance(preds, pandas.Series):
        preds = pandas.Series(preds)
    if not ptypes.is_numeric_dtype(pandas.Series(preds)):
        return False
    return True


def validate_binary(preds):
    if not 0 <= min(preds):
        raise exceptions.ValidationException(
            "Function output cannot be negative for endpoint kind binary"
        )

    if not max(preds) <= 1:
        raise exceptions.ValidationException(
            "Function output cannot exceed 1 for endpoint kind binary"
        )
    return True


def validate_shapes(
    x_frame: pandas.DataFrame, y_series: pandas.Series, preds: Sequence
):
    if not len(x_frame) == len(preds):
        return False
    if not len(x_frame) == len(y_series):
        return False
    return True


def data_frame_convertible(inputs):
    if len(inputs) > 1e6:
        warnings.warn(
            f"inputs is very large (N={len(inputs)}). Please consider using a smaller reference dataset."
        )
    if isinstance(inputs, pandas.DataFrame):
        return True
    try:
        pandas.DataFrame(inputs)
    except ValueError:
        warnings.warn("Could not convert inputs to pd.DataFrame")
        return False
    return True


def series_convertible(y, type_cast=None):
    if isinstance(y, pandas.Series):
        return True
    try:
        y = pandas.Series(y)
        if type_cast:
            y = y.astype(type_cast)
        y.name = y.name or "Outcome"

    except ValueError:
        warnings.warn("Could not convert y to pandas series")
        return False
    return True
