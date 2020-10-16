# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

import re
from pathlib import Path

from setuptools import (setup, find_packages)


# -- utilities ----------------------------------

def find_version(path):
    """Parse the __version__ metadata in the given file.
    """
    with Path(path).open("r") as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# -- dependencies -------------------------------

install_requires = [
    "setuptools",
    "flask >= 1.0.0",
    "configobj",
    "ligo-segments",
]

# -- setup --------------------------------------

setup(
    # metadata
    name="gwdatafind-server",
    version=find_version(Path("gwdatafind_server") / "__init__.py"),
    author="Duncan Macleod",
    author_email="duncan.macleod@ligo.org",
    description="The server library for the GWDataFind service",
    license="GPLv3",
    long_description=open("README.rst", "r").read(),
    url="https://git.ligo.org/gwdatafind/gwdatafind-server",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    # dependencies
    install_requires=install_requires,
    # content
    packages=find_packages(),
    include_package_data=True,
)
