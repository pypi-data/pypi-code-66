from .Node import Node
from .Type import Type
from .Var import Var
from mystix.language.shared.ast.visitor import Visitor


class Declare(Node):

    def __init__(self, t: Type, v: Var):
        self.type = t
        self.var = v

    def accept(self, v: Visitor):
        return v.visit_declare(self)
