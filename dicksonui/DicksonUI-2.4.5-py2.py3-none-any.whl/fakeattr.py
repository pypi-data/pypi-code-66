import json

class JSONError(Exception):pass

def value_handler(value):
    if isinstance(value, fakeattr):
        return value._parent
    else:
        try:
            return str(json.dumps(value))
        except Exception as e:
            raise JSONError(str(e))

class fakeattr():
    def __init__(self, run, parent):
        self._run = run
        self._parent = parent

    def __get__(self):
        return self._run(self._parent+';', True)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return fakeattr(self._run, self._parent+'.'+name)

    def __setattr__(self, name, value):
        if name in ('_parent','_run'):
            self.__dict__[name] = value
        else:
            try:
                self._run(self._parent+'.'+name+'='+value_handler(value)+';')
            except:
                raise RuntimeError("cannot set this value( %s )" % value)

    def __repr__(self):
        try:
            return repr(self.__get__())
        except:
            return "<object %s>" % self._parent

    def __str__(self):
        return self._run(self._parent+'.toString();', True)

    def __coerce__(self,value):
        try:
            return coerce(self.__get__(), value)
        except:
            return None

    def __call__(self, *args, **kwargs):
        e = kwargs.setdefault('e', True)
        e = kwargs.pop('e')
        nargs = []
        for arg in args:
            nargs.append(value_handler(arg))
        return self._run(self._parent+'(%s);'%','.join(nargs), e)

    def __setitem__(self, key, value):
        try:
            if isinstance(key, int):
                self._run(self._parent +
                          value_handler([key])+"="+value_handler(value)+';')
            else:
                self.__setattr__(key, value)
        except Exception as e:
            raise e

    def __and__(self, value):
        try:
            return self._run('%s && %s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() & value

    def __rand__(self, value):
        try:
            return self._run('%s && %s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value & self.__get__()

    def __xor__(self, value):
        try:
            return self._run('%s ^ %s;'%(self._parent, value_handler(value)), True)
        except JSONError:
            return self.__get__() ^ value

    def __rxor__(self, value):
        try:
            return self._run('%s ^ %s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value ^ self.__get__()

    def __or__(self, value):
        try:
            return self._run('%s || %s;'%(self._parent, value_handler(value)), True)
        except JSONError:
            return self.__get__() | value

    def __ror__(self, value):
        try:
            return self._run('%s || %s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value | self.__get__()

    def __hash__(self):
        return hash(self.__get__())

    def __getitem__(self, key):
        try:
            return self[key]
        except:
            try:
                return getattr(self.__get__(), key)
            except:
                return self[key]

    def __lt__(self, value):
        try:
            return self._run('%s<%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()<value

    def __le__(self, value):
        try:
            return self._run('%s<=%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()<=value

    def __eq__(self, value):
        try:
            return self._run('%s==%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()==value

    def __ne__(self, value):
        try:
            return self._run('%s!=%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()!=value

    def __gt__(self, value):
        try:
            return self._run('%s>%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()>value

    def __ge__(self, value):
        try:
            return self._run('%s>=%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()>=value

    def __add__(self, value):
        try:
            return self._run('%s+%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()+value

    def __radd__(self, value):
        try:
            return self._run('%s+%s;'%(value_handler(value), self._parent), True)
        except JSONError:
            return value + self.__get__()

    def __sub__(self, value):
        try:
            return self._run('%s-%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__()-value

    def __rsub__(self, value):
        try:
            return self._run('%s-%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value - self.__get__()

    def __mul__(self, value):
        try:
            return self._run('%s*%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() * value

    def __rmul__(self, value):
        try:
            return self._run('%s*%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value * self.__get__()

    def __mod__(self, value):
        try:
            return self._run('%s % %s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() % value

    def __rmod__(self, value):
        try:
            return self._run('%s+%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value % self.__get__()

    def __divmod__(self, value):
        try:
            return self._run('[({0}-({0}%{1}))/{1},{0}%{1}];'.format(self._parent,value_handler(value)), True)
        except JSONError:
            return divmod(self.__get__(),value)

    def __rdivmod__(self, value):
        try:
            return self._run('[({0}-({0}%{1}))/{1},{0}%{1}];'.format(value_handler(value), self._parent), True)
        except JSONError:
            return divmod(value,self.__get__())

    def __pow__(self, value, mod=None):
        try:
            if mod:
                return self._run('Math.pow(%s,%s)%%s;'%(self._parent,value_handler(value),value_handler(mod)), True)
            else:
                return self._run('Math.pow(%s,%s);'%(self._parent,value_handler(value)), True)
        except JSONError:
            return pow(self.__get__(),value)

    def __rpow__(self, value, mod=None):
        try:
            if mod:
                return self._run('Math.pow(%s,%s);%%s'%(value_handler(value),self._parent, value_handler(mod)), True)
            else:
                return self._run('Math.pow(%s,%s);'%(value_handler(value),self._parent), True)
        except JSONError:
            return pow(value, self.__get__(), mod)

    def __neg__(self):
        return self._run('- %s;'%(self._parent), True)

    def __pos__(self):
        return self._run('+%s;'%(self._parent), True)

    def __abs__(self):
        try:
            return self._run('Math.abs(%s);'%self._parent, True)
        except JSONError:
            return abs(slf.__get__())

    def __bool__(self):
        return self._run(self._parent+'.valueOf() == 0 ? false : true;', True)

    def __invert__(self):
        return self._run('~'+self._parent+';', True)

    def __lshift__(self, value):
        try:
            return self._run('%s<<%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() << value

    def __rlshift__(self, value):
        try:
            return self._run('%s<<%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value << self.__get__()

    def __rshift__(self, value):
        try:
            return self._run('%s>>%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() >> value

    def __rrshift__(self, value):
        try:
            return self._run('%s>>%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value >> self.__get__()

    def __int__(self, base=10):
        if base!=10:
            return self._run('parseInt(%s,%i);'%(self._parent,base), True)
        return self._run('parseInt(%s);'%self._parent, True)

    def __float__(self):
        return self._run('parseFloat(%s);'%self._parent, True)

    def __floordiv__(self, value):
        try:
            return self._run('Math.floor(%s/%s);'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() // value

    def __rfloordiv__(self, value):
        try:
            return self._run('Math.floor(%s/%s);'%(value_handler(value),self._parent), True)
        except JSONError:
            return value // self.__get__()

    def __truediv__(self, value):
        try:
            return self._run('%s/%s;'%(self._parent,value_handler(value)), True)
        except JSONError:
            return self.__get__() / value

    def __rtruediv__(self, value):
        try:
            return self._run('%s/%s;'%(value_handler(value),self._parent), True)
        except JSONError:
            return value / self.__get__()

    def __index__(self):
        return self.__get__().__index__() # not useful see https://docs.python.org/3/reference/datamodel.html#object.__index__

    def conjugate(self):
        return self.__get__().conjugate(*a, **kw)

    def bit_length(self):
        return self._run('%s.toString(2).match(/1/g).length;'%self._parent, True)

    def to_bytes(self, *a, **kw):
        return self.__get__().to_bytes(*a, **kw)

    @classmethod
    def from_bytes(self, *a, **kw):
        return self.__get__().from_bytes(*a, **kw)

    def __trunc__(self):
        return self._run('Math.trunc(%s/%s);'%self._parent, True)

    def __floor__(self):
        return self._run('Math.floor('+self._parent+');', True)

    def __ceil__(self):
        return self._run('Math.ceil('+self._parent+');', True)

    def __round__(self, ndigits=None):
        try:
            if ndigits:
                return self._run('Math.round(%s + "e+%i")  + "e-%i"'%(self._parent,ndigits,ndigits), True)
            else:
                return self._run('Math.round('+self._parent+');', True)
        except JSONError:
            return round(self.__get__(),ndigits)

    def __getnewargs__(self):
        return self.__get__().__getnewargs__()

    def __format__(self, format_spec=''):
        return format(self.__get__(), format_spec)

    def __sizeof__(self):
        return self.__get__().__sizeof__()

    @property
    def real(self):
        return self.__get__().real

    @property
    def imag(self):
        return self.__get__().imag

    @property
    def numerator(self):
        return self.__get__().numerator

    @property
    def denominator(self):
        return self.__get__().denominator

    def as_integer_ratio(self):
        return self.__get__().as_integer_ratio()

    @classmethod
    def fromhex(self, string):
        return self.__get__().fromhex(string)

    def hex(self):
        return hex(self.__get__())

    def is_integer(self):
        return self.__get__().is_integer()

    @classmethod
    def __getformat__(self, typestr):
        return self.__get__().__getformat__(typestr)

    @classmethod
    def __set_format__(self, typestr, fmt):
        return self.__get__().__set_format__(typestr, fmt)

    def __iter__(self):
        return iter(self.__get__())

    def __len__(self):
        return self._run(self._parent+'.length;', True)

    def __contains__(self, key):
        try:
            return self._run('%s in %s;'%(value_handler(key),self._parent), True)
        except JSONError:
            return key in self.__get__()

    def encode(self, encoding='utf-8', errors='strict'):
        return self.__get__().encode(encoding, errors)

    def replace(self, old, new, count=-1):
        if count< 0:
            return self._run(self._parent+'.replace(/%s/g,"%s");' % (old, new), True)
        else:
            return self._run(self._parent+'.replace("%s","%s");' % (old, new), True).replace(old,new,count-1)

    def split(self, sep=None, maxsplit=-1):
        r = self._run(self._parent+'.split("%s");'%sep, True)
        if maxsplit > -1:
            return r[:maxsplit]
        return r

    def rsplit(self, sep=None, maxsplit=-1):
        return self.split(sep, maxsplit).reverse()

    def join(self, iterable):
        return self.__get__().join(iterable)

    def capitalize(self):
        return self._run('{0}.slice(0, 1).toUpperCase() + {0}.slice(1).toLowerCase();'.format(self._parent), True)

    def casefold(self, *a, **kw):
        return self.__get__().casefold(*a, **kw)

    def title(self):
        return self.__get__().title()

    def center(self, width, fillchar=' '):
        return self.__get__().center(width, fillchar)

    def expandtabs(self, tabsize=8):
        return self.__get__().expandtabs(tabsize)

    def find(self, sub, start=0, end=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.indexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).indexOf("%s");' %
                          (start, end, value), True)
        return r

    def partition(self, *a, **kw):
        return self.__get__().partition(*a, **kw)

    def ljust(self, width, fillchar=' '):
        return self.__get__().ljust(width, fillchar)

    def lower(self):
        return self._run(self._parent+'.toLowerCase();', True)

    def lstrip(self, chars=None):
        return self.__get__().lstrip(chars)

    def rfind(self, sub, start=0, end=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.LastIndexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, end, value), True)
        return r

    def rindex(self, value, start=0, stop=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.lastIndexOf("%s",%i);' %
                          (value, start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, stop, value), True)
        if r == -1:
            raise ValueError("substring not found")
        return r

    def rjust(self, width, fillchar=' '):
        return self.__get__().rjust(width, fillchar)

    def rstrip(self, chars=None):
        return self.__get__().rstrip(chars)

    def rpartition(self, sep):
        return self.__get__().rpartition(sep)

    def splitlines(self, keepends=False):
        return self.__get__().splitlines(keepends)

    def strip(self, chars=None):
        ie8code = '''if (!String.prototype.trim) {
  String.prototype.trim = function () {
    return this.replace(/^[\\s\\uFEFF\\xA0]+|[\\s\\uFEFF\\xA0]+$/g, '');
  };
};'''  # for IE 8
        if not chars:
            try:
                return self._run(self._parent+'.trim();', True)
            except:
                return self._run(ie8code+self._parent+'.trim();', True)
        return self.__get__().strip(chars)

    def swapcase(self):
        return self.__get__().swapcase()

    def translate(self, table):
        return self.__get__().translate(table)

    def upper(self):
        c

    def startswith(self, *a, **kw):
        return self.__get__().rindex(*a, **kw)

    def endswith(self, *a, **kw):
        return self.__get__().endswith(*a, **kw)

    def isascii(self):
        return self.__get__().isascii()

    def islower(self):
        return self.__get__().islower()

    def isupper(self):
        return self.__get__().isupper()

    def istitle(self):
        return self.__get__().istitle()

    def isspace(self):
        return self.__get__().isspace()

    def isdecimal(self):
        return self.__get__().isdecimal()

    def isdigit(self):
        return self.__get__().isdigit()

    def isnumeric(self):
        return self.__get__().isnumeric()

    def isalpha(self):
        return self.__get__().isalpha()

    def isalnum(self):
        return self.__get__().isalnum()

    def isidentifier(self):
        return self.__get__().isidentifier()

    def isprintable(self):
        return self.__get__().isprintable()

    def zfill(self, width):
        return self.__get__().zfill(width)

    def format(self, *a, **kw):
        return self.__get__().format(*a, **kw)

    def format_map(self, *a, **kw):
        return self.__get__().format_map(*a, **kw)

    @staticmethod
    def maketrans(x, y=None, z=None):
        return self.__get__().maketrans(x, y, z)

    def __delitem__(self, key):
        self._run(self._parent+".pop("+str(int(key))+");", False)

    def __iadd__(self, value):
        try:
            self._run(self._parent+"+="+value_handler(value)+';', False)
        except Exception as e:
            raise e

    def __imul__(self, value):
        try:
            self._run(self._parent+"*="+value_handler(value)+';', False)
        except Exception as e:
            raise e

    def __iter__(self):
        return iter(self.__get__())

    def __reversed__(self):
        return reversed(self.__get__())

    def append(self, object):
        try:
            self._run(self._parent+".push("+value_handler(object)+');', False)
        except Exception as e:
            raise e

    def clear(self):
        code='''if (Array.isArray(this)) {
        this=[];
    } else if (this.constructor === Object) {
        this={};
    } else {throw ReferenceError(\"this has no attribute 'clear'\")}'''
        try:
            self._run(code.replace('this',self._parent), False)
        except Exception as e:
            raise e
    def copy(self):
        return self.__get__()

    def count(self, value):
        code='''if (!String.prototype.count) {
String.prototype.count = function (x) {
while (true) {
i = this.indexOf(x, i);
if (i < 0) break;
count += 1;
i += Math.max(1, x.length);
} return count;};
};'''
        return self.__get__().count()

    def extend(self, iterable):
        try:
            self._run(self._parent +
                      ".push.apply("+self._parent+","+value_handler(list(iterable))[1:-1]+');', False)
        except Exception as e:
            raise e

    def index(self, value, start=0, stop=2147483647):
        if stop == 2147483647:
            r = self._run(self._parent+'.indexOf(%s,%i);' %
                          (value_handler(value), start), True)
        else:
            r = self._run(self._parent+'.slice(%i,%i).LastindexOf("%s");' %
                          (start, stop, value_handler(value)), True)
        if r == -1:
            raise ValueError("substring not found")
        return r
        return self.__get__().index(value, start, stop)

    def insert(self, index, object):
        self._run(self._parent+".splice(%i,0,%s);" %
                  (index, value_handler(object)))

    def pop(self, index=-1):  # TODO: working with dicts
        try:
            if index > -1:
                self._run(self._parent+".pop("+str(index)+");")
            else:
                self._run(self._parent+".pop();")
        except Exception as e:
            raise e

    def remove(self, value):
        self._run("if(! %s in %s){throw Error('list.remove(x): x not in list')};%s.splice(%s.indexOf(%s),1);" % (
            value_handler(value), self._parent, self._parent, self._parent, value_handler(value)))

    def reverse(self):
        self._run(self._parent+".reverse();")

    def sort(self, key=None, reverse=False):
        code = "%s.sort(function(a, b){if(a<b){return -1};if(a>b){return 1};return 0})"% self._parent
        if key:
            arr = self.__get__()
            arr.sort(key=key, reverse=reverse)
            self._run(self._parent+"=%s;" % value_handler(arr))
            return
        if reverse:
            self._run(code +'.reverse();')
        else:
            self._run(code +';')

    def items(self):
        return self.__get__().items()

    def keys(self):
        return self.__get__().items()

    def values(self):
        return self.__get__().values()

    def popitem(self):
        return self.pop()

    def setdefault(self, key, default=None):
        return self.__get__().setdefault(self, key, default)

    def update(self, *a, **kw):
        new = {}
        new.update(*a, **kw)
        src = ""
        for i in new:
            src += self._parent+"."+i+"="+value_handler(new[i])+";"
        self._run(src, False)

    @classmethod
    def fromkeys(self, iterable, value=None):
        return self.__get__().fromkeys(iterable, value)
