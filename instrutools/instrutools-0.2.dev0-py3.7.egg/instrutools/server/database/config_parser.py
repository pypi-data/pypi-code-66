from ...shared import keys as K
import yaml
from .base import db_join, PRIVATE_KEYS
from ..functions.io import  find_config_file
from .vtypes import db_parsers_req




DEFAULT_TIMEOUT = 5*60.

def _empty():
    return None

def _default_timeout():
    return DEFAULT_TIMEOUT

rules = {
    K.SYSTEM: { # generic type, can contain anything 
        "defaults": {K.DESCRIPTION:str}, 
        "parents" : {K.SYSTEM},
        "setup" : True           
    },
    K.VAR: { # define a variable and its meta data can be child of everythins except ARGUMENT and VAR
        "defaults": {K.VALUE:_empty, K.DESCRIPTION:str, K.VTYPE:tuple}, 
        "parents" : {K.SYSTEM, K.DEVICE, K.COMMAND, K.PROCESS},
        "setup" : True            
    },
    K.PROCESS: { # Define a process can be only inside a SYSTEM
        "defaults": {K.DESCRIPTION:str}, 
        "parents" : {K.SYSTEM},         
        "setup" : True         
    },
    K.COMMAND: { # can only be inside a process define a command, can contain VAR and ARGUMENT
        "defaults": {K.DESCRIPTION:str, K.REQUIREMENTS:dict, K.TIMEOUT:_default_timeout}, 
        "parents" : {K.PROCESS},  
        "setup" : False          
    },
    K.ARGUMENT: { # almost the same as var  excep that it can be only inside a COMMAND
        "defaults": {K.DESCRIPTION:str}, 
        "parents" : {K.COMMAND},
        "setup" : False           
    },       
}

def read_file(f, db, root="", suffix=""):
    try:
        s = f.read()
    except AttributeError:
        if isinstance(f, str):
            d = _load_file(f)
        raise ValueError('file must be a string or an object with .read() method as file ')
    else:
        d = _load_str(s)
    
    read_dict(d, db)

def read_str(s, db, root="", suffix=""):
    d = _load_str(s)
    read_dict(d, db)

def read_dict(d, db, root="", suffix="", type=None):
    
    if not _is_sub_obj(d):
        # this is a keyword
        if suffix not in [K.TYPE]:
            db.setdefault(db_join(root, K.KEYWORDS), []).append(suffix)
        db[db_join(root,suffix)] = d
        return 
    
    d = _load(d, db, root, suffix)
    #d = _load(d)    
    type = d.get(K.TYPE, type)
    
    if type is None:
        # type = db.get(db_join(root,suffix,K.TYPE), None)
        # if type is None:            
            raise ValueError("config has no type %s"%d)
    try:
        reader = type_reader_loockup[type] 
    except KeyError:
        raise ValueError("unknown type %r in %r"%(type, db_join(root, suffix)))    
    reader(d, db, root=root, suffix=suffix)
    




def _load_file(fname :str):
    with open(find_config_file(fname)) as f:
        d =  _load_str(f.read())            
    return d

def _load_str(s : str):
    return yaml.load(s, Loader=yaml.CLoader)


# def _load_(d):    
#     mdb = {}
#     d = d.copy()    
#     if K.MODEL in d:                
#         read_dict(_load_file(d[K.MODEL]), mdb)
#         if K.TYPE in d and K.TYPE in mdb and d[K.TYPE]!=mdb[K.TYPE]:
#             raise Exception('including model %r as a %s however this is a %s'%(d[K.MODEL], d[K.TYPE], mdb[K.TYPE]))
#         for key, value in mdb.items():
#             d.setdefault(key, value)                                   
#     return d

