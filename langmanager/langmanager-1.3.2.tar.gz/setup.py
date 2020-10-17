# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['langmanager']
setup_kwargs = {
    'name': 'langmanager',
    'version': '1.3.2',
    'description': 'this library allows you to create translations of projects into other languages',
    'long_description': "# LangManager\n\n![Image alt](https://img.shields.io/github/license/ASVIEST/LangManager?logo=GitHub&logoColor=orange&style=flat-square)\n![Image alt](https://img.shields.io/discord/762602867088818218?color=green&label=server&logo=discord&logoColor=white&style=flat-square)\n![GitHub repo size](https://img.shields.io/github/repo-size/ASVIEST/LangManager?color=green&label=size&logo=GitHub&logoColor=cAF7a6&style=flat-square)\n\nthis library allows you to create translations of projects into other languages\n#### Simple example:\n```python\nfrom langmanager import *\n\nlanguage = input('language:   ')\nlang(language)\ntrans = translate_get('hello world')\n\nprint(lan())\nprint(trans)\n```\nlanguage file(en):\n```\n'hello world':'hello world';\n'hello i':'hello i';\n```\nAnd language file(ru):\n```\n'hello world':'привет мир';\n'hello i':'привет я';\n```\n###### language standard file name - lan(ISO 639-1).txt examples: en.txt, ru.txt, zh.txt\n###### But file name can change through function filepath_en , filepath_ru and others\n##### language can be changed during working\n#### change filepath example:\n```python\nfrom langmanager import *\n\nlanguage = input('language:   ')\nlang(language)\ntrans = translate_get('hello world')\n\nprint(lan())\nprint(trans)\n\nlang(ru)\nfilepath_ru('en.txt')\ntrans = translate_get('hello i')\nprint(trans)\n```\n```\n'hello world':'hello world';\n'hello i':'hello i';\n```\nAnd language file(ru):\n```\n'hello world':'привет мир';\n'hello i':'привет я';\n```\n",
    'author': 'ASVI',
    'author_email': 'aaaaaabbbbbbccscc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.1,<4.0',
}


setup(**setup_kwargs)
