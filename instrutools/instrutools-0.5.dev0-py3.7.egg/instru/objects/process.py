from .. import keys as K
from .base import (add_type_class, _DbBaseObject, _ParametersProperty, _RParametersProperty, 
                   _CommandsProperty)
from ..database.base import path_join

class Process(_DbBaseObject):     
    parameters = _ParametersProperty()
    rparameters = _RParametersProperty()
    commands = _CommandsProperty()
    
    _authorized_child = {K.COMMAND:K.COMMANDS, K.PARAMETER:K.PARAMETERS}
    _protected_config = [K.TYPE, K.COMMANDS, K.PARAMETERS]
    def __init__(self, db, prefix):   
        prefix = path_join(prefix)       
        try:
            tpe = db.query( (prefix, K.TYPE) )
        except KeyError:
            raise ValueError('the sub-database at %r does not have type property'%prefix)
              
        if tpe != K.PROCESS:
            raise ValueError('(sub)db is not a process but a %s at %r'%prefix)
        self.__dict__['_db'] = db
        self.__dict__['_path'] = prefix    
                    
    def __str_ascii__(self, p):        
        tab = " "*len(self._path)                
        txt = [p.write_margin(self._path)]
                        
        pp = p.child(tab_str=tab, level=1)
        # for sysname, system in self.systems.items():            
        #     txt.append(publish(system, pp))
        # 
        # for devname, device in self.devices.items():
        #     txt.append(publish(device, pp)) 
        # 
        # for pname, param in self.parameters.items():
        #     txt.append(publish(param, pp)) 
        
        return "\n".join(txt)            
    
process = Process
add_type_class(K.PROCESS, Process)
