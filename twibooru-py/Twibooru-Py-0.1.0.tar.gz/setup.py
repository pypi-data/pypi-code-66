#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

setup(
  name = "Twibooru-Py",
  description = "Python bindings for Twibooru's API",
  url = "https://github.com/Atronar/Twibooru-Py",
  version = "0.1.0",
  author = "ATroN",
  author_email = "master.atron@gmail.com",
  license = "Simplified BSD License",
  platforms = ["any"],
  packages = find_packages(),
  python_requires='>=3.6',
  install_requires = ["requests"],
  include_package_data = True,
  classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: BSD License",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 3"
  ]
)
