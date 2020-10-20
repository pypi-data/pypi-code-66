# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:54:59 2020

@author: LENOVO
"""
from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name="matgen_rester",
      version='1.7.0',
      description="A python wrapper for matgen dft API",
      url="https://github.com",
      author="nscc.gz",
      author_email="test@mail.nscc.gz",
      license="MIT",
      packages=['matgen_rester'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['PyYaml','numpy','requests'],
      )