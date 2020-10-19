# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplemonads']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'simplemonads',
    'version': '1.0.9',
    'description': 'Easy to use monads (containers) that improve the quality of your python code. Use Just to end checking for None, Success to end unhandled exceptions, Future for async, and Reader for dependencies.',
    'long_description': '# [simplemonads](https://sdaves.github.io/simplemonads/)\n\nEasy to use monads (containers) that improve the quality of your python code. Use `Just` to end checking for None, `Success` to end unhandled exceptions, `Future` for async, and `Reader` for dependencies.\n\n## Platform support\n\nJust `pip install simplemonads` and you\'re done. You can also download [this single file](https://sdaves.github.io/simplemonads/tests/simplemonads.py) into your project and use it as you wish without dependencies. Works across all platforms, so CPython >= 3.5 (Windows, Linux, Mac, Android, iOS), in a [single standalone html](https://sdaves.github.io/simplemonads/tests/test_brython_standalone.html) file, multiple files in the browser with [dynamic loading](https://sdaves.github.io/simplemonads/tests/index.html), and [even on microcontrollers with micropython](https://micropython.org)!\n\n![Screenshot of test_reader.py](https://imgur.com/ZnAwyVc.png)\n\n\n## Example GUI using monads: `Success`, `Failure`, `Just`, `Reader`, and `Printer`\n\n```python\nimport simplemonads as sm\n\ntry:\n    from typing import Callable, Protocol, Union, Any\n\n    class Deps(Protocol):\n        "Dependencies for your application"\n\n        def popup(self, msg) -> None:\n            "Display a popup with the specified message."\n\n\n    import PySimpleGUI\n\n\nexcept:\n    pass\n\n\ndef make(make_gui: "Callable[[],PySimpleGUI]") -> "Callable[[],Deps]":\n    gui = make_gui()\n\n    class GuiDeps:\n        def popup(self, x: str):\n            gui.Popup(x)\n\n    return GuiDeps\n\n\ndef app(divide_by_zero: bool = False) -> sm.Reader:\n    data = sm.Success(sm.Just(7))\n    double = lambda x: x + (lambda y: y * 2)\n    triple = lambda x: x + (lambda y: y * 3)\n    result = data + triple + double\n\n    if divide_by_zero:\n        result += lambda x: x + (lambda x: x / 0)\n\n    def effect(deps: "Deps") -> "sm.Monad":\n        msg = "Answer to the Universe: "\n        err = "Whoops, an error happened: "\n        result | {\n            sm.Success: lambda x: x | {sm.Just: lambda val: deps.popup(msg + str(val))},\n            sm.Failure: lambda x: deps.popup(err + x),\n        }\n        return result\n\n    return sm.Reader(effect)\n\n\n@sm.run\ndef main():\n    lib = sm.Success() + (lambda x: __import__("PySimpleGUI"))\n    gui = lib | {sm.Success: lambda x: x, sm.Failure: lambda x: sm.Printer()}\n    return app() + make(lambda: gui)\n```\n\n## Handling exceptions\n\nTo demonstrate exception handling the above example can be changed to:\n\n```python\n    return app(divide_by_zero=True) + make(lambda: gui)\n```\n\nThis will result in safely handling the divide by zero exception and will run the following without interrupting the flow of the application:\n\n```python\n            sm.Failure: lambda x: deps.popup(err + x),\n```\n\n## Example monad `Future`\n\n```python\nfrom simplemonads import Future\n\nasync def effect(data=1):\n    import asyncio\n    await asyncio.sleep(0.1)\n    return data ** data\n\nassert Future(2) | { Future: lambda x: x } == 2\n\nassert Future(2) + effect | { Future: lambda x: x } == 4\n\nassert Future(2) + effect + effect | { Future: lambda x: x } == 256\n\n```\n\nThis allows easily adding async functions into the monadic pipeline. If you need special concurrency options, you can await multiple tasks from inside the effect function.\n',
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
