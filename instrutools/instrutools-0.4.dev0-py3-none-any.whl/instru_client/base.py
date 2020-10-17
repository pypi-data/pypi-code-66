import asyncio
import websockets
import json
from .client_image import ClientDbImage, BaseDbImageInterface

try:
    eval('async')    
except SyntaxError:
    from .coroutine_37 import _send_msg 
except NameError:
    from .coroutine_35 import _send_msg    

def jsonify(cmd, args):
    return json.dumps({'cmd':cmd, 'args':args})    

def unjsonify(msg):
    r = json.loads(msg)
    return r['cmd'], r['args']

class BaseClient:
    def __init__(self, uri='ws://localhost:8765'):
        self.uri = uri
        self._log_counter = 0
        
    
    jsonify = staticmethod(jsonify)
    
    def send_str(self, msg):
        """ send message to server and retrieve result 
        
        the message is a json string, as formated by the jsonify function
        
        Args:
            msg: str
                json formated string. must have mendatory keywords "cmd" (command name) 
                and args command argument 
                
        Returns:
            res : a dictionary containing keywords:
                     "status": (int) 0 if no error append >0 if errors
                     "cmd" : (str) the command applied 
                     "rtime": (float) os time when execution started
                     "time" : (float) os time when execution finished
                 
                 if status ==0 (no error)
                     "answer" : any type it will depend on the command applied
                 
                 if status >0 the following keyword must be present:
                     "rtype": str or int error reference
                     "message": the error message description              
        """
        str_ret =  asyncio.run(_send_msg(msg, uri=self.uri))
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
    
    
    def send(self, cmd, *args):
        """ send message to server and retrieve result 
        
        Args:
            cmd:  (str) command name 
            *args: command arguments
        
        Returns:
            res : a dictionary containing keywords:
                     "status": (int) 0 if no error append >0 if errors
                     "cmd" : (str) the command applied 
                     "rtime": (float) os time when execution started
                     "time" : (float) os time when execution finished
                 
                 if status ==0 (no error)
                     "answer" : any type it will depend on the command applied
                 
                 if status >0 the following keyword must be present:
                     "rtype": str or int error reference
                     "message": the error message description      
        """ 
        msg = self.jsonify(cmd, args)  
        return self.send_str(msg)
            
    def image(self, node=''):                
        dbi = BaseDbImageInterface({}, self)
        dbi.selfupdate(node)        
        c =  ClientDbImage(dbi, node)        
        return c
        
class Client(BaseClient):
    pass

class LocalClient(BaseClient):
    def __init__(self, server):
        self.server = server
        self._log_counter = 0
        
    
    def send(self, cmd, *args):
        """ send message to server and retrieve result 
        
        Args:
            cmd:  (str) command name 
            *args: command arguments
          
        """ 
        return self.server.process(cmd, *args)
    
    def send_str(self, msg):
        return self.send(*unjsonify(msg))
        