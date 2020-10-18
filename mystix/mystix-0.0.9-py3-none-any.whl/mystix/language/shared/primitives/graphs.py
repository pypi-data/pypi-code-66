

class Graph:
    def equals(self, g) -> bool:
        return False


class LineXYGraph(Graph):
    def equals(self, g: Graph) -> bool:
        return isinstance(g, LineXYGraph)

    def __repr__(self):
        return "line"


class ScatterXYGraph(Graph):
    def equals(self, g: Graph) -> bool:
        return isinstance(g, ScatterXYGraph)

    def __repr__(self):
        return "scatter"
