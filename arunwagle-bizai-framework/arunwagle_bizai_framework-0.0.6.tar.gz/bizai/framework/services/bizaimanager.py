
"""Use built-in abc to implement Abstract classes and methods"""

from abc import ABC, abstractmethod

"""Class Dedicated to Command"""


class BizaiManager(ABC):
    
    """process method"""    
    @abstractmethod
    def process(self):
        pass