def _load(d, db, root, suffix):    
    mdb = {}
      
    if K.MODEL in d:                
        read_dict(_load_file(d[K.MODEL]), mdb)
        if K.TYPE in d and K.TYPE in mdb and d[K.TYPE]!=mdb[K.TYPE]:
            raise Exception('including model %r as a %s however this is a %s'%(d[K.MODEL], d[K.TYPE], mdb[K.TYPE]))
        for key, value in mdb.items():
            db.setdefault( db_join(root, suffix, key), value)
        if K.TYPE in mdb: 
            d.setdefault(K.TYPE, mdb[K.TYPE])                                   
    return d

def _is_sub_obj(d):
    if isinstance(d, dict):
        return K.TYPE in d or K.MODEL in d
    return False

def _read_setup(setup, db,  root , suffix):
    """ read everything under setups
    setups shoud be key/value pairs, the key should point to variable relative 
    to where it starts (root)        
    """
    for k,v in setup.items():
        nk = db_join(root, suffix, k)
        if not  db_join(nk, K.TYPE) in db:
            raise ValueError('error in setup unknown key %s'%nk)
        if db[db_join(nk, K.TYPE)]!= K.VAR:
            raise ValueError('error in setup %r is not a var'%nk)        
        db[db_join(nk, K.VALUE)] = v   

def _check_root_type(db, root, new_type, valid_rtypes):
    if not root: 
        return None
    
    rtype = db.get(db_join(root, K.TYPE), '')
    if not rtype:
        print(db)
        raise ValueError("BUG: (sub)database must define a type at %r"%root)
    if rtype not in valid_rtypes:
        raise ValueError('A %r can only be included in %r and not in a %r'%(new_type, valid_rtypes, rtype))


def _read_gen(tpe, d, db, root= "",  suffix=""):
    r = rules[tpe]
    _check_root_type(db, root, tpe, r['parents'])
    path = db_join(root, suffix)
    db[db_join(path, K.TYPE)] = tpe
    
    if suffix:
        db.setdefault(db_join(root, K.CHILDREN), {}).setdefault(tpe,[]).append(suffix)
    
    for sub_name, sub_def in d.items():
        read_dict(sub_def, db, path, suffix=sub_name)
    
    for k,v in r['defaults'].items():        
        db.setdefault( db_join(path, k), v() )
    
    if False:#r['setup']:
        setups = d.get(K.SETUP, {})
        _read_setup(setups, db,  root, suffix)
    
def _read_system(d, db, root= "",  suffix=""):    
    _read_gen( K.SYSTEM, d, db, root,  suffix)    

def _read_process(d, db, root= "", suffix=""):
    _read_gen( K.PROCESS, d, db, root,  suffix)   
         
        
def _read_device(d, db, root="",  suffix=""):    
    _read_gen( K.DEVICE, d, db, root,  suffix)   

    
def _read_var(d, db, root="", suffix=""):
    _read_gen( K.VAR, d, db, root,  suffix)
    # do some cleaning 
    vtk = db_join(root, suffix, K.VTYPE)
    if isinstance( db[vtk], str):
        db[vtk] = (db[vtk],) # vtype should always be a tuple
    for p in db[vtk]:
        if p not in db_parsers_req:
            raise ValueError('vtype %r is unknonw at %s.%s'%(p, root, suffix))
        for k in db_parsers_req[p]:
            if not db_join(root, suffix, k) in db:
                raise ValueError("vtype %r needs %r attribute at %s.%s"%(p, k, root, suffix))
        
        
def _read_command(d, db, root="", suffix=""):
    _read_gen( K.COMMAND, d, db, root,  suffix)   
    
    path = db_join(root, suffix)
    for argname, argdef in d.get(K.ARGS, {}).items():
        _read_command_arg(argdef, db, path, suffix=argname)
    
        

def _read_command_arg(d, db, root="",  suffix=""):
    _read_gen( K.ARG, d, db, root,  suffix)      

type_reader_loockup = {
    K.SYSTEM: _read_system, 
    K.VAR: _read_var, 
    K.COMMAND: _read_command, 
    K.ARG: _read_command_arg,     
    K.PROCESS : _read_process,
}
