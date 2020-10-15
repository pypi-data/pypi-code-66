import os
import sys
from setuptools.command.test import test as TestCommand
from setuptools import Extension
from setuptools import setup


class Test(TestCommand):
    """Introduce test command to run test suite using pytest."""

    _IMPLICIT_PYTEST_ARGS = [
        "--verbose",
        "-l",
        "-s",
        "-vv",
        "tests/",
    ]

    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        super().initialize_options()
        self.pytest_args = None

    def finalize_options(self):
        super().finalize_options()
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        passed_args = list(self._IMPLICIT_PYTEST_ARGS)

        if self.pytest_args:
            self.pytest_args = [arg for arg in self.pytest_args.split() if arg]
            passed_args.extend(self.pytest_args)

        sys.exit(pytest.main(passed_args))


def get_version():
    with open(os.path.join("termial_random", "__init__.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            # dirty, remove trailing and leading chars
            return line.split(" = ")[1][1:-2]
    raise ValueError("No version identifier found")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = get_version()
setup(
    name="termial-random",
    version=VERSION,
    description="Extensions to standard Python's heapq for performance applications",
    long_description=read("README.rst"),
    author="Fridolin Pokorny",
    author_email="fridolin@redhat.com",
    url="https://github.com/thoth-station/termial-random",
    download_url="https://pypi.org/project/termial-random",
    license="GPLv3+",
    packages=["termial_random"],
    ext_modules=[
        Extension(
            "termial_random.random",
            sources=["termial_random/random.c"],
            extra_compile_args = ["-std=c17", "-lm"],
        ),
    ],
    cmdclass={"test": Test},
)
