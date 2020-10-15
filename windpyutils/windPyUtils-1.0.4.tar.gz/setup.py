# -*- coding: UTF-8 -*-
""""
Created on 23.12.19

:author:     Martin Dočekal
"""
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='windPyUtils',
    version='1.0.4',
    description='Useful tools for Python projects.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='The Unlicense',
    packages=find_packages(),
    author='Martin Dočekal',
    keywords=['utils', 'general usage'],
    url='https://github.com/windionleaf/windPyUtils',
    install_requires=[
    ]
)

if __name__ == '__main__':
    setup(**setup_args)