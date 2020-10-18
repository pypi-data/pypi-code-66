
"""Use built-in abc to implement Abstract classes and methods"""

from abc import ABC, abstractmethod

"""Class Dedicated to StepExecutor"""


class StepExecutor(ABC):

    """constructor method"""

    def __init__(self):
        print("#######init StepExecutor######")
        

    """execute step"""
    @abstractmethod
    def execute(self, **input):
        pass

    # def __repr__(self):
    #     return "Test input:% s " % (self._input)

    # def __str__(self):
    #     return "From str method of Test: a is % s, " \
    #         " " % (self._input)
