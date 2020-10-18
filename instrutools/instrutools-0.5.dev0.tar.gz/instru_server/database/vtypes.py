from .base import add_db_parser, add_db_encoder, add_db_decoder, K
from datetime import datetime 

def _getav(dbi, path, attr):
    """ return attribute if not found try with variable """
    try:
        return dbi.get(dbi.dbp.join(path,attr))
    except KeyError:
        return dbi.get( dbi.dbp.join(path,attr,K.VALUE) )

def str_parser(dbi, path, data):
    return str(data)
add_db_parser('str', str_parser)

def float_parser(dbi, path, data):
    return float(data)
add_db_parser('float', float_parser)

def int_parser(dbi, path, data):
    return int(data)
add_db_parser('int', int_parser)

def bool_parser(dbi, path, data):
    return bool(data)
add_db_parser('bool', bool_parser)

def list_parser(dbi, path, data):
    return list(data)
add_db_parser('list', list_parser)

def dict_parser(dbi, path, data):
    return dict(data)
add_db_parser('dict', dict_parser)

def listed_parser(dbi, path, data):      
    lst = _getav(dbi, path, 'list')  
    if data in lst:
        return data
    raise ValueError("%r is not in list: %r at %r"%(data, lst, path))    
add_db_parser('listed', listed_parser)

def bounded_parser(dbi, path, data):
    try:        
        mn = _getav(dbi, path, 'min')
    except KeyError:
        pass
    else: 
        if data<mn:
            raise ValueError('%s is lower than %s at %r'%(data, mn, path))    
    try:
        mx = _getav(dbi, path, 'max')
    except KeyError:
        pass
    else: 
        if data>mx:
            raise ValueError('%s is above %s at %r'%(data, mx, path))
    return data        
add_db_parser('bounded', bounded_parser)

def clipped_parser(dbi, path, data):
    try:        
        mn = _getav(dbi, path, 'min')
    except KeyError:
        pass
    else: 
        if data<mn:
            return mn                
    try:
        mx = _getav(dbi, path, 'max')        
    except KeyError:
        pass
    else: 
        if data>mx:
            return mx            
    return data        
add_db_parser('clipped', clipped_parser)


def str2date(dbi, path, data):
    return datetime.fromisoformat(data)
def date2str(dbi, path, data):
    return data.isoformat()

add_db_decoder('str2date', str2date)
add_db_encoder('date2str', date2str)    


