from typing import List

from ..Node import Node
from .Func import Func
from mystix.language.shared.ast.visitor import Visitor


class MathFuncs(Node):

    def __init__(self, function_list: List[Func]):
        self.mth_func_lst: List[Func] = function_list

    def accept(self, v: Visitor):
        return v.visit_math_funcs(self)
