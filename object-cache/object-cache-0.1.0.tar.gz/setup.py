# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['object_cache']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'object-cache',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'u-masao',
    'author_email': '4973920+u-masao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
