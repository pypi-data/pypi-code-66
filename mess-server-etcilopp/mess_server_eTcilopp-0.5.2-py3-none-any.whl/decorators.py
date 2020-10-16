import logging
import sys
import inspect

CALLER = 'server'

if 'client' in sys.argv[0]:
    CALLER = 'client'

LOGGER = logging.getLogger(CALLER)


class Log:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            LOGGER.debug(f'Decorated function {func.__name__} was called '
                         f'with parameters: {args}, {kwargs}. '
                         f'Calling module: {func.__module__}. '
                         f'Calling function: {inspect.stack()[1][3]}.')
            return result

        return wrapper
