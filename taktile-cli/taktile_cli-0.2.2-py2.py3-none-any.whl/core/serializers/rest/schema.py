import json
from collections.abc import Sequence
from typing import Any, Dict, List, Type, Union

import numpy
import pandas
from pydantic import BaseModel, conlist

from tktl.core.serializers.base import CustomDeserializingModelT
from tktl.core.serializers.utils import get_list_shape


def get_single_value_model(_value: Any) -> Type[CustomDeserializingModelT]:
    class SingleValueModel(CustomDeserializingModelT):
        value: type(_value)

        def deserialize(self):
            return self.value

    return SingleValueModel


def get_dataframe_model(
    df: pandas.DataFrame, base_model: Type[BaseModel]
) -> Type[CustomDeserializingModelT]:
    class DataFrame(base_model, CustomDeserializingModelT):
        _columns = df.columns
        _dtypes = df.dtypes

        def deserialize(self):
            _df = pandas.DataFrame.from_dict(self.dict())
            _df = _df[self._columns]  # column order
            _df = _df.astype(self._dtypes)  # column types
            return _df

    return DataFrame


def get_series_model(
    series: pandas.Series, base_model: Type[BaseModel]
) -> Type[CustomDeserializingModelT]:
    class Series(base_model, CustomDeserializingModelT):
        _name = series.name
        _dtype = series.dtype

        def deserialize(self):
            values = self.dict()[self._name]
            _series = pandas.Series(values)
            _series = _series.astype(self._dtype)  # column types
            return _series

    return Series


def get_jsonable_encoder_sequence_model(
    base_model: Type[BaseModel],
) -> Type[CustomDeserializingModelT]:
    class JsonableEncoderModel(base_model, CustomDeserializingModelT):
        def deserialize(self):
            return json.loads(self.values)

    return JsonableEncoderModel


def get_nested_sequence_model(sequence: Sequence) -> Type[CustomDeserializingModelT]:
    shape, types = get_list_shape(sequence)
    inner_model = conlist(Union[types], max_items=shape[-1], min_items=shape[-1])

    for s in reversed(shape[:-1]):
        inner_model = conlist(inner_model, max_items=s, min_items=s)
    return _nested_sequence_model(inner_models=inner_model)


def get_array_model(base_model) -> Type[CustomDeserializingModelT]:
    class ArrayModel(base_model, CustomDeserializingModelT):
        def deserialize(self):
            return numpy.array(self.dict()["__root__"])

    return ArrayModel


def get_mapping_model(base_model: Type[BaseModel]) -> Type[CustomDeserializingModelT]:
    class MappingModel(base_model, CustomDeserializingModelT):
        def deserialize(self):
            return self.dict()

    return MappingModel


class SequenceEncoderModel(CustomDeserializingModelT):
    __root__: List

    def deserialize(self):
        return self.dict()["__root__"]


def _nested_sequence_model(inner_models):
    class NestedSequenceModel(SequenceEncoderModel):
        __root__: inner_models

    return NestedSequenceModel
