from mystix.language.shared.ast.visitor import Visitor
from abc import ABC, abstractmethod


class Node(ABC):
    """
    The highest-level type in the syntax tree. Should not be directly
    instantiated.
    """
    
    @abstractmethod
    def accept(self, v: Visitor):
        pass
