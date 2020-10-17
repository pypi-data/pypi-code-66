#!/usr/bin/env python

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
import os
import codecs

about = {}
with open('lfu_cache/__about__.py') as f:
    exec(f.read(), about)

install_requires = []
extras_require = {}

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]


EXCLUDE_FROM_PACKAGES = []

setup(
    name=about['__title__'],
    version=about['__version__'],
    url=about['__url__'],
    license=about['__license__'],
    description=about['__description__'],
    long_description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.6',
    classifiers=classifiers,
)
