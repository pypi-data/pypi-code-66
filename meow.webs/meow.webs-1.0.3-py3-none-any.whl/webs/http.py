import json
import types
import typing
import datetime
import uuid
import dataclasses
from enum import Enum
from functools import cached_property
from urllib.parse import ParseResult, urlparse, parse_qsl
from .datastructures import MultiMapping, ImmutableHeaders, MutableHeaders


Method = typing.NewType("Method", str)
Scheme = typing.NewType("Scheme", str)
Host = typing.NewType("Host", str)
Port = typing.NewType("Port", int)
Path = typing.NewType("Path", str)
QueryString = typing.NewType("QueryString", str)
QueryParam = typing.NewType("QueryParam", str)
Header = typing.NewType("Header", str)
Body = typing.NewType("Body", bytes)
PathParams = typing.NewType("PathParams", typing.Dict[str, str])
PathParam = typing.NewType("PathParam", str)
RequestData = typing.NewType("RequestData", object)
Headers = typing.NewType("Headers", ImmutableHeaders)
ExcInfo = typing.Tuple[typing.Type[BaseException], BaseException, types.TracebackType]


class FormData(MultiMapping[str, typing.Union[str, typing.IO[bytes]]]):
    ...


class URL(str):
    """
    A string that also supports accessing the parsed URL components.
    eg. `url.components.query`
    """

    @cached_property
    def components(self) -> ParseResult:
        return urlparse(self)


class QueryParams(MultiMapping[str, str]):
    def __init__(
        self,
        value: typing.Optional[
            typing.Union[
                str,
                bytes,
                typing.Mapping[str, str],
                typing.List[typing.Tuple[str, str]],
            ]
        ] = None,
    ):
        if isinstance(value, str):
            super().__init__(parse_qsl(value, keep_blank_values=True))
        elif isinstance(value, bytes):
            super().__init__(
                parse_qsl(value.decode("latin-1"), keep_blank_values=True)
            )  # pragma: nocover
        else:
            super().__init__(value)


class Request:
    def __init__(self, method: Method, url: URL, headers: Headers, body: Body) -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body


class Response:
    media_type: typing.Optional[str] = None
    charset: str = "utf-8"

    def __init__(
        self,
        content: object,
        status_code: int = 200,
        headers: typing.Optional[
            typing.Union[
                typing.Mapping[str, str], typing.Iterable[typing.Tuple[str, str]]
            ]
        ] = None,
        exc_info: typing.Optional[ExcInfo] = None,
    ) -> None:
        self.content = self.render(content)
        self.headers = MutableHeaders(headers)
        self.status_code = status_code
        self.set_default_headers()
        self.exc_info = exc_info

    def render(self, content: object) -> bytes:
        if isinstance(content, bytes):
            return content

        elif isinstance(content, str) and self.charset is not None:
            return content.encode(self.charset)

        valid_types = "bytes" if self.charset is None else "string or bytes"
        raise RuntimeError(
            "%s content must be %s. Got %s."
            % (self.__class__.__name__, valid_types, type(content).__name__)
        )

    def set_default_headers(self) -> None:
        if "content-length" not in self.headers:
            self.headers["content-length"] = str(len(self.content))

        if "content-type" not in self.headers and self.media_type is not None:
            content_type = self.media_type
            if self.charset is not None:
                content_type += "; charset=%s" % self.charset
            self.headers["content-type"] = content_type


class HTMLResponse(Response):
    media_type = "text/html"


def encode_datetime(obj: datetime.datetime) -> str:
    value = obj.isoformat()
    if value.endswith("+00:00"):
        value = value[:-6] + "Z"
    return value


_JSON_ENCODERS = {
    datetime.datetime: encode_datetime,
    datetime.date: encode_datetime,
    datetime.time: encode_datetime,
    uuid.UUID: str,
}


class JSONResponse(Response):
    media_type = "application/json"

    def render(self, content: object) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
            default=self.default,
        ).encode("utf-8")

    # noinspection PyDefaultArgument
    @staticmethod
    def default(obj: object, _encoders=_JSON_ENCODERS) -> object:  # type: ignore
        # noinspection PyTypeChecker
        if encode := _encoders.get(type(obj)):
            return encode(obj)
        elif isinstance(obj, Enum):
            # noinspection PyUnresolvedReferences
            return obj.name
        elif dataclasses.is_dataclass(obj):
            # noinspection PyDataclass
            return dataclasses.asdict(obj)
        raise TypeError(
            "Object of type '%s' is not JSON serializable." % type(obj).__name__
        )
