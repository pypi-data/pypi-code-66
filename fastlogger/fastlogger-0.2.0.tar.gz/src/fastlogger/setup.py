"""This module expose two functions that are useful to setup your application logging.

Functions:

- setup_logger: Setup global logging using loguru.
  This function requires positional or keywork arguments.

- setup_logger_from_settings: Setup global logging using loguru.
  This function requires a single positional argument which must be
  a valid LoggingSettings instance.

"""
from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Optional, Tuple

from loguru import logger

from .handlers import InterceptHandler, TestHandler
from .settings import LoggingSettings


def setup_logger(
    level: str,
    format: str,
    filepath: Optional[Path] = None,
    rotation: Optional[str] = None,
    retention: Optional[str] = None,
    test_mode: bool = False,
) -> Tuple[int, ...]:
    """Define the global logger to be used by your entire application.

    Arguments:
        level: the minimum log-level to log.
        format: the logformat to use.
        filepath: the path where to store the logfiles.
        rotation: when to rotate the logfile.
        retention: when to remove logfiles.

    Returns:
        the logger to be used by the service.

    References:
        [Loguru: Intercepting logging logs #247](https://github.com/Delgan/loguru/issues/247)
        [Gunicorn: generic logging options #1572](https://github.com/benoitc/gunicorn/issues/1572#issuecomment-638391953)
    """
    # Remove loguru default logger
    logger.remove()
    if test_mode:
        handler_id = logger.add(TestHandler(), format="{message} {extra}")
        return (handler_id,)

    # Cath all existing loggers
    # The manager attribute from the RootLogger instance cannot be found mypy or any other linters
    # This is due to the attribute being created on the fly  on line 1826 of logging/__init__.py
    # We don't have any other choice than ignoring type check here
    LOGGERS = [logging.getLogger(name) for name in logging.root.manager.loggerDict]  # type: ignore
    # Add stdout logger
    stdout_handler_id = logger.add(
        sys.stdout,
        enqueue=True,
        colorize=True,
        backtrace=True,
        level=level.upper(),
        format=format,
    )
    # Optionally add filepath logger
    file_handler_id = 0
    if filepath:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        file_handler_id = logger.add(
            str(filepath),
            rotation=rotation,
            retention=retention,
            enqueue=True,
            colorize=False,
            backtrace=True,
            level=level.upper(),
            format=format,
        )
    # Overwrite config of standard library root logger
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    # Overwrite handlers of all existing loggers from standard library logging
    for _logger in LOGGERS:
        _logger.handlers = [InterceptHandler()]
        _logger.propagate = True if test_mode else False

    if file_handler_id:
        return stdout_handler_id, file_handler_id
    return (stdout_handler_id,)


def setup_logger_from_settings(settings: LoggingSettings) -> Tuple[int, ...]:
    """Define the global logger to be used by your entire application.

    Arguments:
        settings: the logging settings to apply.

    Returns:
        the logger instance.
    """
    return setup_logger(
        settings.level,
        settings.format,
        settings.filepath,
        settings.rotation,
        settings.retention,
        settings.test_mode,
    )


def setup_logger_from_env() -> Tuple[int, ...]:
    """Override all standard library logging handlers to be intercepted and forwared to loguru.

    Once this function is applied, you can simply use the code below to log messages from anywhere:

    >>> from loguru import logger

    >>> logger.debug("This is a debug message")
    >>> logger.info("This is an info message")
    >>> logger.warning("This is a warning")
    >>> logger.error("This is an error")
    """
    settings = LoggingSettings()
    return setup_logger_from_settings(settings)
