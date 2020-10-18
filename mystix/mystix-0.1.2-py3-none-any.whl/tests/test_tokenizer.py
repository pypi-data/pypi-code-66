
import unittest as ut
from typing import List
from mystix.ui.util import read_program_file
from mystix.language.tokenization import Tokenizer, TokenizationError
from mystix.language.shared.ast import Program


class TestTokenizer(ut.TestCase):

    def test_Tokenizer_1(self):
        def run_compile(content: str) -> List[str]:
            return Tokenizer(content).tokenize()
        p: List[str] = read_program_file(
            "tests/res/programs/example1", run_compile)
        res = ['program:', ';', 'source', '=', 'remote', "(",
               '"', 'www.coviddata.com/stream', '"', ")",';', 'map', "(",
               'source', ")", '"', 'case_date', '"', 'to', 'number', 'date', ';', 'number',
               'count', '=', '0', ';',
               'observe', "(", 'source', ")", "do", 'count++', ';', 'plot',
               'scatter_xy',"(" ,
               'date', ",", 'age', ")",
               'titled', '"', 'age_graph', '"', ';',
               'plot', 'line_xy', "(",'date', ",",'log','(', 'count', ')',")",
               'titled',
               '"', 'cases_', 'log', '"', ';', 'start!']
        self.assertEqual(res, p)

    def test_Tokenizer_2(self):
        def run_compile(content: str) -> List[str]:
            return Tokenizer(content).tokenize()
        p: List[str] = read_program_file(
            "tests/res/programs/example2", run_compile)
        res = ['<START>', ';', 'source', '=',
               '"', 'http://winterolympicsmedals.com/medals.csv', '"',
               ';', 'map', 'source', '"', 'Year', '"', 'to', 'number', 'year', ';',
               'map', 'source', '"', 'Medal', '"', 'to', 'number',
               'medal', ';',
               'year', '=', 'year','/', '100', ';',
               'year', '=', 'year','*', '10', ';',
               'year', '=', 'year','+', '23', ';',
               'year', '=', 'year','-', '12', ';',
               'plot', 'xy', 'year', 'medal', 'titled', 'medal_graph', ';', '<END>']
        self.assertEqual(res, p)

    def test_Tokenizer_3(self):
        def run_compile(content: str) -> List[str]:
            return Tokenizer(content).tokenize()
        p: List[str] = read_program_file(
            "tests/res/programs/example3", run_compile)
        res = ['<START>', ';', 'source', '=', 'static', 'remote',
               '"', 'http://winterolympicsmedals.com/medals.csv','"',
               ';', 'map', 'source', '"', 'Year', '"', 'to', 'number', 'year', ';',
               'map', 'source', '"', 'Medal', '"', 'to', 'number',
               'medal', ';', 'number', 'shortyear', '=', 'year', '-', '1900', ';', 'number', 'addyear', '=', 'year',
               '+', '50', ';', 'number', 'timesyear', '=', 'year', '*', '10', ';', 'number', 'divyear', '=', 'year',
               '/', '100', ';', 'number', 'sin',
               'year',
               '=',
               'sin',
               '(',
               'year',
               ')',
               ';',
               'number',
               'cos',
               'year',
               '=',
               'cos',
               '(',
               'year',
               ')',
               ';',
               'number',
               'exp',
               'year',
               '=',
               'exp',
               '(',
               'year',
               ')', ';', 'number', 'sqyear', '=', 'year', '^', '2', ';', 'number',
               'thing', '=', '2000', ';', 'thing--', ',', 'addyear++', ';', 'binary',
               'bin', '=', 'true', ';', 'binary', 'bin2', '=',
               'false', ';', 'plot', 'xy', 'cos', '(', 'year', ')', 'medal', 'titled',
                                    'cos', '_medal_graph', ';', '<END>']
        self.assertEqual(res, p)

    def test_Tokenizer_get_next(self):
        def run_compile(content: str) -> str:
            return Tokenizer(content).get_next()
        def run_compile2(content: str) -> str:
            token_obj = Tokenizer(content)
            token_obj.get_next()
            return token_obj.get_next()
        def run_compile3(content: str) -> str:
            token_obj = Tokenizer(content)
            token_obj.get_next()
            token_obj.get_next()
            return token_obj.get_next()
        p: str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertEqual('program:', p)
        p = read_program_file("tests/res/programs/example1", run_compile2)
        self.assertEqual(';', p)
        p = read_program_file("tests/res/programs/example1", run_compile3)
        self.assertEqual('source', p)

    def test_Tokenizer_check_next(self):
        def run_compile(content: str) -> str:
            token_obj = Tokenizer(content)
            return token_obj.check_next()
        p: str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertEqual('program:', p)
        
    def test_Tokenizer_check_next2(self):
        def run_compile(content: str) -> str:
            return Tokenizer(content).check_next()
        p: str = read_program_file("tests/res/programs/empty", run_compile)
        self.assertEqual("NO MORE TOKENS", p)

    def test_Tokenizer_check_token(self):
        def run_compile(content: str) -> bool:
            token_obj = Tokenizer(content)
            return token_obj.check_token('program:')
        def run_compile2(content: str) -> bool:
            token_obj = Tokenizer(content)
            token_obj.get_next()
            token_obj.get_next()
            return token_obj.check_token('program:')
        p: bool = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p)
        p = read_program_file("tests/res/programs/example1", run_compile2)
        self.assertFalse(p)

    def test_Tokenizer_get_and_check_next(self):
        def run_compile(content: str) -> str:
            return Tokenizer(content).get_and_check_next('program:')
        p: str = read_program_file("tests/res/programs/example1", run_compile)
        self.assertEqual('program:', p)

    def test_Tokenizer_get_and_check_next2(self):
        def run_compile(content: str):
            try:
                Tokenizer(content).get_and_check_next('source')
                self.fail()
            except TokenizationError:
                pass
        read_program_file("tests/res/programs/example1", run_compile)

    def test_Tokenizer_more_tokens(self):
        def run_compile(content: str) -> bool:
            return Tokenizer(content).more_tokens()
        p: bool = read_program_file("tests/res/programs/example1", run_compile)
        self.assertTrue(p)

    def test_Tokenizer_more_tokens2(self):
        def run_compile(content: str) -> bool:
            return Tokenizer(content).more_tokens()
        p: bool = read_program_file("tests/res/programs/empty", run_compile)
        self.assertFalse(p)
