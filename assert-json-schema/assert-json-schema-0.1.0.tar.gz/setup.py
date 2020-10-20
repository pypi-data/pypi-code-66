# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assert_json_schema']

package_data = \
{'': ['*']}

install_requires = \
['jsonschema>=3.2.0,<4.0.0']

setup_kwargs = {
    'name': 'assert-json-schema',
    'version': '0.1.0',
    'description': 'Assert json schema, also provide $ref:relative_file wrapper to $ref:file:{absolute_path}',
    'long_description': None,
    'author': 'Bastien Germond',
    'author_email': 'bastien.germond@epita.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BastienGermond/assert-json-schema',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
