import unittest
from typing import List


from mystix.language.shared import ast
from mystix.language.parsing import Parser
from mystix.language.tokenization import Tokenizer, TokenizationError
from mystix.language.evaluation import Evaluator
from mystix.language.shared.primitives import Types, values, graphs
from mystix.ui.util import read_program_file
from tests.util import ast_equal


class CompilePipelineTests(unittest.TestCase):
    """
    Test tokenization through evaluation
    useful right now for validating function stubs
    """

    def test(self):
        content = "NOT A REAL PROGRAM"
        try:
            t = Tokenizer(content)
            t.tokenize()
            program: ast.Program = Parser(t).parseProgram()
            result: int = Evaluator(graphics=False).evaluate(program, duration=5000)
            self.fail()
        except TokenizationError:
            pass

    def test_regular(self):
        p_expected: ast.Program = ast.Program(
            ast.Body([

                # source = live remote "https://covid-api.com/api/reports"
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),

                # map source "confirmed" to number confirmed
                ast.Mapper(ast.Var("source"), "confirmed",
                           ast.Declare(ast.Type(Types.NUMBER), ast.Var("confirmed"))),

                # number count = 0
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(values.IntegerValue(0))),

                # observe(source) do count++
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),

                # plot line_xy(count,confirmed) called "confirmed_cases"
                ast.Plotter(ast.Graph(graphs.LineXYGraph()),
                            ast.VarAxis(ast.Var("count")),
                            ast.VarAxis(ast.Var("confirmed")), "confirmed_cases"),

            ]))

        def parse(content) -> ast.Program:
            t = Tokenizer(content)
            t.tokenize()
            return Parser(t).parseProgram()

        p: ast.Program = read_program_file("tests/res/programs/regular_program.mstx",
                                           parse)

        self.assertTrue(ast_equal(p_expected, p))
