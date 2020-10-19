# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetblack_datagram']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jetblack-datagram',
    'version': '0.4.0',
    'description': 'A Python 3 asyncio datagram library',
    'long_description': '# jetblack-datagram\n\nA Python 3.8+ asyncio helper library for UDP datagram clients and servers.\n\n## Status\n\nThis is working, but still under continuous development, so there may be breaking changes.\n\n## Overview\n\nThis package provides a simple asyncio API for UDP datagrams, following a\nsimilar pattern to the TCP streams API.\n\nA UDP server is started by calling `start_udp_server` which is\nanalogous to the\n[start_server](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server)\nfunction provided by `asyncio`.\nThis returns a `DatagramServer`, which provides methods for reading (`read`), writing (`sendto`),\nand closing (`close` and `wait_closed`). This differs from the TCP variant which provides\na callback when a client connects with a read and write stream. This is because UDP is connection-less\nso there is no connect (or disconnect) event. Also the data is sent and received in *packets*,\nso there seems to eb no benefit to provide separate read and write stream.\n\nThe following creates a server, reads then writes some data.\n\n```python\nserver = await start_udp_server((\'0.0.0.0\', 8000))\n\ndata, addr = await server.recvfrom()\nprint(f"Received {data} from {addr}")\nserver.sendto(b"Hello", addr)\n\nserver.close()\nawait server.wait_closed()\n```\n\nA UDP client is started by calling `open_udp_connection` which is analogous\nto the\n[open_connection](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection)\nfunction provided by the `asyncio` library for TCP, which returns a `DatagramClient`. This provides similar functionality to the\nserver, however the `addr` is not present when reading or writing, as the socket is bound\nto the server address when it is created.\n\n```python\nclient = await open_udp_connection((\'127.0.0.1\', 8000))\n\nclient.send(b"Hello, World!")\ndata = await client.recv()\nprint(f"Received {data}")\n\nclient.close()\nawait client.wait_closed()\n```\n\n\n\n## Installation\n\nInstall using pip.\n\n```bash\npip install jetblack-datagram\n```\n\n## Getting Started\n\nTo create an echo server:\n\n```python\nimport asyncio\n\nfrom jetblack_datagram import start_udp_server\n\n\nasync def main():\n    server = await start_udp_server((\'127.0.0.1\', 9999))\n\n    count = 0\n    while count < 5:\n        count += 1\n        print("Reading")\n        data, addr = await server.recvfrom()\n        print(f"Received {data!r} from {addr}")\n        print(f"Send {data!r} to {addr}")\n        server.sendto(data, addr)\n\n    print("Closing")\n    server.close()\n    print("Waiting for server to close")\n    await server.wait_closed()\n    print("Closed")\n\n    print("Done")\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n```\n\nTo create an echo client:\n\n```python\nimport asyncio\n\nfrom jetblack_datagram import open_udp_connection\n\n\nasync def main():\n    client = await open_udp_connection((\'127.0.0.1\', 9999))\n\n    print("Sending data")\n    client.send(b"Hello, World!")\n    print("reading data")\n    data = await client.recv()\n    print(f"Received {data!r}")\n\n    print("closing client")\n    client.close()\n    print("waiting for client to close")\n    await client.wait_closed()\n\n\nif __name__ == \'__main__\':\n    asyncio.run(main())\n```\n\n## Usage\n\nThe UDP protocol is connection-less, so unlike TCP it makes\nno sense to provide a reader for each server connection, or to\nprovide a callback for connections.\n\n### Common\n\nThe following methods are common for both clients and servers.\n\n* close() -> None\n* async wait_closed() -> None\n\n### Server\n\nThe following methods are specific to the server.\n\n* sendto(data: bytes, addr: Union[Address, str]) -> None\n* async recvfrom() -> Tuple[bytes, Address]\n\n### Client\n\nThe following methods are specific to the client.\n\n* send(data: bytes) -> None\n* async recv() -> bytes\n\n### Helpers\n\nThere is a helper to create the server and the client.\n\nFor the server:\n\n```python\nasync def start_udp_server(\n        addr: Address,\n        *,\n        loop: Optional[AbstractEventLoop] = None,\n        maxreadqueue: int = 0\n) -> DatagramServer:\n```\n\nFor the client:\n\n```python\nasync def open_udp_connection(\n        addr: Address,\n        *,\n        loop: Optional[AbstractEventLoop] = None,\n        maxreadqueue: int = 0\n) -> DatagramClient:\n```\n',
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
