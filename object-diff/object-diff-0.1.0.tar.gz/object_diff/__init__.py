# Copyright (C) 2020  Rolandas Valteris <rolandas.valteris@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from enum import Enum
from typing import Dict, Iterator, Iterable, Any, Optional, List

import poetry_version
import logging

__version__ = poetry_version.extract(__file__)

logger = logging.getLogger(__name__)

ABSENT_VALUE = NotImplemented


class ChangeType(Enum):
    INSERT = 1
    MODIFY = 2
    REMOVE = 3


class Diff:
    """
    Encapsulates a single difference in a hierarchical data structure, e.g. nested ``dict`` s
    """

    def __init__(self, path: Iterable, change_type: ChangeType, old_value: Any, new_value: Any):
        self.path = path
        self.change_type = change_type
        if change_type in [ChangeType.REMOVE, ChangeType.MODIFY]:
            self.old_value = old_value
        else:
            self.old_value = ABSENT_VALUE
        if change_type in [ChangeType.INSERT, ChangeType.MODIFY]:
            self.new_value = new_value
        else:
            self.new_value = ABSENT_VALUE

    def __eq__(self, other):
        if not isinstance(other, Diff):
            return False
        if self is other:
            return True
        return (self.path, self.change_type, self.old_value, self.new_value) == (
            other.path,
            other.change_type,
            other.old_value,
            other.new_value,
        )

    def __hash__(self):
        return hash((*self.path, self.change_type, self.old_value, self.new_value))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.path}, {self.change_type}, {self.old_value}, {self.new_value})"


def dict_diff_iter(old_dict: Dict, new_dict: Dict) -> Iterator[Diff]:
    if not isinstance(old_dict, dict) or not isinstance(new_dict, dict):
        return value_diff(old_dict, new_dict)

    old_keys = set(old_dict.keys())
    new_keys = set(new_dict.keys())

    common_keys = old_keys.intersection(new_keys)
    for k in common_keys:
        d = value_diff(old_dict[k], new_dict[k], [k])
        if d is not None:
            yield d

    inserted_keys = new_keys.difference(old_keys)
    for k in inserted_keys:
        d = value_diff(ABSENT_VALUE, new_dict[k], [k])
        if d is not None:
            yield d

    removed_keys = old_keys.difference(new_keys)
    for k in removed_keys:
        d = value_diff(old_dict[k], ABSENT_VALUE, [k])
        if d is not None:
            yield d


def value_diff(old_value: Any, new_value: Any, path: List[Any] = []) -> Optional[Diff]:
    """
    Creates diff between ``old_value`` and ``new_value`` treating them as scalar values

    :param old_value:
    :param new_value:
    :param path: path of the values in a hierarchical data structure
    :return: diff between old_value and new_value. None, if values a equal.
    """
    if old_value is ABSENT_VALUE:
        if new_value is ABSENT_VALUE:
            return None
        else:
            return Diff(path, ChangeType.INSERT, ABSENT_VALUE, new_value)

    if new_value is ABSENT_VALUE:
        return Diff(path, ChangeType.REMOVE, old_value, ABSENT_VALUE)

    if old_value is new_value or old_value == new_value:
        return None

    return Diff(path, ChangeType.MODIFY, old_value, new_value)
