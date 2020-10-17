# -*- coding: utf-8 -*-

from functools import update_wrapper
from types import MethodType
from typing import Any, Callable, Optional, Union

from simplethread.thread import start_new

__all__ = ("threaded",)


class threaded(object):
    """
    A decorator to run a ``user_function`` in a separate thread.
    """
    def __init__(self, user_function: Callable[..., Any]) -> None:
        if not callable(user_function) and not hasattr(user_function, "__get__"):
            raise TypeError(f"{user_function!r} is not callable or a descriptor")

        self.user_function = user_function
        update_wrapper(self, user_function)

    def __call__(self, *args: Any, **kwargs: Any) -> int:
        return start_new(self.user_function, args, kwargs)

    def __get__(self, instance: Any, owner: Optional[type] = None) -> Union["threaded", MethodType]:
        return self if instance is None else MethodType(self, instance)
