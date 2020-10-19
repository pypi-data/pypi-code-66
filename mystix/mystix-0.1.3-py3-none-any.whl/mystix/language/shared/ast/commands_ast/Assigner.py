from .Command import Command
from ..Value import Value
from ..Declare import Declare
from mystix.language.shared.ast.visitor import Visitor


class Assigner(Command):

    def __init__(self, decl: Declare, value: Value):
        self.decl = decl
        self.value: Value = value

    def accept(self, v: Visitor):
        return v.visit_assigner(self)
