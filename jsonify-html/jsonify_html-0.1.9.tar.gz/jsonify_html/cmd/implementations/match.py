from ..base import JsonifyCommand
from ..exceptions import ArgumentError
from lxml.cssselect import CSSSelector


class CMDMatch(JsonifyCommand):
    def __init__(self, root, args):
        super().__init__(root)
        self.implementation, self.selector = args

    def execute(self):
        if self.implementation in ['x', 'xpath']:
            xpath = self.selector
        elif self.implementation in ['css', 'c']:
            xpath = CSSSelector(self.selector).path
        else:
            raise ArgumentError('invalid selector implementation.')
        for result in self.root.xpath(xpath):
            if result == self.root:
                return True
        return False
