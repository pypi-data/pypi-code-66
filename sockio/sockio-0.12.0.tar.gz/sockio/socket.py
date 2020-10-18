import socket
import asyncio


from .common import IPTOS_LOWDELAY, ConnectionEOFError, ConnectionTimeoutError, log


def configure_socket(sock, no_delay=True, tos=IPTOS_LOWDELAY, keep_alive=None):
    if hasattr(socket, "TCP_NODELAY") and no_delay:
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    if hasattr(socket, "IP_TOS"):
        sock.setsockopt(socket.SOL_IP, socket.IP_TOS, tos)
    if keep_alive is not None and hasattr(socket, "SO_KEEPALIVE"):
        if isinstance(keep_alive, (int, bool)):
            keep_alive = dict(active=1 if keep_alive in {1, True} else False)
        active = keep_alive.get('active')
        idle = keep_alive.get('idle')  # aka keepalive_time
        interval = keep_alive.get('interval')  # aka keepalive_intvl
        retry = keep_alive.get('retry')  # aka keepalive_probes
        if active is not None:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, active)
        if idle is not None:
            sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, idle)
        if interval is not None:
            sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, interval)
        if retry is not None:
            sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, retry)


async def open_connection(
    host=None,
    port=None,
    loop=None,
    no_delay=True,
    tos=IPTOS_LOWDELAY,
    keep_alive=None,
):
    if loop is None:
        loop = asyncio.get_event_loop()
    sock = socket.socket()
    sock._loop = loop
    sock.setblocking(False)
    configure_socket(sock, no_delay=no_delay, tos=tos, keep_alive=keep_alive)
    await loop.sock_connect(sock, (host, port))
    return sock


class TCP:

    def __init__(
        self,
        host,
        port,
        eol=b"\n",
        auto_reconnect=True,
        on_connection_made=None,
        on_connection_lost=None,
        on_eof_received=None,
        no_delay=True,
        tos=IPTOS_LOWDELAY,
        connection_timeout=None,
        timeout=None,
        keep_alive=None,
    ):
        self.host = host
        self.port = port
        self.eol = eol
        self.auto_reconnect = auto_reconnect
        self.connection_counter = 0
        self.on_connection_made = on_connection_made
        self.on_connection_lost = on_connection_lost
        self.on_eof_received = on_eof_received
        self.no_delay = no_delay
        self.tos = tos
        self.connection_timeout = connection_timeout
        self.timeout = timeout
        self.keep_alive = keep_alive
        self._sock = None
        self._buffer = asyncio.Queue()
        self._read_task = None
        self._log = log.getChild("TCP({}:{})".format(host, port))

    def __repr__(self):
        return "{}({}, {})".format(type(self).__name__, self.host, self.port)

    def connected(self):
        return self._sock is not None and self._read_task is not None

    def close(self):
        if self._sock:
            self._sock.close()
            self._sock = None

    async def open(self, **kwargs):
        connection_timeout = kwargs.get("timeout", self.connection_timeout)
        if self.connected():
            raise ConnectionError("socket already open")
        self._log.debug("open connection (#%d)", self.connection_counter + 1)
        self.close()
        coro = open_connection(
            self.host,
            self.port,
            no_delay=self.no_delay,
            tos=self.tos,
            keep_alive=self.keep_alive
        )
        if connection_timeout is not None:
            coro = asyncio.wait_for(coro, connection_timeout)

        try:
            self._sock = await coro
        except asyncio.TimeoutError:
            addr = self.host, self.port
            raise ConnectionTimeoutError("Connect call timeout on {}".format(addr))

        self._read_task = asyncio.create_task(self._read_loop())

        if self.on_connection_made is not None:
            try:
                res = self.on_connection_made()
                if asyncio.iscoroutine(res):
                    await res
            except Exception:
                log.exception(
                    "Error in connection_made callback %r",
                    self.on_connection_made.__name__,
                )
        self.connection_counter += 1

    async def _read_loop(self):
        while True:
            data = await self.reader.read(2**14)
            if not data:  # EOF
                pass
    # TODO: Finish this ;-)

