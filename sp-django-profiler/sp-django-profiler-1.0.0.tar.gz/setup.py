#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django_profiler import __version__
from setuptools import setup, find_packages

setup(
    name='sp-django-profiler',
    version=__version__,
    description='Tools for profiling of code and Django queries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Simone Pozzoli',
    author_email='simonepozzoli1@gmail.com',
    url='https://github.com/pozzolana93/django-profiler',

    zip_safe=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    install_requires=[
        'django'
    ],

    packages=find_packages(),
)
