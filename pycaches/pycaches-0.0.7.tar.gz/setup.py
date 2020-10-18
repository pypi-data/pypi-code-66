# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycaches']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycaches',
    'version': '0.0.7',
    'description': 'Python caching made easy',
    'long_description': '![Logo](https://raw.githubusercontent.com/codingjerk/pycaches/master/assets/social.png)\n\n[![PyPI](https://img.shields.io/pypi/v/pycaches?style=flat-square)](https://pypi.org/project/pycaches/)\n[![Travis build on master](https://img.shields.io/travis/codingjerk/pycaches/master?style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)\n[![Travis build on develop](https://img.shields.io/travis/codingjerk/pycaches/develop?label=develop&style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)\n[![Codecov coverage](https://img.shields.io/codecov/c/gh/codingjerk/pycaches/develop?token=VHP5IBJTDJ&style=flat-square)](https://codecov.io/gh/codingjerk/pycaches/)\n[![Chat on Gitter](https://img.shields.io/gitter/room/codingjerk/pycaches?style=flat-square)](https://gitter.im/codingjerk/pycaches)\n![License](https://img.shields.io/pypi/l/pycaches?style=flat-square)\n\nA bunch of caches.\n\n## Features\n\n✓ Ease of use `cache` decorator\n\n✓ Support for non-`Hashable` keys (dictionaries, lists, sets)\n\n✓ Different cache replacement policies (random, LRU)\n\n✓ Time-based item expiration\n\n□ Cache hit/miss statistics\n\n□ Rich configuration, sane defaults\n\n□ Optional persistency\n\n## Installation\n\nRecommended way is to use [poetry](https://python-poetry.org/):\n\n```shell\npoetry install pycaches\n```\n\nBut you also can install library with pip:\n\n```shell\npip install pycaches\n```\n\n## Usage\n\n### `cache` decorator\n\n```python\nfrom pycaches import cache\n\n\n@cache()\ndef example():\n    print("Hi, I will be called once!")\n\n\nexample()  # Prints "Hi, I will be called once!"\nexample()  # Is not called\n```\n\n```python\nimport time\n\nfrom pycaches import cache\n\n\n@cache()\ndef long_computation(x):\n    print("Performing long computation...")\n    time.sleep(1)\n    return x + 1\n\n\nlong_computation(5)  # Sleeps for 1 second and returns 6\nlong_computation(5)  # Immediately returns 6\n\nlong_computation(6)  # Sleeps for 1 second and returns 7\nlong_computation(6)  # Immediately returns 7\nlong_computation(6)  # And again\n```\n\n### `Cache` class\n\n```python\nimport time\nfrom datetime import timedelta\n\nfrom pycaches import Cache\n\n\ncache = Cache()\ncache.save("a", 1)\ncache.save("b", 2)\ncache.save("c", 3, expire_in=timedelta(seconds=10))\n\ncache.has("c")  # returns True\ncache.get("a")  # returns 1\n\ntime.sleep(10)\ncache.has("c")  # False\ncache.get("c")  # raises KeyError\n```\n\n### Different cache replacement policies\n\n```python\nfrom pycaches import Cache\nfrom pycaches.policies import LRU\n\n"""\nLRU stands for Least Recently Used.\nSo LRU policy removes Least Recently Used item from cache\nif it\'s size exceed max_items.\n"""\n\n\ncache = Cache(max_items=2, replacement_policy=LRU())\ncache.save("a", 1)\ncache.save("b", 2)\ncache.save("c", 3)\n\ncache.has("a")  # returns False\ncache.has("b")  # returns True\n\ncache.save("d", 4)\n\ncache.has("b")  # returns False\n```\n\n### Disable `deepcopy` for keys\n\n```python\nfrom pycaches import cache\n\n"""\nCache class and cache decorator accepts `copy_keys` argument.\nIf you can garantee that keys will not change even if they are mutable,\nyou may set it to `True` to speed things up.\n"""\n\n\n@cache(copy_keys=False)\ndef faster_caching(x):\n    return x\n\n\nfaster_caching({1, 2, 3})  # returns {1, 2, 3}\n```\n\n## Contribution\n\nJust clone repository, make your changes and create a pull request.\n\nDo not forget to make sure code quality is high: run linters, typecheckers, check code coverage, etc. You can do it all with `make`:\n\n1. `make lint`: `pylint` and `pycodestyle`\n1. `make typecheck`: `mypy`\n1. `make test`: `pytest`\n1. `make coverage`: `pytest` with `pytest-cov`\n1. `make quality`: `radon`\n1. `make build`: `setup.py`\n\nAnd just `make` or `make all` to run all these targets.\n',
    'author': 'Denis Gruzdev',
    'author_email': 'codingjerk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/codingjerk/pycaches',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
