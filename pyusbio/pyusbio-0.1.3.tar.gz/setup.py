# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyusbio']

package_data = \
{'': ['*']}

install_requires = \
['pyusb>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['usbio_config = pyusbio.usbio_config:main']}

setup_kwargs = {
    'name': 'pyusbio',
    'version': '0.1.3',
    'description': 'USB-IO2 control library for Python',
    'long_description': 'pyusbio\n=======\n\nこれは、[USB-IO2.0](http://km2net.com/usb-io2.0/index.shtml)をコントロールする\nためのライブラリです。\n\n\n使い方\n------\n    >>> import pyusbio\n    >>> usbio = usbio.USBIO()\n    >>> if usbio.find_and_init():\n    ...   port0, port1 = usbio.send2read([0x00, 0x01])\n    ...   print("{0:x}, {1:x}".format(port0, port1))\n\n\n必須依存ライブラリ\n------------------\n\n* [PyUSB](https://github.com/pyusb/pyusb)\n\n\n動作を確認しているOS\n--------------------\n\n* Linux (Debian Sid)\n* Windows10\n\n\n対応Python\n-------\n\nPython3.6以上  \n(Python2系列は未サポートです。)\n\n\n制限事項\n--------\n\n* １つのUSB-IO2.0しか認識できません。\n\n\nライセンス\n----------\n\nMIT\n\n\nおまけ\n------\n\n付属のusbio\\_config.pyは、USB-IO2.0の内部設定を変更するツールです。\n使い方については、 python usbio\\_config.py --help で表示されるヘルプ情報を参照してください。\n',
    'author': 'Yusuke Ohshima',
    'author_email': 'ohshima.yusuke@yukke.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/yukkeorg',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
