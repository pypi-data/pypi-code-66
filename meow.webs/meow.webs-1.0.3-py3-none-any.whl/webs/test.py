import io
import typing
import requests
from urllib.parse import unquote, urlparse
from meow.webs import App, wsgi


class _MockOriginalResponse:
    def __init__(self, headers: typing.Iterable[typing.Tuple[str, str]]):
        self.msg = requests.packages.urllib3.response.HTTPHeaderDict(headers)
        self.closed = False

    def isclosed(self) -> bool:
        return self.closed

    def close(self) -> None:
        self.closed = True  # pragma: nocover


class _WSGIAdapter(requests.adapters.HTTPAdapter):
    """
    A transport adapter for `requests` that makes requests directly to a
    WSGI app, rather than making actual HTTP requests over the network.
    """

    def __init__(self, app: App) -> None:
        self.app = app

    @staticmethod
    def get_environ(request: requests.PreparedRequest) -> typing.Dict[str, typing.Any]:
        body = request.body
        if isinstance(body, str):
            body_bytes = body.encode("utf-8")
        else:
            body_bytes = body or b""

        assert request.url is not None

        url_components = urlparse(request.url)
        environ: typing.Dict[str, typing.Any] = {
            "REQUEST_METHOD": request.method,
            "wsgi.url_scheme": url_components.scheme,
            "SCRIPT_NAME": "",
            "PATH_INFO": unquote(url_components.path),
            "wsgi.input": io.BytesIO(body_bytes),
        }

        if url_components.query:
            environ["QUERY_STRING"] = url_components.query

        if url_components.port:
            environ["SERVER_NAME"] = url_components.hostname
            environ["SERVER_PORT"] = str(url_components.port)
        else:
            environ["HTTP_HOST"] = url_components.hostname

        for key, value in request.headers.items():
            key = key.upper().replace("-", "_")
            if key not in ("CONTENT_LENGTH", "CONTENT_TYPE"):
                key = "HTTP_" + key
            environ[key] = value

        return environ

    def send(
        self, request: requests.PreparedRequest, *args: object, **kwargs: object
    ) -> requests.Response:
        raw_kwargs: typing.Dict[str, typing.Any] = {}

        def start_response(
            status: str,
            headers: typing.Iterable[typing.Tuple[str, str]],
            exc_info: typing.Optional[wsgi.ExcInfo] = None,
        ) -> None:
            if exc_info is not None:
                raise exc_info[0].with_traceback(exc_info[1], exc_info[2])
            status, _, reason = status.partition(" ")
            raw_kwargs["status"] = int(status)
            raw_kwargs["reason"] = reason
            raw_kwargs["headers"] = headers
            raw_kwargs["version"] = 11
            raw_kwargs["preload_content"] = False
            raw_kwargs["original_response"] = _MockOriginalResponse(headers)

        # Make the outgoing request via WSGI.
        environ = self.get_environ(request)
        wsgi_response = self.app(environ, start_response)

        # Build the underlying urllib3.HTTPResponse
        raw_kwargs["body"] = io.BytesIO(b"".join(wsgi_response))
        raw = requests.packages.urllib3.HTTPResponse(**raw_kwargs)

        return self.build_response(request, raw)  # type: ignore


class Client(requests.Session):
    def __init__(
        self, app: App, scheme: str = "http", hostname: str = "testserver"
    ) -> None:
        super().__init__()
        interface = getattr(app, "interface", None)
        # if interface == "asgi":
        adapter = _WSGIAdapter(app)
        self.mount("http://", adapter)
        self.mount("https://", adapter)
        self.headers.update({"User-Agent": "testclient"})
        self.scheme = scheme
        self.hostname = hostname

    def request(  # type: ignore
        self, method: str, url: str, *args: typing.Any, **kwargs: typing.Any
    ) -> requests.Response:
        if not (url.startswith("http:") or url.startswith("https:")):
            assert url.startswith("/"), (
                "TestClient expected either "
                "an absolute URL starting 'http:' / 'https:', "
                "or a relative URL starting with '/'. URL was '%s'." % url
            )
            url = "%s://%s%s" % (self.scheme, self.hostname, url)
        return super().request(method, url, *args, **kwargs)
