import sys
from meow.di import Component
from .app import App
from .settings import Settings
from .router import Route, Include
from .templates import Templates
from . import http


if sys.version_info < (3, 8):
    raise Exception("Python < 3.8 is not supported")  # pragma: nocover


__version__ = "1.0.3"
__all__ = ["App", "Settings", "Route", "Include", "Component", "Templates", "http"]
