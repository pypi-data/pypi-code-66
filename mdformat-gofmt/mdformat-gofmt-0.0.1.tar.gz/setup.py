# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdformat_gofmt']

package_data = \
{'': ['*']}

install_requires = \
['mdformat>=0.3.5']

entry_points = \
{'mdformat.codeformatter': ['go = mdformat_gofmt:format_go']}

setup_kwargs = {
    'name': 'mdformat-gofmt',
    'version': '0.0.1',
    'description': 'Mdformat plugin to gofmt Go code blocks',
    'long_description': '[![Build Status](https://github.com/hukkinj1/mdformat-gofmt/workflows/Tests/badge.svg?branch=master)](<https://github.com/hukkinj1/mdformat-gofmt/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)\n[![PyPI version](<https://img.shields.io/pypi/v/mdformat-gofmt>)](<https://pypi.org/project/mdformat-gofmt>)\n\n# mdformat-gofmt\n> Mdformat plugin to gofmt Go code blocks\n\n## Description\nmdformat-gofmt is an [mdformat](https://github.com/executablebooks/mdformat) plugin\nthat makes mdformat format Go code blocks with [gofmt](https://golang.org/cmd/gofmt).\nThe plugin invokes gofmt in a subprocess so having Go installed is a requirement.\n\n## Installing\n1. [Install Go](https://golang.org/doc/install)\n1. Install mdformat-gofmt\n   ```bash\n   pip install mdformat-gofmt\n   ```\n\n## Usage\n```bash\nmdformat YOUR_MARKDOWN_FILE.md\n```\n',
    'author': 'Taneli Hukkinen',
    'author_email': 'hukkinj1@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hukkinj1/mdformat-gofmt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
