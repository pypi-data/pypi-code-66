
psep = "."
root = ''

class DbPath:
    """ class to handle database path manipulation """
    def __init__(self, sep=psep, root=root):
        self.sep = sep
        self.root = root
    
    def parse(self, p):
        if isinstance(p, tuple):
            return self.sep.join(self.parse(a) for a in p if a)
            #return self.sep.join(p)
        if isinstance(p, str):
            return p
        raise ValueError('%r is not a valid path or path fraction')    
        
    def to_str(self, p):
        return p

    def join(self, *obj):        
        return self.sep.join(self.parse(a) for a in obj if a)
        #return self.sep.join(obj)
        # if isinstance(obj, str):
        #     return obj
        # return ".".join( a for a in obj if a)        
        #return (".".join( sum( (a.split(".") for a in obj), []))).strip('.')

    def split(self, path):    
        s,_,p = path[::-1].partition(self.sep)
        return  p[::-1], s[::-1]

    def suffix(self, path, prefix):
        if prefix:
            return path[len(prefix)+1:]
        else:
            return path
            
    def prefix(self, path, suffix):
        if suffix:
            return path[:-len(suffix)-1]
        else:
            return path
        
    def isroot(self, path, root):
        """ check if a path has the given root"""
        if root:
            return path.startswith(root+self.sep)
        else:
            return True
            
    def isendding(self, path, suffix):
        if suffix:
            return path.endswith(self.sep+suffix)
        else:
            return True
    
    def is_path(self, path):
        return self.sep in path
        


# def path_parse(p):
#     if isinstance(p, tuple):
#         return psep.join(path_parse(a) for a in p if a)
#     if isinstance(p, str):
#         return p
#     raise ValueError('%r is not a valid path or path fraction')    
# 
# def path_to_str(p):
#     return p
# 
# def path_join(*obj):
#     return psep.join(path_parse(a) for a in obj if a)
#     # if isinstance(obj, str):
#     #     return obj
#     # return ".".join( a for a in obj if a)        
#     #return (".".join( sum( (a.split(".") for a in obj), []))).strip('.')
# 
# def path_split(path, root=None):    
#     s,_,p = path[::-1].partition(psep)
#     return  p[::-1], s[::-1]
# 
# def path_suffix(path, prefix):
#     if prefix:
#         return path[len(prefix)+1:]
#     else:
#         return path
# 
# def path_prefix(path, suffix):
#     if suffix:
#         return path[:-len(suffix)-1]
#     else:
#         return path
# 
# def path_isroot(path, root):
#     """ check if a path has the given root"""
#     if root:
#         return path.startswith(root+psep)
#     else:
#         return True
# 
# def path_isendding(path, suffix):
#     if suffix:
#         return path.endswith(psep+suffix)
#     else:
#         return True
# 
# def is_path(path):
#     return psep in path


# ###################################################
# root = tuple()
# 
# def path_parse(p):
#     if isinstance(p, str):
#         return tuple(p.split(psep))
#     return p
# 
# def path_join(*args):
#     return sum((path_parse(p) for p in args if p), root)    
# 
# def path_to_str(path):    
#     return psep.join(path)
# 
# def path_split(path):    
#     return path[:-1], path[-1:]
# 
# def path_suffix(path, prefix):
#     if prefix:
#         return path[-len(prefix)+1:]
#     return path
# 
# def path_prefix(path, suffix):
#     if suffix:
#         return path[:-len(suffix)]
#     return path
# 
# def path_isroot(path, root):
#     """ check if a path has the given root"""
#     return path[:len(root)] == root
# 
# def path_isendding(path, suffix):
#     if suffix:
#         return path[-len(suffix):] == suffix    
#     else:
#         return True
# 
# def is_path(path):
#     return len(path)>1    
