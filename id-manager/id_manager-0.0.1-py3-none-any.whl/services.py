import os

class TaskManager:
    def __init__ (self, name):
        self.name = name
    
    def start(self):
        os.chdir('/tmp')
        if not os.path.exists('{}.LOCK'.format(self.name)):
            os.mkdir('{}.LOCK'.format(self.name))
            return True
        return False
    
    def close(self):
        os.chdir('/tmp')
        os.rmdir('{}.LOCK'.format(self.name))
        return True