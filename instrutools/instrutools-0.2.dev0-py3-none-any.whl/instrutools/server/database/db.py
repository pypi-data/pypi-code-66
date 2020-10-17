from . import config_parser as cp
from ...shared import keys as K
from .base import path_join, path_isroot, path_suffix, path_prefix
from .vtypes import db_parsers
from glob import fnmatch

def _dictionary_subset(d, prefix, newprefix):
    od = {}
    for key, value in d.items():
        if key.startswith(prefix):
            _,_,suffix = key.partition(prefix)
            od[path_join((newprefix,suffix.strip('.')))] = value
    return od

class EMPTY:
    pass


def db_init_var(db, p):
    try:
        children = db._get(K.CHILDREN, p)
    except KeyError:
        pass
    else:
        for l in children.values():
            for c in l:
                db_init_var(db, path_join(p,c))
    
    try:
        sd = db._get(K.INIT, p)
    except KeyError:
        pass
    else:
        for k,v in sd.items():
            db_set_value(db, path_join(p,k), v)
    
def db_set_value(db, p, value):
                    
    try:
        tpe = db._get(K.TYPE, p)
    except KeyError:
        raise KeyError("%r"%p)
    
    if tpe != K.VAR:
        raise KeyError("%r does not point to an edditable variable")
    
    try:
        parsers = db._get(K.VTYPE, p)
    except KeyError:
        pass
    else:
        for prs in parsers:
            value = db_parsers[prs](db, p, value)        
    db._set(K.VALUE, value, p)
                                    
    
class BaseDataBase:
        
    def __init__(self, _d):
        self._d = _d
        db_init_var(self, '')
        
    def _get(self, key, path=''):           
        try:
            return self._d[path_join(path, key)]    
        except KeyError:                
            raise KeyError('%r'%path_join(path, key))
        
    def _set(self, key, value, path=''):
        # can only set existing keyword in the structure 
        try:
            self._d[path_join(path, key)]
        except KeyError:
            raise KeyError(path_join(path, key)) 
        else:
            self._d[path_join(path, key)] = value    
    
    def query(self, key, pattern):
        d = {}                     
        for k in fnmatch.filter(self._d , path_join(pattern, key)):
            d[path_prefix(k, key)] = self._d[k]            
        return d
        
    def todict(self, path=None):
        if not path:
            return self._d.copy()
        
        d = {}
        
        for k,v in self._d.items():
            if path_isroot(k, path):
                sp = path_suffix(path)
                d[sp] = v
        return d
    
    def load_from_yaml_file(self, p, f):
        _d = {}
        cp.read_file(f, _d)
        for k,v in _d.items():
            self._d[path_join(p,k)] = v
        
    def load_from_yaml_str(self, p, s):
        _d = {}
        cp.read_str(s, _d)
        for k,v in _d.items():
            self._d[path_join(p,k)] = v
    
    def load_from_dict(self, p, d):
        _d = {}
        cp.read_dict(d, _d)
        for k,v in _d.items():
            self._d[path_join(p,k)] = v
    
    @classmethod
    def from_yaml_file(cl, f):
        _d = {}
        cp.read_file(f, _d)
        return cl(_d)
    
    @classmethod
    def from_yaml_str(cl, s):
        _d = {}
        cp.read_str(s, _d)
        return cl(_d)
    
    @classmethod
    def from_dict(cl, d):
        _d = {}
        cp.read_dict(d, _d)
        return cl(_d)

DataBase = BaseDataBase   
    
