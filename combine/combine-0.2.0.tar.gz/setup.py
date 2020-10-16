# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['combine', 'combine.files', 'combine.jinja']

package_data = \
{'': ['*'], 'combine': ['base_content/*']}

install_requires = \
['Pygments>=2.6.1,<3.0.0',
 'beautifulsoup4>=4.9.1,<5.0.0',
 'click>=7.1.2,<8.0.0',
 'jinja2>=2.11.2,<3.0.0',
 'markdown>=3.2.2,<4.0.0',
 'python-frontmatter>=0.5.0,<0.6.0',
 'pyyaml>=5.3.1,<6.0.0',
 'watchdog>=0.10.3,<0.11.0']

entry_points = \
{'console_scripts': ['combine = combine.cli:cli']}

setup_kwargs = {
    'name': 'combine',
    'version': '0.2.0',
    'description': 'A straightforward static site builder.',
    'long_description': '# combine\n',
    'author': 'Dropseed',
    'author_email': 'python@dropseed.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://combine.dropseed.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
