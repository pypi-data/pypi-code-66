from .base import ERROR, reply_error , reply_ok, new_reply
from ..database.base import path_join
from ..functions.log import get_log
import time

log = get_log('db')

dbProc = """
type: process
get:
    type: command
    description: 
"""

def db_process(SYS, cmd, args=None, timeout=None):
    r = new_reply('db', cmd, args)
    
    log.notice('receive command %s'%cmd, 3)
    
    if cmd == "query":
        if isinstance(args, dict):
            try:
                keys = args['parameters']
            except KeyError:
                return reply_error(r, ERROR.ARGS, "argument 'parameters' in the input dictionary is missing", log=log)
        else:
            if isinstance(args, str):
                keys = [args]
            elif isinstance(args,list):
                keys = args
            else:
                return reply_error(r, ERROR.ARGS, "argument must be a dict, a str or a list got a %s"%(type(args)), log=log)
                        
        result = {}
        for key in keys:
            key = path_join(key)
            try:
                obj = SYS[key]
            except (ValueError, TypeError, KeyError):
                return reply_error(r, ERROR.PARAMETER, "%s is not a parameter"%key, log=log)
                
            if not hasattr(obj, "get"):
                return reply_error(r, ERROR.PARAMETER,  "%s is not a parameter"%key, log=log)
                
        
            try:
                val = obj.get()
            except Exception as er:
                return reply_error(r, ERROR.PARAMETER,  "problem when getting parameter %s: %s"%(key,er), log=log)
            result[key] = val
        
        log.notice('query of parameters: %s'%keys, 3)
        return reply_ok(r, result)
    
    
    if cmd == "set":        
        if isinstance(args, dict):
            try:
                keyvalue_pairs = args['values']
            except KeyError:
                return reply_error(r, ERROR.ARGS, "the input dictionary must have 'values' keyword", log=log)
        else:                
            keyvalue_pairs = args
        
        if hasattr(keyvalue_pairs, 'item'):
            iterator = keyvalue_pairs.items()
        else:
            iterator =   keyvalue_pairs  
                                    
        result = {}
        for key,value in iterator:
            key = path_join(key)
            try:
                obj = SYS[key]
            except (ValueError, TypeError, KeyError):
                return reply_error(r, ERROR.PARAMETER, "%s is not a parameter"%key, log=log)
                
            if not hasattr(obj, "set"):
                return reply_error(r, ERROR.PARAMETER, "%s is not a parameter"%key, log=log)
                
        
            try:
                obj.set(value)
            except Exception as er:
                return reply_error(r, ERROR.PARAMETER, "problem when setting parameter %s to value %s: %s"%(key,value,er), log=log)
            result[key] = value
        log.notice('setting parameters: %s'%(keyvalue_pairs), 3)    
        return reply_ok(r, result)
    
    if cmd == "_flush":
        # TODO: Do not like the SYS._db._d to be changed
        
        prefix = args.pop('prefix', None)
        if args:
            return reply_error(r, ERROR.ARGS, "_flush does takes only one optional argument 'prefix'", log=log)
        log.notice('flushing database', 3)
        return reply_ok(r, SYS._db.flush(prefix))
    
    if cmd == "_set":
        if isinstance(args, dict):
            try:
                keyvalue_pairs = args['values']
            except KeyError:
                return reply_error(r, ERROR.ARGS, "the input dictionary must have 'values' keyword", log=log)
        else:                
            keyvalue_pairs = args
        
        try:
            log.notice("Raw setting of %s"%keyvalue_pairs, 3)
            SYS._db.update(keyvalue_pairs)
        except Exception as er:
            return reply_error(r, ERROR.RUNTIME, "when updating database: %s"%er, log=log)
        
        kp = dict(keyvalue_pairs)
        try:
            res = SYS._db.queries( kp.keys() )
        except Exception as er:
            return reply_error(r, ERROR.BUG, "Cannot retrieve back the values set in database: %s"%er, log=log)
        
        return reply_ok(r, res)
                
    if cmd == "_query":
        # TODO: Do not like the SYS._db._d to be changed
        
        if isinstance(args, dict):
            try:
                keys = args['keywords']
            except KeyError:
                return reply_error(r, ERROR.ARGS,  "argument 'keywords' in the input dictionary is missing", log=log)
        else:
            if isinstance(args, str):
                keys = [args]
            elif isinstance(args,list):
                keys = args
            else:
                return reply_error(r, ERROR.ARGS,  "argument must be a dict, a str or a list got a %s"%(type(args)), log=log)
                    
        try:
            items = SYS._db.queries(keys)
        except KeyError as er:
            return reply_error(r, ERROR.PARAMETER, "cannot get on of the query keys %s"%er, log=log)   
            
        #log.notice('raw _QUEERY of %s'%(", ".join(keys)), 3)             
        log.notice('raw _query of %s'%list(items.keys()), 3)        
        return reply_ok(r,items)
        
    return reply_error(r, ERROR.UNKNOWNCMD, "Unknown command %s"%cmd, log=log)
                
        
        
        
    
    