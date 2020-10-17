import time
from ..functions.log import get_log
    
class ERROR:
    UNKNOWNCMD = "E_UNKNOWNCMD"
    UNKNOWNPROC = "E_UNKNOWNPROC"
    UNKNOWNERROR = "E_UNKNOWNERROR"
    ARGS  = "E_ARGS"
    STATE = "E_STATE"
    SUBSTATE = "E_SUBSTATE"
    BADID = "E_ID"
    REQUIREMENT = "E_REQUIREMENT"
    TIMEOUT = "E_TIMEOUT"
    RUNTIME = "E_RUNTIME"
    PARAMETER = "E_PARAMETER"
    BUG = "E_BUG"


def new_reply(process, cmd, args):
    return  {'process':process, 'cmd':cmd, 'args':args, 'rtime':time.time()}
    
def reply_ok(r, val, log=None):
    if log:
        log.reply(r['cmd'])
    r.update( status=0, time = time.time())        
    r['return'] = val
    return r

def reply_error(r, er, msg, log=None):
    if log:
        log.error("{er} {msg}".format(er=er, msg=msg))
    r.update( status = 4, rtype=er, message=msg, time=time.time())
    return r

# def reply_error(er, cmd,  msg, log=None):
#     if log:
#         log.error("{er} {msg}".format(er=er, msg=msg))
#     return {
#         'status' : 4, 
#         'cmd': cmd, 
#         'rtype': er, 
#         'message': msg
#     }
# 
# def reply_ok(cmd, val, log=None, **kwargs):
#     if log:
#         log.reply(cmd)
#     kwargs['cmd'] = cmd
#     kwargs['status'] = 0
#     kwargs['return'] = val
#     kwargs['time']= time.time()    
#     return kwargs
    
    
# class Process:
#     def __init__(self, process_name, timeout=None, thread_frequency=1):
#         self.process_name = process_name
#         self.timeout = timeout 
#         self.thread_frequency
#         self.log = get_log(process_name)        
#         self._cmd_siwtch = {}
#         self._prep_funcs = []
#         self.debug = False
# 
# 
#     def reply_ok(self, cmd, val, log=None, **kwargs):
#         r = reply_ok(cmd, val, log=self.log if log is None else log, **kwargs)
#         r['process'] = self.process_name
#         return r
# 
#     def reply_error(self, er, cmd,  msg, log=None):
#         r = reply_error(er, cmd, msg, log=self.log if log is None else log)
#         r['process'] = self.process_name
#         return r
# 
#     def command_switcher(self, cmd):
#         if cmd == "*":
#             def prep_function(func):
#                 self._prep_funcs.append(func)
#         else:
#             def switcher_function(func):
#                 self.switch[cmd] = func
#         return switcher_function
# 
#     def __call__(self, OBJ, cmd, args=None, timeout=None):
#         for func in self._prep_funcs:
#             r = func(self, OBJ, cmd, args, timeout)        
#             if r['status']:
#                 return r
# 
#         try:
#             process_func = self._cmd_switch[cmd]
#         except KeyError:
#             return reply_error(ERROR.UNKNOWNCMD, None, "Unknown command %r for process %r"%(cmd, self.process_name))
#         else:
#             if self.debug:
#                 # TODO: The debug condition should not be present here
#                 return process_func(self, OBJ, cmd, args, timeout)
#             else:
#                 try:
#                     return process_func(self, OBJ, cmd, args, timeout)
#                 except Exception as er:
#                     return reply_error(ERROR.BUG, cmd, "An Unknown error occured when executing cmd %r in process %r : %s"%(cmd, self.process_name, er))
# 
# 
        
            
        
        
        