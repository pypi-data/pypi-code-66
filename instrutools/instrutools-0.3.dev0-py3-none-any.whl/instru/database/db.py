from . import config_parser as cp
from .base import path_join

def _dictionary_subset(d, prefix, newprefix):
    od = {}
    for key, value in d.items():
        if key.startswith(prefix):
            _,_,suffix = key.partition(prefix)
            od[path_join((newprefix,suffix.strip('.')))] = value
    return od

class EMPTY:
    pass

class DataBase:
    def __init__(self, d):
        self._d = d
    
    def query(self, key):        
        return self._d[path_join(key)]
    
    def queries(self, key_list):
        """ return a key/value pair inside a dictionary from a list of keys"""
        return {path_join(key):self._d[path_join(key)] for key in key_list}
    
    def selfupdate(self, key_list=None, uri=None):
        """ selfupdate is used only if the data base is a mirror of a remote database 
        
        The keys in the given key_list will be updated 
        """
        pass 
    
    def set(self, key, value):
        self._d[path_join(key)] = value 
    
    def update(self, __d__={}, **kwargs):
        self._d.update(__d__, **kwargs)
    
    def new_subset(self, prefix, newprefix=''):
        prefix = path_join(prefix)
        newprefix = path_join(newprefix)
        
        if not prefix:
            return DataBase(self._d)
        return DataBase(_dictionary_subset(self._d, prefix, newprefix))
    
    def flush(self):
        return self._d
    
    def __str__(self):
        # TODO: str of DataBase object        
        return "\n".join( "%-50s: %s"%(key, item) for key, item in self._d.items())
    
    @classmethod
    def from_config(cl, d):
        _db = {}
        cp.read_file(d, _db)
        return cl(_db)
