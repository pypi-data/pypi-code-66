from __future__ import annotations
from typing import TYPE_CHECKING as STATIC_CHECK
if STATIC_CHECK:
    from mystix.language.shared.ast import *
from mystix.language.shared.ast.visitor import Visitor


class ProgramPrinter(Visitor):

    def print(self, p: Program) -> str:
        return self.visit_program(p)

    def visit_program(self, p: Program) -> str:
        return "(Program %s)" % p.body.accept(self)

    def visit_body(self, b: Body) -> str:
        commands = [c.accept(self) for c in b.commands]
        return "(Body %s)" % " ".join(commands)

    def visit_loader(self, l: Loader) -> str:
        return "(Loader %s %s)" % \
            (l.name.accept(self), l.source.accept(self))

    def visit_mapper(self, m: Mapper) -> str:
        return "(Mapper %s '%s' %s)" % \
            (m.src.accept(self), m.tbl_field, m.decl.accept(self))

    def visit_declare(self, d: Declare) -> str:
        return "(Declare %s %s)" % \
            (d.type.accept(self), d.var.accept(self))

    def visit_assigner(self, a: Assigner) -> str:
        return "(Assigner %s %s)" % \
            (a.decl.accept(self), a.value.accept(self))

    def visit_trigger(self, t: Trigger) -> str:
        return "(Trigger %s %s)" % \
            (t.var1.accept(self), t.math_funcs.accept(self))

    def visit_plotter(self, pltr: Plotter) -> str:
        return "(Plotter %s %s %s '%s')" % \
            (pltr.graph.accept(self),
             pltr.x.accept(self),
             pltr.y.accept(self), pltr.graph_name)

    def visit_var(self, v: Var) -> str:
        return "(Var '%s')" % v.name

    def visit_source(self, s: Source) -> str:
        return "(Source '%s')" % s.url

    def visit_type(self, t: Type) -> str:
        return "(Type %s)" % t.type

    def visit_value(self, v: Value) -> str:
        return "(Value %s)" % repr(v.value)

    def visit_graph(self, g: Graph) -> str:
        return "(Graph '%s')" % repr(g.graph)

    def visit_var_axis(self, va: VarAxis) -> str:
        return "(VarAxis %s)" % va.var.accept(self)

    def visit_func_axis(self, fa: FuncAxis) -> str:
        return "(FuncAxis %s)" % fa.fun.accept(self)

    def visit_math_funcs(self, mf: MathFuncs) -> str:
        return "(%s)" % \
            " ".join([f.accept(self) for f in mf.mth_func_lst])

    def visit_simple_func(self, smp: SimpleFunc) -> str:
        return "(%s %s %s)" % \
            (smp.op.accept(self),
             smp.impacted_var.accept(self), smp.rhs.accept(self))

    def visit_increment(self, i: Increment) -> str:
        return "(Increment %s)" % i.impacted_var.accept(self)

    def visit_decrement(self, d: Decrement) -> str:
        return "(Decrement %s)" % d.impacted_var.accept(self)

    def visit_builtin_func(self, bltn: BuiltinFunc) -> str:
        return "(BuiltinFunc %s %s)" % \
            (bltn.fun, bltn.input.accept(self))

    def visit_operand(self, op: Operand) -> str:
        return "%s" % op.op
