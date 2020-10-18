from .Func import Func
from ..Var import Var
from .Operand import Operand
from ..Value import Value
from mystix.language.shared.ast.visitor import Visitor


class SimpleFunc(Func):

    def __init__(self, impacted_var: Var, op: Operand, v: Value):
        self.impacted_var: Var = impacted_var
        self.op: Operand = op
        self.rhs = v

    def accept(self, v: Visitor):
        return v.visit_simple_func(self)
