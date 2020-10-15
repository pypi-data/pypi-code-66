""" Unit-тесты клиента """

import sys
import os
import unittest
from client.common.vars import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import generate_requirement, server_answer
sys.path.append(os.path.join(os.getcwd(), '..'))



class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_def_generate_presence(self):
        """Тест коректного запроса"""
        test = generate_requirement()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(server_answer({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(server_answer({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        with self.assertRaises(ValueError):
            server_answer({})


if __name__ == '__main__':
    unittest.main()
