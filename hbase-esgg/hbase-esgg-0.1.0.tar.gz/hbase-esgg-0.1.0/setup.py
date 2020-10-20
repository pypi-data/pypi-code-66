# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 9:10
# @Author  : 
from setuptools import setup, find_packages
with open("README.md","r") as fh:
    long_description = fh.read()


setup(
    name="hbase-esgg",
    version="0.1.0",
    author="xin",
    # license='MIT',
    # url='http://gitlab.weyesns.com/jcsp/library/hbase-thrift-py-sdk',
    long_description=long_description,
    long_description_type="text/markdown",
    # packages=find_packages(),
    # package_data={
    #     'hbase_thrift': ['Hbase.thrift']},
    # data_files=[('.', ['README.md', 'requirements.txt'])
    #             ],
    # include_package_data=True,
    # platforms='any',
)
