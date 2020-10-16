from typing import Any, Dict, cast

import jinja2
from sanic.app import Sanic


@jinja2.contextfunction
def url_for(context: Dict[str, Any], view_name: str, **kwargs):
    app = cast(Sanic, context['app'])
    return app.url_for(view_name, **kwargs)


@jinja2.contextfunction
def static_url(context: Dict[str, Any], filename: str, **kwargs):
    app = cast(Sanic, context['app'])
    return app.url_for('static', filename=filename, **kwargs)
