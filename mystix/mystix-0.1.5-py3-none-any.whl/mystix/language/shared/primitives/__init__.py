"""
Contains all internal data-structures which represent
concrete items in our engine. These are expressed with
the 'Concrete' prefix so as to not pollute the abstract
syntax namespace.
"""

from .types import Types
from .values import Value as ConcreteValue
from .graphs import Graph as ConcreteGraph
from .numerical import NumOp as ConcreteNumOp
