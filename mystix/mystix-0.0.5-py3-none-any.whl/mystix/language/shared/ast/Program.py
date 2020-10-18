from .Node import Node
from .Body import Body
from mystix.language.shared.ast.visitor import Visitor


class Program(Node):
    """
    Represents a program. This contains no additional fields other than
    the program body but is kept here for consistency with the Grammar
    """
    def __init__(self, b: Body):
        self.body: Body = b
        

    def accept(self, v: Visitor):
        return v.visit_program(self)
