# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iso_4217']

package_data = \
{'': ['*'], 'iso_4217': ['data/*']}

setup_kwargs = {
    'name': 'iso-4217',
    'version': '0.2.180829',
    'description': 'ISO 4217 currency code library',
    'long_description': "``iso_4217``: Yet another currency data package for Python\n==========================================================\n.. image:: https://travis-ci.org/ikseek/iso_4217.svg?branch=main\n   :target: https://travis-ci.org/ikseek/iso_4217\n.. image:: https://img.shields.io/pypi/v/iso-4217.svg\n   :target: https://pypi.org/project/iso-4217/\n\nThis package contains ISO 4217 active and historical currency data.\nWritten and tested for Python 3.6 and above.\n\n>>> from iso_4217 import Currency\n>>> Currency.USD\n<Currency.USD: 840>\n>>> Currency.USD.full_name\n'US Dollar'\n>>> Currency(840)\n<Currency.USD: 840>\n>>> Currency.JPY.entities\nfrozenset({'JAPAN'})\n>>> Currency.ZWR\n<Currency.ZWR: 935>\n>>> Currency.ZWR.entities\nfrozenset()\n>>> Currency.ZWR.withdrew_entities\n(('ZIMBABWE', '2009-06'),)\n\nInspired by `iso4217`_ package by Hong Minhee.\n\n.. _iso4217: https://github.com/dahlia/iso4217\n",
    'author': 'Igor Kozyrenko',
    'author_email': 'igor@ikseek.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikseek/iso_4217',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
