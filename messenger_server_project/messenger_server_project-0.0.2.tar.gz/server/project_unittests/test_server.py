import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import ERROR, ACTION, RESPONSE, PRESENCE, TIME, USER, ACCOUNT_NAME
from server import analyze_request


class TestServer(unittest.TestCase):
    correct_req_dict = {RESPONSE: 200}
    incorrect_req_dict = {RESPONSE: 400, ERROR: 'Incorrect Request'}

    def test_not_equal_1(self):
        self.assertNotEqual(analyze_request({ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Guest'}}),
                            self.incorrect_req_dict)

    def test_not_equal_2(self):
        self.assertNotEqual(analyze_request({ACTION: RESPONSE, TIME: 1, USER: {ACCOUNT_NAME: 'Guest'}}),
                            self.correct_req_dict)

    def test_not_equal_3(self):
        self.assertNotEqual(analyze_request({ACTION: RESPONSE, USER: {ACCOUNT_NAME: 'Guest'}}),
                            self.correct_req_dict)

    def test_not_equal_4(self):
        self.assertNotEqual(analyze_request({ACTION: RESPONSE, TIME: 1, USER: {ACCOUNT_NAME: 'Prisoner'}}),
                            self.correct_req_dict)

    def test_equal(self):
        self.assertEqual(analyze_request({ACTION: PRESENCE, TIME: 1, USER: {ACCOUNT_NAME: 'Prisoner'}}),
                         self.incorrect_req_dict)


if __name__ == '__main__':
    unittest.main()
