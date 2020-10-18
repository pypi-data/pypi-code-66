import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from typing import List, Dict


class DiagramDescriptor(TypedDict):
    name: str
    filename: str
    direction: str
    curvestyle: str
    outformat: str
    show: bool
    graph_attr: dict
    node_attr: dict
    edge_attr: dict


class NodeAttrs(TypedDict):
    label: str
    direction: str
    graph_attr: dict


class NodeDescriptor(TypedDict):
    id: str
    provider: str
    resource_type: str
    name: str
    attrs: NodeAttrs


class DiagramAttrs(DiagramDescriptor):
    nodes: List[NodeDescriptor]
    links: Dict[str, str]
