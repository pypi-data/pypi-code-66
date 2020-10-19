import typing
from functools import cached_property


_K = typing.TypeVar("_K")
_V = typing.TypeVar("_V")


class MultiMapping(typing.Mapping[_K, _V]):
    def __init__(
        self,
        value: typing.Optional[
            typing.Union[typing.Mapping[_K, _V], typing.Iterable[typing.Tuple[_K, _V]]]
        ] = None,
    ) -> None:
        if not value:
            self._list: typing.List[typing.Tuple[_K, _V]] = []
        elif isinstance(value, MultiMapping):
            self._list = list(value._list)
        elif isinstance(value, typing.Mapping):
            self._list = list(value.items())
        else:
            self._list = list(value)

    @cached_property
    def _dict(self) -> typing.Dict[_K, _V]:
        dct = {}
        if self._list:
            for k, v in self._list:
                if k not in dct:
                    dct[k] = v
        return dct

    def keys(self) -> typing.KeysView[_K]:
        return self._dict.keys()

    def values(self) -> typing.ValuesView[_V]:
        return self._dict.values()

    def items(self) -> typing.ItemsView[_K, _V]:
        return self._dict.items()

    def multi_items(self) -> typing.List[typing.Tuple[_K, _V]]:
        return list(self._list)

    @typing.overload
    def get(self, key: _K) -> typing.Optional[_V]:
        ...  # pragma: nocover

    @typing.overload
    def get(self, key: _K, default: typing.Any = None) -> typing.Any:
        ...  # pragma: nocover

    def get(self, key: _K, default: typing.Any = None) -> typing.Any:
        try:
            return self._dict[key]
        except KeyError:
            return default

    def getlist(self, key: _K) -> typing.List[_V]:
        return [item_value for item_key, item_value in self._list if item_key == key]

    def __getitem__(self, key: _K) -> _V:
        return self._dict[key]

    def __contains__(self, key: object) -> bool:
        return key in self._dict

    def __iter__(self) -> typing.Iterator[_K]:
        return iter(self._dict.keys())

    def __len__(self) -> int:
        return len(self._dict)

    def __eq__(self, other: typing.Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return sorted(self._list) == sorted(other._list)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._list!r})"


class ImmutableHeaders(typing.Mapping[str, str]):
    _dict: typing.Dict[str, str]

    def __init__(self, value: typing.Dict[str, str]):
        self._dict = value

    def keys(self) -> typing.KeysView[str]:
        return self._dict.keys()

    def values(self) -> typing.ValuesView[str]:
        return self._dict.values()

    def items(self) -> typing.ItemsView[str, str]:
        return self._dict.items()

    @typing.overload
    def get(self, key: str) -> typing.Optional[str]:
        ...  # pragma: nocover

    @typing.overload
    def get(self, key: str, default: typing.Any = None) -> typing.Any:
        ...  # pragma: nocover

    def get(self, key: str, default: typing.Any = None) -> typing.Any:
        try:
            return self._dict[key.lower()]
        except KeyError:
            return default

    def __getitem__(self, key: str) -> str:
        return self._dict[key.lower()]

    def __contains__(self, key: object) -> bool:
        return isinstance(key, str) and key.lower() in self._dict

    def __iter__(self) -> typing.Iterator[str]:
        return iter(self._dict.keys())

    def __len__(self) -> int:
        return len(self._dict)

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, self.__class__) and self._dict == other._dict

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._dict!r})"


class MutableHeaders(ImmutableHeaders):
    def __init__(
        self,
        value: typing.Optional[
            typing.Union[
                typing.Mapping[str, str], typing.Iterable[typing.Tuple[str, str]]
            ]
        ] = None,
    ):
        if not value:
            self._list = []
        elif isinstance(value, typing.Mapping):
            self._list = [(k.lower(), v) for k, v in value.items()]
        else:
            self._list = [(k.lower(), v) for k, v in value]

    @cached_property
    def _dict(self) -> typing.Dict[str, str]:  # type: ignore
        dct = {}
        if self._list:
            for k, v in self._list:
                if k not in dct:
                    dct[k] = v
        return dct

    def multi_items(self) -> typing.List[typing.Tuple[str, str]]:
        return list(self._list)

    def add(self, key: str, value: str) -> None:
        key = key.lower()
        value = str(value)
        if key not in self._dict:
            self._dict[key] = value
        self._list.append((key, value))

    def getlist(self, key: str) -> typing.List[str]:
        key = key.lower()
        return [item_value for item_key, item_value in self._list if item_key == key]

    def __setitem__(self, key: str, value: str) -> None:
        key = key.lower()
        value = str(value)
        if key not in self._dict:
            self._list.append((key, value))
        else:
            found_indexes = [
                idx for idx, (item_key, _) in enumerate(self._list) if item_key == key
            ]
            for idx in reversed(found_indexes[1:]):
                del self._list[idx]
            self._list[found_indexes[0]] = (key, value)
        self._dict[key] = value

    def __delitem__(self, key: str) -> None:
        key = key.lower()
        del self._dict[key]
        found_indexes = [
            idx for idx, (item_key, _) in enumerate(self._list) if item_key == key
        ]
        for idx in reversed(found_indexes):
            del self._list[idx]

    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, self.__class__) and sorted(self._list) == sorted(
            other._list
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._list!r})"
