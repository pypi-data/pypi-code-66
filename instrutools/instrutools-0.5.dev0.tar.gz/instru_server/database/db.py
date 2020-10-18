from . import config_parser as cp
from .. import keys as K
from .base import DictDataBaseInterface, db_parsers, db_encoders, db_decoders
from glob import fnmatch
from ..functions.publisher import ASCII, publish

class EMPTY:
    pass

class ValIO:
    def __init__(self):
        self.parsers = db_parsers.copy()
        self.encoders = db_encoders.copy()
        self.decoders = db_decoders.copy()
    
    def parse(self, dbi, path, value):
        
        try:
            vtypes = dbi.get( dbi.dbp.join(path,K.VTYPE) )
        except KeyError:
            return value
                    
        if vtypes is None:
            return value
        
        for vtype in vtypes:            
            try:
                parser = self.parsers[vtype]
            except KeyError:
                raise ValueError("Unknown parser {0!r} at {1}".format(vtype, path))
            
            value = parser(dbi, path, value)
        return value 
    
    def encoded(self, dbi, path, data):
        try:
            enc = dbi.get( dbi.dbp.join(path,K.VENCODER) )
        except (KeyError, AttributeError):
            return data
        
        try:
            encoder = self.encoders[enc]
        except (KeyError, AttributeError):
            raise ValueError("Unknown encoder {0!r} at {1}".format(enc, path))        
        return encoder(dbi, path, data)
    
    def decoded(self, dbi, path, data):
        if data is None:
            return None
        
        try:
            dec = dbi.get( dbi.dbp.join(path,K.VDECODER) )
        except (KeyError, AttributeError):
            return data
        
        try:
            decoder = self.decoders[dec]
        except KeyError:
            raise ValueError("Unknown decoder {0!r} at {1}".format(dec, path))        
        return decoder(dbi, path, data)

    
