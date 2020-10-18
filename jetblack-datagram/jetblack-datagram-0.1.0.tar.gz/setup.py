# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetblack_datagram']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jetblack-datagram',
    'version': '0.1.0',
    'description': 'A Python 3 asyncio datagram library',
    'long_description': '# jetblack-datagram\n\nA Python 3 asyncio helper library for UDP datagram clients and servers.\n\n## Installation\n\nInstall using pip.\n\n```bash\npip install jetblack-datagram\n```\n\n## Usage\n\nTo create an echo server:\n\n```python\nimport asyncio\n\nfrom jetblack_datagram import create_datagram_server\n\n\nasync def main():\n    server = await create_datagram_server((\'127.0.0.1\', 9999))\n\n    count = 0\n    while count < 5:\n        count += 1\n        print("Reading")\n        data, addr = await server.read()\n        print(\'Received %r from %s\' % (data, addr))\n        print(\'Send %r to %s\' % (data, addr))\n        server.sendto(data, addr)\n\n    print("Closing")\n    server.close()\n    print("Waiting for server to close")\n    await server.wait_closed()\n    print("Closed")\n\n    print("Done")\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n```\n\nTo create an echo client:\n\n```python\nimport asyncio\n\nfrom jetblack_datagram import create_datagram_client\n\n\nasync def main():\n    client = await create_datagram_client((\'127.0.0.1\', 9999))\n\n    print("Sending data")\n    client.send(b\'Hello, World!\')\n    print("reading data")\n    data, addr = await client.read()\n    print(\'Received %r from %s\' % (data, addr))\n\n    print("closing client")\n    client.close()\n    print("waiting for client to close")\n    await client.wait_closed()\n\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n```\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/jetblack-datagram',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
