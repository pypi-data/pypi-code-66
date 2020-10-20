from setuptools import setup
from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()
setup(
    name="nicktest",
    version="1.0.3",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
