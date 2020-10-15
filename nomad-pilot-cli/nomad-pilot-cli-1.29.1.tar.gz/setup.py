# coding: utf-8

"""
    Nomad Pilot

    This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing. Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf- express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_. Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_ and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_. - Install for node with ``npm install nomad_pilot_cli`` - Install for python with ``pip install nomad-pilot-cli``  # noqa: E501

    The version of the OpenAPI document: 1.29.1
    Contact: paul@samarkand.global
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "nomad-pilot-cli"
VERSION = "1.29.1"
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
    description="Nomad Pilot",
    author="OpenAPI Generator community",
    author_email="paul@samarkand.global",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Nomad Pilot"],
    install_requires=REQUIRES + ["querystring==0.1.0"],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
This is the API descriptor for the Nomad Pilot API, responsible for shipping and logistics processing.

    Developed by `Samarkand Global <https://samarkand.global>`_ in partnership with `SF Express <https://www.sf-
    express.com/cn/sc/>`_, `eSinotrans <http://www.esinotrans.com/haitao.html>`_.

    Read the documentation online at `Nomad API Suite <https://api.samarkand.io/>`_
    and Check out the detailed `changelog <https://gitlab.com/samarkand-nomad/nomad_readme/-/raw/master/history/nomad_pilot.md>`_.

    - Install for node with ``npm install nomad_pilot_cli``
    - Install for python with ``pip install nomad-pilot-cli``
    """
)
