from fastapi import FastAPI
from jaeger_client import Config
from loguru import logger
from opentracing.scope_managers.asyncio import AsyncioScopeManager
from opentracing.tracer import Tracer

from .middleware import OpentracingMiddleware
from .settings import TracingSettings


def setup_opentracing(
    service_name: str,
    jaeger_host: str,
    jaeger_port: int,
    sampler_type: str,
    sampler_rate: float,
    trace_id_header: str,
    logging: bool = False,
) -> Tracer:
    """
    Helper function to setup opentracing with Jaeger client during setup.
    Use during app startup as follows:
    .. code-block:: python
        app = FastAPI()
        @app.on_event('startup')
        async def startup():
            setup_opentracing(app)
    :param app: app object, instance of FastAPI
    :return: None
    """
    config = Config(
        config={
            "local_agent": {
                "reporting_host": jaeger_host,
                "reporting_port": jaeger_port,
            },
            "sampler": {"type": sampler_type, "param": sampler_rate},
            "trace_id_header": trace_id_header,
            "logging": logging,
        },
        service_name=service_name,
        validate=True,
        scope_manager=AsyncioScopeManager(),
    )
    logger.debug(
        f"Reporting traces to Jaeger UDP collector: <udp://{jaeger_host}:{jaeger_port}>"
    )
    # this call also sets opentracing.tracer
    return config.initialize_tracer()


def setup_opentracing_from_settings(
    service_name: str, settings: TracingSettings
) -> Tracer:
    """Define the global tracer to be used by your entire service.

    Arguments:
        settings: the tracing settings to apply.

    Returns:

        the OpenTracing tracer instance.
    """
    return setup_opentracing(
        service_name,
        settings.jaeger_host,
        settings.jaeger_port,
        settings.sampler_type,
        settings.jaeger_sampler_rate,
        settings.trace_id_header,
    )


def setup_application_opentracing_from_settings(
    service_name: str, app: FastAPI, settings: TracingSettings,
) -> None:
    """Setup opentracing integration based on given service name, application and settings."""
    if settings.enable:
        tracer = setup_opentracing_from_settings(service_name, settings)
        app.state.tracer = tracer  # type: ignore
        app.add_middleware(OpentracingMiddleware)
