#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='cutebb',
    version='0.0.1',
    author='IcedOtaku',
    author_email='i@waitforaday.site',
    url='https://waitforaday.site',
    description=u'for my cute baby',
    packages=['cutebb'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mua=cutebb:mua',
        ]
    }
)