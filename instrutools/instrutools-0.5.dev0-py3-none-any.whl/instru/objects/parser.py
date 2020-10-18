from .. import keys as K 
from .base import  add_parser
from ..database.base import path_join


class BaseParser:
    def __init__(self, db, prefix):
        self._db = db
        self._path = path_join(prefix)
        
    def __call__(self, data):
        return data            

class StrParser(BaseParser):
    def __call__(self, data):
        return str(data)
add_parser('str', StrParser)        
        
class IntParser(BaseParser):
    def __call__(self, data):
        return int(data)
add_parser('int', IntParser)


class FloatParser(BaseParser):
    def __call__(self, data):
        return float(data)
add_parser('float', FloatParser)


class BoolParser(BaseParser):
    def __call__(self, data):
        return True if data else False
add_parser('bool', BoolParser)

class ListParser(BaseParser):
    def __call__(self, data):
        return list(data)
add_parser('list', ListParser)

class ListedParser(BaseParser):
    def __init__(self, db, prefix):
        prefix = path_join(prefix)
        
        try:
            lst = db.query( (prefix,'list') )
        except KeyError:
            raise ValueError("listed parameter must have the 'list' property at %r"%prefix)
        else:
            if not hasattr(lst, '__iter__'):
                raise ValueError("'list' of a 'listed' parameter must be iterable at %r"%prefix)        
        BaseParser.__init__(self, db, prefix)    
    
    def __call__(self, value):        
        lst = self._db.query( (self._path,'list') )
        if value not in lst: 
            raise ValueError("%r is not in list: %r at %r"%(value, lst, self._path))
        return value
        
add_parser('listed', ListedParser)        

class BoundedParser(BaseParser):
    def __init__(self, db, prefix):  
        prefix = path_join(prefix)          
        try:
            db.query( (prefix,'min') )
        except KeyError:
            raise ValueError('missing "min" attribute for bounded parameter at %r'%prefix)
        try:
            db.query( (prefix,'max') )
        except:
            raise ValueError('missing "max" attribute for bounded parameter at %r'%prefix)
        
        BaseParser.__init__(self, db, prefix)
                    
    def __call__(self, value):
        mn = self._db.query( (self._path, 'min') )
        mx = self._db.query( (self._path, 'max') )        
        if value<mn:
            raise ValueError('%s is lower than %s at %r'%(value, mn, self._path))
        if value>mx:
            raise ValueError('%s is above %s at %r'%(value, mx, self._path))        
        return value 
add_parser('bounded', BoundedParser)

class ClippedParser(BaseParser):
    def __init__(self, db, prefix):   
        prefix = path_join(prefix)         
        try:
            db.query( (prefix,'min') )
        except KeyError:
            raise ValueError('missing "min" attribute for bounded parameter at %r'%prefix)
        try:
            db.query( (prefix,'max') )
        except:
            raise ValueError('missing "max" attribute for bounded parameter at %r'%prefix)
                    
        BaseParser.__init__(self, db)
            
    def __call__(self, value):
        mn = self._db.query( (self._path, 'min') )
        mx = self._db.query( (self._path, 'max') )             
        if value<mn:
            return mn
        if value>mx:
            return mx
        return value 
add_parser('clipped', ClippedParser)
