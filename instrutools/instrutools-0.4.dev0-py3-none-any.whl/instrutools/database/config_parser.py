from .. import keys as K
import yaml
from .base import db_join, PRIVATE_KEYS
from ..functions.io import  find_config_file





DEFAULT_TIMEOUT = 5*60.

def _empty():
    return None

def _default_timeout():
    return DEFAULT_TIMEOUT

rules = {
    K.SYSTEM: {
        "defaults": {K.DESCRIPTION:str, K.SUBSYSTEMS:list, K.DEVICES:list, K.PARAMETERS:list, K.PROCESSES:list}, 
        "parents" : {K.SYSTEM},
        "childs": {K.SYSTEM, K.DEVICE, K.PARAMETER, K.PROCESS}, 
        "list": K.SUBSYSTEMS, 
        "setup" : True           
    },
    K.DEVICE: {
        "defaults": {K.DESCRIPTION:str, K.PARAMETERS:list}, 
        "parents" : {K.SYSTEM},
        "childs": {K.DEVICE, K.PARAMETER}, 
        "list": K.DEVICES, 
        "setup" : True            
    },
    K.PARAMETER: {
        "defaults": {K.VALUE:_empty, K.DESCRIPTION:str}, 
        "parents" : {K.SYSTEM, K.DEVICE, K.COMMAND, K.PROCESS},
        "childs" : set(), 
        "list": K.PARAMETERS, 
        "setup" : True            
    },
    K.PROCESS: {
        "defaults": {K.DESCRIPTION:str, K.COMMANDS:list, K.PARAMETERS:list}, 
        "parents" : {K.SYSTEM},
        "childs": {K.PARAMETER, K.COMMAND},         
        "list": K.PROCESSES, 
        "setup" : True         
    },
    K.COMMAND: {
        "defaults": {K.DESCRIPTION:str, K.ARGS:list, K.REPLIES:list, K.REQUIREMENTS:dict, K.TIMEOUT:_default_timeout}, 
        "parents" : {K.PROCESS},
        "childs": {K.COMMAND},   
        "list": K.COMMANDS, 
        "setup" : False          
    },
    K.ARG: {
        "defaults": {}, 
        "parents" : {K.COMMAND},
        "childs": set(), 
        "list": K.COMMANDS, 
        "setup" : False           
    },
    K.REPLY: {
        "defaults": {}, 
        "parents" : {K.COMMAND},
        "childs": set(),
        "list": K.REPLIES, 
        "setup" : False  
    }        
}


def read_file(f, db, root="", suffix=""):
    d = _load_file(f)
    read_dict(d, db)


def read_dict(d, db, root="", suffix="", type=None):
    
    if not _is_sub_obj(d):
        # this is a keyword
        if suffix not in [K.TYPE]:
            db.setdefault(db_join(root, K.METADATA), []).append(suffix)
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
    




def _load_file(d):
    if isinstance(d, str):
        with open(find_config_file(d)) as f:
            d = yaml.load(f.read())
    return d
    
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
    setups shoud be key/value pairs, the key should point to parameter relative 
    to where it starts (root)        
    """
    for k,v in setup.items():
        nk = db_join(root, suffix, k)
        if not  db_join(nk, K.TYPE) in db:
            raise ValueError('error in setup unknown key %s'%nk)
        if db[db_join(nk, K.TYPE)]!= K.PARAMETER:
            raise ValueError('error in setup %r is not a parameter'%nk)        
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
        db.setdefault(db_join(root, r['list']), []).append(suffix)
    
    for sub_name, sub_def in d.items():
        read_dict(sub_def, db, path, suffix=sub_name)
    
    for k,v in r['defaults'].items():        
        db.setdefault( db_join(path, k), v() )
    
    if r['setup']:
        setups = d.get(K.SETUP, {})
        _read_setup(setups, db,  root, suffix)
    
def _read_system(d, db, root= "",  suffix=""):    
    _read_gen( K.SYSTEM, d, db, root,  suffix)    

def _read_process(d, db, root= "", suffix=""):
    _read_gen( K.PROCESS, d, db, root,  suffix)   
         
        
def _read_device(d, db, root="",  suffix=""):    
    _read_gen( K.DEVICE, d, db, root,  suffix)   

    
def _read_parameter(d, db, root="", suffix=""):
    _read_gen( K.PARAMETER, d, db, root,  suffix)    
        
    
def _read_command(d, db, root="", suffix=""):
    _read_gen( K.COMMAND, d, db, root,  suffix)   
    
    path = db_join(root, suffix)
    for argname, argdef in d.get(K.ARGS, {}).items():
        _read_command_arg(argdef, db, path, suffix=argname)
    
        

def _read_command_arg(d, db, root="",  suffix=""):
    _read_gen( K.ARG, d, db, root,  suffix)      

type_reader_loockup = {
    K.SYSTEM: _read_system, 
    K.DEVICE: _read_device, 
    K.PARAMETER: _read_parameter, 
    K.COMMAND: _read_command, 
    K.ARG: _read_command_arg,     
    K.PROCESS : _read_process,
}
