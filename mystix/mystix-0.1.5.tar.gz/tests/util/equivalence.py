from mystix.language.shared.ast import *
from typing import cast
from mystix.util.errors import NonExhaustiveTypeCaseError


def value_equal(v1: Value, v2: Value) -> bool:
    return v1.value.equals(v2.value)


def type_equal(t1: Type, t2: Type) -> bool:
    return t1.type == t2.type


def var_equal(v1: Var, v2: Var) -> bool:
    return v1.name == v2.name


def declare_equal(d1: Declare, d2: Declare) -> bool:
    return type_equal(d1.type, d2.type) and var_equal(d1.var, d2.var)


def operand_equal(o1: Operand, o2: Operand) -> bool:
    return o1.op == o2.op


def builtin_func_equal(f1: BuiltinFunc, f2: BuiltinFunc) -> bool:
    return f1.fun == f2.fun and var_equal(f1.input, f2.input)


def fast_func_equal(f1: FastFunc, f2: FastFunc) -> bool:
    t = type(f1)
    if t is not type(f2):
        return False
    else:
        return var_equal(f1.impacted_var, f2.impacted_var)


def simple_func_equal(f1: SimpleFunc, f2: SimpleFunc) -> bool:
    return var_equal(f1.impacted_var, f2.impacted_var) \
           and operand_equal(f1.op,f2.op) \
           and value_equal(f1.rhs, f2.rhs)


def func_equal(f1: Func, f2: Func) -> bool:
    t = type(f1)
    if t is not type(f2):
        return False
    elif t is BuiltinFunc:
        return builtin_func_equal(cast(BuiltinFunc, f1), cast(BuiltinFunc, f2))
    elif isinstance(f1, FastFunc):
        return fast_func_equal(cast(FastFunc, f1), cast(FastFunc, f2))
    elif t is SimpleFunc:
        return simple_func_equal(cast(SimpleFunc, f1), cast(SimpleFunc, f2))
    else:
        raise NonExhaustiveTypeCaseError()


def axis_equal(a1: Axis, a2: Axis) -> bool:
    t = type(a1)
    if t is not type(a2):
        return False
    elif t is VarAxis:
        return var_equal(cast(VarAxis, a1).var, cast(VarAxis, a2).var)
    elif t is FuncAxis:
        return func_equal(cast(FuncAxis, a1).fun, cast(FuncAxis, a2).fun)
    else:
        raise NonExhaustiveTypeCaseError()


def graph_equal(g1: Graph, g2: Graph) -> bool:
    return g1.graph.equals(g2.graph)


def plotter_equal(p1: Plotter, p2: Plotter) -> bool:
    return graph_equal(p1.graph, p2.graph)


def mapper_equal(m1: Mapper, m2: Mapper) -> bool:
    return var_equal(m1.src, m2.src) and m1.tbl_field == m2.tbl_field and \
        declare_equal(m1.decl, m2.decl)


def source_equal(s1: Source, s2: Source) -> bool:
    return s1.url == s2.url


def loader_equal(l1: Loader, l2: Loader) -> bool:
    return var_equal(l1.name, l2.name) and source_equal(l1.source, l2.source)


def assigner_equal(a1: Assigner, a2: Assigner) -> bool:
    return declare_equal(a1.decl, a2.decl) and value_equal(a1.value, a2.value)


def math_funcs_equal(fs1: MathFuncs, fs2: MathFuncs) -> bool:
    l1 = len(fs1.mth_func_lst)
    if l1 != len(fs2.mth_func_lst):
        return False
    else:
        for i in range(l1):
            if not func_equal(fs1.mth_func_lst[i], fs2.mth_func_lst[i]):
                return False
        return True


def trigger_equal(t1: Trigger, t2: Trigger) -> bool:
    return var_equal(t1.var1, t2.var1) \
           and math_funcs_equal(t1.math_funcs, t2.math_funcs)


def command_equal(c1: Command, c2: Command) -> bool:
    t = type(c1)
    if t is not type(c2):
        return False
    elif t is Command:
        return True
    elif t is Assigner:
        return assigner_equal(cast(Assigner, c1), cast(Assigner, c2))
    elif t is Loader:
        return loader_equal(cast(Loader, c1), cast(Loader, c2))
    elif t is Mapper:
        return mapper_equal(cast(Mapper, c1), cast(Mapper, c2))
    elif t is Plotter:
        return plotter_equal(cast(Plotter, c1), cast(Plotter, c2))
    elif t is Trigger:
        return trigger_equal(cast(Trigger, c1), cast(Trigger, c2))
    else:
        raise NonExhaustiveTypeCaseError()


def body_equal(b1: Body, b2: Body) -> bool:
    l1 = len(b1.commands)
    if l1 != len(b2.commands):
        return False
    else:
        for i in range(l1):
            if not command_equal(b1.commands[i], b2.commands[i]):
                return False
        return True


def ast_equal(p1: Program, p2: Program) -> bool:
    """
    Should return true if p1 and p2 represent the same program
    """
    return body_equal(p1.body, p2.body)  # stub
