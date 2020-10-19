class NameError(Exception):
    pass


class Name:
    MINIMUM_ELEMENT_LENGTH = 2
    ELEMENT_SEPARATOR = '__'
    CLASS_SEPARATOR = '___'


class Stub:

    @classmethod
    def from_stub(cls, stub: str):
        raise NameError(f'Method from_stub() must be overridden in child '
                        f'class \'{cls.__name__}\'')

    def stub(self):
        raise NameError(f'Method stub() must be overridden in child '
                        f'class \'{type(self).__name__}')

