from .. import keys as K
import ipywidgets as widgets
from .linker import interface, Input, Output
from ..database import path_split

def instanceChecker(cl):
    return lambda obj: isinstance(obj, cl)

def childFinder(cl):
    def findChild(parent, child):
        return None
    return findChild
    
def findChild(parent, child):
    return None


@interface(Input, K.ARG, instanceChecker(widgets.Text), finder=childFinder(widgets.Text))
def link_arg_QLineEdit(self, linker, wg, **kwargs):
    command_path, name = path_split(self.path)
    def getter():
        return wg.value
            
    linker.add_command_arg(self.group, name, getter)
    
@interface(Output, K.PARAMETER, instanceChecker(widgets.Label), finder=childFinder(widgets.Text))
def link_arg_ipyLabel(self, linker, wg, **kwargs):
    command_path, name = path_split(self.path)
    param = linker.OBJ[self.path]    
    def setter():
        wg.value = str(param.get())
    linker.add_wg_setter(setter)
    
