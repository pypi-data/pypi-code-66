

from mystix.language.shared import ast
from mystix.language.shared.primitives import Types
from mystix.language.shared.primitives.values import IntegerValue
from mystix.language.shared.primitives.graphs import ScatterXYGraph, LineXYGraph
from mystix.language.shared.primitives.numerical import NumFunction


def example_1() -> ast.Program:
    """
    Instantiates program example 1 as a native AST
    """
    return ast.Program(
        ast.Body([

            # source = live remote "www.coviddata.com/stream"
            ast.Loader(ast.Var("source"),
                                    ast.Source("www.coviddata.com/stream")),

            # map source "case_date" to number date
            ast.Mapper(ast.Var("source"), "case_date",
                       ast.Declare(ast.Type(Types.NUMBER), ast.Var("date"))),

            # number count = 0
            ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                         ast.Value(IntegerValue(0))),

            # on new data from source count++
            ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                "count"))])),

            # plot xy date age titled age_graph
            ast.Plotter(ast.Graph(ScatterXYGraph()),
                        ast.VarAxis(ast.Var("date")),
                        ast.VarAxis(ast.Var("age")), "age_graph"),

            # plot line xy date log(count) titled cases_log
            ast.Plotter(ast.Graph(LineXYGraph()),
                        ast.VarAxis(ast.Var("date")),
                        ast.FuncAxis(ast.BuiltinFunc(NumFunction.LOG, ast.Var(
                            "count"))),
                        "age_graph"),
        ]))


def simple_plot_example() -> ast.Program:

    return ast.Program(ast.Body([
        ast.Plotter(ast.Graph(ScatterXYGraph()),
                    ast.VarAxis(ast.Var("t")),
                    ast.FuncAxis(ast.BuiltinFunc(NumFunction.SIN, ast.Var(
                        "t"))),
                    "sine_wave"),

    ]))
