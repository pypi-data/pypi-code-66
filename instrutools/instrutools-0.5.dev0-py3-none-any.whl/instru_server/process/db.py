from .base import ERROR, Reply, Process

from .. import keys as K
from ..functions.log import get_log
from ..database.db import DB
import time

log = get_log('db')

dbProcCfg = """
type: process
authorized_types: [uservar, var] # list of allowed edditable entries

get:
    type: command
    description: get one unique variable value from database
    
    path:
        type: argument
        decription: path to the required variable

set:
    type: command
    description: set one unique variable value from database
    
    path:
        type: argument
        decription: path to the required variable
    
    val:
        type: argument
        desciption: value to be set

query:
    type: command
    description: query database from a glob (as a shell, e.g.  SYS.*, or MOTOR[1-4].POS, etc...)
    
    pattern:
        type: argument
        vtype: str
        desciption: glob pattern of the query e.i. 'MOT*.POS' 
    
get_values:
    type: command
    description: get a dictionary of path/value of a given list of path 
    paths:
        type: argument
        vtype: list
        desciption: list of path pointing to database values 

setup:
     type: command
     description: setup a set of variable from path/value dictionary 
     values:
        type: argument
        vtype: dict
        desciption: dict of path/value pairs

dump:
    type: command
    description: dump the raw data base into a key/valu flat dictionary
    
    path:
        type: argument
        decription: path to the required variable
        default: ''
"""


class DbProcess(Process):  
    cfg = DB.from_yaml_str(dbProcCfg)
    
    def _check_type(self, db, path):
        l = self.cfg.authorized_types
        
        if l is None:
            return True
        
        try:
            tpe = db.getattr( (path,K.TYPE) )
        except KeyError:
            return False
        return tpe in l
    
    def get(self, db, path=None, attribute=K.VALUE):        
        try:
            val = db.getattr( (path,attribute) ) 
        except KeyError:
            return self.reply.error(ERROR.VAR, "%r has no %r attribute"%(path, attribute))
            
        return self.reply.ok(val, level=4)    
    
    def set(self, db, path=None, val=None):                
        oldval = None
        
        if not self._check_type(db, path):
            return self.reply.error(ERROR.VAR, "cannot set variable %r, not allowed by type"%path)
        
        try:
            oldval = db.get_value(path)
        except KeyError:
            pass         
        
                
        try:
            db.set_value(path, val)
        except KeyError:
            return self.reply.error(ERROR.VAR, "cannot set variable %r"%path)
        except ValueError as er:
            return self.reply.error(ERROR.VAR, "cannot set variable %r: %s"%(path,er))
            
        self.log.notice('setting parameters: %s'%(path), 3)  
        return self.reply.ok(oldval, level=2)
    
    def query(self, db, pattern=None, attribute=K.VALUE):
                        
        try:
            lst = list(db.query(pattern, attr=attribute))
        except Exception as er:
            return self.reply.error(ERROR.ARGS, "error when query db with pattern %r : %s"%(pattern,er))
        
        self.log.notice('query: %s'%(pattern), 3)  
        return self.reply.ok(lst, level=4)
    
    def get_values(self, db, paths=None):        
        try:
            # need to call getattr to avoid decoding
            d = {k:db.getattr((k, K.VALUE)) for k in paths}        
        except Exception as er:
            return self.reply.error(ERROR.ARGS, "error when getting db dictionary with pattern: %s"%(er))
        
        return self.reply.ok(d, level=4)    
    
    def setup(self, db, values=None):                
        for path in values:
            if not self._check_type(db, path):                
                return self.reply.error(ERROR.VAR, "cannot set variable %r, not allowed by type"%path)          
        try:
            db.setup(values)
        except Exception as er:
            return self.reply.error(ERROR.ARGS, "error when setup db with pattern: %s"%(er))
        return self.reply.ok(None, level=2)
    
    def dump(self, db, path=None):                
        self.log.notice('dumping database', 3)
            
        try:
            d = db.flatdict(path)
        except Exception as er:
            return self.reply.error(ERROR.ARGS, "error when dumping database : %s"%(er))          
        
        ie = db.__dbi__.dbp.isendding
        d = {k:v for k,v in d.items() if not ie(k, K.VALUE)}              
        return self.reply.ok(d)

        
        
        
    
    