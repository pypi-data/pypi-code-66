import six
import functools


if six.PY3:
    reduce = functools.reduce


def partial(f, *args, **kwargs):
    pf = functools.partial(f, *args, **kwargs)
    f = functools.update_wrapper(pf, f)
    return f


def mapped(f):
    """
        coverts a simple function into a map-like function
        to be used as a decorator
    """
    @functools.wraps(f)
    def __mapped(i):
        return map(f, i)
    return __mapped


def reduced(f):
    """
        coverts a simple function into a reduce-like function
        to be used as a decorator
    """
    @functools.wraps(f)
    def __reduced(i):
        return reduce(f, i)
    return __reduced


def compose(*args):
    """
        composes a new function
        creates a function composed of other functions
    """
    def __pipe(v):
        for f in args:
            v = f(v)
        return v
    return __pipe


def translate(s, old, new):
    '''
        Translate each character in old to the character
        at the same positionin new
    '''
    if six.PY3:
        trans = type(old).maketrans(old, new)
    else:
        import string
        trans = string.maketrans(old, new)
    return s.translate(trans)


def sequence_matcher(a=None, b=None, isjunk=None):
    '''
        Short for the SequenceMatcher constructor.
        isjunk is moved to the right so it's not required
        when providing a and b parameters.
    '''
    import difflib
    return difflib.SequenceMatcher(isjunk, a, b)


def ratio(a, b):
    '''
        Return a measure of the sequences' similarity.
    '''
    return sequence_matcher(a, b).ratio()


def qratio(a, b):
    '''
        Return an upper bound on ratio() very quickly.
    '''
    return sequence_matcher(a, b).real_quick_ratio()


def opcodes(a, b):
    '''
        Get a list of tuples describing how to turn a into b.
    '''
    return sequence_matcher(a, b).get_opcodes()


def qmatch(a, b, ratio=1):
    '''
        Fast test the similarity of two sequences by testing with
        real_quick_ratio() first.
    '''
    smo = sequence_matcher(a, b)
    if smo.real_quick_ratio() < ratio:
        return False
    else:
        if smo.ratio() < ratio:
            return False
        else:
            return True


def hash(s, algorithm='sha1'):
    '''
        Return the digest of the string passed in s. This string may contain
        non-ASCII characters, including null bytes.

        algorithm parameter defaults to sha1.
    '''
    import hashlib
    h = hashlib.new(algorithm)
    h.update(s)
    return h.digest()


def int_bytes(n):
    '''
        Converts integers to bytes.
    '''
    r = six.binary_type()
    while n > 0:
        r += chr(n % 256).encode()
        n = int(n / 256)
    return r
