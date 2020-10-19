import types
import typing
import inspect
from urllib.parse import quote
from http import HTTPStatus
from inspect import Parameter
from werkzeug.wsgi import get_input_stream
from .datastructures import ImmutableHeaders
from . import Component, http


WSGIEnviron = typing.Dict[str, str]
ExcInfo = typing.Tuple[typing.Type[BaseException], BaseException, types.TracebackType]


WSGIStartResponse = typing.Callable[
    [str, typing.List[typing.Tuple[str, str]], typing.Optional[ExcInfo]], None
]
# class WSGIStartResponse(typing.Protocol):
#     def __call__(
#         self,
#         status: str,
#         headers: typing.Iterable[typing.Tuple[str, str]],
#         exc_info: typing.Optional[ExcInfo] = None,
#     ) -> None:
#         ...  # pragma: nocover


RESPONSE_STATUS_TEXT = {
    status.value: "%d %s" % (status.value, status.phrase) for status in HTTPStatus
}


class MethodComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Method

    def resolve(self, environ: WSGIEnviron) -> str:
        return environ["REQUEST_METHOD"].upper()


class URLComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.URL

    def resolve(self, environ: WSGIEnviron) -> http.URL:
        scheme = environ["wsgi.url_scheme"]
        url = scheme + "://"
        if environ.get("HTTP_HOST"):
            url += environ["HTTP_HOST"]
        else:
            url += environ["SERVER_NAME"]
            if scheme == "https":
                if environ["SERVER_PORT"] != "443":
                    url += ":" + environ["SERVER_PORT"]
            elif environ["SERVER_PORT"] != "80":
                url += ":" + environ["SERVER_PORT"]

        url += quote(environ["SCRIPT_NAME"], encoding="latin1")
        url += quote(environ["PATH_INFO"], safe="/;=,", encoding="latin1")
        if environ.get("QUERY_STRING"):
            url += "?" + environ["QUERY_STRING"]
        return http.URL(url)


class SchemeComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Scheme

    def resolve(self, environ: WSGIEnviron) -> str:
        return environ["wsgi.url_scheme"]


class HostComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Host

    def resolve(self, environ: WSGIEnviron) -> str:
        return environ.get("HTTP_HOST") or environ["SERVER_NAME"]


class PortComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Port

    def resolve(self, environ: WSGIEnviron) -> int:
        if environ["wsgi.url_scheme"] == "https":
            return int(environ.get("SERVER_PORT", 443))
        return int(environ.get("SERVER_PORT", 80))


class PathComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Path

    def resolve(self, environ: WSGIEnviron) -> str:
        return environ["SCRIPT_NAME"] + environ["PATH_INFO"]


class QueryStringComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.QueryString

    def resolve(self, environ: WSGIEnviron) -> str:
        return environ.get("QUERY_STRING", "")


class QueryParamsComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.QueryParams

    def resolve(self, environ: WSGIEnviron) -> http.QueryParams:
        return http.QueryParams(environ.get("QUERY_STRING", ""))


class QueryParamComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.QueryParam

    def resolve(
        self, parameter: Parameter, query_params: http.QueryParams
    ) -> typing.Optional[str]:
        return query_params.get(parameter.name)


class HeadersComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Headers

    def resolve(self, environ: WSGIEnviron) -> ImmutableHeaders:
        header_items = {
            key[5:].replace("_", "-").lower(): value
            for key, value in environ.items()
            if key.startswith("HTTP_")
        }
        if value := environ.get("CONTENT_TYPE"):
            header_items["content-type"] = value
        if value := environ.get("CONTENT_LENGTH"):
            header_items["content-length"] = value
        return ImmutableHeaders(header_items)


class HeaderComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Header

    def resolve(
        self, parameter: Parameter, headers: http.Headers
    ) -> typing.Optional[str]:
        name = parameter.name.replace("_", "-")
        return headers.get(name)


class BodyComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.Body

    def resolve(self, environ: WSGIEnviron) -> bytes:
        return get_input_stream(environ).read()


class RequestComponent(Component):
    def resolve(
        self, method: http.Method, url: http.URL, headers: http.Headers, body: http.Body
    ) -> http.Request:
        return http.Request(method, url, headers, body)


WSGI_COMPONENTS = [
    MethodComponent(),
    URLComponent(),
    SchemeComponent(),
    HostComponent(),
    PortComponent(),
    PathComponent(),
    QueryStringComponent(),
    QueryParamsComponent(),
    QueryParamComponent(),
    HeadersComponent(),
    HeaderComponent(),
    BodyComponent(),
    RequestComponent(),
]
