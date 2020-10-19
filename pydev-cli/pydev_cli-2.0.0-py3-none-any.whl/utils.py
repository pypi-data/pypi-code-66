"""Useful functions for pydev-cli package."""
import platform
import sys
from pathlib import Path

import toml
from typer import Exit, echo

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


def panic(error_msg):
    """Exit after dispplaying error message on standard error."""
    echo(error_msg, file=sys.stderr)
    raise Exit(1)
