from .fakeattr import fakeattr
import json




class undefined(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'undefined'
        fakeattr.__init__(self, run, name)

    def __call__(*args, **kwargs):
        raise TypeError('undefined is not callable')


class Number(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Number'
        fakeattr.__init__(self, run, name)
    def __call__(self, *args):
        nargs = []
        for arg in args:
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return fakeattr('new '+self.name+'(%s)'%','.join(nargs),self.run)
    

class Boolean(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Boolean'
        fakeattr.__init__(self, run, name)
    def __call__(self, *args):
        nargs = []
        for arg in args:
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return fakeattr('new '+self.name+'(%s)'%','.join(nargs),self.run)
    

class String(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'String'
        fakeattr.__init__(self, run, name)
    def __call__(self, *args):
        nargs = []
        for arg in args:
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return fakeattr('new '+self.name+'(%s)'%','.join(nargs),self.run)
    

class Array(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Array'
        fakeattr.__init__(self, run, name)
    def __call__(self, *args):
        nargs = []
        for arg in args:
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return fakeattr('new '+self.name+'(%s)'%','.join(nargs),self.run)
    

class Math(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Math'
        fakeattr.__init__(self, run, name)


class Date(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Date'
        fakeattr.__init__(self, run, name)
    def __call__(self, *args):
        nargs = []
        for arg in args:
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return fakeattr('new '+self.name+'(%s)'%','.join(nargs),self.run)
    

class Random(fakeattr):
    def __init__(self, window):
        self.run = window.run
        self.name = 'Math.random'
        fakeattr.__init__(self, run, name)
    def __call__(self, min=0, max=10):
        nargs = []
        for arg in (min,max):
            if isinstance(arg, fakeattr):
                nargs.append(json.dumps(arg._parent))
            else:
                nargs.append(json.dumps(arg))
        return self.run('Math.floor(Math.random() * (%s - %s + 1) ) + %s;'%(nargs[1],nargs[0],nargs[0]),True)
    

Object = dict


def globalVar(name, attr):
    attr._run("window.%s=%s;" % (name, attr._parent))
    return fakeattr(attr._run, "window."+name)


def setCall(target, args=[]):
    if isinstance(target, fakeattr):
        target = target._parent
    nargs = []
    for arg in args:
        if isinstance(arg, fakeattr):
            nargs.append(json.dumps(arg._parent))
        else:
            nargs.append(json.dumps(arg))
    return target+'(%s);' % ','.join(nargs)


class function():
    def __init__(self, *args):
        self.args = args

    def fake(*args): return '<function>'

    def __call__(self, code):
        return fakeattr(self.fake, 'function(%s){%s}' % (','.join(self.args), code))


def code(c):
    def fake(*args): return '<function>'
    return fakeattr(fake, c)


def increment(x):
    return x._run(x._parent+'++;')


def decrement(x):
    return x._run(x._parent+'--;')


def assign(x, y): x = y


def assign_helper(x, y, op):
    if isinstance(y, fakeattr):
        y = y._parent
    else:
        y = json.dumps(y)
    x._run(x._parent+op+y+';')


def addAssign(x, y): return assign_helper(x, y, '+=')
def subAssign(x, y): return assign_helper(x, y, '-=')
def mulAssign(x, y): return assign_helper(x, y, '*=')
def divAssign(x, y): return assign_helper(x, y, '/=')
def expAssign(x, y): return assign_helper(x, y, '**=')
def modAssign(x, y): return assign_helper(x, y, '%=')


def comparison_helper(x, y, op):
    runner = None
    if isinstance(x, fakeattr):
        runner = x._run
        x = x._parent
    else:
        x = json.dumps(x)
    if isinstance(y, fakeattr):
        runner = y._run
        y = y._parent
    else:
        y = json.dumps(y)
    if runner:
        return runner(x+op+y+';', True)
    else:
        raise Exception("no runner")


def equal(x, y):
    try:
        return comparison_helper(x, y, '==')
    except:
        return x == y


def Is(x, y):
    try:
        return comparison_helper(x, y, '===')
    except:
        return x == y and type(x) == type(y)


def notEqual(x, y):
    try:
        return comparison_helper(x, y, '!=')
    except:
        return x != y


def isNot(x, y):
    try:
        return comparison_helper(x, y, '!==')
    except:
        return x != y or type(x) != type(y)


def greaterThan(x, y):
    try:
        return comparison_helper(x, y, '>')
    except:
        return x > y


def lessThan(x, y):
    try:
        return comparison_helper(x, y, '<')
    except:
        return x < y


def greaterThanEqual(x, y):
    try:
        return comparison_helper(x, y, '>=')
    except:
        return x >= y


def lessThanEqual(x, y):
    try:
        return comparison_helper(x, y, '<=')
    except:
        return x <= y

def In(x, y):
    try:
        return comparison_helper(x, y, ' in ')
    except:
        return x <= y

def notIn(x, y):
    runner = None
    if isinstance(x, fakeattr):
        runner = x._run
        x = x._parent
    else:
        x = json.dumps(x)
    if isinstance(y, fakeattr):
        runner = y._run
        y = y._parent
    else:
        y = json.dumps(y)
    if runner:
        return runner('! '+x+' in '+y+';', True)
    else:
        raise Exception("no runner")


def ternary(x, y):
    # TODO
    try:
        return comparison_helper(x, y, '==')
    except:
        return x == y


def And(x, y):
    try:
        return comparison_helper(x, y, '&&')
    except:
        return x and y


def Or(x, y):
    try:
        return comparison_helper(x, y, '||')
    except:
        return x or y


def Not(x):
    if isinstance(x, fakeattr):
        runner = x._run
        x = x._parent
    try:
        return runner('!'+x+';', True)
    except:
        return not x


def AND(x, y):
    try:
        return comparison_helper(x, y, '&')
    except:
        return x and y


def OR(x, y):
    try:
        return comparison_helper(x, y, '|')
    except:
        return x or y
def XOR(x, y):
    try:
        return comparison_helper(x, y, '^')
    except:
        return x or y
def lShift(x, y):
    try:
        return comparison_helper(x, y, '<<')
    except:
        return x or y
def rShift(x, y):
    try:
        return comparison_helper(x, y, '>>')
    except:
        return x or y


def NOT(x):
    if isinstance(x, fakeattr):
        runner = x._run
        x = x._parent
    try:
        return runner('~'+x+';', True)
    except:
        return not x


def typeof(x):
    if isinstance(x, fakeattr):
        runner = x._run
        x = x._parent
    try:
        return runner('typeof '+x+';', True)
    except:
        return not x