class DbHandler:
    _db = None
    _p = ''
    def __init__(self, db, prefix=''):
        self.__dict__['_db'] = db
        self.__dict__['_p'] = prefix
        
    def _path(self, *args):
        return path_join(self._p, *args)
    
    def todict(self):
        return self._db.todict(self._p)
    
    def get(self, key, default=EMPTY):
        
        p = self._path(key)
        
        try:            
            return self._db._get(K.VALUE, p)
        except KeyError:
            if self._db._get(K.TYPE, p) != K.VAR:
                raise KeyError("%r does not point to a variable")
            if default is EMPTY:
                raise KeyError("%r"%key)
                
    def set(self, key, value):
        p = self._path(key)
        try:
            db_set_value(self._db, p, value)
        except KeyError:
            raise KeyError("%r"%key)
            
    def get_child(self, path):
        p = self._path(path)
        try:
            self._db._get(K.TYPE, p)
        except KeyError:
            raise KeyError("%r"%path)
        
        return db_handler(self._db, p)
    
    
    def children(self, tpe=''):
        children = self._db._get(K.CHILDREN, self._p)
        if not tpe:                
            for tpe, l in children.items():
                for p in l:
                    yield db_handler(self._db, self._path(p), tpe)
        else:
            try:
                l = children[tpe]
            except KeyError:
                return 
            for p in l:
                yield db_handler(self._db, self._path(p), tpe)
    
    def child_items(self, tpe=''):
        children = self._db._get(K.CHILDREN, self._p)
        if not tpe:                
            for tpe, l in children.items():
                for p in l:
                    yield p, db_handler(self._db, self._path(p), tpe)
        else:
            try:
                l = children[tpe]
            except KeyError:
                return 
            for p in l:
                yield p, db_handler(self._db, self._path(p), tpe)
    
    def child_keys(self, tpe=''):
        children = self._db._get(K.CHILDREN, self._p)
        if not tpe:                
            for l in children.values():
                for p in l:
                    yield p
        else:
            try:
                l = children[tpe]
            except KeyError:
                return 
            for p in l:
                yield p
    
    def query(self, pattern, attr=K.VALUE):
        return {path_suffix(k,self._p):v for k,v in self._db.query(attr, path_join(self._p, pattern)).items()}
        
    def __getattr__(self, attr):
        try:
            return self._db._get(attr, self._p)
        except KeyError:
            raise AttributeError("%r"%attr)        
        
    def __setattr__(self, attr, value):
        
        try:
            self._db._get(attr, self._p)
        except KeyError:
            raise AttributeError("%r"%attr) 
        self._db._set(attr, value, self._p)        
    
    def __getitem__(self, item):
        return self.get(item)
    
    def __setitem__(self, item, value):
        self.set(item, value)
    
    @classmethod
    def from_yaml_file(cl, f, prefix=''):
        _d = {}
        cp.read_file(f, _d)
        
        return cl(BaseDataBase(_d), prefix)
        
    @classmethod
    def from_yaml_str(cl, s, prefix=''):
        _d = {}
        cp.read_str(s, _d)
        return cl(BaseDataBase(_d), prefix)
    
    @classmethod
    def from_dict(cl, d, prefix=''):
        _d = {}
        cp.read_dict(d, _d)
        return cl(BaseDataBase(_d), prefix)        
    
    def new_from_dict(self, name, d):
        self._db.load_from_dict( self._path(name), d)
    
    def new_from_yaml_str(self, name, s):
        self._db.load_from_yaml_str( self._path(name), s)
    
    def new_from_yaml_file(self, name, f):
        self._db.load_from_yaml_file( self._path(name), f)
    

class VariableHandler(DbHandler):
    def new_from_dict(self, name, d):
        raise RuntimeError("Vairable has no child")
    
    def new_from_yaml_str(self, name, s):
        raise RuntimeError("Vairable has no child")
        
    def new_from_yaml_file(self, name, f):
        raise RuntimeError("Vairable has no child")
    
    def get(self):        
        return self._db._get(K.VALUE, self._p)
    
    def set(self, value):
        db_set_value(self._db, self._p, value)        
    
    def get_child(self, p):
        raise RuntimeError("Variable has no child")
    
    def children(self, p):
        raise RuntimeError("Variable has no child")
    
    def child_keys(self, p):
        raise RuntimeError("Variable has no child")
    
    def child_items(self, p):
        raise RuntimeError("Variable has no child")
    
    def setup(self, d=None):
        if d:
            raise ValueError("Variable can't be setup")

    
db_handler_loockup = {}
def db_handler(db, prefix='', tpe=None):
    if not tpe:        
        tpe = db._get(K.TYPE, prefix)
    try:
        Handler = db_handler_loockup[tpe]
    except KeyError:
        Handler = DbHandler
    return Handler(db, prefix)
    

db_handler_loockup[K.VAR] = VariableHandler
    



    