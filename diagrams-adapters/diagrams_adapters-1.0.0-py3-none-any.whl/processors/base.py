import abc
import operator as operators
from typing import List, ClassVar, Dict
from diagrams import Diagram, Node
from importlib import import_module

from diagrams_adapters.typings import DiagramAttrs, DiagramDescriptor, NodeDescriptor


DIAGRAM_PKG = 'diagrams'
NODE_LINK_OPERATOR_MAPPING = {
    '>>': 'rshift',
    '<<': 'lshift',
    '-': 'sub'
}


class BaseAdapter(abc.ABC):
    _data: DiagramDescriptor = None
    _nodes: List[NodeDescriptor] = []
    _links: Dict[str, str]
    many = False

    def __init__(self, data: DiagramAttrs):
        for key in ['nodes', 'links']:
            value = data.pop(key)
            setattr(self, f'_{key}', value)
        self._data = data

    @staticmethod
    def _get_module_package(node: dict) -> List[str]:
        ret = [DIAGRAM_PKG]
        for key in ('provider', 'resource_type'):
            ret.append(node[key])
        return ret

    def _import_node(self, node: dict) -> ClassVar[Node]:
        import_package = '.'.join(self._get_module_package(node))
        import_name = node['name']
        module = import_module(import_package)
        return getattr(module, import_name)

    def _get_node_instance_from(self, node_data: dict) -> Node:
        node_class = self._import_node(node_data)
        if node_class:
            return node_class(**node_data['attrs'])

    @staticmethod
    def apply_operator(operator, *items):
        for idx, item in enumerate(items):
            if idx + 1 >= len(items):
                break
            operator(item, items[idx + 1])

    def _link(self, nodes, operator, sequence) -> None:
        for item in sequence:
            args = [nodes[_id] for _id in item]
            if args:
                self.apply_operator(operator, *args)

    def _generate(self, diagram_data: DiagramDescriptor) -> None:
        with Diagram(**diagram_data):
            nodes = {}
            for node_data in self._nodes:
                instance = self._get_node_instance_from(node_data)
                nodes[node_data['id']] = instance or Node()

            for key in self._links:
                operator = getattr(operators, NODE_LINK_OPERATOR_MAPPING[key])
                self._link(nodes, operator, self._links[key])

    @abc.abstractmethod
    def generate(self):
        self._generate(self._data)
