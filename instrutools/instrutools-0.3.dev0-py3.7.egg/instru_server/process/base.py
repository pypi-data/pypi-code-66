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
    def __init__(self, proc='', cmd='', args=None, log=None, method=''):
        self.r = {'process':proc, 'cmd':cmd, 'args':args, 'method':method, 'rtime':time.time()}
        self.log = log
        
    def ok(self, answer, level=None):
        if self.log:
            self.log.reply( "{cmd} {method}".format(**self.r), level=level)
        return dict(self.r, answer=answer, status=0, time=time.time())
    
    def error(self, er, msg):
        if self.log:
            self.log.error("{cmd} {method} {er} {msg}".format(er=er, msg=msg, **self.r))
        return dict(self.r, status = 4, rtype=er, message=msg, time=time.time())
