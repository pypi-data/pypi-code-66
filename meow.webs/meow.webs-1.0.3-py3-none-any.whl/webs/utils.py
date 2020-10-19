import os
import typing
import importlib
from importlib.util import find_spec


def get_package_path(package_path: str) -> str:
    if ":" in package_path:
        package, path = package_path.split(":", 1)
        spec = find_spec(package)
        if spec and spec.origin:
            package_dir = os.path.dirname(spec.origin)
            return os.path.join(package_dir, path)
        raise ValueError(f"Package {package} not found")  # pragma: nocover
    else:
        return package_path


T = typing.TypeVar("T")


@typing.overload
def import_string(dot_path: str) -> object:
    ...  # pragma: nocover


@typing.overload
def import_string(dot_path: str, tp: typing.Type[T]) -> T:
    ...  # pragma: nocover


def import_string(dot_path, tp=None):  # type: ignore
    path, attr = dot_path.rsplit(".", 1)
    module = importlib.import_module(path)

    try:
        ret = getattr(module, attr)
    except AttributeError:
        raise ImportError(f"Could not load name {dot_path}") from None

    if tp is None or isinstance(ret, tp):
        return ret

    raise TypeError(
        f"{dot_path} must be an instance of {tp}, got {ret!r}"
    )  # pragma: nocover
