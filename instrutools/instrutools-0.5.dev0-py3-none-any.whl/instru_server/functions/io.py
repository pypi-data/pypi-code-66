import os
import yaml
from ..config import system_config_path, guis_path

def find_config_file(name):
    for root in system_config_path:
        path = os.path.join(root, name)
        if os.path.exists(path):
            return path    
    raise ValueError("cannot found file %r in any of path directories : '%s'"%(name, "', '".join(system_config_path)))    

def find_ui_file(ui):
    for path in guis_path:
        for dirname, dirnames, filenames in os.walk(path):
            if ui in filenames:
                return os.path.join(dirname, ui)
    raise ValueError("Cannot find ui file %r in any of the path '%s'"%(ui, "', '".join(guis_path)))
    
def load_config_file(fname: str):
    with open(find_config_file(fname)) as f:
        d =  _load_str(f.read())            
    return d

def _load_str(s : str):
    return yaml.load(s, Loader=yaml.CLoader)
