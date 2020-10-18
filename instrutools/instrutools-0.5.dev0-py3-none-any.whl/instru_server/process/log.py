from .base import ERROR, Reply, Process
from ..functions.log import get_log, genlog
from ..database.db import DB
from .. import config

import time

logProcCfg = """
type: process

set_verbose:
    type: command
    description: set the log verbose level of server
    
    level:
        type: argument
        vtype: int
        desciption: log verbose level int>0
    
get_logs:
    type: command
    description: return last number of log
    
    N:
        type: argument
        vtype: int
        description: return the N last log message
"""
class LogProcess(Process):
    cfg = DB.from_yaml_str(logProcCfg)
    
    def set_verbose(self, db, level=None):
        try:
            config.log_verbose_level = int(level)
        except Exception as er:
            return self.reply.error(ERROR.ARGS, "cannot set verbose : %s"%er)
        
        self.log.notice("log verbose level changed to %s"%config.log_verbose_level)    
        return self.reply.ok({'level':config.log_verbose_level})
    
    def get_logs(self, db, N=None):
            
        if not N:        
            logs = []
        else:
            logs = list(genlog._core.buffer)[-N:]
        
        trueN = len(logs)        
        self.log.notice("getting %s last log out of %s asked"%(trueN, N), 3)
        return self.reply.ok({'logs':logs, 'N':trueN, 'verbose':config.log_verbose_level})

        
            
        
