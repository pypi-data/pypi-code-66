# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getadvice']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'getadvicetest',
    'version': '0.0.6',
    'description': 'This is a fancy `Hello World` to publishing Python library to PyPi.',
    'long_description': '==========\nGet Advice\n==========\n\n\nIntroduction\n============\n\nThis is a fancy `Hello World` to publishing Python library to PyPi.\n\n\n\nUsage\n=====\n\n.. code-block:: python\n\n   import getadvice as gadv\n   gadv.advice(<insert_name>)\n\n\n\nDescription\n===========\n\n1. Input to advice() is a text string\n2. Retrieve advice via REST-API\n\n\n\nReferences\n==========\n\n* https://www.pythoncheatsheet.org/blog/python-projects-with-poetry-and-vscode-part-1/\n* https://python-poetry.org/docs/repositories/#adding-a-repository',
    'author': 'Rich Leung',
    'author_email': 'kleung.hkg@gmail.com',
    'maintainer': 'Dimitrios Mangonakis',
    'maintainer_email': 'mangonakis@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)