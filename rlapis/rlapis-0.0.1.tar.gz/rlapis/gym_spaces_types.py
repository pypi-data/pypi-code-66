from typing import Type, TypeVar, List, Optional, Dict, Any
from types import new_class
import pydantic
import gym
import numpy as np

from gym_spaces_types_errors import GymDiscreteError


class GymDiscrete(int):
    n: int
    gym_spaces_class = gym.spaces.Discrete

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            type="integer",
            description=f"gym.spaces.{cls.gym_spaces_class.__name__} type with n={cls.n}",
            gym_spaces_type=cls.gym_spaces_class.__name__,
            n={cls.n},
        )

    @classmethod
    def validate(cls, v, field: "ModelField"):
        pydantic.validators.int_validator(v)

        if v >= field.type_.n or v < 0:
            raise GymDiscreteError(value=v, n=field.type_.n)

        return cls(v)


def gym_discrete(*, n: int) -> GymDiscrete:
    # use kwargs then define conf in a dict to aid with IDE type hinting
    namespace = dict(n=n)
    return type("GymDiscreteValue", (GymDiscrete,), namespace)


T = TypeVar("T")

# This types superclass should be List[T], but cython chokes on that...
class GymBox(list):  # type: ignore
    # Needed for pydantic to detect that this is a list
    __origin__ = list
    __args__: List[Type[T]]  # type: ignore

    low: float
    high: float
    dtype: np.dtype = np.float32
    gym_spaces_class = gym.spaces.Box

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.list_length_validator

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        pydantic.utils.update_not_none(
            field_schema, low=cls.low, high=cls.high, dtype=cls.dtype
        )

    @classmethod
    def list_length_validator(
        cls, v: "List[dtype]", field: "ModelField"
    ) -> "List[dtype]":
        if v is None and not field.required:
            return None

        # v = pydantic.validators.list_validator(v)
        # v_len = len(v)

        # if cls.min_items is not None and v_len < cls.min_items:
        #     raise pydantic.errors.ListMinLengthError(limit_value=cls.min_items)

        # if cls.max_items is not None and v_len > cls.max_items:
        #     raise pydantic.errors.ListMaxLengthError(limit_value=cls.max_items)

        return cls(v)


def gym_box(
    item_type: Type[T], *, low: float, high: float, dtype: np.dtype = np.float32
) -> Type[List[T]]:
    # __args__ is needed to conform to typing generics api
    namespace = {
        "low": low,
        "high": high,
        "item_type": item_type,
        "dtype": dtype,
        "__args__": np.array([], dtype=dtype),
    }
    # We use new_class to be able to deal with Generic types
    return new_class("GymBoxValue", (GymBox,), {}, lambda ns: ns.update(namespace))
