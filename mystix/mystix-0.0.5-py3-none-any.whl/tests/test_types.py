import sys
import unittest

from mypy import api


class TypingTests(unittest.TestCase):

    def test_types(self):
        result = api.run(["mystix", "tests"])
        if result[0]:
            print('\nType checking report:\n')
            print(result[0])  # stdout
        if result[1]:
            print('\nError report:\n')
            print(result[1])  # stderr
        status: int = result[2]
        if result[2] != 0:
            self.fail(status)
        print('\nExit status:', status)
