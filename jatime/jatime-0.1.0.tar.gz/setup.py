# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jatime']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'flask>=1.1.2,<2.0.0']

entry_points = \
{'console_scripts': ['jatime = jatime.cui:cli']}

setup_kwargs = {
    'name': 'jatime',
    'version': '0.1.0',
    'description': 'Time expression analyzer for Japanese.',
    'long_description': '# Jatime: Time Expression Analyzer for Japanese\n\n[![PyPI Version](https://img.shields.io/pypi/v/jatime.svg)](https://pypi.org/pypi/jatime/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/jatime.svg)](https://pypi.org/pypi/jatime/)\n[![License](https://img.shields.io/pypi/l/jatime.svg)](https://pypi.org/pypi/jatime/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[![Test Status](https://github.com/poyo46/jatime/workflows/Test/badge.svg)](https://github.com/poyo46/jatime/actions?query=workflow%3ATest) \n\nJatime is a Python library to extract Japanese time expressions from a given text and turning them into objects. \n[Try Jatime now from your browser!](https://poyo46.github.io/jatime/)\n\n## Installing jatime\n\nInstall with `pip` or your favorite PyPI package manager.\n\n```\n$ pip install jatime\n```\n\n## Using jatime\n\nHere\'s how to analyze Japanese text using jatime. \nNote that "dow" means the day of the week.\n\n**From within Python**\n\n```python\nfrom jatime.analyzer import analyze\n\n\nresult = analyze("それは令和２年十月十七日の出来事でした。")\nprint(result)\n```\n\n```\n[\'それは\', {\'string\': \'令和２年十月十七日\', \'year\': 2020, \'month\': 10, \'day\': 17, \'dow\': 5, \'hour\': None, \'minute\': None}, \'の出来事でした。\']\n```\n\n**From the command line**\n\n```console\n$ jatime analyze --format-json それは令和２年十月十七日の出来事でした。\n[\n  "それは",\n  {\n    "string": "令和２年十月十七日",\n    "year": 2020,\n    "month": 10,\n    "day": 17,\n    "dow": 5,\n    "hour": null,\n    "minute": null\n  },\n  "の出来事でした。"\n]\n```\n\n**Over HTTP communication**\n```console\n$ jatime serve\n```\n\n```\n$ curl --get "http://localhost:1729/analysis" --data-urlencode "string=それは令和２年十月十七日の出来事でした。"\n["それは",{"day":17,"dow":5,"hour":null,"minute":null,"month":10,"string":"令和２年十月十七日","year":2020},"の出来事でした。"]\n```\n\n## Features\n* Jatime does not change the given string at all. It just objectifies the extracted time expressions.\n* Jatime supports a variety of time expressions. `22:30`, `午後十時半` and `P.M.10:30` are all interpreted as the same time as we want.\n* Jatime tries to make up for the missing time information whenever possible. That is, jatime calculates the year given the month, day and day of the week.\n* Jatime will tell us why the time information is inconsistent if it is inconsistent.\n',
    'author': 'poyo46',
    'author_email': 'poyo4rock@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://poyo46.github.io/jatime/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
