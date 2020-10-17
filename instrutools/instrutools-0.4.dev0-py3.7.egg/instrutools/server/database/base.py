import os
from ...shared import keys as K
PRIVATE_KEYS = (K.TYPE, K.PROTOTYPES, K.DESCRIPTION, 
                K.FILE, K.PROTOTYPE, K.SETUP, K.MODEL)

def path_parse(p):
    if isinstance(p, tuple):
        return ".".join(a for a in p if a)
    if isinstance(p, str):
        return p
    raise ValueError('%r is not a valid path or path fraction')    

def path_join(*obj):
    return ".".join(path_parse(a) for a in obj if a)
    # if isinstance(obj, str):
    #     return obj
    # return ".".join( a for a in obj if a)

        
    #return (".".join( sum( (a.split(".") for a in obj), []))).strip('.')

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
    
def path_isroot(path, root):
    """ check if a path has the given root"""
    return path.startswith(root+".")

    
def db_join(*args):
    return (".".join( sum( (a.split(".") for a in args), []))).strip('.')

def dbquery(db, *args):
    return db.query(db_join(*args))
    

    
