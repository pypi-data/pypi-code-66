import asyncio
import websockets
import json
from ..shared_doc import redoc
from .database import DataBaseImage, DataBaseImageRW
from ..objects.system import system

try:
    eval('async')    
except SyntaxError:
    from .coroutine_37 import _send_msg 
except NameError:
    from .coroutine_35 import _send_msg    

def jsonify(process, cmd, args={}, timeout=None):
    return json.dumps({'process':process, 'cmd':cmd, 'args':args, 'timeout':timeout})    

def unjsonify(msg):
    r = json.loads(msg)
    return r['process'], r['cmd'], r['args'], r['timeout']

class Client:
    def __init__(self, uri):
        self.uri = uri
        self._log_counter = 0
    
    jsonify = staticmethod(jsonify)
    
    @redoc
    def send_str(self, msg):
        """ send message to server and retrieve result 
        
        the message is a json string, as formated by the jsonify function
        
        Args:
            msg: str
                json formated string. must have mendatory keywords "process" (process name) 
                and "cmd" (command name)
                Other optional keyword are "args" for command arguments (dictionary) and 
                timeout (float) the optional timeout in seconds                     
            
                uri: (str, oprional) server address, default is "ws://localhost:8765"
        Returns:
            {process_return}
                      
        """
        str_ret =  asyncio.run(_send_msg(msg, uri=self.uri))
        #loop = asyncio.new_event_loop()
        #str_ret = loop.run_until_complete(_send_msg(msg, uri=self.uri))
        #str_ret =  asyncio.get_event_loop().run_until_complete(_send_msg(msg, uri=self.uri))
        return json.loads(str_ret)
    
    #def _send_threaded(self, process, cmd, args={}, timeout=None):
    #    msg = self.jsonify(process, cmd, args=args, timeout=timeout)  
    #    return self._send_str_threaded(msg)

    # def _send_str_threaded(self, msg):
    #     return self.send_str(msg)
    #     loop = asyncio.new_event_loop()
    #     asyncio.set_event_loop(loop)
    #     str_ret =  loop.run_until_complete(_send_msg(msg, uri=self.uri))
    #     return json.loads(str_ret)
    
    @redoc
    def send(self, process, cmd, args={}, timeout=None):
        """ send message to server and retrieve result 
        
        Args:
            process: (str) process name
            cmd:  (str) command name 
            args: (dict, optional) dictionary matching command need
            timeout: (float, optional) timeout time in second used if relevant for 
                     the command applied
                     
            uri: (str, oprional) server address, default is "ws://localhost:8765"
        
        Returns:
            {process_return}     
        """ 
        msg = self.jsonify(process, cmd, args=args, timeout=timeout)  
        return self.send_str(msg)
    
    def db_set(self, *args, **kwargs):
        if len(args)%2: 
            raise ValueError('need a number of odd arguments')
        kp = dict(zip(args[::2], args[1::2]))
        kp.update(kwargs)
        r = self.send('db', 'set', {'values':kp})
        if r['status']:
            raise KeyError("{message}".format(**r))
        
    def db_query(self, key):
        r = self.send('db', 'query', key)
        if r['status']:
            raise KeyError("{message}".format(**r))
        return r['return'][key]

    def db_queries(self, keys):
        r = self.send('db', 'query', list(keys))
        if r['status']:
            raise KeyError("{message}".format(**r))
        return [r['return'][key] for key in keys]
    
    def get_logs(self, since=None):
        since = self._log_counter if since is None else since
        r = self.send('log', 'get_logs', since)
        if r['status']:
            raise RuntimeError("{message}".format(**r))
        self._log_counter = r['return']['counter']
        return r['return']['logs']
    
    def get_log_counter(self):
        r = self.send('log', 'get_logs', -1)
        if r['status']:
            raise RuntimeError("{message}".format(**r))
        return r['return']['counter']
    
    def set_log_verbose(self, level):
        r = self.send('log', 'set_verbose', level)
        if r['status']:
            raise RuntimeError("{message}".format(**r))
            
    def get_log_verbose(self):
        r = self.send('log', 'get_logs', -1)
        if r['status']:
            raise RuntimeError("{message}".format(**r))
        return r['return']['verbose']
        
    def system_view(self, rw=False):
        if rw:
            db = DataBaseImageRW(self)
        else:
            db = DataBaseImage(self)
        db.selfupdate()
        return system(db,'')
        
class LocalClient(Client):
    def __init__(self, server):
        self.server = server
        self._log_counter = 0
    
    @redoc
    def send(self, process, cmd, args={}, timeout=None):
        """ send message to server and retrieve result 
        
        Args:
            process: (str) process name
            cmd:  (str) command name 
            args: (dict, optional) dictionary matching command need
            timeout: (float, optional) timeout time in second used if relevant for 
                     the command applied
                     
            uri: (str, oprional) server address, default is "ws://localhost:8765"
        
        Returns:
            {process_return}     
        """ 
        return self.server.process(process, cmd, args, timeout)
    
    def send_str(self, msg):
        return self.send(*unjsonify(msg))
        