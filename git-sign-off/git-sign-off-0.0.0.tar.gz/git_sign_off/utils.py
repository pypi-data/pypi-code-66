import sys


def error(err):
    """
    Print the Exception and abort the program.
    """
    print(f"{err.__class__.__name__}: {err}")
    sys.exit(1)
