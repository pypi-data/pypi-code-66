from .Command import Command
from ..Var import Var
from ..Declare import Declare
from mystix.language.shared.ast.visitor import Visitor


class Mapper(Command):

    def __init__(self, src: Var, tbl_field: str, decl: Declare):
        self.src: Var = src
        self.tbl_field: str = tbl_field
        self.decl = decl

    def accept(self, v: Visitor):
        return v.visit_mapper(self)
