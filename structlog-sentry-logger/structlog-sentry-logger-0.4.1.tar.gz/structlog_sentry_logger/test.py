import structlog_sentry_logger

LOGGER = structlog_sentry_logger.get_logger()
MODULE_NAME = structlog_sentry_logger.get_namespaced_module_name(__file__)

TestErrorClass = ConnectionError
try:
    err_msg = "DUMMY ERROR TO TEST DEFAULT SENTRY REPORT VS. **LOGGER** REPORT"
    raise TestErrorClass(err_msg)
except TestErrorClass as err:
    # This line sends the above exception event to Sentry, with all the breadcrumbs included
    LOGGER.exception("structlog-sentry-logger report")
    raise RuntimeError("Sentry report after logger.exception-based report")
