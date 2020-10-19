# -*- coding: UTF-8 -*-
import sys, os, re
from sys import argv

class SceneryOrganizer:
    def __init__(self):
        self.xp_path = self.get_path()
        self.airport_list   = []
        self.library_list   = []
        self.mesh_list      = []
        self.global_list    = []
        self.undefined_list = []
        self.counter        = 0
        
    def get_path(self):
        for index, arg in enumerate(sys.argv):
            if arg == "-d":
                return sys.argv[int(index) + 1]
            
    def get_scenery_list(self):
        for name in os.listdir(self.xp_path):
            if os.path.isdir(os.path.join(self.xp_path, name)):
                print(name + " é livraria" if self.is_library(name) else name + " não é livraria")
                self.counter += 1
        return ("There are {} folders here".format(self.counter))
    
    def is_library(self, scenery):
        regex = r"library"
        return re.finditer(regex, scenery, re.IGNORECASE)
        

scenery = SceneryOrganizer()

print(scenery.get_scenery_list())

# if os.path.exists(correct_dir):
#     os.chdir(correct_dir)
#     for directories in os.listdir(os.getcwd()):
#         print(directories if directories != "." else "")