# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_same_dir']

package_data = \
{'': ['*']}

install_requires = \
['mkdocs>=1.0,<2.0']

entry_points = \
{'mkdocs.plugins': ['same-dir = mkdocs_same_dir.plugin:SameDirPlugin']}

setup_kwargs = {
    'name': 'mkdocs-same-dir',
    'version': '0.1.0',
    'description': 'MkDocs plugin to allow placing mkdocs.yml to the same directory as documentation',
    'long_description': None,
    'author': 'Oleh Prypin',
    'author_email': 'oleh@pryp.in',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/oprypin/mkdocs-same-dir',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
