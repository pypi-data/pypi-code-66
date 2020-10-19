import typing
from . import App
from .wsgi import WSGIEnviron, WSGIStartResponse

# from . asgi import ASGIReceive, ASGIScope, ASGISend


def serve_static_wsgi(
    app: App, environ: WSGIEnviron, start_response: WSGIStartResponse
) -> typing.Sequence[bytes]:
    return app.statics(environ, start_response)


# async def serve_static_asgi(app: App, scope: ASGIScope, receive: ASGIReceive, send: ASGISend):
#     instance = app.statics(scope)
#     await instance(receive, send)
