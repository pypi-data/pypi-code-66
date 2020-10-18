from typing import List

from .Node import Node
from .commands_ast.Command import Command
from mystix.language.shared.ast.visitor import Visitor


class Body(Node):
    """
    Program body
    """
    def __init__(self, cs: List[Command]):
        self.commands: List[Command] = cs
        

    def accept(self, v: Visitor):
        return v.visit_body(self)