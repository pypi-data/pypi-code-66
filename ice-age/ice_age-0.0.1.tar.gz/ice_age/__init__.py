__author__ = 'dpepper'
__version__ = '0.0.1'
__all__ = [
    'IceAge',
    'TestCase',
]


import os
import unittest


class IceAge:
    @classmethod
    def freeze(cls):
        cls.env = os.environ.copy()

    @classmethod
    def isFrozen(cls):
        return hasattr(cls, 'env')

    @classmethod
    def restore(cls):
        os.environ.clear()
        os.environ.update(cls.env)


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        IceAge.freeze()
        self.addCleanup(IceAge.restore)
