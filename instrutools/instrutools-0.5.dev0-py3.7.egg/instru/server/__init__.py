import asyncio
import websockets
import json
from ..process.base import  ERROR, reply_error
from ..functions.log import get_log
from ..process.thread import kill_all_threads
from .. import config
import signal

MAINSYSTEM = None

try:
    eval('async')
    #eval('_toto_') # force using _35 for debug 
except SyntaxError:
    from .coroutine_37 import coroutine
except NameError:
    from .coroutine_35 import coroutine

class Server:
    def __init__(self, SYS, processes, host=None, port=None):
        self.SYS = SYS        
        self.host = config.ws_host if host is None else host
        self.port = config.ws_port if port is None else port
        self.log = get_log(self.host)
        for key,a in processes.items():
            try:
                path, func = a
            except ValueError:
                raise ValueError("process must be a tuple of (path, func) got %s"%a)
            if not hasattr(func, "__call__"):
                raise ValueError("process must be a tuple of (path, func) func is not callable")
        self.processes = dict(processes)
    
    def process(self, procname, cmd, args=None, timeout=None):
        SYS = self.SYS
        #args = {} if args is None else args 
        try:
            path, proc_func = self.processes[procname]
        except (ValueError,KeyError):
            return reply_error(ERROR.UNKNOWNPROC, cmd, "Unknown process '%s'"%procname, log=self.log)
            
        SYS = SYS[path] if path else SYS
        
        return proc_func(SYS, cmd, args=args, timeout=timeout)
        
    
    def serve(self):                
        receive = coroutine(self.process)
        start_ws_server = websockets.serve(receive, self.host, self.port)
        self.log.notice(f"Server starting at ws://{self.host}:{self.port}")    
        asyncio.get_event_loop().run_until_complete(start_ws_server)
        asyncio.get_event_loop().run_forever()
        
