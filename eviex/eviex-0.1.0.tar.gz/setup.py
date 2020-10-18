# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eviex']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.2,<2.0.0', 'pandas>=1.1.3,<2.0.0']

setup_kwargs = {
    'name': 'eviex',
    'version': '0.1.0',
    'description': 'EVents Inverted indEX',
    'long_description': '# eviex\neviex\n',
    'author': 'Lou Marvin Caraig',
    'author_email': 'loumarvincaraig@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/se7entyse7en/eviex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
