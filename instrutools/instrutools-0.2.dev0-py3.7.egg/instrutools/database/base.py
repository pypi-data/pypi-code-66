import os
from .. import keys as K
PRIVATE_KEYS = (K.TYPE, K.PROTOTYPES, K.DESCRIPTION, 
                K.FILE, K.PROTOTYPE, K.SETUP, K.MODEL)

def path_join(obj):
    if isinstance(obj, str):
        return obj
    return ".".join( a for a in obj if a)
        
    #return (".".join( sum( (a.split(".") for a in obj), []))).strip('.')

def path_split(path):
    s,_,p = path[::-1].partition('.')
    return  p[::-1], s[::-1]
        
def db_join(*args):
    return (".".join( sum( (a.split(".") for a in args), []))).strip('.')

def dbquery(db, *args):
    return db.query(db_join(*args))
    

    
