
import unittest as ut
from mystix.ui.util import read_program_file
from mystix.language.tokenization.tokenizer import Tokenizer, TokenizationError
from mystix.language.parsing.parser import Parser, ParseError
from mystix.language.shared.ast import *
from mystix.language.shared.primitives import Types
from mystix.language.shared.primitives import values
from mystix.language.shared.primitives.graphs import LineXYGraph, ScatterXYGraph
from mystix.language.shared.primitives.numerical import NumOp, NumFunction


class TestParse(ut.TestCase):

    def test_program(self):
        tokens, parser = self.setup("parse_program")
        res = parser.parseProgram()
        commands = res.body.commands
        self.assertIsInstance(commands[0].graph.graph, LineXYGraph)
        self.assertEqual(commands[0].x.var.name, 'x')
        self.assertEqual(commands[0].y.fun.fun, NumFunction.LOG)
        self.assertEqual(commands[0].graph_name, 'line')
        self.assertEqual(commands[1].var1.name, 'triggerVar')
        self.assertEqual(len(commands[1].math_funcs.mth_func_lst), 2)
        self.assertEqual(commands[1].math_funcs.mth_func_lst[0].impacted_var.name, 'triggerVar')
        self.assertEqual(commands[1].math_funcs.mth_func_lst[1].impacted_var.name, 'triggerVar')
        self.assertEqual(commands[1].math_funcs.mth_func_lst[1].op.op, NumOp.PLUS)
        self.assertIsInstance(commands[1].math_funcs.mth_func_lst[1].rhs.value,
                              values.IntegerValue)
        self.assertTrue(commands[1].math_funcs.mth_func_lst[1].rhs.value.equals(
            values.IntegerValue(1)))
        self.assertEqual(commands[2].decl.type.type, Types.CATEGORY)
        self.assertEqual(commands[2].decl.var.name, 'a')
        self.assertTrue(commands[2].value.value.equals(values.IntegerValue(123456)))

    def test_example1(self):
        tokens, parser = self.setup("example1")
        res = parser.parseProgram()
        print("Parsed")
        commands = res.body.commands
        self.assertIsInstance(commands[0], Loader)
        self.assertIsInstance(commands[1], Mapper)
        self.assertIsInstance(commands[2], Assigner)
        self.assertIsInstance(commands[3], Trigger)
        self.assertIsInstance(commands[4], Plotter)
        self.assertIsInstance(commands[5], Plotter)

    def test_loader(self):
        tokens, parser = self.setup("parse_loader")
        res = parser.parseLoader()
        self.assertEqual(res.name.name, "x")
        self.assertEqual(res.source.url, "www.coviddata.com/stream")
    
    def test_fast_func(self):
        tokens, parser = self.setup("parse_fast_func")
        res = parser.parseFastFunc()
        self.assertEqual(res.impacted_var.name, 'x')
        self.assertIsInstance(res, Increment)

    def test_simp_func(self):
        tokens, parser = self.setup("parse_simp_func")
        res = parser.parseFunc(tokens)
        self.assertEqual(res.impacted_var.name, 'x')
        self.assertEqual(res.op.op, NumOp.PLUS)
        self.assertIsInstance(res, SimpleFunc)
    
    def test_mapper(self):
        tokens, parser = self.setup("parse_mapper")
        res = parser.parseMapper()
        self.assertEqual(res.src.name, 'testVar')
        self.assertEqual(res.tbl_field, 'testingAxis')
        self.assertEqual(res.decl.type.type, Types.CATEGORY)
        self.assertEqual(res.decl.var.name, 'a')

    def test_assigner(self):
        tokens, parser = self.setup("parse_assigner")
        res = parser.parseAssigner()
        self.assertEqual(res.decl.type.type, Types.CATEGORY)
        self.assertEqual(res.decl.var.name, 'a')
        print("RES VALUE IS ", res.value.__class__.__name__)
        self.assertEqual(res.value.value.value, 123456)
    
    def test_math_funcs(self):
        tokens, parser = self.setup("parse_math_funcs")
        res = parser.parseMathFuncs()
        self.assertEqual(len(res.mth_func_lst), 3)
        self.assertIsInstance(res.mth_func_lst[0], Increment)
        self.assertIsInstance(res.mth_func_lst[1], SimpleFunc)
        self.assertIsInstance(res.mth_func_lst[2], BuiltinFunc)

    def test_trigger(self):
        tokens, parser = self.setup("parse_trigger")
        res = parser.parseTrigger()
        self.assertEqual(res.var1.name, 'triggerVar')
        self.assertEqual(len(res.math_funcs.mth_func_lst), 2)
        self.assertEqual(res.math_funcs.mth_func_lst[0].impacted_var.name, 'triggerVar')
        self.assertEqual(res.math_funcs.mth_func_lst[1].impacted_var.name, 'triggerVar')
        self.assertEqual(res.math_funcs.mth_func_lst[1].op.op, NumOp.PLUS)
        self.assertTrue(res.math_funcs.mth_func_lst[1].rhs.value.equals(
            values.IntegerValue(1)))
    
    def test_plotter(self):
        tokens, parser = self.setup("parse_plotter")
        res = parser.parsePlotter()
        self.assertIsInstance(res.graph.graph, LineXYGraph)
        self.assertEqual(res.x.var.name, 'x')
        self.assertEqual(res.y.fun.fun, NumFunction.LOG)
        self.assertEqual(res.graph_name, 'line')

    def test_empty_program(self):
        tokens, parser = self.setup("empty_program")
        res = parser.parseProgram()
        self.assertEqual(res.body.commands, [])

    def test_missing_program_beginning(self):
        tokens, parser = self.setup("missing_beginning")
        with self.assertRaises(TokenizationError):
            parser.parseProgram()

    def test_string_program(self):
        tokens, parser = self.setup("string_program")
        with self.assertRaises(ParseError):
            parser.parseProgram()
    
    def test_missing_command_sep(self):
        tokens, parser = self.setup("missing_sep")
        with self.assertRaises(TokenizationError):
            parser.parseProgram()

    def test_capital_var(self):
        tokens, parser = self.setup("capital_var")
        with self.assertRaises(ParseError):
            parser.parseVar()

    def test_invalid_remote(self):
        tokens, parser = self.setup("invalid_remote_call")
        with self.assertRaises(TokenizationError):
            parser.parseSource()

    def test_missing_parenth_remote(self):
        tokens, parser = self.setup("missing_remote_parenth")
        with self.assertRaises(TokenizationError):
            parser.parseSource()

    def test_declare_without_type(self):
        tokens, parser = self.setup("no_type_decelaration")
        with self.assertRaises(ParseError):
            parser.parseDeclare()

    def test_invalid_typeself(self):
        tokens, parser = self.setup("invalid_type")
        with self.assertRaises(ParseError):
            parser.parseAssigner()

    def test_empty_trigger(self):
        tokens, parser = self.setup("empty_observer")
        with self.assertRaises(ParseError):
            parser.parseTrigger()

    def test_empty_mapper(self):
        tokens, parser = self.setup("empty_mapper")
        with self.assertRaises(ParseError):
            parser.parseMapper()

    def test_invalid_graph_title(self):
        tokens, parser = self.setup("invalid_title")
        with self.assertRaises(ParseError):
            parser.parsePlotter()

    def test_invalid_no_graph_title(self):
        tokens, parser = self.setup("missing_graph_title")
        with self.assertRaises(ParseError):
            parser.parsePlotter()

    def test_invalid_bltn_func(self):
        tokens, parser = self.setup("invalid_bltn_type")
        with self.assertRaises(ParseError):
            parser.parseFunc(tokens)

    def test_bltn_invalid_var(self):
        tokens, parser = self.setup("bltn_invalid_var")
        with self.assertRaises(TokenizationError):
            parser.parseBltnFunc()

    def test_missing_comma_funcs(self):
        tokens, parser = self.setup("missing_comma_funcs")
        with self.assertRaises(ParseError):
            parser.parseProgram()

    def setup(self, input = None):
        def run_compile(content: str) -> Tokenizer:
            print("::::::::: Running - ", self._testMethodName, " :::::::::")
            tk = Tokenizer(content)
            tk.tokenize()
            return tk
        if (input is not None):
            tk = read_program_file(f"tests/res/programs/{input}", run_compile)
        else:
            tk = read_program_file("tests/res/programs/example1", run_compile)
        print("GOT TOKENS")
        tokens = tk.tokens
        print(tokens)
        parser = Parser(tk)
        return tokens, parser