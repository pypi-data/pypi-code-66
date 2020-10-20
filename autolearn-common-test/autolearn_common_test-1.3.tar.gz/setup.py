from setuptools import setup #import setuptools python package
from setuptools import find_packages

setup(name='autolearn_common_test', #Name of the package
    version='1.3', #Version of the package
    packages=find_packages("src"),
    package_dir={"": "src"})