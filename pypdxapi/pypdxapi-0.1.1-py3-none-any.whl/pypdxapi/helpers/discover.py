""" Python implementation of Paradox module discover."""
import sys
import logging
from typing import List
from socket import (socket, timeout, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_REUSEADDR,
                    SO_REUSEPORT, SO_BROADCAST)
from urllib.parse import parse_qsl

_LOGGER = logging.getLogger(__name__)


def discover_modules(num_attempts: int = 5) -> List[dict]:
    """ Discover paradox modules on the network.

    :param num_attempts: (optional) Number of discovery attempts.
    :return: List of discovered modules.
    """
    port = 10000

    discovery = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    _set_sock_opt(discovery, SO_REUSEADDR, 1)
    _set_sock_opt(discovery, SO_REUSEPORT, 1)
    _set_sock_opt(discovery, SO_BROADCAST, 1)
    discovery.settimeout(0.5)

    attempt = 1
    modules = []
    try:
        discovery.bind(('', port))
        discovery.sendto(b'paradoxip?', ('<broadcast>', port))
        _LOGGER.debug("Paradox discovery announcement sent (%s attempt)...", attempt)

        while True:
            try:
                data, addr = discovery.recvfrom(1024)
            except timeout:
                attempt += 1
                if attempt > num_attempts:
                    break
                discovery.sendto(b'paradoxip?', ('<broadcast>', port))
                _LOGGER.debug("Paradox discovery announcement sent (%s attempt)...", attempt)
            else:
                response = data.decode()
                if response.startswith('paradoxip!'):
                    _LOGGER.debug("Found Paradox module on %s: %s", addr, response)
                    modules.append(_parse_response(response))

    except OSError:
        _LOGGER.exception("Discovery error.")
    finally:
        discovery.close()

    return _remove_duplicates(modules)


def _set_sock_opt(sck: socket, optname: int, value: int):
    try:
        sck.setsockopt(SOL_SOCKET, optname, value)
    except AttributeError:
        _LOGGER.error("Systems don't support this socket option %s with value: %s", optname, value)


def _parse_response(result: str) -> dict:
    if sys.version_info >= (3, 9):
        return dict(parse_qsl(result.removeprefix('paradoxip!')))

    return dict(parse_qsl(result[len('paradoxip!'):]))


def _remove_duplicates(modules: List[dict]) -> List[dict]:
    return [dict(t) for t in {tuple(d.items()) for d in modules}]
