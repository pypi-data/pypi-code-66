from unittest import TestCase

from mystix.language.shared.primitives.graphs import ScatterXYGraph
from mystix.language.shared.primitives.numerical import NumFunction
from mystix.language.shared.primitives import Types
from tests.util.example_ast import simple_plot_example
import mystix.language.shared.ast as ast
from mystix.language.evaluation import Evaluator
from mystix.language.evaluation.errors import LanguageError
from mystix.language.evaluation.vars import UndefinedVariableError
from mystix.language.shared.primitives import values,  graphs


class GraphicsEvaluationTests(TestCase):

    """
    tests portions of evaluator with graphical side-effects
    This test should be ignored if graphics do not work on
    your system.
    """

    def test_plot_undefined_axis_no_source(self):
        """
        Should return without error
        """
        print("Testing undefined variable in Axis - no source")
        program = simple_plot_example()
        e = Evaluator(graphics=False)
        code, err = e.evaluate(program, duration=4000)
        self.assertEqual(0, code)

    def test_plot_undefined_axis(self):
        """
        Should briefly create a plot then error
        """
        print("Testing undefined variable in Axis")
        program = ast.Program(ast.Body([
            ast.Loader(ast.Var("source"),
                       ast.Source("https://covid-api.com/api/reports")),
            ast.Mapper(ast.Var("source"), "confirmed",
                       ast.Declare(ast.Type(Types.NUMBER), ast.Var("confirmed"))),
            ast.Plotter(ast.Graph(ScatterXYGraph()),
                        ast.VarAxis(ast.Var("t")),
                        ast.FuncAxis(ast.BuiltinFunc(NumFunction.SIN, ast.Var(
                            "t"))),
                        "sine_wave"),

        ]))
        e = Evaluator(graphics=False)
        code, err = e.evaluate(program, duration=4000)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, UndefinedVariableError))

    """
    FIXME: running two tests consecutively with graphics enabled 
    creates seg-faults and QT errors
    """

    def test_plot_manual_define(self):
        """
        Should successfully create a plot and update with
        a constant value
        """
        print("Testing hard-coded variable value")
        program = simple_plot_example()
        e = Evaluator(graphics=False)
        e.env.extend('t', values.FloatValue(0.5))
        code, err = e.evaluate(program, duration=7000)
        self.assertEqual(0, code)

    def test_regular_program(self):
        """
        Should successfully create a plot and update with
        new values
        """
        print("Testing a full program")
        p = ast.Program(
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
        e = Evaluator(graphics=True)
        code, err = e.evaluate(p, duration=7000)
        self.assertEqual(0, code)
