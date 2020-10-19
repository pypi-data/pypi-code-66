from .Node import Node
from mystix.language.shared.ast.visitor import Visitor


class Source(Node):

    def __init__(self, url: str):
        self.url: str = url

    def accept(self, v: Visitor):
        return v.visit_source(self)
