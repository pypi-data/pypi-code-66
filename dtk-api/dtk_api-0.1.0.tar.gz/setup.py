# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dtk_api']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<3.7', 'pydantic>=1.6,<1.7', 'requests>=2.24,<2.25']

setup_kwargs = {
    'name': 'dtk-api',
    'version': '0.1.0',
    'description': '大淘客接口',
    'long_description': None,
    'author': 'dev',
    'author_email': 'dev@qiyutech.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
