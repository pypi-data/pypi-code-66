from unittest import TestCase

from mystix.language.evaluation.main import run_program
from mystix.language.parsing import ParseError
from mystix.language.evaluation.errors import LanguageError


class EndToEndTests(TestCase):

    def test_undefined_source(self):
        code, err = run_program("tests/res/programs/e2e_undefined_source.mstx")
        self.assertEqual(1, code)
        self.assertIsInstance(err, LanguageError)

    def test_invalid_command(self):
        code, err = run_program("tests/res/programs/e2e_comment_command.mstx")
        self.assertEqual(2, code)
        self.assertIsInstance(err, ParseError)

    def test_nexist_file(self):
        code, err = run_program("tests/res/programs/e2e_does_not_exist.mstx")
        self.assertEqual(3, code)
        self.assertIsInstance(err, FileNotFoundError)
