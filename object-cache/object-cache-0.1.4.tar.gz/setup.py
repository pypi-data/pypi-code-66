# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['object_cache']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'object-cache',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'u-masao',
    'author_email': '4973920+u-masao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
