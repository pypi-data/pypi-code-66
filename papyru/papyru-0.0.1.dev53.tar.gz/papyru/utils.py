from contextlib import contextmanager
from datetime import datetime


@contextmanager
def limited_runtime(timeout):
    start_time = datetime.now()

    def has_runtime_left():
        return (datetime.now() - start_time) < timeout

    try:
        yield has_runtime_left
    finally:
        pass


def parse_bool(value):
    if isinstance(value, bool):
        return value
    elif isinstance(value, str):
        return value.lower() in ('true', '1', 'yes')
    else:
        raise TypeError('cannot parse bool from "%s".' % value)
