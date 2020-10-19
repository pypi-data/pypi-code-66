"""Rest API written using FastAPI."""
from fastapi import FastAPI

from .logging import LoggingSettings, setup_logger_from_settings
from .routes import router
from .tracing import TracingSettings, setup_application_opentracing_from_settings

# Fetch settings from environment variable
logging_settings = LoggingSettings()
# Apply global settings
setup_logger_from_settings(logging_settings)


app = FastAPI(
    title="Demo FastAPI", description="A demo application to show FastAPI features."
)

# Fetch tracing settings from environment variable
tracing_settings = TracingSettings()
# Apply global distributed tracing
setup_application_opentracing_from_settings("demo_fastapi", app, tracing_settings)

# Include router
app.include_router(router)
