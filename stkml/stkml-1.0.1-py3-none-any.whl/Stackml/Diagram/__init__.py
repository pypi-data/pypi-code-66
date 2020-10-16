#Copyright STACKEO - INRIA 2020 .
import os

from Stackml import MODULE_DIR
from Stackml.Diagram.Graphviz.LayerDiagram import LayerDiagram
from Stackml.Diagram.Graphviz.RegionDiagram import RegionDiagram
from Stackml.Diagram.Graphviz.SystemDiagram import SystemDiagram
from Stackml.Diagram.Graphviz.Node import DiagramNode
from Stackml.Diagram.Graphviz.Layer import Diagramlayer
from Stackml.Diagram.Map.NodeMarker import NodeMarker
from Stackml.Diagram.Map.TopologyMap import TopologyMap
from Stackml.Stackml import Stackml


class StackmlDiagram:

    def __init__(self, icons: str):
        self._icon_dir = os.path.join(os.getcwd(), icons)
        self.default_icons = os.path.join(MODULE_DIR, 'templates/diagram/resources/')
        self.diagram_attr = {"pad": "0.2", "splines": "ortho", "nodesep": "0.6",
                             "ranksep": "1", "fontname": "Sans-Serif", "fontsize": "15", "fontcolor": "#2D3436"}

        self.funcs = {1: SystemDiagram, 2: RegionDiagram, 3: TopologyMap}

    def diagram_from_stackml(self, type_: int, stackml: Stackml, output: str) -> str:
        bound = self.funcs[type_](self.default_icons, self._icon_dir, self.diagram_attr)
        return bound.from_stackml(stackml, output)
