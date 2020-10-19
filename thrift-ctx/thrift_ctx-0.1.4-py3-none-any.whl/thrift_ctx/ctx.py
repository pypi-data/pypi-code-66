import logging
import sys
import threading
import time
import uuid
from functools import partial

from thrift.protocol.THeaderProtocol import THeaderProtocolFactory
from thrift.transport import TTransport

from thrift.server.TServer import TThreadPoolServer
from werkzeug.local import LocalStack, LocalProxy

logger = logging.getLogger("thrift_ctx")

_sentinel = object()

_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()



_app_ctx_err_msg = """\
Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.\
"""

def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)

g = LocalProxy(partial(_lookup_app_object, "g"))


class _AppCtxGlobals:

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name, default=_sentinel):
        if default is _sentinel:
            return self.__dict__.pop(name)
        else:
            return self.__dict__.pop(name, default)

    def setdefault(self, name, default=None):
        return self.__dict__.setdefault(name, default)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)


class App:
    app_ctx_globals_class = _AppCtxGlobals

    def app_context(self):
        return AppContext(self)

class AppContext:

    def __init__(self, app):
        self.app = app
        self.g = app.app_ctx_globals_class()

        self._refcnt = 0

    def push(self):
        """Binds the app context to the current context."""
        self._refcnt += 1
        _app_ctx_stack.push(self)

    def pop(self, exc=_sentinel):
        """Pops the app context."""
        try:
            self._refcnt -= 1
            if self._refcnt <= 0:
                if exc is _sentinel:
                    exc = sys.exc_info()[1]
                self.app.do_teardown_appcontext(exc)
        finally:
            rv = _app_ctx_stack.pop()
        assert rv is self, f"Popped wrong app context.  ({rv!r} instead of {self!r})"

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pop(exc_value)

class RequestContext:

    def __init__(self, app, environ, request=None, session=None):
        self.app = app
        self.request = request
        self.flashes = None
        self.session = session

        self._implicit_app_ctx_stack = []

        self.preserved = False

        self._preserved_exc = None

        self._after_request_functions = []

    @property
    def g(self):
        return _app_ctx_stack.top.g

    @g.setter
    def g(self, value):
        _app_ctx_stack.top.g = value



    def push(self):
        top = _request_ctx_stack.top
        if top is not None and top.preserved:
            top.pop(top._preserved_exc)

        app_ctx = _app_ctx_stack.top
        if app_ctx is None or app_ctx.app != self.app:
            app_ctx = self.app.app_context()
            app_ctx.push()
            self._implicit_app_ctx_stack.append(app_ctx)
        else:
            self._implicit_app_ctx_stack.append(None)
        self._implicit_app_ctx_stack.append(None)

        _request_ctx_stack.push(self)


    def pop(self, exc=_sentinel):
        app_ctx = self._implicit_app_ctx_stack.pop()
        clear_request = False

        try:
            if not self._implicit_app_ctx_stack:
                self.preserved = False
                self._preserved_exc = None
                if exc is _sentinel:
                    exc = sys.exc_info()[1]

                clear_request = True
        finally:
            rv = _request_ctx_stack.pop()

            if app_ctx is not None:
                app_ctx.pop(exc)

            assert (
                rv is self
            ), f"Popped wrong request context. ({rv!r} instead of {self!r})"

    def auto_pop(self, exc):
        self.pop(exc)

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.auto_pop(exc_value)



class MyTThreadPoolServer(TThreadPoolServer):
    def serveClient(self, client):
        """Process input/output from a client for as long as possible"""
        itrans = self.inputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)

        if isinstance(self.inputProtocolFactory, THeaderProtocolFactory):
            otrans = None
            oprot = iprot
        else:
            otrans = self.outputTransportFactory.getTransport(client)
            oprot = self.outputProtocolFactory.getProtocol(otrans)

        ctx = RequestContext(App(), "")
        error = None
        try:
            while True:
                ctx.push()
                g.request_id = str(uuid.uuid4())[-6:]

                # 请求开始时间
                _req_start = time.time()
                # msg_start = "request start"
                # logger.info(msg_start)

                self.processor.process(iprot, oprot)

                # 打印请求总耗时
                dt = time.time() - _req_start
                msg_end = "request end, cost: {} s".format(dt)
                logger.info(msg_end)

                ctx.auto_pop(error)
        except TTransport.TTransportException:
            pass
        except Exception as x:
            logger.exception(x)
            error = sys.exc_info()[1]
        finally:
            try:
                ctx.auto_pop(error)
            except:
                pass

        itrans.close()
        if otrans:
            otrans.close()

    def serveThread(self):
        """Loop around getting clients from the shared queue and process them."""
        while True:
            try:
                client = self.clients.get()
                self.serveClient(client)
            except Exception as x:
                logger.exception(x)

    def serve(self):
        """Start a fixed number of worker threads and put client into a queue"""
        for i in range(self.threads):
            try:
                t = threading.Thread(target=self.serveThread)
                t.setDaemon(self.daemon)
                t.start()
            except Exception as x:
                logger.exception(x)

        # Pump the socket for clients
        self.serverTransport.listen()
        while True:
            try:

                client = self.serverTransport.accept()
                if not client:
                    continue
                self.clients.put(client)
            except Exception as x:
                logger.exception(x)