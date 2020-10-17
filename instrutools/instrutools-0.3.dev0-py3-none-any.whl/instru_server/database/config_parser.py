""" define a parser for a yaml like database """

from .. import keys as K
import yaml
from . import vtypes # import is necessary to fill up the vtype dictionary
from ..functions.io import  find_config_file

# default attribute constructor 
defaults_attributes = {
    K.DESCRIPTION:str,
    K.VALUE: lambda: None 
}
def stt(val):
    """ string to tuple parser """
    if isinstance(val, str):
        return tuple(s.strip() for s in val.split(","))
    return val 
_attr_prs = {K.VTYPE:stt}


class _FmtDbi:
    """ a class to format a dbinterface attribute """
    def __init__(self, dbi, prefix):
        self.__dict__['__dbi__'] = dbi
        self.__dict__['_prefix_'] = prefix
        
    def __getattr__(self,attr):
        dbi = self.__dict__['__dbi__']
        p = self.__dict__['_prefix_']
        try:
            return dbi.get(attr, p)
        except KeyError:
            if dbi.has(K.TYPE, dbi.dbp.join(p,attr)):
                return _FmtDbi(dbi, dbi.dbp.join(p,attr))
            raise AttributeError(attr)
    
    def __getitem__(self, item):
        dbi = self.__dict__['__dbi__']
        p = self.__dict__['_prefix_']
        
        return dbi.get(K.VALUE, dbi.dbp.join(p,item))
    
    def keys(self):
        return list(self.__dict__['__dbi__'].get(K.CHILDREN))+list(self.__dict__['__dbi__'].get(K.ATTRIBUTES))

def fmtDict(dbi, prefix):    
    d =  {suffix:_FmtDbi(dbi, dbi.dbp.join(prefix, suffix)) for suffix in dbi.get(K.CHILDREN, prefix)}
    d.update( {suffix:dbi.get(suffix, prefix) for suffix in dbi.get(K.ATTRIBUTES, prefix)} )
    return d
    
def _parse_attr(attr, value):
    """ parse an attribute accordinto rules defined in _attr_prs"""    
    try:
        f = _attr_prs[attr]
    except KeyError:
        return value
    return f(value)    


def read_file(f, dbi, root="", suffix=""):
    """ read a yaml database configuration file """    
    try:
        r = f.read
    except AttributeError:
        if isinstance(f, str):
            d = _load_file(f)
        else:
            raise ValueError('file must be a string or an object with .read() method as file ')
    else:
        d = _load_str(r())    
    read_obj(d, dbi, root=root, suffix=suffix)

def read_str(s, dbi, root="", suffix=""):
    """ read a yaml database configuration string """ 
    d = _load_str(s)
    read_obj(d, dbi, root=root, suffix=suffix)

def read_obj(d, dbi, root="", suffix="", type=None):
    """ read a dict as it is defined in yaml file """
    return dbi.add_obj( dbi.dbp.join(root,suffix), d)
    
    if hasattr(d, 'flatdict'):
        dbi.merge(d, (root, suffix))
        return 
         
    if not _is_sub_obj(d):
        # this is a keyword
        attrs = dbi.setdefault(K.ATTRIBUTES, [], root)        
        if not dbi.dbp.is_path(suffix):
            if suffix not in attrs:
                attrs.append(suffix)
                
        dbi.set(suffix, _parse_attr(suffix, d), root)
        return 
    
    isTemplate = d.get(K.ISTEMPLATE, False)
    if isTemplate:
        p_dbi = dbi
        isuffix = suffix
        iroot = root
        suffix = '' 
        root = ''
        dbi = dbi.__class__({})
        dbi.dpb = p_dbi.dbp
                
    d = _load_template(d, dbi, root, suffix)
    #d = _load(d)    
    type = d.get(K.TYPE, type)
    
    if type is None:         
        raise ValueError("config has no type %s"%d)
            
    _read_group(type, d, dbi, root=root, suffix=suffix)
    
    if isTemplate:
        p_dbi.add_template(isuffix, dbi)

def _load_file(fname :str):
    with open(find_config_file(fname)) as f:
        d =  _load_str(f.read())            
    return d

def _load_str(s : str):
    return yaml.load(s, Loader=yaml.CLoader)

def _load_template(d, dbi, root, suffix):  
    """ loading template on the dbi from 'template' keyword or 'include' keyword """      
    if K.TEMPLATE in d:
        try:
            tpl = dbi.get_template(d[K.TEMPLATE])
        except KeyError:
            raise ValueError('template %r is unknown at %s %s'%(d[K.TEMPLATE], root, suffix))
        
        for key, value in tpl.flatdict().items():            
            dbi.setdefault( key, value, dbi.dbp.join(root, suffix))
        if tpl.has(K.TYPE):
            d.setdefault(K.TYPE, tpl.get(K.TYPE))     
        
    if K.INCLUDE in d:
        mdbi = dbi.__class__({})
        mdbi.dbp = dbi.dbp
                        
        read_obj(_load_file(d[K.INCLUDE]), mdbi)
        if K.TYPE in d and mdbi.has(K.TYPE) and d[K.TYPE]!=mdbi.get(K.TYPE):
            raise ValueError('including config %r as a %s however this is a %s'%(d[K.INCLUDE], d[K.TYPE], mdbi.get(K.TYPE)))
        for key, value in mdbi.flatdict().items():            
            dbi.setdefault( key, value, dbi.dbp.join(root, suffix))
        if mdbi.has(K.TYPE):
            d.setdefault(K.TYPE, mdbi.get(K.TYPE))                                  
    return d

def _is_sub_obj(d):
    if isinstance(d, dict):
        return K.TYPE in d or K.INCLUDE in d or K.TEMPLATE in d
    return False

def _read_init(init, dbi,  root , suffix):
    """ read everything under 'init'
    init shoud be a dict, the key should point to variable relative 
    to where it starts (root) without the .value attribute        
    """
    for k,v in init.items():
        nk = dbi.dbp.join(root, suffix, k)
        dbi.set(K.VALUE, v, nk)
    
def _read_group(tpe, d, dbi, root= "",  suffix=""):        
    path = dbi.dbp.join(root, suffix)        
    dbi.set(K.TYPE, tpe, path)
        
    if suffix:
        children = dbi.setdefault(K.CHILDREN, [], root)
        if not suffix in children:
            children.append(suffix)        
    
    for sub_name, sub_def in d.items():
        read_obj(sub_def, dbi, path, suffix=sub_name)
    
    for k,v in defaults_attributes.items():
        if not dbi.has(k, path):              
            dbi.set(k, v(), path)
        attributes = dbi.setdefault(K.ATTRIBUTES, [], path) 
        if not k in attributes:
            attributes.append(k)
    
    dbi.setdefault(K.ATTRIBUTES, [], path)
    dbi.setdefault(K.CHILDREN, [], path)
        
    init = d.get(K.INIT, {})
    _read_init(init, dbi,  root, suffix)
    
    
    # shall we do some more cleanup ?