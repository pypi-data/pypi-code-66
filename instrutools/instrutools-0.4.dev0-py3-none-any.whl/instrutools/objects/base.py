from ..shared import keys as K
from ..database import DataBase
from ..database import path_join
from ..functions.publisher import Info
from ..process.thread import FuncThread, register_thread, unregister_thread

type2class_loockup = {}

_json_serialisable = (int, float, bool, str, bytes, list, tuple, dict, type(None))

def type2class(tpe):
    try:
        cl = type2class_loockup[tpe]
    except KeyError:
        raise ValueError("Bug unknown type %s"%tpe)
    return cl

def add_type_class(tpe, cl):
    type2class_loockup[tpe] = cl

parser_loockup = {}
def add_parser(name, f):
    parser_loockup[name] = f

def get_parser(name):
    return parser_loockup[name]

def read_obj(db, prefix):
    prefix = path_join(prefix)
    try:
        tpe = db.query((prefix, K.TYPE))
    except KeyError:
        try:
            aval = db.query( prefix )
        except KeyError:
            raise KeyError(prefix)
        else:
            return aval
    else:        
        obj = type2class(tpe)(db, prefix)
        return obj

def _arg_parsers(db, prefix):
    prefix = path_join(prefix)
    
    try:
        ptype = db.query( (prefix,'ptype') )
    except KeyError:
        ptype = 'str'
    if isinstance(ptype, str):
        ptype = [ptype]   
     
    return tuple(get_parser(p)(db, prefix) for p in ptype)

def _parse_data(parsers, data):
    for p in parsers:
        data = p(data)
    return data

def parse_arg(db, prefix, data):    
    return _parse_data(_arg_parsers(db, prefix), data)


class _BaseParameter:
    _parsers = tuple()
    _db = None
    _path = None
    _monitor_thread = None
        
    def __init__(self, db, path):
        path = path_join(path)                
        self.__dict__['_db'] = db     
        # set _aprsers to None, it will be filled when using parse for the 
        # first time. It will save object creation time for readonly objects   
        self.__dict__['_parsers'] = None#_arg_parsers(db, path)        
        self.__dict__['_path'] = path 
        
    def __getattr__(self, attr):
                
        pf = self.__dict__['_path']
        
        try:
            return self.__dict__['_db'].query( (pf, attr) )
        except KeyError:
            raise AttributeError('%s is not a valid attribute (not in database) at %r'%(attr, pf))
    
    def __setattr__(self, attr, value):                
        raise AttributeError('%s attribute does not exists or read only at %r'%(attr, self.__dict__['_path']))        
    
    def __eq__(self,right):
        if not isinstance(right, self.__class__): return False
        return self._db is right._db and self._path == right._path
    
    def __hash__(self):
        return hash(self._db)+hash(self._path)
    
    @property
    def client(self):
        """ client handler """
        return getattr(self._db , 'client', None)
    
    def parse(self, value):
        # first time called the _parsers list should be None
        if self._parsers is None:
            self.__dict__['_parsers'] = _arg_parsers(self._db, self._path)         
        return _parse_data(self._parsers, value)
    
    def config(self, __d__=None, **kwargs):
        d = dict(__d__ or {}, **kwargs)
        for key,value in d.items():
            if key in self._protected_config:
                raise ValueError('keyword %r is not configurable'%key)
            if not isinstance(value, _json_serialisable):
                raise ValueError('get a %r object only allowed : %s'%(value, _json_serialisable))
            self._db.set( (self._path, path_join(key)), value)   
        
        # update the parser, they may have changed 
        self.__dict__['_parsers'] = _arg_parsers(self._db, self._path) 
        
    def selfupdate(self): 
        """ The value insisde the database is updated.
        
        Only used if the database is an database image
        """       
        keywords = [(self._path, K.VALUE)]
        self._db.selfupdate(keywords) 
        
    def start_monitoring(self, delay=1.0):
        thread = FuncThread(self.selfupdate, description="monitor- %s"%self._path, delay=delay)
        self.__dict__['_monitor_thread'] = thread
        register_thread(thread)
        thread.start()
        
    def stop_monitoring(self):
        thread = self.__dict__.get('_monitor_thread', None)
        if thread is not None:
            thread.kill()
        unregister_thread(thread)
    
    @property
    def i(self):
        return Info(self)
        
