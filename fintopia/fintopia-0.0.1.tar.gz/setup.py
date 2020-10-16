#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import setuptools
import setuptools.command.test

VERSION = '0.0.1'

# PyPI项目名称
## from fintopia import devops
NAME = 'fintopia'

PACKAGES = setuptools.find_packages(include=(
    'devops',
))

CLASSES = """
    Development Status :: 1 - Planning
    License :: OSI Approved :: BSD License
    Programming Language :: Python
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Framework :: Django
    Framework :: Django :: 3.0
    Operating System :: OS Independent
    Topic :: Communications
    Topic :: System :: Distributed Computing
    Topic :: Software Development :: Libraries :: Python Modules
"""
classifiers = [s.strip() for s in CLASSES.split('\n') if s]


if sys.version_info < (3, 6):
    raise Exception(f'{NAME} {VERSION} requires Python 3.6 or later!')

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    version=VERSION,
    name=NAME,
    packages=PACKAGES,
    description='Python3 common module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='fintopia',
    author='devops',
    author_email='devops@yangqianguan.com',
    url='',
    platforms=['any'],
    license='BSD',
    classifiers=classifiers,
    # install_requires='celery>=4.4,<5.0',
    zip_safe=False,
    include_package_data=False,
)
