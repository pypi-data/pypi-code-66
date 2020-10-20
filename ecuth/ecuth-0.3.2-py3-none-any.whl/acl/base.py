class Acl:

    def read(self, item):
        raise NotImplementedError

    def write(self, item):
        raise NotImplementedError

    def val(self, item):
        raise NotImplementedError

