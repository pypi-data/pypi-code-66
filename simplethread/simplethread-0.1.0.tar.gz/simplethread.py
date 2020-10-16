# -*- coding: utf-8 -*-

"""
Some useful utilities for Python's threading module.
"""

from functools import update_wrapper
from types import MethodType
from typing import Any, Callable, Optional

__all__ = ["threaded"]


class threaded(object):
    def __init__(self, user_function: Callable[..., Any]) -> None:
        if not callable(user_function) and not hasattr(user_function, "__get__"):
            raise TypeError(f"{user_function!r} is not callable or a descriptor")

        self.user_function = user_function
        update_wrapper(self, user_function)

    def __call__(self, *args: Any, **kwargs: Any) -> int:
        from _thread import start_new_thread as _
        return _(self.user_function, args, kwargs)

    def __get__(self, instance: Any, owner: Optional[type] = None) -> Any:
        return self if instance is None else MethodType(self, instance)
