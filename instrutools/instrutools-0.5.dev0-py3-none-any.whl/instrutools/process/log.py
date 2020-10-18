from .base import ERROR, reply_error, reply_ok, new_reply
from ..database.base import path_join
from ..functions.log import get_log, genlog
from .. import config

import time

log = get_log('log')


def log_process(SYS, cmd, args=None, timeout=None):
    r = new_reply("log", cmd, args)
    
    log.notice('receive command %s'%cmd, 3)
    
    if cmd == "set_verbose":
        if isinstance(args, dict):        
            try:
                level = args['level']
            except KeyError:
                return reply_error(r, ERROR.ARGS,  "keyword  'level' is missing in input dictionary", log=log)
        else:
            try:
                level = int(args)
            except TypeError:
                return reply_error(r, ERROR.ARGS, "argument must be an integer got a %s"%type(args), log=log)
            
        try:
            config.log_verbose_level = int(level)
        except Exception as er:
            return reply_error(r, ERROR.ARGS, "cannot set verbose : %s"%er, log=log)
        
        log.notice("log verbose level changed to %s"%config.log_verbose_level)
        
        return reply_ok(r, {'level':config.log_verbose_level})
        
    elif cmd == "get_logs":
        counter = genlog._core.counter
        
        if isinstance(args, dict):
            try:
                since = args['since']
            except KeyError as er:
                return reply_error(r, ERROR.ARGS, "keyword 'since' is missing in input dictionary: %s"%er, log=log)    
        else:
            try:
                since = int(args)
            except (TypeError,ValueError) as er:
                return reply_error(r, ERROR.ARGS, "argument is not an integer: %s"%er, log=log) 
        
        
        if since<0:
            N = -since
        else:                       
            N = max(0,   counter-since)
            
        if not N:        
            logs = []
        else:
            logs = list(genlog._core.buffer)[-N:]
        
        trueN = len(logs)        
        log.notice("getting %s last log out of %s asked"%(trueN, N), 3)
        return reply_ok(r, {'logs':logs, 'N':trueN, 'counter':counter, 'verbose':config.log_verbose_level})
    
    return reply_error(r, ERROR.UNKNOWNCMD, "Unknown command %s"%cmd, log=log)
        
        
            
        
