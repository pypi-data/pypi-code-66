from unittest import TestCase

from tests.util import ast_equal
from tests.util.example_ast import example_1
from mystix.language.shared import ast
from mystix.language.shared.primitives import Types
from mystix.language.shared.primitives.values import IntegerValue
from mystix.language.shared.primitives.graphs import ScatterXYGraph, LineXYGraph
from mystix.language.shared.primitives.numerical import NumFunction


class EquivalenceUtilTests(TestCase):

    def test_trivial(self):
        self.assertTrue(ast_equal(
            ast.Program(ast.Body([])), ast.Program(ast.Body([]))))

    def test_identical_construction(self):
        self.assertTrue(ast_equal(example_1(), example_1()))

    def test_identical_commands(self):
        self.assertTrue(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ])),
        ast.Program(
            ast.Body([
                ast.commands_ast.Loader(ast.Var("source"),
                                        ast.Source("www.coviddata.com/stream")),
            ]))))

    def test_diff_num_commands(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ])),
                ast.Program(
                    ast.Body([]))))

    def test_diff_commands(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ])),
                ast.Program(
                    ast.Body([ast.Mapper(ast.Var("source"), "case_date",
                                         ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))]))))

    def test_multiple_commands(self):
        self.assertTrue(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ]))))

    def test_diff_order(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var(
                                       "date"))),
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ]))))

    def test_different_load_var_names(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ])),
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source1"),
                                                ast.Source("www.coviddata.com/stream")),
                    ]))))

    def test_diff_load_url(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("https://www.coviddata.com/stream")),
                    ])),
                ast.Program(
                    ast.Body([
                        ast.commands_ast.Loader(ast.Var("source"),
                                                ast.Source("www.coviddata.com/stream")),
                    ]))))

    def test_diff_map_var(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("SOURCE"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ]))))

    def test_diff_map_field(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_data",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ]))))

    def test_diff_map_declare_type(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.BINARY), ast.Var(
                                       "date")))
                    ]))))

    def test_diff_map_declare_var(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var("date")))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Mapper(ast.Var("source"), "case_date",
                                   ast.Declare(ast.Type(Types.NUMBER), ast.Var(
                                       "count")))
                    ]))))

    def test_diff_math_funcs_(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                            "count"))]))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Decrement(ast.Var(
                            "count"))]))
                    ]))))

    def test_diff_num_math_funcs_(self):
        self.assertFalse(
            ast_equal(
                ast.Program(
                    ast.Body([
                        ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                            "count"))]))
                    ])),
                ast.Program(
                    ast.Body([
                        ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                            "count")), ast.Decrement(ast.Var(
                            "count"))]))
                    ]))))
