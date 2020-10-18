from .Func import Func
from ..Var import Var
from mystix.language.shared.ast.visitor import Visitor


class FastFunc(Func):

    def __init__(self, impacted_var: Var):
        self.impacted_var: Var = impacted_var


class Increment(FastFunc):

    def accept(self, v: Visitor):
        return v.visit_increment(self)


class Decrement(FastFunc):

    def accept(self, v: Visitor):
        return v.visit_decrement(self)
