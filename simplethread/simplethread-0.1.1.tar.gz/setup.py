#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup

setup(
    name="simplethread",
    version="0.1.1",
    author="Andrew Malchuk",
    author_email="andrew.malchuk@yandex.ru",
    description="Some useful utilities for Python's threading module",
    long_description=Path(__file__).with_name("README.md").read_text("utf-8"),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/amalchuk/simplethread",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Typing :: Typed"
    ],
    python_requires=">=3.6, <4.0",
    packages=["simplethread"],
    package_data={
        "simplethread": ["py.typed"]
    },
    zip_safe=False
)
