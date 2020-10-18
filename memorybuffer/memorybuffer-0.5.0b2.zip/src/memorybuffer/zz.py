
class obj(object):
    pass
    #__slots__ = ('__cache__',)

    #def __init__(self, *args, **kwargs):
    #    pass


class AAA(obj):

    def __init__(self, a, b):
        super(AAA, self).__init__(a, b)


a = AAA(1, 2)