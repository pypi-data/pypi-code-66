# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['itest2']

package_data = \
{'': ['*']}

install_requires = \
['PyHamcrest>=2.0.2,<3.0.0',
 'curlify>=2.2.1,<3.0.0',
 'genson>=1.2.2,<2.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'records>=0.5.3,<0.6.0',
 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'itest2',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ZhangHao',
    'author_email': 'zhanghao@growingio.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
