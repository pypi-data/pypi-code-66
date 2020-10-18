# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trashpy']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.12.3,<2.0.0',
 'google-auth-oauthlib>=0.4.1,<0.5.0',
 'google-auth>=1.22.1,<2.0.0']

entry_points = \
{'console_scripts': ['trashpy = trashpy.main:main']}

setup_kwargs = {
    'name': 'trashpy',
    'version': '1.0.6',
    'description': 'Download your Google Drive Trash folder',
    'long_description': '# TrashPy\n\nDownload your google drive trash folder\n\n## Install\n\n*Make sure to use Python 3*\n\n```\nsudo pip3 install trashpy\n```\n\n## Usage\n\n```\ntrashpy\n```\n\nIt will ask you to authenicate then it will download all your trash to: `gtrash`\n',
    'author': 'Paul Bailey',
    'author_email': 'paul.m.bailey@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pizzapanther/pydrive-trash-backup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
