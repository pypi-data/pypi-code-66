from .Command import Command
from ..Var import Var
from ..Source import Source
from mystix.language.shared.ast.visitor import Visitor


class Loader(Command):

    def __init__(self, name: Var, source: Source):
        self.name: Var = name
        self.source: Source = source

    def accept(self, v: Visitor):
        return v.visit_loader(self)
