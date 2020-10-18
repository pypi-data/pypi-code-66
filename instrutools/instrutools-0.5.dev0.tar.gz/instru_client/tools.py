def setitem(obj, key, val):
    obj[key]=val
    

class Linker:
    def __init__(self, data, client, root='', setfunc=setitem):
        self.client = client
        self.root = root
        self.nodes = set()
        self.callbacks = set()
        self.data = data
        self.setfunc = setfunc
    
    def update(self):
        
        r = self.client.send('rget', self.root, *self.nodes)
        if r['status']:
            return 
            
        data = self.data
        for key,val in r['answer'].items():
            self.setfunc(data, key, val)
        
        for callback in self.callbacks:
            callback(data)
            