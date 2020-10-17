""" log system  """
import datetime
from .. import config
import collections

NOTICE, REPLY, BUG, WARNING, ERROR = tuple(2**i for i in range(5))

ltype_str = {c:s for s,c in zip( ("NOTICE", "REPLY","BUG", "WARNING", "ERROR"), (NOTICE, REPLY, BUG, WARNING, ERROR))}


DEFAULT_LEVEL = 0

class bcolors:
    DEFAULT = '\033[94m'
    NOTICE = '\033[94m'
    REPLY = '\033[92m'
    BUG = '\033[93m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'    
    UNDERLINE = '\033[4m'
    
def color_log(msg):
    
    for s in ("NOTICE", "REPLY", "BUG", "WARNING", "ERROR"):
        msg = msg.replace(s, getattr(bcolors, s, bcolors.DEFAULT)+" "+s+" "+bcolors.ENDC)
    return msg

class CoreLog:
    def __init__(self):
        self.buffer = collections.deque(maxlen=config.log_buffer_size)
        self.counter = 0
    def write(self, msg):                            
        print(color_log(msg))
        self.buffer.append(msg)
        self.counter += 1
        #open('/Users/guieus/tmp/testlog', 'a').write(msg+"\n")
        
class Log:
    fmt = "{time} {process:10} {stype:10} {msg}"
    process = "unknown"
    def __init__(self, corelog, process, level=None):
        self._core = corelog
        self._level = level
        self.process = process
    
    @property
    def level(self):
        if self._level is None:
            return config.log_verbose_level
        else:
            return self._level
            
    @level.setter
    def level(self, l):
        self._level = int(l)
        
    def log(self, ltype, msg, level=DEFAULT_LEVEL):
        
        # if level is above the log level configuration, do nothing
        # meaning that user should take care that ERROR or WARNING must have a low level        
        if level>self.level:
            return 
        
        process = self.process
        
        try:
            stype = ltype_str[ltype]
        except KeyError:
            raise ValueError("BUG: unknown log type %s"%ltype)
        
        # TODO: change log to a file
        time = datetime.datetime.now().isoformat()[0:19]
        
        self._core.write((self.fmt.format(**locals())))
    
    def bug(self,  msg, level=DEFAULT_LEVEL):
        return self.log(BUG, msg, level)

    def notice(self, msg,  level=DEFAULT_LEVEL):
        return self.log(NOTICE, msg, level)
    
    def warning(self, msg, level=DEFAULT_LEVEL):
        return self.log(WARNING, msg, level)
    
    def error(self, msg, level=DEFAULT_LEVEL):
        return self.log(ERROR, msg, level)
    
    def reply(self, msg, level=DEFAULT_LEVEL):
        return self.log(REPLY, msg, level)
    
    def of_process(self, process):
        newlog = Log()
        for k in ['fmt']:
            setattr(newlog, k, getattr(self, k))
        newlog.process = process
        
        return newlog


process_log_loockup = {}
coreLog = CoreLog()

genlog = Log(coreLog, None)

def get_log(process=None):
    """ get the log object associated to a process 
    
    To save some time the log object are stored in a dictionary or created on fly 
    One should be carefull to not add infinite number of log by process.
    """    
    global process_log_loockup, genlog
    if process is None:
        return genlog
    try:
        return process_log_loockup[process]
    except KeyError:
        log = Log(genlog._core, process)
        log.fmt = genlog.fmt
        log._level = genlog._level
        process_log_loockup[process] = log
        return log        
    
