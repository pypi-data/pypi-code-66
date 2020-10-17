# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['langmanager']
setup_kwargs = {
    'name': 'langmanager',
    'version': '1.3.8',
    'description': 'this library allows you to create translations of projects into other languages',
    'long_description': '# LangManager\n\n![Image alt](https://img.shields.io/github/license/ASVIEST/LangManager?logo=GitHub&logoColor=orange&style=flat-square)\n![GitHub repo size](https://img.shields.io/github/repo-size/ASVIEST/LangManager?color=green&label=size&logo=GitHub&logoColor=cAF7a6&style=flat-square)\n![PyPI](https://img.shields.io/pypi/v/langmanager?color=yellow&label=version&logo=pypi&logoColor=orange&style=flat-square)\n\nthis library allows you to create translations of projects into other languages\n\n## install:\n<img alt="pypi_icon" src="https://raw.githubusercontent.com/ASVIEST/LangManager/main/mini_pypi_icon.png">\n\n#### installing with pypi\n\n```diff\npip install langmanager\n```\n\n<img alt="git_icon" src="https://raw.githubusercontent.com/ASVIEST/LangManager/main/mini_git_icon.png">\n\n#### installing with git\n\n```diff\ngit clone https://github.com/ASVIEST/LangManager.git\n```\n#### Simple example:\n```python\nfrom langmanager import *\n\nlanguage = input(\'language:   \')\nlang(language)\ntrans = translate_get(\'hello world\')\n\nprint(lan())\nprint(trans)\n```\nlanguage file(en):\n```\n\'hello world\':\'hello world\';\n```\nAnd language file(ru):\n```\n\'hello world\':\'привет мир\';\n```\n```diff\n!language standard file name - lan(ISO 639-1).txt examples: en.txt, ru.txt, zh.txt\n!But file name can change through function filepath_en , filepath_ru and others\n```\n###### language can be changed during working\n#### improved example:\n```python\nfrom langmanager import *\n\nlanguage = input(\'language:   \')\nlang(language)\ntrans = translate_get(\'hello world\')\n\nprint(lan())\nprint(trans)\n\nlang(\'ru\')\nfilepath_ru(\'en.txt\')\ntrans = translate_get(\'hello i\')\nprint(trans)\n```\n```\n\'hello world\':\'hello world\';\n\'hello i\':\'hello i\';\n```\nAnd language file(ru):\n```\n\'hello world\':\'привет мир\';\n\'hello i\':\'привет я\';\n```',
    'author': 'ASVI',
    'author_email': 'aaaaaabbbbbbccscc@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ASVIEST/LangManager',
    'py_modules': modules,
    'python_requires': '>=3.1,<4.0',
}


setup(**setup_kwargs)
