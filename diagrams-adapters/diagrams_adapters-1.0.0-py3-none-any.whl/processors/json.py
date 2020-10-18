import json
from .base import BaseAdapter


class JSONAdapter(BaseAdapter):
    """
    Generate diagram from json config string.
    """
    def __init__(self, data: str):
        self.diagram = json.loads(data)['diagram']
        if len(self.diagram) == 1:
            self.diagram = self.diagram[0]
        self.many = isinstance(self.diagram, list) and len(self.diagram) > 1

    def generate(self) -> None:
        if self.many:
            for item in self.diagram:
                super().__init__(item)
                super().generate()
        else:
            super().__init__(self.diagram)
            super().generate()
