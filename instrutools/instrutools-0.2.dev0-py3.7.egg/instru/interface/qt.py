from .linker import Input, Output, interface
from .. import path_split
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel
import os
import sys

from .. import keys as K

def instanceChecker(cl):
    return lambda obj: isinstance(obj, cl)


def childFinder(cl):
    def findChild(parent, child):
        return parent.findChild(cl, child)
    return findChild
    
def findChild(parent, child):
    return parent.findChild(QtWidgets.QtWidget, child)


@interface(Input, K.ARG, instanceChecker(QLineEdit), finder=childFinder(QLineEdit))
def link_arg_QLineEdit(self, linker, wg, **kwargs):
    command_path, name = path_split(self.path)
    def getter():
        sval = wg.text()
        return linker.OBJ[self.path].parse(sval)
    
    linker.add_command_arg(self.group, name, getter)

@interface(Input, K.COMMAND, instanceChecker(QPushButton), finder=childFinder(QPushButton))
def link_command_QPushButton(self, linker, wg, **kwargs):
    # TODO: better way to find command name in process
    _, cmd = path_split(self.path)
    def send():
        linker.send_command(self.group, cmd)            
        linker.update()
    wg.clicked.connect(send)
    linker._processes.setdefault(self.group, linker.process)


@interface(Output, K.PARAMETER, instanceChecker(QLabel), finder=childFinder(QLabel))
def link_parameter_QLabel(self, linker, wg, **kwargs):
    formater = kwargs.get("formater", str)
    param = linker.OBJ[self.path]
    def setter():
        wg.setText( formater(param.get()) )
    linker.add_wg_setter(setter)


live_seq = ["~--", "-~-", "--~", "-~-"]
def link_window(linker, window, map):
    linker.map(map, window)  
    
    liveLabel = window.findChild(QtWidgets.QLabel, 'liveLabel')
    if liveLabel:
        def live_seq_update():
            liveLabel.setText(live_seq[linker.counter%len(live_seq)])            
        linker.add_func(live_seq_update)
    linker.add_func(window.update)


def create(name, qtCreatorFile):    
    Ui_QDialog, QtBaseClass = uic.loadUiType(qtCreatorFile)
        
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_QDialog.__init__(self)
        self.setupUi(self)        
        self.show()
            
    return type(name, (QtBaseClass, Ui_QDialog), {"__init__":__init__})
            