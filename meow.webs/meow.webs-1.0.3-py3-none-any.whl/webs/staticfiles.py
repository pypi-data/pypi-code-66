import typing
from .utils import get_package_path
from .wsgi import WSGIEnviron, WSGIStartResponse
from . import exceptions

try:
    import whitenoise
except ImportError:  # pragma: nocover
    whitenoise = None


class BaseStaticFiles:
    def __call__(
        self, environ: WSGIEnviron, start_response: WSGIStartResponse
    ) -> typing.Sequence[bytes]:
        raise NotImplementedError()


class StaticFiles(BaseStaticFiles):
    """
    Static file handling for WSGI applications, using `whitenoise`.
    """

    def __init__(
        self,
        prefix: str,
        static_dirs: typing.Tuple[typing.Union[str, typing.Dict[str, str]], ...],
    ):
        if whitenoise is None:
            raise RuntimeError(
                "`whitenoise` must be installed to use `StaticFiles`."
            )  # pragma: nocover

        self.whitenoise = whitenoise.WhiteNoise(application=self.not_found)

        prefix = prefix.rstrip("/")
        for static_dir in static_dirs:
            if isinstance(static_dir, dict):
                for files_prefix, path in static_dir.items():
                    self.whitenoise.add_files(
                        get_package_path(path),
                        prefix=(prefix + "/" + files_prefix).rstrip("/"),
                    )
            else:
                self.whitenoise.add_files(get_package_path(static_dir), prefix=prefix)

    def __call__(
        self, environ: WSGIEnviron, start_response: WSGIStartResponse
    ) -> typing.Sequence[bytes]:
        return self.whitenoise(environ, start_response)  # type: ignore

    def not_found(
        self, environ: WSGIEnviron, start_response: WSGIStartResponse
    ) -> typing.NoReturn:
        raise exceptions.NotFound()
