import asyncio
import websockets
import weakref

from ..process.base import  ERROR, Reply
from ..functions.log import get_log
from .. import keys as K
from .. import config


global_process = {}
def add_global_process(name, proc):
    global_process[name] = proc

def get_global_process(name):
    return global_process[name]


try:
    eval('async')
    #eval('_toto_') # force using _35 for debug 
except SyntaxError:
    from .coroutine_37 import coroutine
except NameError:
    from .coroutine_35 import coroutine


class Server:
    def __init__(self, db, processes, host=None, port=None):
                
        self.host = config.ws_host if host is None else host
        self.port = config.ws_port if port is None else port
        self.log = get_log(self.host)
        self.db = db
        
        self._processes = dict(processes)
                  
    def get_process(self, procname):
        try:
            proc = self._processes[procname]
        except KeyError:
            try:
                proc = global_process[procname]
            except KeyError:
                raise ValueError('unknown process %r'%procname)
        return proc
    
    
    def cmd_gets(self, root, nodes):
        attr = K.VALUE
        reply = Reply(cmd='gets', log=self.log)
        
        try:
            rootnode = self.db.getchild(root)
        except (KeyError, ValueError):
            return reply.error(ERROR.UNKNOWNODE, "unknown node %r"%(root))
        
        values = {}
        for n in nodes:
            try:
                val = rootnode.getattr( (n, attr))
            except (KeyError, ValueError):
                return reply.error(ERROR.UNKNOWNODE, "unknown node %r or attribute %r"%(n, attr))    
            values[n] = val
        return reply.ok(values, level=3)
    
    
    def cmd_get(self, node, attr=None):
        attr = K.VALUE if attr is None else attr
        reply = Reply(cmd='get', log=self.log)
        try:
            val = self.db.getattr( (node, attr) ) 
        except (KeyError, ValueError):
            return reply.error(ERROR.UNKNOWNODE, "unknown attribute %r for node %r"%(attr, node) )    
        return reply.ok(val, level=3)
        
    
    def cmd_set(self, node, value):
        attr = K.VALUE
        reply = Reply(cmd='set', log=self.log)
        try:
            self.db.setattr( (node, attr), value)
        except (KeyError, ValueError):
            return reply.error(ERROR.UNKNOWNODE, "unknown node %r or attribute %r"%(node, attr))    
        return reply.ok(value, level=3)
    
    def cmd_setup(self, root, values):
        attr = K.VALUE
        reply = Reply(cmd='setup', log=self.log)
        
        for node, value in values.items():
            try:
                self.db.setattr( (root, node, attr), value)      
            except (KeyError, ValueError):
                return reply.error(ERROR.UNKNOWNODE, "unknown node %r"%(node))
        return reply.ok(None)
              
    
    def cmd_dump(self, node_name):
        
        reply = Reply(cmd='dump', log=self.log)
        try:
            d = self.db.flatdict(node_name)
        except Exception as er:
            return reply.error(ERROR.ARGS, "error when dumping database : %s"%(er))          
        
        ie = self.db.__dbi__.dbp.isendding
        d = {k:v for k,v in d.items() if not ie(k, K.VALUE)}              
        return reply.ok(d,level=1)
    
    def cmd_call(self, nodename, methodname, args=None):
        reply = Reply(cmd='call', log=self.log)
        args = tuple() if args is None else args
        
        try:
            node = self.db.getchild(nodename)
        except (KeyError, ValueError):
            return reply.error(ERROR.UNKNOWNPROC, "unknown node %r"%(nodename,))
        
        try:
            method = node.getchild(methodname)
        except (KeyError, ValueError):
            return reply.error(ERROR.UNKNOWNPROC, "unknown method %r for node %r"%(methodname, nodename))
        
        try:
            procname = method.getattr(K.PROCESS)
        except (KeyError, ValueError):
            try:
                procname = node.getattr(K.PROCESS)
            except (KeyError, ValueError):
                return reply.error(ERROR.UNKNOWNPROC,"node %r has no process"%nodename)
                        
        try:
            proc = self.get_process(procname)
        except ValueError:
            return reply.error(ERROR.UNKNOWNPROC, "Unknown process '%s'"%procname)
        
        try:
            func = getattr(proc, methodname)
        except AttributeError:
            return reply.error(ERROR.UNKNOWNPROC, "process does not contain method %r"%methodname)
        
        argnames = method.getattr('args', []) 
        new_args = []   
        for argname, arg in zip(argnames, args):
            try:
                adef = method.getchild(argname)
            except (KeyError, ValueError):
                new_args.append(arg)
            else:
                new_args.append(adef.parseval(arg))
        
        return func(node, {'cmd':'call', 'proc':procname, 'method':methodname, 'args':new_args},  *new_args)     
    
    
    def process(self, cmd_name, *args): 
        
        try:
            cmd = getattr(self, "cmd_"+cmd_name)
        except AttributeError:
            return Reply(cmd='', log=self.log).error(ERROR.UNKNOWNCMD, "Server does not have command %r"%cmd_name)
        return cmd(*args)     
        
    
    def serve(self):                
        receive = coroutine(self.process)
        start_ws_server = websockets.serve(receive, self.host, self.port)
        self.log.notice(f"Server starting at ws://{self.host}:{self.port}")    
        asyncio.get_event_loop().run_until_complete(start_ws_server)
        asyncio.get_event_loop().run_forever()
        
