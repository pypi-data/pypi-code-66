#!/usr/bin/env python
"""Hooks ran after project generation."""
from distutils.util import strtobool
from pathlib import Path
from shutil import rmtree
from subprocess import check_call
import platform
import sys

IS_WINDOWS = platform.system() == "Windows"


def panic(error: Exception, msg_fmt: str, *args, **kwargs):
    print(msg_fmt.format(*args, **kwargs), file=sys.stderr)
    print(f"Error: {error}.", file=sys.stderr)
    sys.exit(1)


def init_git() -> None:
    """Init a git repository."""
    try:
        check_call(["git", "init"])
        check_call(["git", "checkout", "-b", "next"])
    except Exception as error:
        panic(error, "Error encountered during 'git init' post install hook. Do you have git installed ?")


def install_precommit() -> None:
    """Install pre-commit hooks."""
    try:
        check_call(["poetry", "run", "pre-commit", "install"], shell=IS_WINDOWS)
        check_call(["poetry", "run", "pre-commit", "install", "--hook-type", "commit-msg"], shell=IS_WINDOWS)
    except Exception as error:
        panic(error, "Error encountered during 'pre-commit' post-install hook")


def first_commit() -> None:
    """Commit after repository has been generated successfully."""
    try:
        check_call(["poetry", "run", "git", "add", "."], shell=IS_WINDOWS)
        check_call(["poetry", "run", "git", "commit", "-m", "chore: first commit"], shell=IS_WINDOWS)
    except Exception as error:
        panic(error, "Error encountered during 'git commit' post-install hook.")


def install_package() -> None:
    """Install package using poetry."""
    try:
        check_call(["poetry", "install"], shell=IS_WINDOWS)
    except Exception as error:
        panic(error, "Error encountered during 'poetry install' post-install hook.")


if __name__ == "__main__":
    init_git()
    install_package()
    install_precommit()
    first_commit()