class DbHandler:
    __dbi__  = None
    __path__ = None
    
    def __init__(self, dbi=None, path=None, io=None):
        if dbi is None:
            dbi = DictDataBaseInterface()        
        self.__dict__['__dbi__'] = dbi
        self.__dict__['__path__'] = path or dbi.dbp.root
        self.__dict__['__io__'] = ValIO() if io is None else io
            
    def __iter__(self):
        children = self.__dbi__.get( self._new_path(K.CHILDREN) )                                      
        for c in children:                                
            yield self.childConstructor(c)(self.__dbi__, self._new_path(c))        
            
    def _new_path(self, *args):
        return self.__dbi__.dbp.join(self.__path__, *args)
        
    def _parse_path(self, p):
        return self.__dbi__.dbp.parse(p)
    
    @property
    def path(self):
        return self.__path__
    
    def childConstructor(self, path=None):
        """return a class or constructor function for children default is self.__class__"""
        return self.__class__
    
    def get_child(self, path):
        path = self._parse_path(path)        
        try:
            self.__dbi__.get( self._new_path(path, K.TYPE) )
        except KeyError:
            raise KeyError("%r"%path)            
        return self.childConstructor(path)(self.__dbi__, self._new_path(path), self.__io__)
    
    def master(self):
        return self.childConstructor('')(self.__dbi__, None, self.__io__)
    
    @property
    def attributes(self):
        return AttributeIterator(self)
    
    @property
    def children(self):        
        return ChildIterator(self)
    
    def flatdict(self, path=''):
        path = self._parse_path(path)
        return self.__dbi__.flatdict(self._new_path(path))
            
    def setup(self, __d__={}, **kwargs):
        for k,v in dict(__d__, **kwargs).items():
            self.set_value(k,v)
        
    def getattr(self, path, default=EMPTY):
        path = self._parse_path(path)
                
        try:            
            return self.__dbi__.get( self._new_path(path) )
        except KeyError:            
            if default is EMPTY:                
                raise KeyError("%r"%path)
            else:
                return default   
    
    def setattr(self, path, value):
        path = self._parse_path(path)        
        # should raise keyerror if path does not exists            
        self.__dbi__.get(self._new_path(path))        
        self.__dbi__.set(self._new_path(path), value) 
    
    def hasattr(self, path):
        path = self._parse_path(path)
        try:
            self.__dbi__.get(self._new_path(path))  
        except KeyError:
            return False
        else:
            return True 
              
    def haschild(self, path):
        path = self._parse_path(path)
        
        try:
            self.__dbi__.get(self._new_path(K.TYPE))  
        except KeyError:
            return False
        else:
            return True
      
    
      
    def get_value(self, key='', default=EMPTY): 
        key = self._parse_path(key)
                              
        try:            
            data = self.__dbi__.get( self._new_path(key, K.VALUE) )
        except KeyError:            
            if default is EMPTY:                
                raise KeyError("%r"%key)
            else:
                data = default
        
        return self.__io__.decoded(self.__dbi__, self._new_path(key), data)
        
    def get_values(self, path_list, default=EMPTY):
        return {k:self.get_value(k, default=default) for k in path_list}
    
    def set_value(self, *args):
        if len(args)==2:
            key, value = args
        elif len(args)==1:
            value, = args
            key = ''
        else:
            raise ValueError('expecting one or 2 arguments got %d'%len(args)) 
        key = self._parse_path(key)
        
        
        # this should raise KeyError
        self.__dbi__.get( self._new_path(key, K.VALUE) )
        
        p = self._new_path(key)
        value = self.__io__.parse(self.__dbi__, p, value)
        data = self.__io__.encoded(self.__dbi__, p, value)        
        try:
            self.__dbi__.set( self._new_path(key,K.VALUE), data )
            
        except KeyError:
            raise KeyError("%r"%key)
    
    def parseval(self, value):
        return self.__io__.parse(self.__dbi__, self.__path__, value)        
    
    def query(self, pattern="*", flt=None, attr=K.TYPE):
            
        if pattern is None:
            # simple list of children 
            keys = self.__dbi__.get(self._new_path(K.CHILDREN))            
        
        elif hasattr(pattern, "__call__"): 
            isr = self.__dbi__.dbp.isroot  
            ise = self.__dbi__.dbp.isendding
            sfx = self.__dbi__.dbp.suffix
            pfx = self.__dbi__.dbp.prefix
            
            keys = list(filter( pattern, (pfx(sfx(k,self.__path__), attr) for k in self.__dbi__.keys() if isr(k, self.__path__) and ise(k, attr))))
        
        elif isinstance(pattern, str):
            pattern = self._new_path(pattern, attr)
            globflt = lambda k: fnmatch.fnmatch(k, pattern)
            
            sfx = self.__dbi__.dbp.suffix
            pfx = self.__dbi__.dbp.prefix
            
            keys = [pfx(sfx(k ,self.__path__), attr) for k in  filter(globflt, self.__dbi__.keys())]
            # keypairs = [(k,path_to_str(k)) for k in self.__dbi__.keys()]
            # 
            # keys =  [path_prefix(path_suffix(k , self.__path__), attr) for k, ks in keypairs if globflt(ks)]       
            #keys = [ path_prefix(path_suffix(k ,self.__path__), attr) for k in  filter(globflt, strkeys)]
                    
        else:
            keys = list(pattern)                                    
        if flt:
            keys = [k for k in keys if  flt(self.get_child(k))]        
        return self.get_values(keys)
        
    
    def __getattr__(self, attr):        
        try:
            return self.getattr(attr)
        except KeyError:
            try:
                return self.get_child(attr)
            except KeyError:
                raise AttributeError('%r'%attr)                        
            
    def __setattr__(self, attr, value):                
        try:
            self.setattr(attr, value)            
        except KeyError:
            raise AttributeError("%r"%attr)                
    
    def __getitem__(self, item):
        return self.get_value(item)
    
    def __setitem__(self, item, value):
        self.set_value(item, value)
    
    def __dir__(self):
        s = set()
        for cls in self.__class__.__mro__:
            s.update( k for k in cls.__dict__ if not k.startswith('_') )
        
        s.update(self.__dbi__.get(self._new_path(K.ATTRIBUTES)))
        s.update(self.__dbi__.get(self._new_path(K.CHILDREN)))
        return s
    
    
                                                             
    def __repr__(self):
        return f"""<{self.__class__.__module__}.{self.__class__.__name__} @{self.__path__!r} type={self.type} value={self.value} >"""
    
    def __eq__(self, right):
        return (self.__dbi__ == right.__dbi__)  and  (self.__path__ == right.__path__)
    
    
    def show(self):
        print(publish(self, ASCII()))
    
    def __str_ascii__(self, p):
                        
        tab = " "*len(self.__path__)                
        txt = [p.write_margin(self.__path__)]
                        
        pp = p.child(tab_str=tab, level=1)        
        
        
        for name, param in self.attributes().items():
            txt.append(pp.write_margin(name))
            txt.append(publish(param, pp)) 
        
        #for name, child in self.children().items():
                    
        #txt.append(".%s"%name+publish(child, pp)) 
        
        return "\n".join(txt)
    
