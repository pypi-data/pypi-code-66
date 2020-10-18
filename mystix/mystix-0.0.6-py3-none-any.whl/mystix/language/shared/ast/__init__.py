"""
AST Data Structures
This is intended to reflect the grammar as defined in the grammar.txt document. Any
change in one definition should accompany a change in the other so that we maintain
consistency.
"""

from .Node import Node
from .Program import Program
from .Body import Body
from .commands_ast.Command import Command
from .commands_ast.Loader import Loader
from .commands_ast.Mapper import Mapper
from .commands_ast.Plotter import Plotter
from .commands_ast.Trigger import Trigger
from .commands_ast.Assigner import Assigner
from .Var import Var
from .Source import Source
from .Type import Type
from .Value import Value
from .graphs_ast.Graph import Graph
from .graphs_ast.Axis import Axis
from .graphs_ast.Axis import VarAxis, FuncAxis
from .math_ast.MathFuncs import MathFuncs
from .math_ast.Func import Func
from .math_ast.SimpleFunc import SimpleFunc
from .math_ast.FastFunc import FastFunc, Increment, Decrement
from .math_ast.BuiltinFunc import BuiltinFunc
from .math_ast.Operand import Operand
from .Declare import Declare
