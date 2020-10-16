# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chameleon_log']

package_data = \
{'': ['*']}

install_requires = \
['logbook>=1.5.3,<2.0.0', 'single-version>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'chameleon-log',
    'version': '0.1.0',
    'description': 'Python colored logging setup which adapts to environment',
    'long_description': None,
    'author': 'Nguyễn Hồng Quân',
    'author_email': 'ng.hong.quan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
