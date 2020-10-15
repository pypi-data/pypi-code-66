"""pickling_decorator - pickle inputs and outputs of a function."""

__version__ = "0.1.0"
__author__ = "fx-kirin <fx.kirin@gmail.com>"
__all__ = []

import datetime
import functools
import inspect
import logging
import pickle
import random
import string
import types
from pathlib import Path

import kanilog

logger = kanilog.get_module_logger(__file__, 1)


def pickling(save_input=True, save_output=True, save_directory="/tmp/pickling_decorator"):
    def decorator(func, save_input=save_input, save_output=save_output, save_directory=save_directory):
        today = datetime.date.today()
        today = str(today)
        save_directory = Path(save_directory)
        rand_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        save_directory = save_directory / today / rand_str
        logger.info(f"[{func.__qualname__}]Pickling data will be saved to {save_directory}")
        save_directory.mkdir(exist_ok=True, parents=True)

        if func.__qualname__.find(".") >= 0:
            @functools.wraps(func)
            def pickled_func(self, *args, **kwargs):
                now = datetime.datetime.now()
                nowstr = now.strftime('%Y-%m-%d_%H-%M-%S.%f')
                if save_input:
                    input_path = save_directory / f"input-{func.__qualname__}-{nowstr}.pickle"
                    input_path.write_bytes(pickle.dumps((args, kwargs)))
                    logger.debug(f"Wrote input {input_path}")
                result = func(self, *args, **kwargs)
                if save_output:
                    output_path = save_directory / f"output-{func.__qualname__}-{nowstr}.pickle"
                    output_path.write_bytes(pickle.dumps(result))
                    logger.debug(f"Wrote output {output_path}")
                return result

        else:
            @functools.wraps(func)
            def pickled_func(*args, **kwargs):
                __import__('pdb').set_trace()
                now = datetime.datetime.now()
                nowstr = now.strftime('%Y-%m-%d_%H-%M-%S.%f')
                if save_input:
                    input_path = save_directory / f"input-{func.__qualname__}-{nowstr}.pickle"
                    input_path.write_bytes(pickle.dumps((args, kwargs)))
                    logger.debug(f"Wrote input {input_path}")
                result = func(*args, **kwargs)
                if save_output:
                    output_path = save_directory / f"output-{func.__qualname__}-{nowstr}.pickle"
                    output_path.write_bytes(pickle.dumps(result))
                    logger.debug(f"Wrote output {output_path}")
                return result
        return pickled_func
    return decorator
