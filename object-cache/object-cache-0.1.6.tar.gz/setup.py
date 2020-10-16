# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['object_cache']

package_data = \
{'': ['*']}

install_requires = \
['cloudpickle>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'object-cache',
    'version': '0.1.6',
    'description': 'This module caches the result of function.',
    'long_description': '=====================\nobject_cache\n=====================\n\ndescription\n============\n\nThis module caches the processing result of the function in the storage, and if the cache hits, skips the processing in the function and returns the result. Create ".object_cache" in the current path and cache it.\n\ninstall\n========\n\n.. code-block:: shell\n\n    pip install object-cache\n\ncode example\n============\n\n.. code-block:: python\n\n    import time\n\n    from object_cache import object_cache\n\n\n    @object_cache\n    def factorial(a):\n        result = 1\n        for i in range(2, a + 1):\n            result *= i\n\n        return result\n\n\n    for _ in range(5):\n        start = time.time()\n        factorial(100000)\n        print("elapsed time", time.time() - start)\n\nclear cache\n============\n\n.. code-block:: shell\n\n    rm -fr .object_cache\n\n',
    'author': 'u-masao',
    'author_email': '4973920+u-masao@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/u-masao/object-cache',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
