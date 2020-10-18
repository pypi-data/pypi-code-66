# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minilop', 'minilop.amqp']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0', 'pika>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'minilop',
    'version': '0.1.9',
    'description': 'A Wrapper for Pika RabbmitMQ Client Library',
    'long_description': None,
    'author': 'Pramote Teerasetmanakul',
    'author_email': 'pramote@findx.co.th',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
