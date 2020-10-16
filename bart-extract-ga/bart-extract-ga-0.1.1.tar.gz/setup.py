# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['extract', 'extract.utils']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client==1.9.1',
 'pandas>=1.0.4,<2.0.0',
 'pyarrow>=0.17.1,<0.18.0',
 's3fs>=0.4.2,<0.5.0']

setup_kwargs = {
    'name': 'bart-extract-ga',
    'version': '0.1.1',
    'description': 'Extract event views to Google Analytics',
    'long_description': '# Bart Extract GA\n\n[![PyPI version](https://badge.fury.io/py/bart-extract-ga.svg)](https://badge.fury.io/py/bart-extract-ga)\n\nExtract event views to Google Analytics\n\n## Install\n```\n$ pip install bart-extract-ga\n```\n\n## Modules\n\n* `extract.processor.extract_yesterday`: exports data from D-1\n* `extract.processor.extract_by_date_ranger`: exports data from date specified in the parameters, `start_date` and `end_date`\n\n\n## Usage\n\n```python\nfrom extract.processor import extract_yesterday\n\nextract_yesterday(\n    ga_viewId="ga:123456789",\n    ga_credential="/tmp/credentials/GA_credentials.json",\n    s3_path="s3://prd-lake-raw-bart",\n)\n\n```\n\n## Obs\n\n* **s3_path**: the path can be a local path or a path to an AWS S3 bucket',
    'author': 'Cesar Augusto',
    'author_email': 'cesarabruschetta@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cesarbruschetta/bart-recs',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<3.7',
}


setup(**setup_kwargs)
