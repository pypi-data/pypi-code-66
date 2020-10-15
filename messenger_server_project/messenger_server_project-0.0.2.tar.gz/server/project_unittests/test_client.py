import sys
import os
import unittest

sys.path.append('../')
from common.variables import RESPONSE, ERROR, ACTION, PRESENCE
from client import create_presence_message, analyze_answer


class TestClient(unittest.TestCase):

    def test_not_equal_1(self):
        self.assertNotEqual(analyze_answer({RESPONSE: 200}), '400 : OK')

    def test_not_equal_2(self):
        self.assertNotEqual(analyze_answer({RESPONSE: 200}), '200 : BAD ERROR')

    def test_raises_1(self):
        with self.assertRaises(ValueError): \
                (analyze_answer({ERROR: 400}), '400 : OK')

    def testin(self):
        test = create_presence_message(account_name='Guest')
        self.assertIn(ACTION, test)

    def testnotin(self):
        test = create_presence_message(account_name='Guest')
        self.assertNotIn(PRESENCE, test)


if __name__ == '__main__':
    unittest.main()
