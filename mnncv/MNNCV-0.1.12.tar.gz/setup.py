#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='MNNCV',
    author='forkong',
    url='https://github.com/alibaba/MNN',
    description='MNNCV python sdk',
    version='0.1.12',
    platforms=['many'],
    packages=['MNNCV'
              ],
    install_requires=[
      "Pillow",
      "streamlit>=0.55.2"
    ]
)