class DB(DbHandler):
    
    def load_dict(self, d,  path='', templates=None):        
        cp.read_obj(d, self.__dbi__, root=self.__path__, suffix=path)
                         
    def load_yaml_str(self, s, path='', templates=None):        
        #cp.read_str(s, self.__dbi__, root=self._new_path(path))
        cp.read_str(s, self.__dbi__, root=self.__path__, suffix=path)
                     
    def load_yaml_file(self, f, path='', templates=None):        
        cp.read_file(f, self.__dbi__, root=self.__path__, suffix=path)    
    
    def merge(self, db, path=''):
        if isinstance(db, DictDataBaseInterface):
            self.__dbi__.merge(db, path)
        else:    
            self.__dbi__.merge(db.__dbi__, path)
    
    def add_template(self, name, tpl):
        self.__dbi__.add_template(name, tpl)
    
    @property
    def _wr(self):
        """ database write access object 
        
        The returned object allow to edit the data base structure by adding 
        new children or attributes.
        """
        return DBW(self.__dbi__, self.__path__)
    
    @classmethod
    def from_yaml_file(cl, f, prefix='', templates=None):
        __dbi__ = DictDataBaseInterface({}, templates=templates)
        cp.read_file(f, __dbi__)  
        return cl(__dbi__, prefix)
        
    @classmethod
    def from_yaml_str(cl, s, prefix='', templates=None):                
        __dbi__ = DictDataBaseInterface({}, templates=templates)
        cp.read_str(s, __dbi__)  
        return cl(__dbi__, prefix)
    
    @classmethod
    def from_dict(cl, d, prefix='', templates=None):
        __dbi__ = DictDataBaseInterface({}, templates=templates)
        cp.read_obj(d, __dbi__)
        return cl(__dbi__, prefix)
    
        
def new_db(tpe, value=None, description='',  **kwargs):
    kwargs[K.TYPE] = tpe
    kwargs[K.VALUE] = value
    kwargs[K.DESCRIPTION] = description
    
    dbi = DictDataBaseInterface()    
    cp.read_obj(kwargs, dbi)
    
    return DB(dbi, '')

    
db_handler_loockup = {}
def db_handler(db, prefix='', tpe=None):
    if not tpe:        
        tpe = db.get(K.TYPE, prefix)
    try:
        Handler = db_handler_loockup[tpe]
    except KeyError:
        Handler = DB
    return Handler(db, prefix)
    
#db_handler_loockup[K.VAR] = VariableHandler

class AttributeIterator:
    def __init__(self, root):
        self.root =root
        
    
    def __iter__(self):
        return self.keys()
    
    def keys(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.ATTRIBUTES))
        for k in l : yield k
    
    def items(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.ATTRIBUTES))
        for k in l : 
            yield k, root.getattr(k)
    
    def values(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.ATTRIBUTES))
        for k in l : 
            yield root.getattr(k)            
    
    def __getitem__(self, key):
        return self.root.getattr(key)        
        
class ChildIterator:
    def __init__(self, root):
        self.root = root        
    
    def __iter__(self):
        return self.keys()
    
    def keys(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l : yield k
    
    def items(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l: 
            yield k, root.get_child(k)
    
    def values(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l : 
            yield root.get_child(k)
    
    def __getitem__(self, key):
        # should raise KeyError if not a child
        return self.root.get_child(key)
            

class FilteredChildIterator:
    def __init__(self, root, filter):
        self.root = root
        self.filter = filter
    
    def __iter__(self):
        return self.keys()
    
    def keys(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l :
            c = root.get_child(k)
            if self.filter(c):
                yield k
                
    def items(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l: 
            c = root.get_child(k)
            if self.filter(c):
                yield k, c   
    
    def values(self):
        root = self.root
        l = root.__dbi__.get(root._new_path(K.CHILDREN))
        for k in l:
            c = root.get_child(k)
            if self.filter(c):
                yield c  
                
    def __getitem__(self, key):
        # should raise KeyError if not a child
        return self.root.get_child(key)


class DBW:
    __dbi__ = None
    __path__ = ''
    def __init__(self, dbi, path=''):
        self.__dict__['__dbi__'] = dbi
        self.__dict__['__path__'] = path
    
    def __setattr__(self, attr, obj):
        if hasattr(obj, "flatdict"):
            self.__dbi__.merge(obj, self.__dbi__.dbp.join(self.__path__, attr))
        else:        
            cp.read_obj(obj, self.__dbi__, root=self.__path__, suffix=attr)        
    
    def __getattr__(self, attr):
        try:
            self.__dbi__.get(self.__dbi__.dbp.join(self.__path__, attr, K.TYPE))
        except KeyError:
            raise AttributeError('Db writer does not have attribute read access')
        return self.__class__(self.__dbi__, self.__dbi__.dbp.join(self.__path__,attr))
        
    def __call__(self, **kwargs):
        for k,v in kwargs.items():
            cp.read_obj(v, self.__dbi__, root=self.__path__, suffix=k) 
    
    def __repr__(self):
        return f"""<{self.__class__.__module__}.{self.__class__.__name__} @{self.__path__!r}"""
    