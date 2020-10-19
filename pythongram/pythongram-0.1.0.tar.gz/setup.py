# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pythongram', 'pythongram.modules']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.8.4,<4.0.0']

setup_kwargs = {
    'name': 'pythongram',
    'version': '0.1.0',
    'description': 'An unofficial Instagram SDK for Python',
    'long_description': '# Python-Instagram\n\n[![Build Status](https://travis-ci.com/dyohan9/python-instagram.svg?branch=main)](https://travis-ci.com/dyohan9/python-instagram)',
    'author': 'Daniel Yohan',
    'author_email': 'dyohan9@gmail.com',
    'maintainer': 'Daniel Yohan',
    'maintainer_email': 'dyohan9@gmail.com',
    'url': 'https://github.com/dyohan9/pythongram',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
