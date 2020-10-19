"""Useful functions for pydev-cli package."""
import platform
import sys
from pathlib import Path
from subprocess import check_call
from typing import TextIO

import toml
from typer import echo

IS_WINDOWS = platform.system() == "Windows"


def get_current_project_name() -> str:
    """Find a pyproject.toml file in curretn directory and return project name, else raise a FileNotFoundError.

    Returns:
        The name of the python package in current directory.

    Raises:
        FileNotFoundError: Proces stopped because file "pyproject.toml" could not be found.
    """
    filepath = Path("pyproject.toml")
    if not filepath.is_file():
        raise FileNotFoundError("Could not find 'pyproject.toml' file.")
    content = toml.loads(filepath.read_text())
    return content["tool"]["poetry"]["name"]


def run(
    cmd: str,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
    verbose: bool = False,
) -> None:
    """Run a command and forward both stdout and stderr to console by default.

    In case of error, process will exit with status code 1.

    Arguments:
        cmd: The command to execute.
        stdout: A TextIO object where process standard output will be redirected.
        stderr: A TextIO object where process standard error will be redirected.
        verbose: Print error traceback in case of process failure.
    """
    try:
        check_call(cmd, stdout=stdout, stderr=stderr, shell=IS_WINDOWS)
    except Exception as error:
        if verbose:
            echo(f"{error}", file=sys.stderr)
        exit(f"Task failed on command: {cmd}")


def exit(error_msg):
    """Exit after dispplaying error message on standard error."""
    echo(error_msg, file=sys.stderr)
    sys.exit(1)
