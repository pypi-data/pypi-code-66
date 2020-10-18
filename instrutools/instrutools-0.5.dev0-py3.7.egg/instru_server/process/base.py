import time
from ..functions.log import get_log
from ..import keys as K
    
class ERROR:
    UNKNOWNCMD = "E_UNKNOWNCMD"
    UNKNOWNPROC = "E_UNKNOWNPROC"
    UNKNOWNERROR = "E_UNKNOWNERROR"
    UNKNOWNODE = "E_UNKNOWNNODE"
    
    ARGUMENT = "E_ARGUMENT"
    ARGS  = "E_ARGS"
    VAR  =  "E_VAR"
    STATE = "E_STATE"
    SUBSTATE = "E_SUBSTATE"
    BADID = "E_ID"
    REQUIREMENT = "E_REQUIREMENT"
    TIMEOUT = "E_TIMEOUT"
    RUNTIME = "E_RUNTIME"
    PARAMETER = "E_PARAMETER"
    BUG = "E_BUG"


class Reply:
    def __init__(self, trace=None, **kwargs):
        self.trace = {} if trace is None else trace
        self.trace.update(kwargs)
        self.log = self.trace.pop('log', None) # pop log of the trace it should not go into reply
        
    def ok(self, answer, level=None):
        if self.log:
            self.log.reply( "{cmd} {method}".format(cmd=self.trace.get('cmd',''), 
                                                    method=self.trace.get('method','')), 
                                                    level=level)
                                                    
        return dict(self.trace, answer=answer, status=0, etime=time.time())
    
    def error(self, er, msg):
        if self.log:
            self.log.error("{cmd} {method} {er} {msg}".format(er=er, msg=msg, 
                                                              cmd=self.trace.get('cmd',''), 
                                                              method=self.trace.get('method','')))
                                                              
        return dict(self.trace, status = 4, rtype=er, message=msg, etime=time.time())
