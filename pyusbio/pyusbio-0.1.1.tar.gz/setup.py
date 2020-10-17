# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyusbio']

package_data = \
{'': ['*']}

install_requires = \
['pyusb>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['usbio_config = pyusbio.usbio_config:main']}

setup_kwargs = {
    'name': 'pyusbio',
    'version': '0.1.1',
    'description': 'USB0-IO2 control library for Python',
    'long_description': None,
    'author': 'Yusuke Ohshima',
    'author_email': 'ohshima.yusuke@yukke.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
