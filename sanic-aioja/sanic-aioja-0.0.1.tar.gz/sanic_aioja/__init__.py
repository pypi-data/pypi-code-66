import asyncio
import os
from enum import Enum
from functools import wraps
from itertools import chain
from typing import Any, Callable, Dict, Iterable, Union

from aioja import (
    ChoiceLoader,
    DictLoader,
    Environment,
    FileSystemLoader,
    FunctionLoader,
    ModuleLoader,
    PackageLoader,
    PrefixLoader,
)
from aioja.loaders import AsyncLoaderMixin
from jinja2.environment import load_extensions
from jinja2.utils import import_string
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, html
from sanic.views import HTTPMethodView

from .defaultglobals import static_url, url_for
from .undefined import ChainableUndefined, DebugUndefined

DEFAULT_GLOBALS = {
    'url': url_for,
    'static': static_url,
}
DEFAULT_FILTERS = {}
DEFAULT_TESTS = {}
DEFAULT_EXTENSIONS = {}

__all__ = [
    'Jinja2', 'ChoiceLoader', 'DictLoader', 'FileSystemLoader', 'FunctionLoader',
    'ModuleLoader', 'PackageLoader', 'PrefixLoader'
]
__version__ = '0.0.1'


class Scope(Enum):
    GLOBALS = 'globals'
    FILTERS = 'filters'
    TESTS = 'tests'
    POLICIES = 'policies'


