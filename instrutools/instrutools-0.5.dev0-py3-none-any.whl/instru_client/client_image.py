from glob import fnmatch
from instru_server.database.path import DbPath
from instru_server.database.db import DbHandler, K

class EMPTY:
    pass

class BaseDbImageInterface:    
    def __init__(self, d, client):
        self.data = d
        self.client = client 
        
        self.monitored = set()
        self.last_update = {}
        
        self.dbp = DbPath()
        
    def get(self, key):
        return self.data[key]           
            
    def set(self, key, value):
        raise RuntimeError('This is a client image, set is not allowed')
    
    def has(self, key):
        return key in self.data
    
    def keys(self):
        return self.data.keys()
    
    def monitor(self, key):        
        # let it raise a keyError
        self.data[self.dbp.join(key, K.TYPE)]    
            
        self.last_update.setdefault(key, None)
    
    def ismonitored(self, key):                            
        return key in self.last_update
    
    def send(self, cmd, *args):
        return self.client.send(cmd,*args)
    
    def update(self):
        client = self.client
        r = client.send('get', list(self.last_update) )
        if r['status']:
            raise RuntimeError(r)
        self.last_update.update(r['answer'])    
        
    def selfupdate(self, node):
        client = self.client
        r =  client.send('dump', node)  
        if r['status']:
            raise RuntimeError(r)
        self.data.update(r['answer'])    
        


class ClientDbImage(DbHandler):    
    def __init__(self, dbi, path='', io=None):        
        super(ClientDbImage, self).__init__(dbi, path, io)      
               
    def childConstructor(self, path=None):
        """return a class or constructor function for children default is self.__class__"""
        return self.__class__
    
    def master(self):
        return self.childConstructor('')(self.__dbi__, '', self.__io__)
    
    def get_child(self, path):
        path = self._parse_path(path)
                       
        try:
            self.__dbi__.get(self._new_path(path,K.TYPE))
        except KeyError:
            raise KeyError("%r"%path)            
        return self.childConstructor(path)(self.__dbi__, self._new_path(path), self.__io__)
        
    def monitor(self, *args):
        for key in args:
            self.__dbi__.monitor(self._new_path(key))
    
    def ismonitored(self, path):
        return self.__dbi__.ismonitored( self._new_path(path) )
    
    def update(self):
        self.__dbi__.update()
    
    def last_update(self):
        dbp = self.__dbi__.dbp
        return {dbp.suffix(k, self.__path__):v for k,v in self.__dbi__.last_update.items() if dbp.isroot(k, self.__path__)}
    
        
    def __getitem__(self,key):
        key = self._parse_path(key)
        try:
            return self.__dbi__.last_update[self._new_path(key)]
        except KeyError:
            raise KeyError('%r is not a monitored value')
                    
    def get_value(self, path='', default=EMPTY):
        # catch non values before sending to server  
        path = self._parse_path(path)
        fullpath = self._new_path(path)      
        
        r = self.__dbi__.send('get', fullpath)    
        if r['status']:
            raise RuntimeError(r)
            
        return self.__io__.decoded(self.__dbi__, fullpath, r['answer'])
        
    get = get_value # get is an alias of get_value
    
                       
    def set_value(self, *args):
        if len(args)==2:
            path, value = args
        elif len(args)==1:
            value, = args
            path = ''
        else:
            raise ValueError('expecting one or 2 arguments got %d'%len(args)) 
        path = self._parse_path(path)
        
        fullpath = self._new_path(path) 
        # catch non values before sending to server
        
        r = self.__dbi__.send('set', fullpath, value)
        if r['status']:
            raise RuntimeError(r)
        return r['answer'] 
           
    set = set_value
    
    def get_values(self, nodes):
        
        r = self.__dbi__.send('rget', self.__path__, *nodes)
        if r['status']:
            raise RuntimeError(r)
        return r['answer']
        
        #return {path_suffix(k,self.__path__):v for k,v in  r['answer'].items()}
    
    def setup(self, values):
        args = sum(values.items(), tuple())
        r = self.__dbi__.send('rset', self.__path__, *args)
        if r['status']:
            raise RuntimeError(r)
        return r['answer']
    
            
    def send(self, cmd, *args):
        return self.__dbi__.client.send(cmd, *args)
    
    def __setattr__(self, attr, value):   
        raise AttributeError('Cannot set attribute on client Image')
    
    def __repr__(self):
        return f"""<{self.__class__.__module__}.{self.__class__.__name__} @{self.__path__!r} type={self.type} >"""
    
    def call(self, *args):
        path_split = self.__dbi__.dbp.split
        tpe = self.__dbi__.get(self._new_path(K.TYPE))
        root, method = path_split(self.__path__)
        
        if tpe != K.METHOD:
            raise RuntimeError('Can only call method, this is a %r'%(tpe,))
        
        return   self.__dbi__.client.send('call', root, method, *args)
    
    def rcall(self, *args):
        r = self.call(*args)
        if r['status']:
            raise RuntimeError(r)
        return r['answer']    
        
    def __call__(self, *args):
        return self.rcall(*args)
        