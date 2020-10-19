from typing import Callable


class FileLoadError(Exception):
    pass


def read_program_file(filename: str, f: Callable):
    """
    Read program content and execute f as a procedure with
    content as input
    """
    result = None
    with open(filename, "r") as file:
        s: str = file.read()
        result = f(s)
    return result
