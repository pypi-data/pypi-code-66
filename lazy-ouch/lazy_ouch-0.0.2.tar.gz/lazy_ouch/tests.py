from unittest import TestCase

from lazy_ouch.core import CustomError


class CustomErrorTests(TestCase):

    def test_custom_error_message(self):
        ce = CustomError()
        self.assertEqual("CustomError - Custom Exception(Base)", ce.prepare_err_message())
        self.assertEqual("CustomError - Custom Exception(Base)", ce.prepare_description())
        self.assertEqual("", ce.prepare_args())
        self.assertEqual("", ce.prepare_kwargs())
