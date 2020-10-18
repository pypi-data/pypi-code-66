# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pkgdownloader']

package_data = \
{'': ['*'], 'pkgdownloader': ['templates/*']}

install_requires = \
['Jinja2>=2.11.2,<3.0.0', 'docker>=4.3.1,<5.0.0']

entry_points = \
{'console_scripts': ['pkg-downloader = pkgdownloader.pkgdownloader:run']}

setup_kwargs = {
    'name': 'pkg-downloader',
    'version': '0.1.0',
    'description': 'A streamlined way to download packages for offline installation.',
    'long_description': '# pdownload',
    'author': 'Dan',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
