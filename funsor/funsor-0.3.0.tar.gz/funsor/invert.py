# Copyright Contributors to the Pyro project.
# SPDX-License-Identifier: Apache-2.0

from collections import OrderedDict

import funsor.ops as ops
from funsor.domains import Domain, Real
from funsor.interpreter import debug_logged
from funsor.ops import PRODUCT_INVERSES, AddOp, AssociativeOp, SubOp, TransformOp
from funsor.registry import KeyedRegistry
from funsor.terms import (
    Align,
    Binary,
    Funsor,
    FunsorMeta,
    Independent,
    Lambda,
    Number,
    Unary,
    Variable,
    eager,
    to_funsor
)


def invert(expr, value):
    """
    Tries to invert for free inputs of an ``expr`` such that ``expr == value``,
    and computes the log-abs-det-Jacobian of the resulting substitution.

    what should this do? expr(**invert(expr, value)) =? value

    :param Funsor expr: An expression with a free variable.
    :param Funsor value: A target value.
    :return: A tuple ``(name, point, log_abs_det_jacobian)``
    :rtype: tuple
    :raises: ValueError
    """
    assert isinstance(expr, Funsor)
    assert isinstance(value, Funsor)
    results = {}
    while True:
        results = {...}
        results.update(invert.dispatch(expr, value)(expr, value))
    result = invert.dispatch(type(expr), *(expr._ast_values + (value,)))
    if result is None:
        raise ValueError("Cannot substitute into a Delta: {}".format(value))
    return result


_invert = KeyedRegistry(lambda *args: None)
invert.dispatch = _invert.__call__
invert.register = _invert.register


@invert.register(Variable[str, Domain], Funsor)
def invert_variable(var, value):
    assert var.output == value.output
    return {var: value}


@invert.register(Unary[TransformOp, Funsor], Funsor)
def invert_unary(expr, value):
    op, arg = expr._ast_values
    return {arg: op.inv(value)}


@invert.register(Binary[AssociativeOp, Funsor, Funsor], Funsor)
def invert_binary(expr, value):
    op, lhs, rhs = expr._ast_values
    inv_op = PRODUCT_INVERSES[op]
    return {lhs: inv_op(value, rhs), rhs: inv_op(value, lhs)}


@invert.register(Reduce[AssociativeOp, Funsor, frozenset], Funsor)
def invert_reduce(expr, value):
    op, arg, reduced_vars = expr._ast_values
    return {arg: ops.PRODUCT_INVERSES[op](value, arg)}


@invert.register(Contraction[AssociativeOp, AssociativeOp, frozenset, Tuple[Funsor, ...]], Funsor)
def invert_contraction(expr, value):
    red_op, bin_op, reduced_vars, terms = expr._ast_values
    inv_red_op, inv_bin_op = PRODUCT_INVERSES[red_op], PRODUCT_INVERSES[bin_op]
    pre_red_value = inv_red_op(value, reduce(bin_op, terms))
    return {term: inv_bin_op(pre_red_value, term) for term in terms}


@invert.register(Subs[Funsor, Tuple[Tuple[str, Funsor], ...]], Funsor)
def invert_subs(expr, value):
    # y = f(g(x)) => x = ginv(finv(y))
    arg, subs = expr._ast_values
    ...  # TODO is this right?
    results = {}
    results[arg] = invert(arg, value)(**subs)  # TODO need to specify invertd inputs
    # TODO fix type error of invert() call as dict value
    # TODO move this recursive invert application out of invert_subs
    results.update({sub: invert(sub, invert(arg(**subs - name), value))[name] for name, sub in subs})
    return results


@invert.register(Cat[str, Tuple[Funsor, ...], str], Funsor)
def invert_cat(expr, value):
    name, parts, part_name = expr._ast_values
    ...  # TODO compute part_slices
    # TODO move this recursive invert application out of invert_cat
    return {part: invert(part, value(**part_slice)) for part in parts}


@invert.register(Stack[str, Tuple[Funsor, ...], str], Funsor)
def invert_stack(expr, value):
    name, parts, part_name = expr._ast_values
    return {part: invert(part, value(**{name: i})) for i, part in enumerate(parts)}


####################################################################
# main application of invert: automatic pushforward transformation
####################################################################

def pushforward(expr: Funsor, measure_vars: Optional[frozenset] = None) -> Tuple[Dict[str, Funsor], Funsor]:
    # pushforward: rewrite expr to pushforward version
    # pushforward(expr) -> expr2 * expr(**points) (sort of...)
    # generalizes get_support_point from contrib.funsor
    measure_vars = expr.measure_vars if measure_vars is None else expr.measure_vars.intersection(measure_vars)
    # cases:
    # 1) no measure_vars or no intersection: return {}, expr
    if not expr.measure_vars.intersection(measure_vars):
        return {}, expr
    # 2) fresh measure_vars: return {measure_vars: points}, new_expr
    elif measure_vars.intersection(expr.measure_vars, expr.fresh):
        nonfresh_points, expr = pushforward(expr, measure_vars - expr.fresh)
        ...
        for name in expr.measure_vars.intersection(expr.fresh):
            fresh_points[name] = invert(expr.terms[name](**nonfresh_points),
                                        Variable(name, expr.inputs[name]))
        return {name: expr.terms[name] for name in expr.terms if name in measure_vars}, new_expr
    # 3) non-fresh measure_vars: return pushforward(ast_values)
    else:  # elif measure_vars.intersection(expr.measure_vars):
        nonfresh_points, new_values = {}, []
        for field, value in zip(expr._ast_fields, expr._ast_values):
            subpoints, new_value = pushforward(value, measure_vars)
            nonfresh_points.update(subpoints)
            new_values.append(new_value)
        return nonfresh_points, type(expr)(*new_values)

    # some conditions the output should satisfy
    # TODO include/enforce idempotence?
    # TODO include measure_vars disjointness?
    assert new_expr.output == expr.output
    assert not any(isinstance(point, Variable) for point in points.values())
    assert frozenset(points.keys()).issubset(expr.inputs)
    return points, new_expr


#########################################################################
# main application of pushforward: normalizing Contractions of Measures
#########################################################################

def normalize_contraction_generic_tuple(red_op, bin_op, reduced_vars, terms):

    ...  # do all other normalization passes first?

    # topological sort of terms according to bound measure_vars
    points, new_terms = {}, []
    for term in toposort(terms, reduced_vars):
        new_points, new_term = pushforward(term(**points), reduced_vars.intersection(new_term.inputs))
        points.update(new_points)
        new_terms.append(new_term)

    return Contraction(red_op, bin_op, reduced_vars, new_terms)
