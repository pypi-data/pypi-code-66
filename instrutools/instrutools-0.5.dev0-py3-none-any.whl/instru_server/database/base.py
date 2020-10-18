import os
from .. import keys as K
from glob import fnmatch
import copy
from .path import DbPath
from ..functions.io import  load_config_file


db_parsers = {}
def add_db_parser(name, f):
    if not hasattr(f, "__call__"):
        raise ValueError("expecting a callable as second argument")
    db_parsers[name] = f

db_encoders = {}
def add_db_encoder(name, f):
    if not hasattr(f, "__call__"):
        raise ValueError("expecting a callable as second argument")
    db_encoders[name] = f

db_decoders = {}
def add_db_decoder(name, f):
    if not hasattr(f, "__call__"):
        raise ValueError("expecting a callable as second argument")
    db_decoders[name] = f

    
global_templates = {}
def add_global_template(name, tpl):
    if not hasattr(tpl, "flatdict"):
        raise ValueError("expecting a database object got a %r"%type(tpl))
    global_templates[name] = DictDataBaseInterface(tpl.flatdict())

def stt(val):
    """ string to tuple parser """    
    if isinstance(val, str):
        return tuple(s.strip() for s in val.split(","))    
    return val 


class DictDataBaseInterface: 
    """ this is a simple database interface 
    
    The so called database is actually stored in a python dictionary. 
    Interface is never exposed to the user.    
    """    
    _empty = {K.TYPE:str, K.DESCRIPTION:str, K.VALUE:lambda:None, K.CHILDREN:list, K.ATTRIBUTES:list}    
    _attr_parsers = {K.VTYPE:stt}
    
    def __init__(self, _d=None, templates=None):
        
        self.data = {} if _d is None else _d        
        self.dbp = DbPath()
        
        
        if templates:
            self._templates = {name:DictDataBaseInterface(tpl.flatdict()) for name, tpl in templates.items()}
        else:
            self._templates = {}        
        ##
        # make all the necessary defaults
        self.new_child('')
        
        
    
    def new_child(self, path):
        parent, child = self.dbp.split(path)
        
        while parent:
            self.new_child(parent)            
            parent, child = self.dbp.split(parent)
                        
        for k,c in self._empty.items():                    
            self.setdefault( self.dbp.join(path, k), c())
        # add this point path must be a scalar path
        parent, child = self.dbp.split(path)
                
        pcl = self.setdefault(self.dbp.join(parent, K.CHILDREN), [])
        if child:            
            if child not in pcl:
                pcl.append(child)                    
        
    def add_obj(self, path, obj, asdefault=False):
        """ add a new object to the dbi 
        
        the object is a child if it is a dictionary 
        with keyword (aka 'attribute' in the db word) 
            type, include or template
            
        if `asdefault` is True, all data attributes are not overwriten if already exists
        """
        if self.is_child(obj):
            # create the new child if necessary
            #self.new_child(path, root)
                        
            isTemplate = obj.get(K.ISTEMPLATE, False)
            if isTemplate and path:
                _, name = self.dbp.split(path)                
                self.add_template(name, obj)
                return 
            
            for ckey, cobj in obj.items():
                self.add_obj(self.dbp.join(path,ckey), cobj, asdefault=asdefault)
            
            try:
                tpl_name = obj[K.TEMPLATE]
            except KeyError:
                pass
            else:
                if tpl_name:
                    self.load_template(tpl_name, path)
            
            try:
                inc_name = obj[K.INCLUDE]
            except KeyError:
                pass
            else:
                if inc_name:
                    self.add_obj(path, load_config_file(inc_name), asdefault=True)                                
                        
            self.new_child(path)
            
        else: # this is an attribute
            if asdefault:
                self.setdefault(path, obj)
            else:
                self.set(path, obj)    
            
    def load_template(self, template_name, path):
        try:
            tpl = self.get_template(template_name)
        except KeyError:
            raise ValueError('template %r is unknown at %r'%(template_name, path))
            
        for key, value in tpl.flatdict().items():
            if key is K.ISTEMPLATE: continue            
            self.setdefault( self.dbp.join(path, key), value )
                
        
    def is_child(self, obj):
        """ check is an object can be considered as a child or attribute
        
        
        return True if the object has a dictionary 
        with keyword 
            'type', 'include' or 'template'
        """
        if isinstance(obj, dict):
            return K.TYPE in obj or K.INCLUDE in obj or K.TEMPLATE in obj
        return False    
                        
    def get(self, key):
        return self.data[key]           
            
    def set(self, path, value):
        
        # check if the attribute value needs
        # to be parsed
        
        try:
            self.data[self.dbp.join(path,K.TYPE)]
        except KeyError:
            pass
        else:
            raise KeyError('cannot set attribute, %r is already a child'%path)
                
        parent, attr = self.dbp.split(path)
        
        # if attr==K.INIT:
        #     # special case of the init keyword, a dictionary 
        #     # is expected with key/value pair (key without the .value attribute)
        #     for k,v in value.items():
        #         self.set(self.dbp.join(parent,k,K.VALUE), v)
        #     return 
        
        try:
            prs = self._attr_parsers[attr]
        except KeyError:
            pass
        else:
            value = prs(value)
                                
        self.data[path] = value
        attrlist = self.data.setdefault(self.dbp.join(parent, K.ATTRIBUTES), [])
        if not attr in attrlist:
            attrlist.append(attr)     
        
    def get_template(self, name):
        try:
            return self._templates[name]
        except KeyError:
            return global_templates[name]
    
    def add_template(self, name, tpl):
        if not hasattr(tpl, "flatdict"):
            dbtpl = DictDataBaseInterface()
            dbtpl.add_obj('', tpl)
        else:
            dbtpl = tpl
        self._templates[name] = dbtpl        
        
    
    def setdefault(self, key, value):
        try:
            return self.data[key]
        except KeyError:
            self.set(key, value)
        return self.data[key]#value    
    
    def has(self, key):
        return key in self.data
        
    def filter(self, flt):
        return {k:v for k,v in self.data.items() if flt(k,v)}
    
    def keys(self):
        return self.data.keys()
        
    def flatdict(self, path=None):
        """ Return a dictionary key/value representation of the data base """
        if not path:
            return copy.deepcopy(self.data)
            
        d = {}        
        for k,v in self.data.items():
            if self.dbp.isroot(k, path):
                sp = self.dbp.suffix(k, path)
                d[sp] = copy.deepcopy(v)
        return d
    
    def merge(self, db, path=''):
        if not hasattr(db, 'flatdict'):
            raise ValueError('expecting a database interface with "flatdict" method got a %r'%type(db))
        
        if not path:
            self.data.update(db.flatdict())
        else:
            for k,v in db.flatdict().items():
                self.data[self.dbp.join(path, k)] = v
        


    
