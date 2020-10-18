from .Node import Node
from mystix.language.shared.primitives import Types
from mystix.language.shared.ast.visitor import Visitor


class Type(Node):

    def __init__(self, t: Types):
        self.type = t

    def accept(self, v: Visitor):
        return v.visit_type(self)
