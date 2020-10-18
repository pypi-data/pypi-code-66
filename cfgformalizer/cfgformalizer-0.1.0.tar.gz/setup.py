# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cfgformalizer']

package_data = \
{'': ['*'], 'cfgformalizer': ['cisco/*']}

entry_points = \
{'console_scripts': ['cfgformalizer = cfgformalizer.command_line:main']}

setup_kwargs = {
    'name': 'cfgformalizer',
    'version': '0.1.0',
    'description': 'Formalize (show run formal) Cisco IOS, IOS-XR and other type of network configs for easy grepping',
    'long_description': None,
    'author': 'xv0x7c0',
    'author_email': '13061441+xv0x7c0@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
