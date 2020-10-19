from .Node import Node
from mystix.language.shared.primitives import ConcreteValue
from mystix.language.shared.ast.visitor import Visitor


class Value(Node):

    def __init__(self, v: ConcreteValue):
        self.value = v

    def accept(self, v: Visitor):
        return v.visit_value(self)
