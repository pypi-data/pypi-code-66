from .. import keys as K
from .base import add_type_class, _DbBaseObject, _ParametersProperty, _RParametersProperty
from ..database.base import path_join
from ..functions.publisher import publish

class Device(_DbBaseObject):  
    _db = None
    _path = None  
    _authorized_child = {K.PARAMETER:K.PARAMETERS}
    _protected_config = [K.TYPE, K.PARAMETERS]
    
    parameters = _ParametersProperty()
    rparameters = _RParametersProperty()
    def __init__(self, db, prefix):
        prefix = path_join(prefix)
        try:
            tpe = db.query( (prefix, K.TYPE) )
        except KeyError:
            raise ValueError('the sub-database at %r does not have type property'%prefix)
        
        if tpe != K.DEVICE:
            raise ValueError('(sub)db is not a device at %r'%prefix)
        self.__dict__['_db'] = db
        self.__dict__['_path'] = prefix
    
    def __str_ascii__(self, p):
                        
        tab = " "*len(self._path)                
        txt = [p.write_margin(self._path)]
                        
        pp = p.child(tab_str=tab, level=1)        
        
        for pname, param in self.parameters.items():
            txt.append(publish(param, pp)) 
        
        return "\n".join(txt)     
    
            
device = Device 
add_type_class(K.DEVICE, device)