class _DbBaseObject(object):
    _monitor_thread = None
    _authorized_child = {}
    _protected_config = [K.TYPE]
    @classmethod
    def from_config(cl, file):
        db = DataBase.from_config(file)
        return cl(db, '')
    
    @property
    def client(self):
        """ client handler """
        return getattr(self._db , 'client', None)
    
    def update(self, __d__={}, **kwargs):
        db = self.__dict__['_db']
        pf = self.__dict__['_path']
        
        d = dict(__d__, **kwargs)
        for key in d:
            try:
                tpe = db.query( (pf, key, K.TYPE) )
            except:
                raise KeyError('""%s" does not point to valide subsatabase at %r'%(key, pf))
            if tpe != K.PARAMETER:
                raise ValueError("cannot update %r, this is not a parameter but a %s at %r"%(key, tpe, pf))        
    
    def add(self, prefix, obj):        
        prefix = path_join(prefix)
        if hasattr(obj, "__iter__"):
            for child in obj.values():
                self.add(prefix, child)
            return 
        
        if obj._path:
            subdb = self._db.new_subset(obj._path, (self._path, prefix) )
        else:
            subdb = obj._db.flush()
                  
        atype = subdb.query((self._path, prefix, K.TYPE))
        
        try:
            child_list_key = self._authorized_child[atype]
        except KeyError:
            raise ValueError('cannot add a %r inside a %r'%(atype, self.type))                        
        
        if child_list_key:
            try:
                lst = self._db.query(child_list_key)                
            except KeyError:
                self._db.set(child_list_key, [prefix])
            else: 
                if not prefix in lst:
                    lst.append(prefix)                
        
        for key, value in subdb.flush().items():
            if isinstance(value, dict):
                value = value.copy()
            elif isinstance(value, list):
                value = list(value)
            self._db.set(key, value)
    
    def config(self, __d__=None, **kwargs):
        d = dict(__d__ or {}, **kwargs)
        for key,value in d.items():
            if key in self._protected_config:
                raise ValueError('keyword %r is not configurable'%key)
            if not isinstance(value, _json_serialisable):
                raise ValueError('get a %r object only allowed : int, float, complex, str, bytes, list, tuple, dict'%type(value))
            self._db.set( (self._path, path_join(key)), value)    
                
    def selfupdate(self,keys=None):
        self.rparameters.selfupdate(keys)
    
    def start_monitoring(self, delay=1.0):
        thread = FuncThread(self.selfupdate, description="monitor- %s"%self._path, delay=delay)
        self.__dict__['_monitor_thread'] = thread
        register_thread(thread)
        thread.start()
        
    def stop_monitoring(self):
        thread = self.__dict__.get('_monitor_thread', None)
        if thread is not None:
            thread.kill()
        unregister_thread(thread)
    
    def __eq__(self,right):
        if not isinstance(right, self.__class__): return False
        return self._db is right._db and self._path == right._path
    
    def __hash__(self):
        return hash(self._db)+hash(self._path)
        
    def __getitem__(self, item):
        item = path_join(item)                
        
        db = self.__dict__['_db']
        pf = self.__dict__['_path']
        try:
            db.query( (pf, item, K.TYPE) )
        except KeyError:
            raise KeyError('""%s" does not point to valide subsatabase at %r'%(item, pf))
        return read_obj(db, (pf,item))        
        
    def __setitem__(self, item):
        raise KeyError("Cannot set an parameter directly (too ambigous) use update method or o[K].set(val)")
        
    def __getattr__(self, attr):
        try:
            val = super().__getattribute__(attr)
        except AttributeError:
            
            db = self.__dict__['_db']
            pf = self.__dict__['_path']
            
            try:
                db.query( (pf, attr, K.TYPE) )
            except KeyError:
                try:
                    return db.query( (pf, attr) )
                except KeyError:
                    raise AttributeError(attr)
            else:
                return  read_obj(db, (pf,attr))                              
        else:              
            return val
    
    def __setattr__(self, attr, value):
        try:
            super().__getattr__(attr)
        except AttributeError:            
            raise AttributeError('%r attribute does not exists or readonly at %r'(attr, self._path))            
        else:                        
            super().__setattr__(attr, value)          
        
    def __str__(self):
        return str(self._db)
    
    def __str_ascii__(self, p):
        return str(self._db)
        
    @property
    def i(self):
        return Info(self)    

class _BaseObjCollection:
    def __init__(self, db, prefix):
        self._db = db
        self._path = prefix
    
    def __iter__(self):
        for pname in self.keys():
            yield pname
    
    def __setitem__(self, item, val):
        raise TypeError('items are read only')
    
    def items(self):
        for pname in self.keys():
            yield pname, self.__getitem__(pname)
    
    def values(self): 
        for pname in self.keys():
            yield self.__getitem__(pname)  
    
class _ParametersProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Parameters(master._db, master._path)

class _RParametersProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _RParameters(master._db, master._path)
                
class _Parameters(_BaseObjCollection):
    
    @property
    def child_type(self):
        return K.PARAMETER
                            
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.PARAMETERS) ):
            raise KeyError(item)
        return type2class(K.PARAMETER)(self._db, (self._path, item))

    def __setitem__(self, item, val):
        raise TypeError('items are read only')
    
    def keys(self):
        for pname in self._db.query( (self._path, K.PARAMETERS) ):
            yield pname
    
    def selfupdate(self, keys=None):
        if keys is None:
            keys = self
        keywords = [(self._path, k, K.VALUE) for k in keys]
        self._db.selfupdate(keywords)

