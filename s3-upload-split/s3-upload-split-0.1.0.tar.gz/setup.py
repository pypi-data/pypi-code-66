# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s3_upload_split']

package_data = \
{'': ['*']}

install_requires = \
['anypubsub>=0.6,<0.7', 'boto3>=1.15.18,<2.0.0']

setup_kwargs = {
    'name': 's3-upload-split',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Cyril Scetbon',
    'author_email': 'cscetbon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cscetbon/s3-upload-split',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
