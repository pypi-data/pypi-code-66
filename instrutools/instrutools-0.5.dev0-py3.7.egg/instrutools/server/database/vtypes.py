from .base import path_join

db_parsers = {}
db_parsers_req = {}
def add_db_parser(name, f, requirement=None):
    if not hasattr(f, "__call__"):
        raise ValueError("expecting a callable as second argument")
    db_parsers[name] = f
    db_parsers_req[name] = requirement or set()
    

def str_parser(db, path, data):
    return str(data)
add_db_parser('str', str_parser)

def float_parser(db, path, data):
    return float(data)
add_db_parser('float', float_parser)

def int_parser(db, path, data):
    return int(data)
add_db_parser('int', int_parser)

def bool_parser(db, path, data):
    return bool(data)
add_db_parser('bool', bool_parser)

def list_parser(db, path, data):
    return list(data)
add_db_parser('list', list_parser)

def listed_parser(db, path, data):
    if data in db._get('list', path):
        return data
    raise ValueError("%r is not in list: %r at %r"%(data, db._get('list', path) , path))
    return list(data)
add_db_parser('listed', listed_parser, {'list'})

def bounded_parser(db, path, data):
    try:
        mn = db._get('min', path)
    except KeyError:
        pass
    else: 
        if data<mn:
            raise ValueError('%s is lower than %s at %r'%(data, mn, path))
    
    try:
        mx = db._get('max', path)
    except KeyError:
        pass
    else: 
        if data>mx:
            raise ValueError('%s is above than %s at %r'%(data, mx, path))
    return data        
add_db_parser('bounded', bounded_parser)

def clipped_parser(db, path, data):
    try:
        mn = db._get('min', path)
    except KeyError:
        pass
    else: 
        if data<mn:
            return mn                
    try:
        mx = db._get('max', path)
    except KeyError:
        pass
    else: 
        if data>mx:
            return mx            
    return data        
add_db_parser('clipped', clipped_parser)