class _RParameters(_Parameters):  
      
    def __getitem__(self, item):
        try:
            tpe = self._db.query( (self._path, path_join(item), K.TYPE ) )
        except KeyError:
            raise KeyError(item)
        if tpe!=K.PARAMETER:
            raise KeyError(item)                
        return type2class(K.PARAMETER)(self._db, (self._path, item))
    
    def keys(self):
        for pname in _parameter_walk(self._db, self._path, ''):
            yield pname
    
            
def _parameter_walk(db, rprefix, prefix):
    stype = db.query((rprefix, prefix, K.TYPE))
    if stype == K.PARAMETER:
        yield prefix
        
    elif stype == K.DEVICE:
        for pname in  db.query( (rprefix, prefix, K.PARAMETERS) ):
            for r in _parameter_walk(db, rprefix, path_join((prefix, pname))):                
                yield r
    
    elif stype == K.SYSTEM:
        for pname in  db.query( (rprefix, prefix, K.PARAMETERS) ):
            for r in _parameter_walk(db, rprefix, path_join((prefix, pname))):                
                yield r
        
        for pname in  db.query( (rprefix, prefix, K.DEVICES) ):
            for r in _parameter_walk(db, rprefix, path_join((prefix, pname))):                
                yield r               
        
        for pname in  db.query( (prefix, rprefix, K.SUBSYSTEMS) ):
            for r in _parameter_walk(db, rprefix, path_join((prefix, pname))):                
                yield r  
        
                 
            
    
class _DevicesProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Devices(master._db, master._path)
                
class _Devices(_BaseObjCollection):
    
    @property
    def child_type(self):
        return K.DEVICE
        
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.DEVICES) ):
            raise KeyError(item)
        return type2class(K.DEVICE)(self._db, (self._path, item))
        
    def keys(self):
        for pname in self._db.query( (self._path, K.DEVICES) ):
            yield pname
        
        


class _SystemsProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Systems(master._db, master._path)
                                
class _Systems(_BaseObjCollection):
    
    @property
    def child_type(self):
        return K.SYSTEM
        
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.SUBSYSTEMS) ):
            raise KeyError(item)
        return type2class(K.SYSTEM)(self._db, (self._path, item))
        
    def keys(self):
        for pname in self._db.query( (self._path, K.SUBSYSTEMS) ):
            yield pname
        
class _ArgsProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Args(master._db, master._path)

class _Args(_BaseObjCollection):
    
    @property
    def child_type(self):
        return K.ARG
        
    def __len__(self):
        return len(self._db.query( (self._path, K.ARGS) ))
    
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.ARGS) ):
            raise KeyError(item)
        return type2class(K.ARG)(self._db, (self._path, item))        
    
    def keys(self):
        for pname in self._db.query( (self._path, K.ARGS) ):
            yield pname
    


class _RepliesProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Replies(master._db, master._path)

class _Replies(_BaseObjCollection):
    @property
    def child_type(self):
        return K.REPLY     
    
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.REPLIES) ):
            raise KeyError(item)
        return type2class(K.REPLY)(self._db, (self._path, item))
    
    def keys(self):
        for pname in self._db.query( (self._path, K.REPLIES) ):
            yield pname                

class _KeywordsProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Keywords(master._db, master._path)

class _Keywords(_BaseObjCollection):    
    @property
    def child_type(self):
        return K.KEYWORD
            
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.KEYWORDS) ):
            raise KeyError(item)
        return type2class(K.KEYWORD)(self._db, (self._path, item))
            
    def keys(self):
        for pname in self._db.query( (self._path, K.KEYWORDS) ):
            yield pname
    
    
                    


class _CommandsProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Commands(master._db, master._path)
            
                                
class _Commands(_BaseObjCollection):    
    @property
    def child_type(self):
        return K.COMMAND
        
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.COMMANDS) ):
            raise KeyError(item)
        return type2class(K.COMMAND)(self._db, (self._path, item))
            
    def keys(self):
        for pname in self._db.query( (self._path, K.COMMANDS) ):
            yield pname    


class _ProcessesProperty:
    def __get__(self, master, cls=None):
        if master is None: 
            return self
        return _Processes(master._db, master._path)
            
                                
class _Processes(_BaseObjCollection):     
    @property
    def child_type(self):
        return K.ARG
               
    def __iter__(self):
        for pname in self._db.query( (self._path, K.PROCESSES) ):
            yield pname
    
    def __getitem__(self, item):
        if item not in self._db.query( (self._path, K.PROCESSES) ):
            raise KeyError(item)
        return type2class(K.PROCESS)(self._db, (self._path, item))
    
    def keys(self):
        for pname in self._db.query( (self._path, K.PROCESSES) ):
            yield pname                
