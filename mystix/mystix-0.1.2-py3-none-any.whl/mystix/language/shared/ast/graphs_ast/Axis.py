from ..Node import Node
from ..Var import Var
from ..math_ast.MathFuncs import Func
from mystix.language.shared.ast.visitor import Visitor


class Axis(Node):

    def accept(self, v: Visitor):
        pass


class VarAxis(Axis):

    def __init__(self, v: Var):
        self.var = v

    def accept(self, v: Visitor):
        return v.visit_var_axis(self)


class FuncAxis(Axis):

    def __init__(self, f: Func):
        self.fun = f

    def accept(self, v: Visitor):
        return v.visit_func_axis(self)
