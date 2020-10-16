# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplemonads']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'simplemonads',
    'version': '1.0.5',
    'description': 'Simple Monads for Python. Use Just to end checking for None, Success to end unhandled exceptions, and Reader for dependency injection.',
    'long_description': "# simplemonads\n\nSimple Monads for Python. Use Just to end checking for None, Success to end unhandled exceptions, and Reader for dependency injection.\n\n## Platform support\n\nWorks across all platforms on CPython >= 3.5, [in browser with Brython](https://raw.githack.com/sdaves/simplemonads/main/tests/test_brython_standalone.html), and even on microcontrollers with micropython!\n\n![Screenshot of test_reader.py](https://imgur.com/ZnAwyVc.png)\n\n\n## Example using monads: `Success`, `Failure`, `Just`, `Reader`, and `Printer`\n\n```python\nfrom simplemonads import Success, Failure, Just, _, Reader, run, Printer\n\nclass AppDeps:\n    def __init__(self, gui=Printer()):\n        self.gui = gui\n     \ndef app(divide_by_zero=False):                      \n    data = Success(Just(7))     \n    double = lambda x: x + (lambda y: y * 2)\n    triple = lambda x: x + (lambda y: y * 3)\n    result = data + triple + double  \n\n    if divide_by_zero:\n        result += (lambda x: x + (lambda x: x / 0))\n    \n    def effect(deps: AppDeps):\n        return result | {\n            Success:lambda x: x | {\n                Just:lambda val: deps.gui.Popup('Answer to the Universe: ' + str(val))\n            },\n            Failure:lambda x: deps.gui.Popup('Whoops, an error happened: ' + x)\n        } is result or result\n    \n    return Reader(effect)\n\nclass GuiAppDeps(AppDeps):\n    def __init__(self, gui=Printer()):\n        try:\n            import PySimpleGUI\n            self.gui = PySimpleGUI                        \n        except:\n            self.gui = gui\n  \n@run \ndef main():        \n    return app() + GuiAppDeps \n```\n\n## Handling exceptions\n\nTo demonstrate exception handling the above example can be changed to:\n\n```python\n    return app(True) + GuiAppDeps\n```\n\nThis will result in safely handling the divide by zero exception and will run the following without interrupting the flow of the application:\n\n```python\n            Failure:lambda x: deps.gui.Popup('Whoops, an error happened: ' + x)\n```\n",
    'author': 'Stephen Daves',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdaves/simplemonads',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
