# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hello_fish']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hello-fish',
    'version': '0.1.0',
    'description': 'Meu primeiro pacote, uma breve descrição de como ele funciona',
    'long_description': None,
    'author': 'Marcus Pereira',
    'author_email': 'hi@marcuspereira.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
