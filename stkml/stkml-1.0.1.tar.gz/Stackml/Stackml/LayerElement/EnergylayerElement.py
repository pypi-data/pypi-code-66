#Copyright STACKEO - INRIA 2020 .
from Stackml.Stackml.LayerElement import LayerElement


class EnergylayerElement(LayerElement):

    def __init__(self, name: str, hub):
        super().__init__(name, type(self).__name__, hub)
