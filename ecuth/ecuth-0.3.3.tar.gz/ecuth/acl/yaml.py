# third-party imports
import yaml

# local imports
from .base import Acl


class YAMLAcl(Acl):

    def __init__(self, data):
        self.data = yaml.load(data, Loader=yaml.FullLoader)

    def read(self, item):
        return self.data['items'].get(item) & 4 > 0

    def write(self, item):
        return self.data['items'].get(item) & 2 > 0

    def val(self, item):
        return self.data['items'].get(item)

    def __str__(self):
        return self.data.__str__()
