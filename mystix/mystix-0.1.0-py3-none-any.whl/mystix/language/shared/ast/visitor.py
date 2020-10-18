"""
To provide type checking for this file (and subclasses of Visitor)
and avoid a circular import between Node types and the Visitor class
itself, we do a dynamic import only in the case of static type
checking.
Per this post:
https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports

To implement the visitor pattern structure, we set this file as the "interface"
in an informal structure.
Using this post for reference:
https://refactoring.guru/design-patterns/visitor/python/example
"""
from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from mystix.language.shared.ast import *
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_program(self, p: Program):
        pass

    @abstractmethod
    def visit_body(self, b: Body):
        pass

    @abstractmethod
    def visit_loader(self, l: Loader):
        pass

    @abstractmethod
    def visit_mapper(self, m: Mapper):
        pass

    @abstractmethod
    def visit_declare(self, d: Declare):
        pass

    @abstractmethod
    def visit_assigner(self, a: Assigner):
        pass

    @abstractmethod
    def visit_trigger(self, t: Trigger):
        pass

    @abstractmethod
    def visit_plotter(self, pltr: Plotter):
        pass

    @abstractmethod
    def visit_var(self, v: Var):
        pass

    @abstractmethod
    def visit_source(self, s: Source):
        pass

    @abstractmethod
    def visit_type(self, t: Type):
        pass

    @abstractmethod
    def visit_value(self, v: Value):
        pass

    @abstractmethod
    def visit_graph(self, g: Graph):
        pass

    @abstractmethod
    def visit_var_axis(self, va: VarAxis):
        pass

    @abstractmethod
    def visit_func_axis(self, fa: FuncAxis):
        pass

    @abstractmethod
    def visit_math_funcs(self, mf: MathFuncs):
        pass

    @abstractmethod
    def visit_simple_func(self, smp: SimpleFunc):
        pass

    @abstractmethod
    def visit_increment(self, i: Increment):
        pass

    @abstractmethod
    def visit_decrement(self, d: Decrement):
        pass

    @abstractmethod
    def visit_builtin_func(self, bltn: BuiltinFunc):
        pass

    @abstractmethod
    def visit_operand(self, op: Operand):
        pass