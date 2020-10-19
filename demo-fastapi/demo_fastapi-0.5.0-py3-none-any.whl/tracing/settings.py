"""Distributed tracing settings for demo_application."""
from pydantic import BaseSettings


class TracingSettings(BaseSettings):
    """Configure your service tracing using a TracingSettings instance.

    All arguments are optional.

    Arguments:
        enable (bool): Whether to enable distributed tracing or not
        jaeger_host (str): jaeger serve host (default: "localhost")
        jaeger_port (int): jaeger server listenning port (default: 6381)
        sampler_type (str): type of sampler to use. (default: "probabilistic")
        sampler_rate (float): rate of request to actually trace. Set to 1 to trace all requests. (default: 1.0)
        trace_id_header (str): name of HTTP header where trace ID can be found. (default: "X-TRACE-ID")
    """

    enable: bool = True
    jaeger_host: str = "localhost"
    jaeger_port: int = 6831
    sampler_type: str = "probabilistic"
    jaeger_sampler_rate: float = 1.0
    trace_id_header: str = "X-TRACE-ID"

    class Config:
        env_prefix = "tracing_"
