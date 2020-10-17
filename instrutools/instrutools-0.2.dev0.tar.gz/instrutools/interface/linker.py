""" Provide tools to build graphical interfaces """
from ..shared import keys as K

def interface(cls, type, checker, finder=None):
    finder = finder
    def clfunc_setter(func):
        setattr(cls, func.__name__, func)
        cls._checkers.setdefault(type, []).append( (checker, func.__name__) )
        if finder is not None:
            cls._finders.setdefault(type, []).append( (finder, func.__name__) )
    return clfunc_setter

def finder(checker):
    checker = checker
    def finder_setter(func):
        pass


def issystem(obj):
    try:
        obj._db
        obj._path
    except AttributeError:
        return False
    return True

class ChildNotFound(ValueError):
    pass

class _BaseIO:    
    def link(self, linker, obj, **kwargs):
        
        ptype = linker.OBJ[self.path].type
        
        if isinstance(obj, tuple):
            parent, childName = obj
            try:
                finders = self._finders[ptype] 
            except KeyError:
                raise ChildNotFound('Cannot search for child for a %r'%ptype)
            for finder, func_name in finders:
                found = finder(parent, childName)
                if found is not None:
                    break
            else:
                raise ChildNotFound('Cannot find child %r for a %r'%(childName, ptype))
            
            obj = found
            
        else:            
            try:
                checkers = self._checkers[ptype]
            except KeyError:
                raise ValueError('Canno link System property of type %r'%ptype)
                
            for checker, func_name in checkers:
                if checker(obj):
                    break
            else:
                raise ValueError('Canno link System property of type %r and object of type %r'%(ptype, type(obj)))
    
        return getattr(self, func_name)(linker, obj, **kwargs)       
                     


def remap(map, prefix):
    newmap = {}
    for io, (name,kwargs) in map.items():
        if isinstance(io, Static):
            newmap[io] = (name,kwargs)
        else:
            newmap[io.__class__( path_join( (prefix, name) ), io._group)] = (name,kwargs)
    
    return newmap

class Input(_BaseIO):
    _checkers = {} # yes this is a class property 
    _finders = {}
        
    def __init__(self, path, group=None):        
        self.path = path
        self.group = group
                                                
class Output(_BaseIO):
    _checkers = {} # yes this is a class property 
    _finders = {}
    def __init__(self, path, group=None):
        self.path = path    
        self.group = group
    
class Static:
    def __init__(self, path, group=None):
        self.path = path    
        self.group = group
    
    def link(self, linker, value, **kwargs):
        
        linker.add_static_arg(self.group, self.path, value)
        
class _Linker:
    def __init__(self, OBJ, process=None, parent=None, error_handler=print):
        self.OBJ = OBJ
        self.client = OBJ.client
        
        if self.client is None:
            raise ValueError("System view has no client, it may be ran from a server")
        
        
        # default wd parent 
        self.parent = parent
        
        
        self._group_args = {None:[]}
        self._group_processes = {None:process}
        self._updators = []
        self.counter = 0 
        
    def link(self, origin, target, parent=None, **kwargs):
        if parent is None:
            parent = self.parent
        if isinstance(target, str):
            if parent is None:
                raise RuntimeError('Cannot find a chidl %r, linker has no parent'%target)            
            target = find_child(parent, target)
        
        origin.link(self, target, **kwargs)
    
    def add_updater(self, func, group=None):
        self._updators.append( (func, group) )
    
    def add_argument(self, group, name, value_or_func):
        args = self._group_args.setdefault(group, {})
        args[name] = value_or_func
    
    def send_command(self, group, cmd, process=None):
        args = self._group_args.get(group, {})
        parsed_args = {k:v() if hasattr(v, "__call__") else v for k,v in args.items()}
        
        if process is None:
            process = self._group_processes.get(group, self._group_processes[None])
        if process is None:
            raise RuntimeError("Their is no default process for group %r"%group)
        
        self.client.send(process, cmd, parsed_args)
    
    def update(self, group=False):
        self.OBJ.selfupdate()
        if group is not False:
            for func, grp in self._updators:
                if group == grp: 
                    func()
        else:
            for func, grp in self._updators:                
                func()        
        self.counter += 1
    
    
    
            
class Linker:
    def __init__(self, OBJ, process=None, error_handler=print):
        self.OBJ = OBJ
        self.client = OBJ.client
        
        if self.client is None:
            raise ValueError("System view has no client, it may be ran from a server")
        
        
        self._wg_setters = []
        self._cmd_args = {}
        self._static_args = {}
        self._processes = {}
        self._funcs = []
        
        self.process = process
        self.error_handler = error_handler
        self.counter = 0 
    
    
    def map(self, map, parent, getter="__getattr__", noerr=False):
        get = getattr(parent, getter)
        
        for io, (objname, kwargs) in map.items():
            if isinstance(io, Static):
                io.link(self, objname, **kwargs)
            else:                
                try:
                    io.link(self, (parent, objname), **kwargs)
                except ChildNotFound as er:
                    if noerr:
                        print("Warning: Child %r cannot be linked"%objname)
                    else:
                        raise er
    
    def group(self, group_name, process=None, **kwargs):
        pass
                
    def add_process(self, group, process):
        self._processes[group] = process
    
    def add_wg_setter(self, setter):
        self._wg_setters.append(setter)
    
    def add_command_arg(self, group, name, getter):
        # set the default process for the command 
        if group is None:
            raise ValueError('command arg must be grouped')
        self._processes.setdefault(group, self.process) 
        self._cmd_args.setdefault(group, []).append((name,getter))
    
    def add_static_arg(self, group, name, value):
        # set the default process for the command 
        if group is None:
            raise ValueError('static arg must be grouped')
        self._processes.setdefault(group, self.process) 
        self._static_args.setdefault(group, []).append((name,value))
    
    def add_func(self, func):
        try:
            func.__call__
        except AttributeError:
            raise ValueError('input object is not callable')
            
        self._funcs.append(func)
    
    def remove_func(self, func):
        try:
            self._funcs.remove(func)
        except ValueError:
            pass
        
    def send_command(self, group, command):
        args = {}
        if group is not None:        
            for g, value_lst in self._static_args.items():
                if g == group:
                    args.update(value_lst)
            
            for g, getter_lst in self._cmd_args.items():
                if g == group:
                    for aname, getter in getter_lst:
                        try:                    
                            args[aname] = getter() 
                        except Exception as er:
                            self.error_handler(str(er))
        process = self._processes[group]
        
        r = self.client.send(process, command, args)
        if r['status']:
            self.error_handler("{process} - {cmd} - {rtype}\n{message}".format(**r))
            return None
        return r['return']    
        
        
    def update(self):
        self.OBJ.selfupdate()
        for setter in self._wg_setters:
            setter()
        for func in self._funcs:
            func()
        self.counter += 1


