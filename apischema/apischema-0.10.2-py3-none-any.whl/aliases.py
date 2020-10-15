from collections import ChainMap
from dataclasses import fields
from typing import Callable, TypeVar, overload

from apischema.types import MappingWithUnion, Metadata

Cls = TypeVar("Cls")


@overload
def alias(alias_: str, *, override: bool = True) -> Metadata:
    ...


@overload
def alias(override: bool) -> Metadata:
    ...


@overload
def alias(aliaser: Callable[[str], str]) -> Callable[[Cls], Cls]:
    ...


def alias(arg=None, *, override: bool = True):  # type: ignore
    """Field alias or class aliaser

    :param alias_: alias of the field
    :param override: alias can be overridden by a class aliaser
    :param aliaser: compute alias for each (overridable) field of the class decorated
    """
    from apischema.metadata.keys import (
        ALIAS_METADATA,
        ALIAS_NO_OVERRIDE_METADATA,
        MERGED_METADATA,
    )

    if callable(arg):

        def aliaser(cls: Cls) -> Cls:
            for field in fields(cls):
                if (
                    field.metadata.get(ALIAS_NO_OVERRIDE_METADATA)
                    or MERGED_METADATA in field.metadata
                ):
                    continue
                alias = arg(field.metadata.get(ALIAS_METADATA, field.name))
                field.metadata = ChainMap({ALIAS_METADATA: alias}, field.metadata)
            return cls

        return aliaser
    metadata = {}
    if arg is not None:
        metadata[ALIAS_METADATA] = arg
    if not override:
        metadata[ALIAS_NO_OVERRIDE_METADATA] = True
    if not metadata:  # pragma: no cover
        raise ValueError("Alias must be called with arguments")
    return MappingWithUnion(metadata)


_global_aliaser: Callable[[str], str] = lambda s: s  # noqa E731
