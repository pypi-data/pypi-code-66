from ..Node import Node
from ..visitor import Visitor


class Command(Node):
    """
    Parent class to Loader, Mapper, Holder, Math, and Plotter
    We assume all visitors visit the subclasses, but provide
    the accept stub for static analysis.
    """

    def accept(self, v: Visitor):
        pass
