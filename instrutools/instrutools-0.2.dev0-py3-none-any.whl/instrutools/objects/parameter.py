from .. import keys as K 
from .base import add_type_class, _BaseParameter, get_parser
from ..database.base import path_join

from . import parser
del parser


def _parameter_parsers(db, prefix):
    prefix = path_join(prefix)
    try:
        ptype = db.query( (prefix,K.PTYPE))
    except KeyError:
        ptype = 'str'
    if isinstance(ptype, str):
        ptype = [ptype]   
     
    return tuple(get_parser(p)(db, prefix) for p in ptype)

def _parse_data(parsers, data):
    for p in parsers:
        data = p(data)
    return data

def parse_parameter(db, prefix, data):    
    return _parse_data(_parameter_parsers(db, prefix), data)

class Parameter(_BaseParameter): 
    
    _protected_config = [K.TYPE]
       
    def __init__(self, db, prefix):
        prefix = path_join(prefix)
        if db.query( (prefix, K.TYPE) ) != K.PARAMETER:
            raise ValueError('%r is not a parameter'%prefix)
        _BaseParameter.__init__(self, db, prefix)         
        # try:
        #     v = self.get()        
        # except KeyError:
        #     pass
        # else:
        #     if v is not None:
        #         db.set( (prefix,K.VALUE) , self.parse(v))
        
    def get(self):
        return self._db.query( (self._path,K.VALUE) )
    
    def set(self, value):
        self._db.set( (self._path, K.VALUE), self.parse(value) )
        
    def seq(self, value):
        return [self._path, self.parse(value)]       
        
    def __str__(self):
        try:
            sval = str(self.get())
        except:
            sval = "ERROR"
        return sval
        
    def __str_ascii__(self, p):                        
        #tab = " "*len(self._path)
        try:
            sval = str(self.get())
        except:
            sval = "ERROR"
                            
        txt = [p.write_margin("%-40s: %s"%(self._path,sval))]                                
        
        return "\n".join(txt) 
        
class _BaseParameters:
    def keys(self):
        for k in self._db.query( (self._path, K.PARAMETERS) ):
            yield k 
    
    def items(self):
        for k in self.keys():
            yield k, self[k]
    
    def values(self):
        for k in self.keys():
            yield self[k]

class Parameters(_BaseParameters):
    _db = None
    _path = None
    def __init__(self, db, prefix):        
        try:
            db.query( (prefix, K.PARAMETERS) )
        except KeyError:
            raise ValueError('(sub)db must must have a "parameters" property at %r'%prefix)    
        self._db = db        
        self._path = prefix 
    
    def __getitem__(self, item):   
        # TODO: Check if cash of Parameters are needed 
        prs = self._db.query( (self._path, K.PARAMETERS) )            
        if item not in prs:
            raise KeyError(item)
        return parameter(self._db, (self._path, item) )

    
# for now parameter is Parameter class
# maybe in the future it will become a function that return a cashed object
# for performance purpose 
parameter = Parameter  
parameters = Parameters

add_type_class(K.PARAMETER, parameter)

