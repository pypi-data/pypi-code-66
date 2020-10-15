# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_package_dr', 'test_package_dr.print']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-package-dr',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'drazum',
    'author_email': 'domagoj.razum1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
