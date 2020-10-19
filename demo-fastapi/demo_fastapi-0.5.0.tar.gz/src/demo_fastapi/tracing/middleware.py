"""Tracing middleware for ASGI applications implemented using OpenTracing."""
import contextvars
from typing import Any

from opentracing import tags
from opentracing.propagation import Format
from opentracing.span import Span
from opentracing.tracer import Tracer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

request_span: Span = contextvars.ContextVar("request_span")


class OpentracingMiddleware(BaseHTTPMiddleware):
    """An ASGI middleware that manages OpenTracing tracer and spans for every request."""

    @staticmethod
    def before_request(request: Request, tracer: Tracer) -> Span:
        """
        Gather various info about the request and start new span within context.

        Arguments:

            request: Starlette's Request object.
            tracer: An OpenTracing tracer instance.

        Returns:
            The OpenTracing span associated with the request.
        """
        # Extract span context from HTTP request headers
        span_context = tracer.extract(
            format=Format.HTTP_HEADERS, carrier=request.headers
        )
        # Start the request span, I.E, a child span from span context.
        # If no span was found in request (I.E, span_context is None), a root span will be created.
        span = tracer.start_span(
            operation_name=f"{request.method} {request.url.path}",
            child_of=span_context,
        )
        # Set tag "http.url" value to the targeted URL
        span.set_tag("http.url", str(request.url))
        # Set remote client IP as tag
        remote_ip = request.client.host
        span.set_tag(tags.PEER_HOST_IPV4, remote_ip or "")
        # Set remote client port as tag
        remote_port = request.client.port
        span.set_tag(tags.PEER_PORT, remote_port or "")

        # Finally return request span
        return span

    async def dispatch(self, request: Request, call_next: Any) -> Response:
        """
        Store span in request state using a scope as context manager to
        ensure that the span will be cleared once request is processed.

        Arguments:

            request: Starlette's Request object
            call_next: Next callable Middleware in chain or final view

        Returns:

            Starlette's Response object
        """
        # Fetch the tracer from the application state
        tracer = request.app.state.tracer
        # Fetch current span
        span = self.before_request(request, tracer)
        # Set active tracing scope to current span.
        with tracer.scope_manager.activate(span, True) as scope:
            request_span.set(span)
            # Update request state
            request.state.opentracing_tracer = tracer
            request.state.opentracing_scope = scope
            request.state.opentracing_span = span
            # Forward request to next callable in chain
            response = await call_next(request)
        return response
