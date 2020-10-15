#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.2.0-rc4
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import find_packages, setup  # noqa: H301

NAME = "polyaxon-sdk"
VERSION = "1.2.0-rc4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Polyaxon SDKs and REST API specification.",
    author="Polyaxon sdk",
    author_email="contact@polyaxon.com",
    url="",
    keywords=[
        "OpenAPI",
        "OpenAPI-Generator",
        "Polyaxon SDKs and REST API specification.",
    ],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Polyaxon SDKs and REST API specification.  # noqa: E501
    """,
)
