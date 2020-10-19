from .Command import Command
from ..graphs_ast.Graph import Graph
from ..graphs_ast.Axis import Axis
from mystix.language.shared.ast.visitor import Visitor


class Plotter(Command):

    def __init__(self, graph: Graph, x_axis: Axis, y_axis: Axis, name: str):
        self.graph: Graph = graph
        self.x: Axis = x_axis
        self.y: Axis = y_axis
        self.graph_name: str = name

    def accept(self, v: Visitor):
        return v.visit_plotter(self)
