# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_entity']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'simple-entity',
    'version': '0.1.0',
    'description': 'Simeple Entity Type for DDD development.',
    'long_description': None,
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
