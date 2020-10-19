import sys
import werkzeug
import typing
from meow.di import Component, ReturnValue, Injector
from . import exceptions
from .http import HTMLResponse, JSONResponse, PathParams, Response
from .router import Router, Route, Include
from .staticfiles import StaticFiles
from .wsgi import RESPONSE_STATUS_TEXT, WSGIEnviron, WSGIStartResponse
from .settings import Settings, load_settings
from .utils import import_string


class App:
    interface = "wsgi"

    def __init__(self, settings_module: str = "settings"):
        self.settings = load_settings(settings_module)
        self.debug = self.settings.DEBUG
        self.propagate_exceptions = self.settings.PROPAGATE_EXCEPTIONS
        if self.propagate_exceptions is None:
            self.propagate_exceptions = self.debug

        routes = import_string(self.settings.ROUTES, list)
        assert all(isinstance(item, (Route, Include)) for item in routes)

        if self.settings.STATIC_DIRS:
            self.statics = StaticFiles(
                self.settings.STATIC_URL, self.settings.STATIC_DIRS
            )
            routes += self.include_static_url(self.settings.STATIC_URL)

        self.init_injector(self.settings.COMPONENTS)
        self.router = Router(routes)

        application_event_hooks = self.settings.EVENT_HOOKS
        self.on_request = tuple(
            hook.on_request
            for hook in application_event_hooks
            if hasattr(hook, "on_request")
        )
        self.on_response = tuple(
            hook.on_response
            for hook in reversed(application_event_hooks)
            if hasattr(hook, "on_response")
        )
        self.on_error = tuple(
            hook.on_error
            for hook in reversed(application_event_hooks)
            if hasattr(hook, "on_error")
        )

    @staticmethod
    def include_static_url(static_url: str) -> typing.List[Route]:
        from .handlers import serve_static_wsgi

        static_url = static_url.rstrip("/") + "/{+filename}"
        return [
            Route(
                static_url,
                method="GET",
                handler=serve_static_wsgi,
                name="static",
                standalone=True,
            )
        ]

    def init_injector(self, components: typing.Tuple[Component, ...]) -> None:
        from .templates import TEMPLATES_COMPONENTS
        from .validation import VALIDATION_COMPONENTS
        from .wsgi import WSGI_COMPONENTS

        found_components = list(components)
        found_components += WSGI_COMPONENTS
        found_components += VALIDATION_COMPONENTS
        found_components += TEMPLATES_COMPONENTS

        initials = {
            "environ": WSGIEnviron,
            "start_response": WSGIStartResponse,
            "exc": Exception,
            "route": Route,
            "response": Response,
            "path_params": PathParams,
        }

        resolved: typing.Mapping[object, object] = {Settings: self.settings, App: self}

        self.injector = Injector(found_components, initials, resolved)

    def static_url(self, filename: str) -> typing.Optional[str]:
        assert self.router is not None, "Router is not initialized"
        return self.router.reverse_url("static", filename=filename)

    def reverse_url(self, name: str, **params: object) -> typing.Optional[str]:
        assert self.router is not None, "Router is not initialized"
        return self.router.reverse_url(name, **params)

    def serve(
        self, host: str, port: int, debug: bool = False
    ) -> None:  # pragma: nocover
        self.debug = debug
        werkzeug.run_simple(host, port, self, use_debugger=debug, use_reloader=debug)

    @staticmethod
    def render_response(return_value: ReturnValue) -> Response:
        if return_value is None:
            return Response("No Content", 204)
        if isinstance(return_value, Response):
            return return_value
        elif isinstance(return_value, (str, bytes)):
            return HTMLResponse(return_value)
        return JSONResponse(return_value)

    @staticmethod
    def exception_handler(exc: Exception) -> Response:
        if isinstance(exc, exceptions.HTTPException):
            return JSONResponse(exc.detail, exc.status_code, exc.get_headers())
        raise exc

    @staticmethod
    def error_handler() -> Response:
        return JSONResponse("Server error", 500, exc_info=sys.exc_info())  # type: ignore

    def finalize_wsgi(
        self, response: Response, start_response: WSGIStartResponse
    ) -> typing.Sequence[bytes]:
        if self.propagate_exceptions and response.exc_info is not None:
            exc_info = response.exc_info
            raise exc_info[0].with_traceback(exc_info[1], exc_info[2])

        status = RESPONSE_STATUS_TEXT.get(response.status_code)
        if status is None:
            status = str(response.status_code)

        headers = response.headers.multi_items()
        start_response(status, headers, response.exc_info)
        return [response.content]

    def __call__(
        self, environ: WSGIEnviron, start_response: WSGIStartResponse
    ) -> typing.Sequence[bytes]:
        state = {
            "environ": environ,
            "start_response": start_response,
            "exc": None,
            "path_params": None,
            "route": None,
            "response": None,
        }
        method = str(environ["REQUEST_METHOD"]).upper()
        path = environ["PATH_INFO"]

        try:
            route, path_params = self.router.lookup(path, method)
            state["route"] = route
            state["path_params"] = path_params
            if route.standalone:
                funcs = route.handlers
            elif self.on_request or self.on_response:
                # noinspection PyTypeChecker
                funcs = (
                    self.on_request
                    + route.handlers
                    + (self.render_response,)
                    + self.on_response
                    + (self.finalize_wsgi,)
                )
            else:
                funcs = route.handlers + (self.render_response, self.finalize_wsgi)
            return self.injector.run(funcs, state)  # type: ignore
        except Exception as exc:
            try:
                state["exc"] = exc
                if self.on_response:
                    # noinspection PyTypeChecker
                    funcs = (
                        (self.exception_handler,)
                        + self.on_response
                        + (self.finalize_wsgi,)
                    )
                else:
                    funcs = (self.exception_handler, self.finalize_wsgi)  # type: ignore
                return self.injector.run(funcs, state)  # type: ignore
            except Exception as inner_exc:
                try:
                    state["exc"] = inner_exc
                    if self.on_error:
                        self.injector.run(self.on_error, state)
                finally:
                    funcs = (self.error_handler, self.finalize_wsgi)  # type: ignore
                    return self.injector.run(funcs, state)  # type: ignore
