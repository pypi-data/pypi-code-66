from abc import abstractmethod

from .SpAuth import SpAuth


class Sp(SpAuth):
    def __init__(self):
        super(Sp, self).__init__()
        self.data = self.search()
        self.parsed = self.parse()

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def parse(self):
        pass
