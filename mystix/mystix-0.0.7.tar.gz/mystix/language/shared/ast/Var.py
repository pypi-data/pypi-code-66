from .Node import Node
from mystix.language.shared.ast.visitor import Visitor


class Var(Node):

    def __init__(self, name: str):
        self.name = name

    def accept(self, v: Visitor):
        return v.visit_var(self)
