"""Custom logging intercept handler to forward all log records to loguru."""
import logging
from logging import LogRecord

from loguru import logger


class InterceptHandler(logging.Handler):
    """A custom class to intercept logs emitted using the standard library."""

    def emit(self, record: LogRecord) -> None:
        """Emit any log intercepted using loguru."""
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = logging.getLevelName(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            depth += 1
            if frame.f_back:
                frame = frame.f_back
            break
        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


class TestHandler(logging.Handler):
    """A handler for test purpose."""

    def emit(self, record: LogRecord) -> None:
        """Emit intercepted logs using standard logging library."""
        logging.getLogger(record.name).handle(record)
