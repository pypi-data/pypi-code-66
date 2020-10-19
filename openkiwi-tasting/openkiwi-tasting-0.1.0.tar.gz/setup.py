# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kiwi_tasting']

package_data = \
{'': ['*'], 'kiwi_tasting': ['assets/img/*']}

install_requires = \
['openkiwi>=2.0.0,<3.0.0',
 'st-annotated-text>=1.0.1,<2.0.0',
 'streamlit>=0.69.2,<0.70.0']

entry_points = \
{'console_scripts': ['kiwi-tasting = kiwi_tasting.__main__:run']}

setup_kwargs = {
    'name': 'openkiwi-tasting',
    'version': '0.1.0',
    'description': 'OpenKiwi demonstration app.',
    'long_description': "# OpenKiwiTasting\nDemonstration UI for OpenKiwi models.\n\nCheckout more details at [OpenKiwi's repository](https://github.com/Unbabel/OpenKiwi).\n",
    'author': 'AI Research, Unbabel',
    'author_email': 'openkiwi@unbabel.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Unbabel/OpenKiwi-Tasting',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
