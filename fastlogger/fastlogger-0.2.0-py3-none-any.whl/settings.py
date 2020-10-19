"""Custom logging settings for demo_application package.

Settings can be loaded from environment variable.
"""
from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings


class LoggingLevel(str, Enum):
    """
    Allowed log levels for the application
    """

    CRITICAL: str = "CRITICAL"
    ERROR: str = "ERROR"
    WARNING: str = "WARNING"
    INFO: str = "INFO"
    DEBUG: str = "DEBUG"


class LoggingSettings(BaseSettings):
    """Configure your application logging using a LoggingSettings instance.

    All arguments are optional.

    Arguments:
        level (str): the minimum log-level to log. (default: "DEBUG")
        format (str): the logformat to use. (default: "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>")
        filepath (Path): the path where to store the logfiles. (default: None)
        rotation (str): when to rotate the logfile. (default: "1 days")
        retention (str): when to remove logfiles. (default: "1 months")
    """

    level: LoggingLevel = LoggingLevel.DEBUG
    format: str = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
    filepath: Optional[Path] = None
    rotation: str = "1 days"
    retention: str = "1 months"
    test_mode: bool = False

    class Config:
        env_prefix = "logging_"
