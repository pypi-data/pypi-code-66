from .pipeable import pipeable
import toolz
import types
import toolz.curried.operator as op

# Reference to THIS module
__self__ = __import__(__name__)

# Functions from toolz to be added HERE
__all__ = [m for m in dir(op) if not m.startswith('__')]


# Decorate and add all the toolz.curried.operator HERE
for name in __all__:
    obj = getattr(op, name)
    if isinstance(obj, toolz.functoolz.curry):
        setattr(__self__, name, pipeable(obj.func))
    elif isinstance(obj, types.FunctionType):
        setattr(__self__, name, pipeable(obj))

