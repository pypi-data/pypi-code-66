
class K:
    TYPE = 'type'
    CHILDREN ='_children_'
    VALUE = 'value'
    COMMAND  = 'command'
    ALIASCMD = 'alias_command'
    PROC = 'proc'
    ARGS = 'args'
    
# To be included from somewere else
def path_parse(p):
    if isinstance(p, tuple):
        return ".".join(path_parse(a) for a in p if a)
    if isinstance(p, str):
        return p
    raise ValueError('%r is not a valid path or path fraction')    

def path_join(*obj):
    return ".".join(path_parse(a) for a in obj if a)
    # if isinstance(obj, str):

def path_split(path, root=None):    
    s,_,p = path[::-1].partition('.')
    return  p[::-1], s[::-1]

def path_suffix(path, prefix):
    if prefix:
        return path[len(prefix)+1:]
    else:
        return path
        
def path_prefix(path, suffix):
    if suffix:
        return path[:-len(suffix)-1]
    else:
        return path

def path_join(*obj):
    return ".".join(path_parse(a) for a in obj if a)


class BaseDbImage:
    
    def __init__(self, d):
        self._d = d
    
    def get(self, key, path=''):
        return self._d[path_join(path, key)]           
            
    def set(self, key, value, path=''):
        raise RuntimeError('This is a client image')
    
    def has(self, key, path=''):
        return path_join(path, key) in self._d    
        
class ClientImage:
    
    def __init__(self, dbi, client, path=''):
        self.__dict__['_dbi'] = dbi
        self.__dict__['client'] = client
        self.__dict__['_p'] = path
    
    def _path(self, *a):
        return path_join(self._p, *a)
    
    def get(self, path=''):
        # catch non values before sending to server
        try:
            self._dbi.get(K.VALUE, self._path(path))
        except KeyError:
            raise KeyError('%r'%(path,))
        return self.client.db_getval(self._path(path))
    
    def set(self, *args):
        if len(args)==2:
            path, value = args
        elif len(args)==1:
            value, = args
            path = ''
        else:
            raise ValueError('expecting one or 2 arguments got %d'%len(args)) 
        
        # catch non values before sending to server
        try:
            self._dbi.get(K.VALUE, self._path(path))
        except KeyError:
            raise KeyError('%r'%(path,))
        return self.client.db_setval(self._path(path), value)
    
    def setup(self, values):
        d = {self._path(k):v for k,v in values.items()}
        self.client.db_setup(d)
        
    def query(self, pattern):
        d = self.client.db_query(self._path(pattern))        
        return {path_suffix(k, self._p):v for k,v in d.items()}
    
    def get_dict(self, paths):        
        d = self.client.db_get_dict( [self._path(p) for p in paths] )
        return {path_suffix(k, self._p):v for k,v in d.items()}
    
    def getchild(self, path):
        p = self._path(path)
        try:
            self._dbi.get(K.TYPE, p)
        except KeyError:
            raise KeyError("%r"%path)
        
        return client_image(self._dbi, self.client, p)
    
    
    def children(self, tpe=''):
        children = self._dbi.get(K.CHILDREN, self._p)
        
        
        if not tpe:                
            for c in children:                                
                yield client_image(self._dbi, self.client, self._path(c))
                
        else:
            for c in children:
                p = self._path(c)
                if self._dbi.get(K.TYPE, p) == tpe:
                    yield client_image(self._dbi, self.client, p)            
    
    def child_items(self, tpe=''):
        children = self._dbi.get(K.CHILDREN, self._p)
        
        
        if not tpe:                
            for c in children:                                
                yield c, client_image(self._dbi, self.client, self._path(c))
                
        else:
            for c in children:
                p = self._path(c)
                if self._dbi.get(K.TYPE, p) == tpe:
                    yield c, client_image(self._dbi, self.client, p) 
    
    def child_keys(self, tpe=''):
        children = self._dbi.get(K.CHILDREN, self._p)
        
        
        if not tpe:                
            for c in children:                                                
                yield c
                
        else:
            for c in children:
                p = self._path(c)
                if self._dbi.get(K.TYPE, p) == tpe:
                    yield c 
    
    def __getattr__(self, attr):
        try:
            return self._dbi.get(attr, self._p)
        except KeyError:
            try:
                self._dbi.get(K.TYPE, (self._p, attr))
            except KeyError:
                raise AttributeError("%r"%attr)
            else:
                return self.getchild(attr)
                
    def __setattr__(self, attr, value):   
        raise AttributeError('Cannot set attribute on client Image')

    def __call__(self, **kwargs):
        tpe = self._dbi.get(K.TYPE, self._p)
        root, cmd = path_split(self._p)
        
        if tpe == K.ALIASCMD:
            try:
                alias_kwargs = self._dbi.get(K.ARGS, self._p)
            except KeyError:
                alias_kwargs = {}
            try:
                proc_name = self._dbi.get(K.PROC, self._p)
            except KeyError:
                raise RuntimeError('Command Alias has no process name')
                
            for k,v in alias_kwargs.items():
                kwargs.setdefault(k, v)                                    
                
        elif tpe == K.COMMAND:
                                    
            if not cmd in self._dbi.get(K.CHILDREN, root):
                raise RuntimeError('cannot locate process of command %r'%cmd)
            
            try:
                proc_name = self._dbi.get(K.PROC, root)
            except KeyError:
                _, proc_name = path_split(root)
        else:
            raise RuntimeError('Can only call command, this is a %r'%(tpe,))
        
        r =  self.client.send(proc_name, cmd, kwargs)
        if r['status']:
            raise RuntimeError(r)
        return r['answer']

        
def client_image(dbi,client,path):
    return ClientImage(dbi, client, path)