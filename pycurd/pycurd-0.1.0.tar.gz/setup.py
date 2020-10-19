# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycurd', 'pycurd.crud', 'pycurd.crud.ext', 'pycurd.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.42.1,<0.43.0',
 'multidict>=5.0.0,<6.0.0',
 'pydantic>=1.6.1,<2.0.0',
 'typing-extensions>=3.7.4']

setup_kwargs = {
    'name': 'pycurd',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'fy',
    'author_email': 'fy0748@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.9',
}


setup(**setup_kwargs)
