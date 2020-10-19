#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 15:44
# @Author  : 程婷婷
# @FileName: setup.py
# @Software: PyCharm
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name= 'zzsnML',
    version= '1.0.1',
    author = 'chengtingting',
    author_email= '2698641198@qq.com',
    packages = find_packages('zzsnML'),
    package_dir = {'':'zzsnML'},
    include_package_data=True,
    description= "Python wrapper for zzsnML: natural language processing",
    long_description=  long_description,
)
