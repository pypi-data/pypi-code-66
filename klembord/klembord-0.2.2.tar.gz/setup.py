# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['klembord']

package_data = \
{'': ['*']}

extras_require = \
{':sys_platform == "linux"': ['python-xlib>=0.26,<0.27',
                              'stopit>=1.1.2,<2.0.0']}

setup_kwargs = {
    'name': 'klembord',
    'version': '0.2.2',
    'description': 'Full toolkit agnostic cross-platform clipboard access',
    'long_description': '# klembord\n\n`klembord` is a python 3 package that provides full clipboard access on supported platforms (Linux and Windows for now, though this may change in the future).\n`klembord` has minimal dependencies, depending only on platform specific apis, which means it can be used with any graphics toolkit or without a toolkit at all.\n\n-------------------\n\nIf you find this software useful,\n\nplease [![Donate](https://d1iczxrky3cnb2.cloudfront.net/button-medium-blue.png)](https://donorbox.org/open-source-support)\n\n-------------------\n\n## Install and dependencies\n\n`klembord` uses `python-xlib` under Linux and `ctypes` on Windows.\nWhen installing with `pip` dependencies will be taken care of automatically.\n\n`pip install klembord`\n\nThat\'s it!\n\n## Usage\n\n```python\n>>> import klembord\n>>> klembord.init()\n>>> klembord.get_text()\n\'example clipboard text\'\n>>>klembord.set_text(\'some string\')\n```\n\n`klembord` also includes convenience functions for working with rich text:\n\n```python\n>>> klembord.get_with_rich_text()\n(\'example html\', \'<i>example html</i>\')\n>>> klembord.set_with_rich_text(\'plain text\', \'<b>plain text</b>\')\n```\n\nRich text function set platform\'s unicode and html formats.\n\nOn Linux accessing selections other than `CLIPBOARD` is easy, just pass selection name to `init`:\n\n```python\nklembord.init(\'PRIMARY\')\n```\n\nIf you need access to other targets/formats you can use `get` and `set` functions:\n\n```python\n>>> content = {\'UTF8_STRING\': \'string\'.encode(), \'text/html\': \'<s>string</s>\'.encode()}\n>>> klembord.set(content)\n>>> klembord.get([\'UTF8_STRING\', \'text/html\', \'application/rtf\'])\n{\'UTF8_STRING\': b\'string\', \'text/html\': b\'<s>string</s>\', \'application/rtf\': None}\n\n>>> from collections import OrderedDict\n>>> content = OrderedDict()\n>>> content[\'HTML Format\'] = klembord.wrap_html(\'<a href="example.com">Example</a>\')\n>>> content[\'CF_UNICODETEXT\'] = \'Example\'.encode(\'utf-16le\')\n>>> klembord.set(content)\n>>> klembord.get([\'HTML Format\', \'CF_RTF\'])\n{\'HTML Format\': b\'<a href="example.com">Example</a>\', \'CF_RTF\': None}\n```\n\nThese examples show manual way of setting clipboard with rich text.\nUnlike convenience functions `get` and `set` takes dicts of bytes as arguments.\nKey should be target/format string and value binary data or encoded string. Every given format/target will be set.\n\nThe first example is Linux usage. Most targets are encoded with `utf8` and it\'s all fairly simple.\nThe second shows usage on Windows. Now windows retrieves formats in order they were defined, so using `collections.OrderedDict` is a good idea to ensure that say html format takes precedence over plain text.\n`CF_UNICODE`, the unicode text format is always encoded in `utf-16le`.\nIf you set this target with `utf8` you\'ll get unknown characters when pasting.\nAnother thing to note is the `wrap_html` function. While setting plain html works on Linux, Windows uses it\'s own (unnecessary) format. This function takes html fragment string and returns formatted bytes object.\n`wrap_html` is only available on Windows.\n\nTo list available targets/formats:\n\n```python\n>>> klembord.get([\'TARGETS\'])\n{\'TARGETS\': [\'TARGETS\', \'SAVE_TARGETS\', \'UTF8_STRING\', \'STRING\']}\n```\n\n### Clipboard persistence on Linux\n\nAs of version 0.1.3 klembord supports storing content in clipboard after application\nexit. You do need to call `klembord.store()` explicitly. Note that this method\nraises `AttributeError` on Windows.\n\n### Selection object\n\nIf you need to access `PRIMARY` selection at the same time as clipboard or you prefer working with objects rather than module level functions, you can use `Selection` objects.\n\n```python\nfrom klembord import Selection\n```\n\nThese objects have the same methods as module level functions, with `klembord.init(SELECTION)` being the `Selection.__init__(SELECTION)`.\n\n## Why klembord\n\nklembord means clipboard in dutch. Since every reasonable name in english was taken on pypi, I decided to cosult a dictionary.\nNow you might think since there\'re so many packages for clipboard access `klembord` is unnecessary.\nAlas, all the other packages only work with plain text, depend on heavy toolkits or external executables, and in one particular case the entire package simply imports copy and paste functions from pyperclip.\nI found the situation rather sad, so I decided to write `klembord`.\n\n## Bugs and limitations\n\n* Setting binary formats should work in theory but it\'s mostly untested.\n* Setting/getting Windows built in binary formats (e.g. `CF_BITMAP`) doesn\'t work and WILL crash python. These require special handling which is currently not implemented in `klembord`\n',
    'author': 'Ozymandias',
    'author_email': 'tomas.rav@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/OzymandiasTheGreat/klembord',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
