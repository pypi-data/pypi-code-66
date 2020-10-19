import logging
import os

from .rg_logger_cache import RGLoggerCache

logger = logging.getLogger('debug')


# noinspection PyBroadException
def info(msg):
    if RGLoggerCache.is_debug_enabled():
        try:
            logger.info("PID: %s, %s", str(os.getpid()), msg)
        except Exception as e:
            logger.info(msg)


def info_important(msg):
    logger.info(msg)


def exception(e, log_message: str = "", can_print_stacktrace: bool = False):
    logger.error("%s, ExceptionMessage:%s", log_message, get_exception_msg(e), exc_info=can_print_stacktrace)


def get_exception_msg(e) -> str:
    try:
        return getattr(e, 'message', repr(e))
    except Exception as e:
        return getattr(e, 'message', repr(e))
