"""Scripts for implementing logic"""
from .if_valid import if_valid  # noqa
import pkgutil
import inspect

__all__ = []

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    for name, value in inspect.getmembers(module):
        if name.startswith("__"):
            continue

        globals()[name] = value
        __all__.append(name)
