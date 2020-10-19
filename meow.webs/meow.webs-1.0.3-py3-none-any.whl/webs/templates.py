import typing
from . import App, Settings, Component


try:
    import jinja2
except ImportError:  # pragma: nocover
    jinja2 = None  # type: ignore


class Templates:
    def render(self, path: str, **context: object) -> str:
        raise NotImplementedError()


class JinjaTemplates(Templates):
    def __init__(self, app: App, settings: Settings):
        if jinja2 is None:  # pragma: nocover
            raise RuntimeError("`jinja2` must be installed to use `Templates`.")

        def get_loader(path: str) -> jinja2.BaseLoader:
            if ":" in path:
                package_name, path = path.split(":", 1)
                return jinja2.PackageLoader(package_name, path)
            else:
                return jinja2.FileSystemLoader(path)

        loaders: typing.List[jinja2.BaseLoader] = []
        for template_dir in settings.TEMPLATE_DIRS:
            if isinstance(template_dir, dict):
                mapping = {
                    prefix: get_loader(path) for prefix, path in template_dir.items()
                }
                loaders.append(jinja2.PrefixLoader(mapping))
            else:
                loaders.append(get_loader(template_dir))

        loader = jinja2.ChoiceLoader(loaders) if len(loaders) > 1 else loaders[0]
        self.env = jinja2.Environment(autoescape=True, loader=loader)
        self.env.globals["reverse_url"] = app.reverse_url
        self.env.globals["static_url"] = app.static_url

    def render(self, path: str, **context: object) -> str:
        template = self.env.get_template(path)
        return template.render(**context)


class TemplatesComponent(Component, singleton=True):
    def resolve(self, app: App, settings: Settings) -> Templates:
        return JinjaTemplates(app, settings)


TEMPLATES_COMPONENTS = [TemplatesComponent()]
