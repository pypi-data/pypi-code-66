# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdfmate']

package_data = \
{'': ['*']}

install_requires = \
['PyPDF2>=1.26.0,<2.0.0',
 'pyppeteer>=0.2.2,<0.3.0',
 'syncasync>=20180812,<20180813']

entry_points = \
{'console_scripts': ['pdfmate-setup = pdfmate.setup:main']}

setup_kwargs = {
    'name': 'pdfmate',
    'version': '0.0.1',
    'description': 'Pyppeteer-based async python wrapper to convert html to pdf',
    'long_description': '# PDFMate: HTML to PDF wrapper\n\nW.I.P.\n',
    'author': 'TK',
    'author_email': 'dk@terminalkitten.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/terminalkitten',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
