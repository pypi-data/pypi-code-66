# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['t61codec']
setup_kwargs = {
    'name': 't61codec',
    'version': '2.0.0',
    'description': 'Python Codec for ITU T.61 Strings',
    'long_description': "Python Codec for ITU T.61 Strings\n=================================\n\nFor information about the codec see https://en.wikipedia.org/wiki/ITU_T.61\n\n\nInstallation\n------------\n\nInstallation follows the standard Python procedure:\n\n::\n\n    pip install t61codec\n\n\nThe package uses Semantic Versioning 2.0 (https://semver.org/spec/v2.0.0.html).\n\n\nUsage\n-----\n\nThe codec can be registered into Python's codec registry. A helper method has\nbeen provided::\n\n    import t61codec\n    t61codec.register()\n\nPlease see the notes on `codecs.register\n<https://docs.python.org/3/library/codecs.html#codecs.register>`_!\n\nAfter registering, the codec is available as either ``'t61'`` or ``'t.61'``::\n\n    >>> b'Hello T.61: \\xe0'.decode('t.61')\n    'Hello T.61: Ω'\n    >>> 'Hello T.61: Ω'.encode('t.61')\n    b'Hello T.61: \\xe0'\n",
    'author': 'Michel Albert',
    'author_email': 'michel@albert.lu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/exhuma/t61codec',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
