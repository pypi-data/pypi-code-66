import inspect
import re
import uuid
import typing
import werkzeug
import types
from werkzeug.routing import Map, Rule
from urllib.parse import urlparse
from .utils import import_string
from . import exceptions


Handler = typing.Union[str, typing.Callable[..., typing.Any]]


class Route:
    name: str

    def __init__(
        self,
        url: str,
        method: str,
        handler: typing.Union[Handler, typing.List[Handler]],
        name: typing.Optional[str] = None,
        standalone: bool = False,
    ):
        if isinstance(handler, list):
            handlers = []
            for item in handler:
                obj = import_string(item) if isinstance(item, str) else item
                assert isinstance(obj, types.FunctionType)
                handlers.append(obj)
        else:
            obj = import_string(handler) if isinstance(handler, str) else handler
            assert isinstance(obj, types.FunctionType)
            handlers = [obj]
        if len(handlers) > 1:
            assert name is not None
            self.name = name
        else:
            self.name = name or handlers[0].__name__
        self.handlers = tuple(handlers)
        self.url = url
        self.method = method
        self.standalone = standalone
        self.support_request_data = method in ("POST", "PUT", "PATCH", "DELETE")


class BaseRouter:
    def lookup(
        self, path: str, method: str
    ) -> typing.Tuple[Route, typing.Dict[str, object]]:
        raise NotImplementedError()

    def reverse_url(self, name: str, **params: object) -> typing.Optional[str]:
        raise NotImplementedError()


class Include:
    def __init__(
        self,
        url: str,
        name: str,
        routes: typing.Union[str, typing.List[typing.Union[Route, "Include"]]],
    ):
        self.url = url
        self.name = name
        if isinstance(routes, str):
            obj = import_string(routes, list)
        else:
            obj = routes
        self.routes = []
        for item in obj:
            if not isinstance(item, (Route, Include)):  # pragma: nocover
                raise exceptions.ConfigurationError(
                    "Route or Include expected, got %r" % item
                )
            self.routes.append(item)


class Router(BaseRouter):
    def __init__(self, routes: typing.List[typing.Union[Route, Include]]):
        rules = []
        name_lookups = {}

        for path, name, route in self.walk_routes(routes):
            path_params = [item.strip("{}") for item in re.findall("{[^}]*}", path)]
            args: typing.Dict[str, typing.Type[object]] = {}
            for handler in route.handlers:
                for param_name, param in inspect.signature(handler).parameters.items():
                    if param_name in args:  # pragma: nocover
                        if args[param_name] != param.annotation:
                            msg = (
                                f"Parameter {param_name} has different signatures: "
                                f"{args[param_name]} and {param.annotation}"
                            )
                            raise exceptions.ConfigurationError(msg)
                    else:
                        args[param_name] = param.annotation

            for path_param in path_params:
                if path_param.startswith("+"):
                    path = path.replace(
                        "{%s}" % path_param, "<path:%s>" % path_param.lstrip("+")
                    )
                else:
                    path = path.replace("{%s}" % path_param, "<string:%s>" % path_param)

            rule = Rule(path, methods=[route.method], endpoint=name)
            rules.append(rule)
            name_lookups[name] = route

        self.adapter = Map(rules).bind("")
        self.name_lookups = name_lookups

        # Use an MRU cache for router lookups.
        self._lookup_cache: typing.Dict[
            str, typing.Tuple[Route, typing.Dict[str, object]]
        ] = {}
        self._lookup_cache_size = 10000

    def walk_routes(
        self,
        routes: typing.List[typing.Union[Route, Include]],
        url_prefix: str = "",
        name_prefix: str = "",
    ) -> typing.List[typing.Tuple[str, str, Route]]:
        walked = []
        for item in routes:
            if isinstance(item, Route):
                walked.append((url_prefix + item.url, name_prefix + item.name, item))
            elif isinstance(item, Include):
                walked.extend(
                    self.walk_routes(
                        item.routes,
                        url_prefix + item.url,
                        name_prefix + item.name + ":",
                    )
                )
        return walked

    def lookup(
        self, path: str, method: str
    ) -> typing.Tuple[Route, typing.Dict[str, object]]:
        lookup_key = method + " " + path
        try:
            return self._lookup_cache[lookup_key]
        except KeyError:
            pass

        try:
            name, path_params = self.adapter.match(path, method)
        except werkzeug.exceptions.NotFound:
            raise exceptions.NotFound() from None
        except werkzeug.exceptions.MethodNotAllowed:
            raise exceptions.MethodNotAllowed() from None
        except werkzeug.routing.RequestRedirect as exc:
            path = urlparse(exc.new_url).path
            raise exceptions.Found(path) from None

        route = self.name_lookups[name]

        self._lookup_cache[lookup_key] = (route, path_params)
        if len(self._lookup_cache) > self._lookup_cache_size:  # pragma: nocover
            self._lookup_cache.pop(next(iter(self._lookup_cache)))

        return route, path_params

    def reverse_url(self, name: str, **params: object) -> typing.Optional[str]:
        try:
            return self.adapter.build(name, params)  # type: ignore
        except werkzeug.routing.BuildError as exc:
            raise exceptions.NoReverseMatch(str(exc)) from None
