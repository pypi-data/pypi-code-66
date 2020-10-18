import os
from ..config import system_config_path

def find_config_file(name):
    for root in system_config_path:
        path = os.path.join(root, name)
        if os.path.exists(path):
            return path    
    raise ValueError("cannot found file %r in any of path directories : '%s'"%(name, "', '".join(system_config_path)))    

