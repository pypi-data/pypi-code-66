from unittest import TestCase
from typing import cast
from mystix.language.evaluation import Evaluator
from mystix.language.shared import ast
from mystix.targets.data.dataLoader import DataLoaderError
from mystix.language.shared.primitives import Types, ConcreteNumOp
from mystix.language.shared.primitives.values import IntegerValue, FloatValue


class LoaderEvaluationTests(TestCase):

    def test_duplicate_name(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("www.source.com")),
                ast.Loader(ast.Var("source"),
                           ast.Source("www.source2.com")),
            ]))
        code, err = e.evaluate(p, duration=4000)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_invalid_host_no_trigger(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-apiiii.com/api/reports")),
            ]))
        code, err = e.evaluate(p, duration=4000)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_invalid_host(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-apiiii.com/api/reports")),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),
            ]))
        code, err = e.evaluate(p, duration=4000)
        self.assertNotEqual(0, code)
        self.assertTrue(isinstance(err, DataLoaderError))

    def test_valid_source(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(IntegerValue(0))),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.Increment(ast.Var(
                    "count"))])),
            ]))
        code, err = e.evaluate(p, duration=4000)
        self.assertEqual(0, code)


class MiscEvaluationTests(TestCase):

    def test_simple_func_baseline(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(IntegerValue(20))),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([])),
            ]))
        code, err = e.evaluate(p, duration=7000)
        self.assertEqual(0, code)
        self.assertEqual(20, cast(IntegerValue, e.env.get_val("count")).value)

    def test_simple_func_divide(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(IntegerValue(20))),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.SimpleFunc(
                    ast.Var("count"), ast.Operand(ConcreteNumOp.DIV),
                    ast.Value(IntegerValue(2)))])),
            ]))
        code, err = e.evaluate(p, duration=7000)
        self.assertEqual(0, code)
        self.assertTrue(cast(IntegerValue, e.env.get_val("count")).value < 20)

    def test_simple_func_pow(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(FloatValue(1.1))),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.SimpleFunc(
                    ast.Var("count"), ast.Operand(ConcreteNumOp.EXP),
                    ast.Value(IntegerValue(2)))])),
            ]))
        code, err = e.evaluate(p, duration=500)
        self.assertEqual(0, code)
        self.assertTrue(cast(IntegerValue, e.env.get_val("count")).value > 1)

    def test_pow_overflow(self):
        e = Evaluator()
        p = ast.Program(
            ast.Body([
                ast.Loader(ast.Var("source"),
                           ast.Source("https://covid-api.com/api/reports")),
                ast.Assigner(ast.Declare(ast.Type(Types.NUMBER), ast.Var("count")),
                             ast.Value(FloatValue(1.1))),
                ast.Trigger(ast.Var("source"), ast.MathFuncs([ast.SimpleFunc(
                    ast.Var("count"), ast.Operand(ConcreteNumOp.EXP),
                    ast.Value(IntegerValue(2)))])),
            ]))
        code, err = e.evaluate(p, duration=10000)
        self.assertNotEqual(0, code)