class Jinja2:
    def __init__(
        self,
        app: Sanic = None,
        debug: bool = False,
        loader: AsyncLoaderMixin = None,
        precompile: bool = None,
        precompile_path: Union[str, os.PathLike] = None,
        precompile_extensions: Iterable[str] = None,

        # jinja options
        **options
    ):
        self.app = app

        self.precompile = precompile if precompile is not None else not debug
        self.precompile_path = precompile_path
        self.precompile_extensions = precompile_extensions or ['html', 'txt', 'jinja2']

        self.env = self.create_env(
            debug=debug,
            loader=loader,
            **options
        )

        # default render strategy
        self.render = AsyncRender()

        if app:
            self.init_app(app)

    @classmethod
    def create_env(cls, debug=False, loader=None, **options) -> Environment:
        # bytecode cache
        bytecode_cache = options.pop('bytecode_cache', {})
        bytecode_cache.setdefault('name', 'default')
        bytecode_cache.setdefault('enabled', False)
        bytecode_cache.setdefault('backend', 'aioja.bccache.aiocache.AioRedisBytecodeCache')
        if bytecode_cache['enabled']:
            bytecode_cls = import_string(bytecode_cache['backend'])
            bytecode_options = bytecode_cache.get('options') or {}
            options['bytecode_cache'] = bytecode_cls(**bytecode_options)

        # undefined
        undefined = options.pop('undefined', None)
        if undefined is not None:
            if isinstance(undefined, str):
                options['undefined'] = import_string(undefined)
            else:
                options['undefined'] = undefined

        if debug:
            options.setdefault('undefined', DebugUndefined)
        else:
            options.setdefault('undefined', ChainableUndefined)

        options.setdefault('auto_reload', debug)
        options.setdefault('autoescape', True)

        # environment
        if isinstance(options.get('environment'), str):
            environment_cls = import_string(options.pop('environment'))
        else:
            environment_cls = Environment

        env = environment_cls(loader=loader, **options)

        env.globals.update(DEFAULT_GLOBALS)
        env.filters.update(DEFAULT_FILTERS)
        env.tests.update(DEFAULT_TESTS)
        env.extensions.update(load_extensions(env, DEFAULT_EXTENSIONS))
        return env

    def init_app(self, app: Sanic):
        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['jinja2'] = self
        app.jinja_env = self.env

        if self.precompile_path:
            self.add_module_loader(self.precompile_path)

        app.register_listener(self.on_server_start, 'before_server_start')

    async def on_server_start(self, app, loop):
        if self.precompile:
            if not self.precompile_path:
                raise ValueError('precompile_path required')

            await self.env.compile_templates(
                self.precompile_path,
                extensions=self.precompile_extensions
            )

        # Strategy pattern
        if 'babel' in app.extensions:
            self.render = BabelAsyncRender()
        else:
            self.render = AsyncRender()

    def add_module_loader(self, precompile_path: str):
        module_loader = ModuleLoader(precompile_path)

        if isinstance(self.env.loader, ChoiceLoader):
            self.env.loader.loaders.insert(0, module_loader)
        else:
            self.env.loader = ChoiceLoader([
                module_loader,
                self.env.loader
            ])

    def extend(self, *args, scope_: Scope = Scope.GLOBALS, **kwargs):
        """
        Add extra filters, tests, globals or policies.
        This method accepts the same arguments as the `dict` constructor:
        A dict, a dict subclass or some keyword arguments.
        """
        extensions = dict(*args, **kwargs)

        target = getattr(self.env, scope_.value)
        for name, ext in extensions.items():
            if isinstance(ext, str):
                ext = import_string(ext)
            target[name] = ext

    # Shortcuts

    def globals(self, *args, **kwargs):
        self.extend(*args, scope_=Scope.GLOBALS, **kwargs)
        return self

    def filters(self, *args, **kwargs):
        self.extend(*args, scope_=Scope.FILTERS, **kwargs)
        return self

    def tests(self, *args, **kwargs):
        self.extend(*args, scope_=Scope.TESTS, **kwargs)
        return self

    def policies(self, *args, **kwargs):
        self.extend(*args, scope_=Scope.POLICIES, **kwargs)
        return self

    def extensions(self, *args):
        extensions = chain.from_iterable(_extensions_iterator(arg) for arg in args)
        self.env.extensions.update(load_extensions(self.env, extensions))
        return self

    # Rendering

    async def render_to_string(
        self,
        request: Request,
        template_name: Union[str, Iterable[str]],
        context: Dict[str, Any] = None,
    ):
        """
        Load a template and render it with a context. Return a string.
        template_name may be a string or a list of strings.
        """
        if isinstance(template_name, (list, tuple)):
            template = await self.env.select_template(template_name)
        else:
            template = await self.env.get_template(template_name)

        context['app'] = request.app
        context['request'] = request
        return await self.render(request, template, context)

    def template(
        self,
        template_name: Union[str, Iterable[str]],
        headers: Dict = None,
        status: int = 200,
        response: Callable = html
    ):
        """
        Decorator for Sanic request handler, that turns it
        into function returning generated jinja template,
        as sanic response.

        Example:
             @app.route('/')
             @jinja2.template('pages/index.html')
             async def handle_index(request):
                return {
                    'page': 'index',
                }
        """

        def decorator(handler):
            @wraps(handler)
            async def wrapper(*args, **kwargs):
                context = await handler(*args, **kwargs)

                # wrapped function return HTTPResponse
                # instead of dict-like object
                if isinstance(context, HTTPResponse):
                    return context

                # wrapped function is class method
                # and got `self` as first argument
                if isinstance(args[0], HTTPMethodView):
                    request = args[1]
                else:
                    request = args[0]

                if context is None:
                    context = {}

                content = await self.render_to_string(request, template_name, context)
                return response(content, headers=headers, status=status)

            return wrapper

        return decorator


class BabelAsyncRender:
    def __init__(self):
        self._lock = asyncio.Lock()

    async def __call__(self, request, template, context):
        babel = request.app.babel_instance
        async with self._lock:
            translations = babel._get_translations(request)
            template.environment.install_gettext_translations(translations)
            return await template.render_async(context)


class AsyncRender:
    async def __call__(self, request, template, context):
        return await template.render_async(context)


def _extensions_iterator(value):
    if isinstance(value, str):
        return [value]
    elif isinstance(value, Iterable):
        return value
    else:
        return [value]
