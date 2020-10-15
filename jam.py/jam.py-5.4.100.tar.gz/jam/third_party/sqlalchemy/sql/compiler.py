# sql/compiler.py
# Copyright (C) 2005-2020 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""Base SQL and DDL compiler implementations.

Classes provided include:

:class:`.compiler.SQLCompiler` - renders SQL
strings

:class:`.compiler.DDLCompiler` - renders DDL
(data definition language) strings

:class:`.compiler.GenericTypeCompiler` - renders
type specification strings.

To generate user-defined SQL strings, see
:doc:`/ext/compiler`.

"""

import collections
import contextlib
import itertools
import re

from . import coercions
from . import crud
from . import elements
from . import functions
from . import operators
from . import roles
from . import schema
from . import selectable
from . import sqltypes
from .base import NO_ARG
from .. import exc
from .. import util

RESERVED_WORDS = set(
    [
        "all",
        "analyse",
        "analyze",
        "and",
        "any",
        "array",
        "as",
        "asc",
        "asymmetric",
        "authorization",
        "between",
        "binary",
        "both",
        "case",
        "cast",
        "check",
        "collate",
        "column",
        "constraint",
        "create",
        "cross",
        "current_date",
        "current_role",
        "current_time",
        "current_timestamp",
        "current_user",
        "default",
        "deferrable",
        "desc",
        "distinct",
        "do",
        "else",
        "end",
        "except",
        "false",
        "for",
        "foreign",
        "freeze",
        "from",
        "full",
        "grant",
        "group",
        "having",
        "ilike",
        "in",
        "initially",
        "inner",
        "intersect",
        "into",
        "is",
        "isnull",
        "join",
        "leading",
        "left",
        "like",
        "limit",
        "localtime",
        "localtimestamp",
        "natural",
        "new",
        "not",
        "notnull",
        "null",
        "off",
        "offset",
        "old",
        "on",
        "only",
        "or",
        "order",
        "outer",
        "overlaps",
        "placing",
        "primary",
        "references",
        "right",
        "select",
        "session_user",
        "set",
        "similar",
        "some",
        "symmetric",
        "table",
        "then",
        "to",
        "trailing",
        "true",
        "union",
        "unique",
        "user",
        "using",
        "verbose",
        "when",
        "where",
    ]
)

LEGAL_CHARACTERS = re.compile(r"^[A-Z0-9_$]+$", re.I)
LEGAL_CHARACTERS_PLUS_SPACE = re.compile(r"^[A-Z0-9_ $]+$", re.I)
ILLEGAL_INITIAL_CHARACTERS = {str(x) for x in range(0, 10)}.union(["$"])

FK_ON_DELETE = re.compile(
    r"^(?:RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT)$", re.I
)
FK_ON_UPDATE = re.compile(
    r"^(?:RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT)$", re.I
)
FK_INITIALLY = re.compile(r"^(?:DEFERRED|IMMEDIATE)$", re.I)
BIND_PARAMS = re.compile(r"(?<![:\w\$\x5c]):([\w\$]+)(?![:\w\$])", re.UNICODE)
BIND_PARAMS_ESC = re.compile(r"\x5c(:[\w\$]*)(?![:\w\$])", re.UNICODE)

BIND_TEMPLATES = {
    "pyformat": "%%(%(name)s)s",
    "qmark": "?",
    "format": "%%s",
    "numeric": ":[_POSITION]",
    "named": ":%(name)s",
}


OPERATORS = {
    # binary
    operators.and_: " AND ",
    operators.or_: " OR ",
    operators.add: " + ",
    operators.mul: " * ",
    operators.sub: " - ",
    operators.div: " / ",
    operators.mod: " % ",
    operators.truediv: " / ",
    operators.neg: "-",
    operators.lt: " < ",
    operators.le: " <= ",
    operators.ne: " != ",
    operators.gt: " > ",
    operators.ge: " >= ",
    operators.eq: " = ",
    operators.is_distinct_from: " IS DISTINCT FROM ",
    operators.isnot_distinct_from: " IS NOT DISTINCT FROM ",
    operators.concat_op: " || ",
    operators.match_op: " MATCH ",
    operators.notmatch_op: " NOT MATCH ",
    operators.in_op: " IN ",
    operators.notin_op: " NOT IN ",
    operators.comma_op: ", ",
    operators.from_: " FROM ",
    operators.as_: " AS ",
    operators.is_: " IS ",
    operators.isnot: " IS NOT ",
    operators.collate: " COLLATE ",
    # unary
    operators.exists: "EXISTS ",
    operators.distinct_op: "DISTINCT ",
    operators.inv: "NOT ",
    operators.any_op: "ANY ",
    operators.all_op: "ALL ",
    # modifiers
    operators.desc_op: " DESC",
    operators.asc_op: " ASC",
    operators.nullsfirst_op: " NULLS FIRST",
    operators.nullslast_op: " NULLS LAST",
}

FUNCTIONS = {
    functions.coalesce: "coalesce",
    functions.current_date: "CURRENT_DATE",
    functions.current_time: "CURRENT_TIME",
    functions.current_timestamp: "CURRENT_TIMESTAMP",
    functions.current_user: "CURRENT_USER",
    functions.localtime: "LOCALTIME",
    functions.localtimestamp: "LOCALTIMESTAMP",
    functions.random: "random",
    functions.sysdate: "sysdate",
    functions.session_user: "SESSION_USER",
    functions.user: "USER",
    functions.cube: "CUBE",
    functions.rollup: "ROLLUP",
    functions.grouping_sets: "GROUPING SETS",
}

EXTRACT_MAP = {
    "month": "month",
    "day": "day",
    "year": "year",
    "second": "second",
    "hour": "hour",
    "doy": "doy",
    "minute": "minute",
    "quarter": "quarter",
    "dow": "dow",
    "week": "week",
    "epoch": "epoch",
    "milliseconds": "milliseconds",
    "microseconds": "microseconds",
    "timezone_hour": "timezone_hour",
    "timezone_minute": "timezone_minute",
}

COMPOUND_KEYWORDS = {
    selectable.CompoundSelect.UNION: "UNION",
    selectable.CompoundSelect.UNION_ALL: "UNION ALL",
    selectable.CompoundSelect.EXCEPT: "EXCEPT",
    selectable.CompoundSelect.EXCEPT_ALL: "EXCEPT ALL",
    selectable.CompoundSelect.INTERSECT: "INTERSECT",
    selectable.CompoundSelect.INTERSECT_ALL: "INTERSECT ALL",
}


RM_RENDERED_NAME = 0
RM_NAME = 1
RM_OBJECTS = 2
RM_TYPE = 3


ExpandedState = collections.namedtuple(
    "ExpandedState",
    [
        "statement",
        "additional_parameters",
        "processors",
        "positiontup",
        "parameter_expansion",
    ],
)


NO_LINTING = util.symbol("NO_LINTING", "Disable all linting.", canonical=0)

COLLECT_CARTESIAN_PRODUCTS = util.symbol(
    "COLLECT_CARTESIAN_PRODUCTS",
    "Collect data on FROMs and cartesian products and gather "
    "into 'self.from_linter'",
    canonical=1,
)

WARN_LINTING = util.symbol(
    "WARN_LINTING", "Emit warnings for linters that find problems", canonical=2
)

FROM_LINTING = util.symbol(
    "FROM_LINTING",
    "Warn for cartesian products; "
    "combines COLLECT_CARTESIAN_PRODUCTS and WARN_LINTING",
    canonical=COLLECT_CARTESIAN_PRODUCTS | WARN_LINTING,
)


class FromLinter(collections.namedtuple("FromLinter", ["froms", "edges"])):
    def lint(self, start=None):
        froms = self.froms
        if not froms:
            return None, None

        edges = set(self.edges)
        the_rest = set(froms)

        if start is not None:
            start_with = start
            the_rest.remove(start_with)
        else:
            start_with = the_rest.pop()

        stack = collections.deque([start_with])

        while stack and the_rest:
            node = stack.popleft()
            the_rest.discard(node)

            # comparison of nodes in edges here is based on hash equality, as
            # there are "annotated" elements that match the non-annotated ones.
            #   to remove the need for in-python hash() calls, use native
            # containment routines (e.g. "node in edge", "edge.index(node)")
            to_remove = {edge for edge in edges if node in edge}

            # appendleft the node in each edge that is not
            # the one that matched.
            stack.extendleft(edge[not edge.index(node)] for edge in to_remove)
            edges.difference_update(to_remove)

        # FROMS left over?  boom
        if the_rest:
            return the_rest, start_with
        else:
            return None, None

    def warn(self):
        the_rest, start_with = self.lint()

        # FROMS left over?  boom
        if the_rest:

            froms = the_rest
            if froms:
                template = (
                    "SELECT statement has a cartesian product between "
                    "FROM element(s) {froms} and "
                    'FROM element "{start}".  Apply join condition(s) '
                    "between each element to resolve."
                )
                froms_str = ", ".join(
                    '"{elem}"'.format(elem=self.froms[from_])
                    for from_ in froms
                )
                message = template.format(
                    froms=froms_str, start=self.froms[start_with]
                )
                util.warn(message)


class Compiled(object):

    """Represent a compiled SQL or DDL expression.

    The ``__str__`` method of the ``Compiled`` object should produce
    the actual text of the statement.  ``Compiled`` objects are
    specific to their underlying database dialect, and also may
    or may not be specific to the columns referenced within a
    particular set of bind parameters.  In no case should the
    ``Compiled`` object be dependent on the actual values of those
    bind parameters, even though it may reference those values as
    defaults.
    """

    _cached_metadata = None

    execution_options = util.immutabledict()
    """
    Execution options propagated from the statement.   In some cases,
    sub-elements of the statement can modify these.
    """

    def __init__(
        self,
        dialect,
        statement,
        bind=None,
        schema_translate_map=None,
        compile_kwargs=util.immutabledict(),
    ):
        """Construct a new :class:`.Compiled` object.

        :param dialect: :class:`.Dialect` to compile against.

        :param statement: :class:`.ClauseElement` to be compiled.

        :param bind: Optional Engine or Connection to compile this
          statement against.

        :param schema_translate_map: dictionary of schema names to be
         translated when forming the resultant SQL

         .. versionadded:: 1.1

         .. seealso::

            :ref:`schema_translating`

        :param compile_kwargs: additional kwargs that will be
         passed to the initial call to :meth:`.Compiled.process`.


        """

        self.dialect = dialect
        self.bind = bind
        self.preparer = self.dialect.identifier_preparer
        if schema_translate_map:
            self.preparer = self.preparer._with_schema_translate(
                schema_translate_map
            )

        if statement is not None:
            self.statement = statement
            self.can_execute = statement.supports_execution
            if self.can_execute:
                self.execution_options = statement._execution_options
            self.string = self.process(self.statement, **compile_kwargs)

    @util.deprecated(
        "0.7",
        "The :meth:`.Compiled.compile` method is deprecated and will be "
        "removed in a future release.   The :class:`.Compiled` object "
        "now runs its compilation within the constructor, and this method "
        "does nothing.",
    )
    def compile(self):
        """Produce the internal string representation of this element.
        """
        pass

    def _execute_on_connection(self, connection, multiparams, params):
        if self.can_execute:
            return connection._execute_compiled(self, multiparams, params)
        else:
            raise exc.ObjectNotExecutableError(self.statement)

    @property
    def sql_compiler(self):
        """Return a Compiled that is capable of processing SQL expressions.

        If this compiler is one, it would likely just return 'self'.

        """

        raise NotImplementedError()

    def process(self, obj, **kwargs):
        return obj._compiler_dispatch(self, **kwargs)

    def __str__(self):
        """Return the string text of the generated SQL or DDL."""

        return self.string or ""

    def construct_params(self, params=None):
        """Return the bind params for this compiled object.

        :param params: a dict of string/object pairs whose values will
                       override bind values compiled in to the
                       statement.
        """

        raise NotImplementedError()

    @property
    def params(self):
        """Return the bind params for this compiled object."""
        return self.construct_params()

    def execute(self, *multiparams, **params):
        """Execute this compiled object."""

        e = self.bind
        if e is None:
            raise exc.UnboundExecutionError(
                "This Compiled object is not bound to any Engine "
                "or Connection.",
                code="2afi",
            )
        return e._execute_compiled(self, multiparams, params)

    def scalar(self, *multiparams, **params):
        """Execute this compiled object and return the result's
        scalar value."""

        return self.execute(*multiparams, **params).scalar()


class TypeCompiler(util.with_metaclass(util.EnsureKWArgType, object)):
    """Produces DDL specification for TypeEngine objects."""

    ensure_kwarg = r"visit_\w+"

    def __init__(self, dialect):
        self.dialect = dialect

    def process(self, type_, **kw):
        return type_._compiler_dispatch(self, **kw)


# this was a Visitable, but to allow accurate detection of
# column elements this is actually a column element
class _CompileLabel(elements.ColumnElement):

    """lightweight label object which acts as an expression.Label."""

    __visit_name__ = "label"
    __slots__ = "element", "name"

    def __init__(self, col, name, alt_names=()):
        self.element = col
        self.name = name
        self._alt_names = (col,) + alt_names

    @property
    def proxy_set(self):
        return self.element.proxy_set

    @property
    def type(self):
        return self.element.type

    def self_group(self, **kw):
        return self


class prefix_anon_map(dict):
    """A map that creates new keys for missing key access.

    Considers keys of the form "<ident> <name>" to produce
    new symbols "<name>_<index>", where "index" is an incrementing integer
    corresponding to <name>.

    Inlines the approach taken by :class:`sqlalchemy.util.PopulateDict` which
    is otherwise usually used for this type of operation.

    """

    def __missing__(self, key):
        (ident, derived) = key.split(" ", 1)
        anonymous_counter = self.get(derived, 1)
        self[derived] = anonymous_counter + 1
        value = derived + "_" + str(anonymous_counter)
        self[key] = value
        return value


class SQLCompiler(Compiled):
    """Default implementation of :class:`.Compiled`.

    Compiles :class:`.ClauseElement` objects into SQL strings.

    """

    extract_map = EXTRACT_MAP

    compound_keywords = COMPOUND_KEYWORDS

    isdelete = isinsert = isupdate = False
    """class-level defaults which can be set at the instance
    level to define if this Compiled instance represents
    INSERT/UPDATE/DELETE
    """

    isplaintext = False

    returning = None
    """holds the "returning" collection of columns if
    the statement is CRUD and defines returning columns
    either implicitly or explicitly
    """

    returning_precedes_values = False
    """set to True classwide to generate RETURNING
    clauses before the VALUES or WHERE clause (i.e. MSSQL)
    """

    render_table_with_column_in_update_from = False
    """set to True classwide to indicate the SET clause
    in a multi-table UPDATE statement should qualify
    columns with the table name (i.e. MySQL only)
    """

    ansi_bind_rules = False
    """SQL 92 doesn't allow bind parameters to be used
    in the columns clause of a SELECT, nor does it allow
    ambiguous expressions like "? = ?".  A compiler
    subclass can set this flag to False if the target
    driver/DB enforces this
    """

    _textual_ordered_columns = False
    """tell the result object that the column names as rendered are important,
    but they are also "ordered" vs. what is in the compiled object here.
    """

    _ordered_columns = True
    """
    if False, means we can't be sure the list of entries
    in _result_columns is actually the rendered order.  Usually
    True unless using an unordered TextualSelect.
    """

    _loose_column_name_matching = False
    """tell the result object that the SQL staement is textual, wants to match
    up to Column objects, and may be using the ._label in the SELECT rather
    than the base name.

    """

    _numeric_binds = False
    """
    True if paramstyle is "numeric".  This paramstyle is trickier than
    all the others.

    """

    _render_postcompile = False
    """
    whether to render out POSTCOMPILE params during the compile phase.

    """

    insert_single_values_expr = None
    """When an INSERT is compiled with a single set of parameters inside
    a VALUES expression, the string is assigned here, where it can be
    used for insert batching schemes to rewrite the VALUES expression.

    .. versionadded:: 1.3.8

    """

    literal_execute_params = frozenset()
    """bindparameter objects that are rendered as literal values at statement
    execution time.

    """

    post_compile_params = frozenset()
    """bindparameter objects that are rendered as bound parameter placeholders
    at statement execution time.

    """

    has_out_parameters = False
    """if True, there are bindparam() objects that have the isoutparam
    flag set."""

    insert_prefetch = update_prefetch = ()

    def __init__(
        self,
        dialect,
        statement,
        column_keys=None,
        inline=False,
        linting=NO_LINTING,
        **kwargs
    ):
        """Construct a new :class:`.SQLCompiler` object.

        :param dialect: :class:`.Dialect` to be used

        :param statement: :class:`.ClauseElement` to be compiled

        :param column_keys:  a list of column names to be compiled into an
         INSERT or UPDATE statement.

        :param inline: whether to generate INSERT statements as "inline", e.g.
         not formatted to return any generated defaults

        :param kwargs: additional keyword arguments to be consumed by the
         superclass.

        """
        self.column_keys = column_keys

        # compile INSERT/UPDATE defaults/sequences inlined (no pre-
        # execute)
        self.inline = inline or getattr(statement, "_inline", False)

        self.linting = linting

        # a dictionary of bind parameter keys to BindParameter
        # instances.
        self.binds = {}

        # a dictionary of BindParameter instances to "compiled" names
        # that are actually present in the generated SQL
        self.bind_names = util.column_dict()

        # stack which keeps track of nested SELECT statements
        self.stack = []

        # relates label names in the final SQL to a tuple of local
        # column/label name, ColumnElement object (if any) and
        # TypeEngine. ResultProxy uses this for type processing and
        # column targeting
        self._result_columns = []

        # true if the paramstyle is positional
        self.positional = dialect.positional
        if self.positional:
            self.positiontup = []
            self._numeric_binds = dialect.paramstyle == "numeric"
        self.bindtemplate = BIND_TEMPLATES[dialect.paramstyle]

        self.ctes = None

        self.label_length = (
            dialect.label_length or dialect.max_identifier_length
        )

        # a map which tracks "anonymous" identifiers that are created on
        # the fly here
        self.anon_map = prefix_anon_map()

        # a map which tracks "truncated" names based on
        # dialect.label_length or dialect.max_identifier_length
        self.truncated_names = {}

        Compiled.__init__(self, dialect, statement, **kwargs)

        if (
            self.isinsert or self.isupdate or self.isdelete
        ) and statement._returning:
            self.returning = statement._returning

        if self.positional and self._numeric_binds:
            self._apply_numbered_params()

        if self._render_postcompile:
            self._process_parameters_for_postcompile(_populate_self=True)

    @property
    def prefetch(self):
        return list(self.insert_prefetch + self.update_prefetch)

    @util.memoized_instancemethod
    def _init_cte_state(self):
        """Initialize collections related to CTEs only if
        a CTE is located, to save on the overhead of
        these collections otherwise.

        """
        # collect CTEs to tack on top of a SELECT
        self.ctes = util.OrderedDict()
        self.ctes_by_name = {}
        self.ctes_recursive = False
        if self.positional:
            self.cte_positional = {}

    @contextlib.contextmanager
    def _nested_result(self):
        """special API to support the use case of 'nested result sets'"""
        result_columns, ordered_columns = (
            self._result_columns,
            self._ordered_columns,
        )
        self._result_columns, self._ordered_columns = [], False

        try:
            if self.stack:
                entry = self.stack[-1]
                entry["need_result_map_for_nested"] = True
            else:
                entry = None
            yield self._result_columns, self._ordered_columns
        finally:
            if entry:
                entry.pop("need_result_map_for_nested")
            self._result_columns, self._ordered_columns = (
                result_columns,
                ordered_columns,
            )

    def _apply_numbered_params(self):
        poscount = itertools.count(1)
        self.string = re.sub(
            r"\[_POSITION\]", lambda m: str(util.next(poscount)), self.string
        )

    @util.memoized_property
    def _bind_processors(self):
        return dict(
            (key, value)
            for key, value in (
                (
                    self.bind_names[bindparam],
                    bindparam.type._cached_bind_processor(self.dialect)
                    if not bindparam._expanding_in_types
                    else tuple(
                        elem_type._cached_bind_processor(self.dialect)
                        for elem_type in bindparam._expanding_in_types
                    ),
                )
                for bindparam in self.bind_names
            )
            if value is not None
        )

    def is_subquery(self):
        return len(self.stack) > 1

    @property
    def sql_compiler(self):
        return self

    def construct_params(self, params=None, _group_number=None, _check=True):
        """return a dictionary of bind parameter keys and values"""

        if params:
            pd = {}
            for bindparam in self.bind_names:
                name = self.bind_names[bindparam]
                if bindparam.key in params:
                    pd[name] = params[bindparam.key]
                elif name in params:
                    pd[name] = params[name]

                elif _check and bindparam.required:
                    if _group_number:
                        raise exc.InvalidRequestError(
                            "A value is required for bind parameter %r, "
                            "in parameter group %d"
                            % (bindparam.key, _group_number),
                            code="cd3x",
                        )
                    else:
                        raise exc.InvalidRequestError(
                            "A value is required for bind parameter %r"
                            % bindparam.key,
                            code="cd3x",
                        )

                elif bindparam.callable:
                    pd[name] = bindparam.effective_value
                else:
                    pd[name] = bindparam.value
            return pd
        else:
            pd = {}
            for bindparam in self.bind_names:
                if _check and bindparam.required:
                    if _group_number:
                        raise exc.InvalidRequestError(
                            "A value is required for bind parameter %r, "
                            "in parameter group %d"
                            % (bindparam.key, _group_number),
                            code="cd3x",
                        )
                    else:
                        raise exc.InvalidRequestError(
                            "A value is required for bind parameter %r"
                            % bindparam.key,
                            code="cd3x",
                        )

                if bindparam.callable:
                    pd[self.bind_names[bindparam]] = bindparam.effective_value
                else:
                    pd[self.bind_names[bindparam]] = bindparam.value
            return pd

    @property
    def params(self):
        """Return the bind param dictionary embedded into this
        compiled object, for those values that are present."""
        return self.construct_params(_check=False)

    def _process_parameters_for_postcompile(
        self, parameters=None, _populate_self=False
    ):
        """handle special post compile parameters.

        These include:

        * "expanding" parameters -typically IN tuples that are rendered
          on a per-parameter basis for an otherwise fixed SQL statement string.

        * literal_binds compiled with the literal_execute flag.  Used for
          things like SQL Server "TOP N" where the driver does not accommodate
          N as a bound parameter.

        """

        if parameters is None:
            parameters = self.construct_params()

        expanded_parameters = {}
        if self.positional:
            positiontup = []
        else:
            positiontup = None

        processors = self._bind_processors

        new_processors = {}

        if self.positional and self._numeric_binds:
            # I'm not familiar with any DBAPI that uses 'numeric'.
            # strategy would likely be to make use of numbers greater than
            # the highest number present; then for expanding parameters,
            # append them to the end of the parameter list.   that way
            # we avoid having to renumber all the existing parameters.
            raise NotImplementedError(
                "'post-compile' bind parameters are not supported with "
                "the 'numeric' paramstyle at this time."
            )

        replacement_expressions = {}
        to_update_sets = {}

        for name in (
            self.positiontup if self.positional else self.bind_names.values()
        ):
            parameter = self.binds[name]
            if parameter in self.literal_execute_params:
                value = parameters.pop(name)
                replacement_expressions[name] = self.render_literal_bindparam(
                    parameter, render_literal_value=value
                )
                continue

            if parameter in self.post_compile_params:
                if name in replacement_expressions:
                    to_update = to_update_sets[name]
                else:
                    # we are removing the parameter from parameters
                    # because it is a list value, which is not expected by
                    # TypeEngine objects that would otherwise be asked to
                    # process it. the single name is being replaced with
                    # individual numbered parameters for each value in the
                    # param.
                    values = parameters.pop(name)

                    leep = self._literal_execute_expanding_parameter
                    to_update, replacement_expr = leep(name, parameter, values)

                    to_update_sets[name] = to_update
                    replacement_expressions[name] = replacement_expr

                if not parameter.literal_execute:
                    parameters.update(to_update)
                    if parameter._expanding_in_types:
                        new_processors.update(
                            (
                                "%s_%s_%s" % (name, i, j),
                                processors[name][j - 1],
                            )
                            for i, tuple_element in enumerate(values, 1)
                            for j, value in enumerate(tuple_element, 1)
                            if name in processors
                            and processors[name][j - 1] is not None
                        )
                    else:
                        new_processors.update(
                            (key, processors[name])
                            for key, value in to_update
                            if name in processors
                        )
                    if self.positional:
                        positiontup.extend(name for name, value in to_update)
                    expanded_parameters[name] = [
                        expand_key for expand_key, value in to_update
                    ]
            elif self.positional:
                positiontup.append(name)

        def process_expanding(m):
            return replacement_expressions[m.group(1)]

        statement = re.sub(
            r"\[POSTCOMPILE_(\S+)\]", process_expanding, self.string
        )

        expanded_state = ExpandedState(
            statement,
            parameters,
            new_processors,
            positiontup,
            expanded_parameters,
        )

        if _populate_self:
            # this is for the "render_postcompile" flag, which is not
            # otherwise used internally and is for end-user debugging and
            # special use cases.
            self.string = expanded_state.statement
            self._bind_processors.update(expanded_state.processors)
            self.positiontup = expanded_state.positiontup
            self.post_compile_params = frozenset()
            for key in expanded_state.parameter_expansion:
                bind = self.binds.pop(key)
                self.bind_names.pop(bind)
                for value, expanded_key in zip(
                    bind.value, expanded_state.parameter_expansion[key]
                ):
                    self.binds[expanded_key] = new_param = bind._with_value(
                        value
                    )
                    self.bind_names[new_param] = expanded_key

        return expanded_state

    @util.dependencies("sqlalchemy.engine.result")
    def _create_result_map(self, result):
        """utility method used for unit tests only."""
        return result.CursorResultMetaData._create_description_match_map(
            self._result_columns
        )

    def default_from(self):
        """Called when a SELECT statement has no froms, and no FROM clause is
        to be appended.

        Gives Oracle a chance to tack on a ``FROM DUAL`` to the string output.

        """
        return ""

    def visit_grouping(self, grouping, asfrom=False, **kwargs):
        return "(" + grouping.element._compiler_dispatch(self, **kwargs) + ")"

    def visit_label_reference(
        self, element, within_columns_clause=False, **kwargs
    ):
        if self.stack and self.dialect.supports_simple_order_by_label:
            selectable = self.stack[-1]["selectable"]

            with_cols, only_froms, only_cols = selectable._label_resolve_dict
            if within_columns_clause:
                resolve_dict = only_froms
            else:
                resolve_dict = only_cols

            # this can be None in the case that a _label_reference()
            # were subject to a replacement operation, in which case
            # the replacement of the Label element may have changed
            # to something else like a ColumnClause expression.
            order_by_elem = element.element._order_by_label_element

            if (
                order_by_elem is not None
                and order_by_elem.name in resolve_dict
                and order_by_elem.shares_lineage(
                    resolve_dict[order_by_elem.name]
                )
            ):
                kwargs[
                    "render_label_as_label"
                ] = element.element._order_by_label_element
        return self.process(
            element.element,
            within_columns_clause=within_columns_clause,
            **kwargs
        )

    def visit_textual_label_reference(
        self, element, within_columns_clause=False, **kwargs
    ):
        if not self.stack:
            # compiling the element outside of the context of a SELECT
            return self.process(element._text_clause)

        selectable = self.stack[-1]["selectable"]
        with_cols, only_froms, only_cols = selectable._label_resolve_dict
        try:
            if within_columns_clause:
                col = only_froms[element.element]
            else:
                col = with_cols[element.element]
        except KeyError as err:
            coercions._no_text_coercion(
                element.element,
                extra=(
                    "Can't resolve label reference for ORDER BY / "
                    "GROUP BY / DISTINCT etc."
                ),
                exc_cls=exc.CompileError,
                err=err,
            )
        else:
            kwargs["render_label_as_label"] = col
            return self.process(
                col, within_columns_clause=within_columns_clause, **kwargs
            )

    def visit_label(
        self,
        label,
        add_to_result_map=None,
        within_label_clause=False,
        within_columns_clause=False,
        render_label_as_label=None,
        result_map_targets=(),
        **kw
    ):
        # only render labels within the columns clause
        # or ORDER BY clause of a select.  dialect-specific compilers
        # can modify this behavior.
        render_label_with_as = (
            within_columns_clause and not within_label_clause
        )
        render_label_only = render_label_as_label is label

        if render_label_only or render_label_with_as:
            if isinstance(label.name, elements._truncated_label):
                labelname = self._truncated_identifier("colident", label.name)
            else:
                labelname = label.name

        if render_label_with_as:
            if add_to_result_map is not None:
                add_to_result_map(
                    labelname,
                    label.name,
                    (label, labelname) + label._alt_names + result_map_targets,
                    label.type,
                )

            return (
                label.element._compiler_dispatch(
                    self,
                    within_columns_clause=True,
                    within_label_clause=True,
                    **kw
                )
                + OPERATORS[operators.as_]
                + self.preparer.format_label(label, labelname)
            )
        elif render_label_only:
            return self.preparer.format_label(label, labelname)
        else:
            return label.element._compiler_dispatch(
                self, within_columns_clause=False, **kw
            )

    def _fallback_column_name(self, column):
        raise exc.CompileError(
            "Cannot compile Column object until " "its 'name' is assigned."
        )

    def visit_column(
        self,
        column,
        add_to_result_map=None,
        include_table=True,
        result_map_targets=(),
        **kwargs
    ):
        name = orig_name = column.name
        if name is None:
            name = self._fallback_column_name(column)

        is_literal = column.is_literal
        if not is_literal and isinstance(name, elements._truncated_label):
            name = self._truncated_identifier("colident", name)

        if add_to_result_map is not None:
            targets = (column, name, column.key) + result_map_targets
            if column._label:
                targets += (column._label,)

            add_to_result_map(name, orig_name, targets, column.type)

        if is_literal:
            # note we are not currently accommodating for
            # literal_column(quoted_name('ident', True)) here
            name = self.escape_literal_column(name)
        else:
            name = self.preparer.quote(name)
        table = column.table
        if table is None or not include_table or not table.named_with_column:
            return name
        else:
            effective_schema = self.preparer.schema_for_object(table)

            if effective_schema:
                schema_prefix = (
                    self.preparer.quote_schema(effective_schema) + "."
                )
            else:
                schema_prefix = ""
            tablename = table.name
            if isinstance(tablename, elements._truncated_label):
                tablename = self._truncated_identifier("alias", tablename)

            return schema_prefix + self.preparer.quote(tablename) + "." + name

    def visit_collation(self, element, **kw):
        return self.preparer.format_collation(element.collation)

    def visit_fromclause(self, fromclause, **kwargs):
        return fromclause.name

    def visit_index(self, index, **kwargs):
        return index.name

    def visit_typeclause(self, typeclause, **kw):
        kw["type_expression"] = typeclause
        return self.dialect.type_compiler.process(typeclause.type, **kw)

    def post_process_text(self, text):
        if self.preparer._double_percents:
            text = text.replace("%", "%%")
        return text

    def escape_literal_column(self, text):
        if self.preparer._double_percents:
            text = text.replace("%", "%%")
        return text

    def visit_textclause(self, textclause, add_to_result_map=None, **kw):
        def do_bindparam(m):
            name = m.group(1)
            if name in textclause._bindparams:
                return self.process(textclause._bindparams[name], **kw)
            else:
                return self.bindparam_string(name, **kw)

        if not self.stack:
            self.isplaintext = True

        if add_to_result_map:
            # text() object is present in the columns clause of a
            # select().   Add a no-name entry to the result map so that
            # row[text()] produces a result
            add_to_result_map(None, None, (textclause,), sqltypes.NULLTYPE)

        # un-escape any \:params
        return BIND_PARAMS_ESC.sub(
            lambda m: m.group(1),
            BIND_PARAMS.sub(
                do_bindparam, self.post_process_text(textclause.text)
            ),
        )

    def visit_textual_select(
        self, taf, compound_index=None, asfrom=False, **kw
    ):

        toplevel = not self.stack
        entry = self._default_stack_entry if toplevel else self.stack[-1]

        populate_result_map = (
            toplevel
            or (
                compound_index == 0
                and entry.get("need_result_map_for_compound", False)
            )
            or entry.get("need_result_map_for_nested", False)
        )

        if populate_result_map:
            self._ordered_columns = (
                self._textual_ordered_columns
            ) = taf.positional

            # enable looser result column matching when the SQL text links to
            # Column objects by name only
            self._loose_column_name_matching = not taf.positional and bool(
                taf.column_args
            )

            for c in taf.column_args:
                self.process(
                    c,
                    within_columns_clause=True,
                    add_to_result_map=self._add_to_result_map,
                )

        return self.process(taf.element, **kw)

    def visit_null(self, expr, **kw):
        return "NULL"

    def visit_true(self, expr, **kw):
        if self.dialect.supports_native_boolean:
            return "true"
        else:
            return "1"

    def visit_false(self, expr, **kw):
        if self.dialect.supports_native_boolean:
            return "false"
        else:
            return "0"

    def visit_clauselist(self, clauselist, **kw):
        sep = clauselist.operator
        if sep is None:
            sep = " "
        else:
            sep = OPERATORS[clauselist.operator]

        text = sep.join(
            s
            for s in (
                c._compiler_dispatch(self, **kw) for c in clauselist.clauses
            )
            if s
        )
        if clauselist._tuple_values and self.dialect.tuple_in_values:
            text = "VALUES " + text
        return text

    def visit_case(self, clause, **kwargs):
        x = "CASE "
        if clause.value is not None:
            x += clause.value._compiler_dispatch(self, **kwargs) + " "
        for cond, result in clause.whens:
            x += (
                "WHEN "
                + cond._compiler_dispatch(self, **kwargs)
                + " THEN "
                + result._compiler_dispatch(self, **kwargs)
                + " "
            )
        if clause.else_ is not None:
            x += (
                "ELSE " + clause.else_._compiler_dispatch(self, **kwargs) + " "
            )
        x += "END"
        return x

    def visit_type_coerce(self, type_coerce, **kw):
        return type_coerce.typed_expression._compiler_dispatch(self, **kw)

    def visit_cast(self, cast, **kwargs):
        return "CAST(%s AS %s)" % (
            cast.clause._compiler_dispatch(self, **kwargs),
            cast.typeclause._compiler_dispatch(self, **kwargs),
        )

    def _format_frame_clause(self, range_, **kw):

        return "%s AND %s" % (
            "UNBOUNDED PRECEDING"
            if range_[0] is elements.RANGE_UNBOUNDED
            else "CURRENT ROW"
            if range_[0] is elements.RANGE_CURRENT
            else "%s PRECEDING"
            % (self.process(elements.literal(abs(range_[0])), **kw),)
            if range_[0] < 0
            else "%s FOLLOWING"
            % (self.process(elements.literal(range_[0]), **kw),),
            "UNBOUNDED FOLLOWING"
            if range_[1] is elements.RANGE_UNBOUNDED
            else "CURRENT ROW"
            if range_[1] is elements.RANGE_CURRENT
            else "%s PRECEDING"
            % (self.process(elements.literal(abs(range_[1])), **kw),)
            if range_[1] < 0
            else "%s FOLLOWING"
            % (self.process(elements.literal(range_[1]), **kw),),
        )

    def visit_over(self, over, **kwargs):
        if over.range_:
            range_ = "RANGE BETWEEN %s" % self._format_frame_clause(
                over.range_, **kwargs
            )
        elif over.rows:
            range_ = "ROWS BETWEEN %s" % self._format_frame_clause(
                over.rows, **kwargs
            )
        else:
            range_ = None

        return "%s OVER (%s)" % (
            over.element._compiler_dispatch(self, **kwargs),
            " ".join(
                [
                    "%s BY %s"
                    % (word, clause._compiler_dispatch(self, **kwargs))
                    for word, clause in (
                        ("PARTITION", over.partition_by),
                        ("ORDER", over.order_by),
                    )
                    if clause is not None and len(clause)
                ]
                + ([range_] if range_ else [])
            ),
        )

    def visit_withingroup(self, withingroup, **kwargs):
        return "%s WITHIN GROUP (ORDER BY %s)" % (
            withingroup.element._compiler_dispatch(self, **kwargs),
            withingroup.order_by._compiler_dispatch(self, **kwargs),
        )

    def visit_funcfilter(self, funcfilter, **kwargs):
        return "%s FILTER (WHERE %s)" % (
            funcfilter.func._compiler_dispatch(self, **kwargs),
            funcfilter.criterion._compiler_dispatch(self, **kwargs),
        )

    def visit_extract(self, extract, **kwargs):
        field = self.extract_map.get(extract.field, extract.field)
        return "EXTRACT(%s FROM %s)" % (
            field,
            extract.expr._compiler_dispatch(self, **kwargs),
        )

    def visit_function(self, func, add_to_result_map=None, **kwargs):
        if add_to_result_map is not None:
            add_to_result_map(func.name, func.name, (), func.type)

        disp = getattr(self, "visit_%s_func" % func.name.lower(), None)
        if disp:
            return disp(func, **kwargs)
        else:
            name = FUNCTIONS.get(func.__class__, None)
            if name:
                if func._has_args:
                    name += "%(expr)s"
            else:
                name = func.name
                name = (
                    self.preparer.quote(name)
                    if self.preparer._requires_quotes_illegal_chars(name)
                    or isinstance(name, elements.quoted_name)
                    else name
                )
                name = name + "%(expr)s"
            return ".".join(
                [
                    (
                        self.preparer.quote(tok)
                        if self.preparer._requires_quotes_illegal_chars(tok)
                        or isinstance(name, elements.quoted_name)
                        else tok
                    )
                    for tok in func.packagenames
                ]
                + [name]
            ) % {"expr": self.function_argspec(func, **kwargs)}

    def visit_next_value_func(self, next_value, **kw):
        return self.visit_sequence(next_value.sequence)

    def visit_sequence(self, sequence, **kw):
        raise NotImplementedError(
            "Dialect '%s' does not support sequence increments."
            % self.dialect.name
        )

    def function_argspec(self, func, **kwargs):
        return func.clause_expr._compiler_dispatch(self, **kwargs)

    def visit_compound_select(
        self, cs, asfrom=False, compound_index=0, **kwargs
    ):
        toplevel = not self.stack
        entry = self._default_stack_entry if toplevel else self.stack[-1]
        need_result_map = toplevel or (
            compound_index == 0
            and entry.get("need_result_map_for_compound", False)
        )

        self.stack.append(
            {
                "correlate_froms": entry["correlate_froms"],
                "asfrom_froms": entry["asfrom_froms"],
                "selectable": cs,
                "need_result_map_for_compound": need_result_map,
            }
        )

        keyword = self.compound_keywords.get(cs.keyword)

        text = (" " + keyword + " ").join(
            (
                c._compiler_dispatch(
                    self, asfrom=asfrom, compound_index=i, **kwargs
                )
                for i, c in enumerate(cs.selects)
            )
        )

        kwargs["include_table"] = False
        text += self.group_by_clause(cs, **dict(asfrom=asfrom, **kwargs))
        text += self.order_by_clause(cs, **kwargs)
        text += (
            (cs._limit_clause is not None or cs._offset_clause is not None)
            and self.limit_clause(cs, **kwargs)
            or ""
        )

        if self.ctes and toplevel:
            text = self._render_cte_clause() + text

        self.stack.pop(-1)
        return text

    def _get_operator_dispatch(self, operator_, qualifier1, qualifier2):
        attrname = "visit_%s_%s%s" % (
            operator_.__name__,
            qualifier1,
            "_" + qualifier2 if qualifier2 else "",
        )
        return getattr(self, attrname, None)

    def visit_unary(self, unary, **kw):
        if unary.operator:
            if unary.modifier:
                raise exc.CompileError(
                    "Unary expression does not support operator "
                    "and modifier simultaneously"
                )
            disp = self._get_operator_dispatch(
                unary.operator, "unary", "operator"
            )
            if disp:
                return disp(unary, unary.operator, **kw)
            else:
                return self._generate_generic_unary_operator(
                    unary, OPERATORS[unary.operator], **kw
                )
        elif unary.modifier:
            disp = self._get_operator_dispatch(
                unary.modifier, "unary", "modifier"
            )
            if disp:
                return disp(unary, unary.modifier, **kw)
            else:
                return self._generate_generic_unary_modifier(
                    unary, OPERATORS[unary.modifier], **kw
                )
        else:
            raise exc.CompileError(
                "Unary expression has no operator or modifier"
            )

    def visit_istrue_unary_operator(self, element, operator, **kw):
        if (
            element._is_implicitly_boolean
            or self.dialect.supports_native_boolean
        ):
            return self.process(element.element, **kw)
        else:
            return "%s = 1" % self.process(element.element, **kw)

    def visit_isfalse_unary_operator(self, element, operator, **kw):
        if (
            element._is_implicitly_boolean
            or self.dialect.supports_native_boolean
        ):
            return "NOT %s" % self.process(element.element, **kw)
        else:
            return "%s = 0" % self.process(element.element, **kw)

    def visit_notmatch_op_binary(self, binary, operator, **kw):
        return "NOT %s" % self.visit_binary(
            binary, override_operator=operators.match_op
        )

    def visit_empty_set_expr(self, element_types):
        raise NotImplementedError(
            "Dialect '%s' does not support empty set expression."
            % self.dialect.name
        )

    def _literal_execute_expanding_parameter_literal_binds(
        self, parameter, values
    ):
        if not values:
            replacement_expression = self.visit_empty_set_expr(
                parameter._expanding_in_types
                if parameter._expanding_in_types
                else [parameter.type]
            )

        elif isinstance(values[0], (tuple, list)):
            replacement_expression = (
                "VALUES " if self.dialect.tuple_in_values else ""
            ) + ", ".join(
                "(%s)"
                % (
                    ", ".join(
                        self.render_literal_value(value, parameter.type)
                        for value in tuple_element
                    )
                )
                for i, tuple_element in enumerate(values)
            )
        else:
            replacement_expression = ", ".join(
                self.render_literal_value(value, parameter.type)
                for value in values
            )

        return (), replacement_expression

    def _literal_execute_expanding_parameter(self, name, parameter, values):
        if parameter.literal_execute:
            return self._literal_execute_expanding_parameter_literal_binds(
                parameter, values
            )

        if not values:
            to_update = []
            replacement_expression = self.visit_empty_set_expr(
                parameter._expanding_in_types
                if parameter._expanding_in_types
                else [parameter.type]
            )

        elif isinstance(values[0], (tuple, list)):
            to_update = [
                ("%s_%s_%s" % (name, i, j), value)
                for i, tuple_element in enumerate(values, 1)
                for j, value in enumerate(tuple_element, 1)
            ]
            replacement_expression = (
                "VALUES " if self.dialect.tuple_in_values else ""
            ) + ", ".join(
                "(%s)"
                % (
                    ", ".join(
                        self.bindtemplate
                        % {"name": to_update[i * len(tuple_element) + j][0]}
                        for j, value in enumerate(tuple_element)
                    )
                )
                for i, tuple_element in enumerate(values)
            )
        else:
            to_update = [
                ("%s_%s" % (name, i), value)
                for i, value in enumerate(values, 1)
            ]
            replacement_expression = ", ".join(
                self.bindtemplate % {"name": key} for key, value in to_update
            )

        return to_update, replacement_expression

    def visit_binary(
        self,
        binary,
        override_operator=None,
        eager_grouping=False,
        from_linter=None,
        **kw
    ):

        if from_linter and operators.is_comparison(binary.operator):
            from_linter.edges.update(
                itertools.product(
                    binary.left._from_objects, binary.right._from_objects
                )
            )

        # don't allow "? = ?" to render
        if (
            self.ansi_bind_rules
            and isinstance(binary.left, elements.BindParameter)
            and isinstance(binary.right, elements.BindParameter)
        ):
            kw["literal_execute"] = True

        operator_ = override_operator or binary.operator
        disp = self._get_operator_dispatch(operator_, "binary", None)
        if disp:
            return disp(binary, operator_, **kw)
        else:
            try:
                opstring = OPERATORS[operator_]
            except KeyError as err:
                util.raise_(
                    exc.UnsupportedCompilationError(self, operator_),
                    replace_context=err,
                )
            else:
                return self._generate_generic_binary(
                    binary, opstring, from_linter=from_linter, **kw
                )

    def visit_function_as_comparison_op_binary(self, element, operator, **kw):
        return self.process(element.sql_function, **kw)

    def visit_mod_binary(self, binary, operator, **kw):
        if self.preparer._double_percents:
            return (
                self.process(binary.left, **kw)
                + " %% "
                + self.process(binary.right, **kw)
            )
        else:
            return (
                self.process(binary.left, **kw)
                + " % "
                + self.process(binary.right, **kw)
            )

    def visit_custom_op_binary(self, element, operator, **kw):
        kw["eager_grouping"] = operator.eager_grouping
        return self._generate_generic_binary(
            element, " " + operator.opstring + " ", **kw
        )

    def visit_custom_op_unary_operator(self, element, operator, **kw):
        return self._generate_generic_unary_operator(
            element, operator.opstring + " ", **kw
        )

    def visit_custom_op_unary_modifier(self, element, operator, **kw):
        return self._generate_generic_unary_modifier(
            element, " " + operator.opstring, **kw
        )

    def _generate_generic_binary(
        self, binary, opstring, eager_grouping=False, **kw
    ):

        _in_binary = kw.get("_in_binary", False)

        kw["_in_binary"] = True
        text = (
            binary.left._compiler_dispatch(
                self, eager_grouping=eager_grouping, **kw
            )
            + opstring
            + binary.right._compiler_dispatch(
                self, eager_grouping=eager_grouping, **kw
            )
        )

        if _in_binary and eager_grouping:
            text = "(%s)" % text
        return text

    def _generate_generic_unary_operator(self, unary, opstring, **kw):
        return opstring + unary.element._compiler_dispatch(self, **kw)

    def _generate_generic_unary_modifier(self, unary, opstring, **kw):
        return unary.element._compiler_dispatch(self, **kw) + opstring

    @util.memoized_property
    def _like_percent_literal(self):
        return elements.literal_column("'%'", type_=sqltypes.STRINGTYPE)

    def visit_contains_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__add__(binary.right).__add__(percent)
        return self.visit_like_op_binary(binary, operator, **kw)

    def visit_notcontains_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__add__(binary.right).__add__(percent)
        return self.visit_notlike_op_binary(binary, operator, **kw)

    def visit_startswith_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__radd__(binary.right)
        return self.visit_like_op_binary(binary, operator, **kw)

    def visit_notstartswith_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__radd__(binary.right)
        return self.visit_notlike_op_binary(binary, operator, **kw)

    def visit_endswith_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__add__(binary.right)
        return self.visit_like_op_binary(binary, operator, **kw)

    def visit_notendswith_op_binary(self, binary, operator, **kw):
        binary = binary._clone()
        percent = self._like_percent_literal
        binary.right = percent.__add__(binary.right)
        return self.visit_notlike_op_binary(binary, operator, **kw)

    def visit_like_op_binary(self, binary, operator, **kw):
        escape = binary.modifiers.get("escape", None)

        # TODO: use ternary here, not "and"/ "or"
        return "%s LIKE %s" % (
            binary.left._compiler_dispatch(self, **kw),
            binary.right._compiler_dispatch(self, **kw),
        ) + (
            " ESCAPE " + self.render_literal_value(escape, sqltypes.STRINGTYPE)
            if escape
            else ""
        )

    def visit_notlike_op_binary(self, binary, operator, **kw):
        escape = binary.modifiers.get("escape", None)
        return "%s NOT LIKE %s" % (
            binary.left._compiler_dispatch(self, **kw),
            binary.right._compiler_dispatch(self, **kw),
        ) + (
            " ESCAPE " + self.render_literal_value(escape, sqltypes.STRINGTYPE)
            if escape
            else ""
        )

    def visit_ilike_op_binary(self, binary, operator, **kw):
        escape = binary.modifiers.get("escape", None)
        return "lower(%s) LIKE lower(%s)" % (
            binary.left._compiler_dispatch(self, **kw),
            binary.right._compiler_dispatch(self, **kw),
        ) + (
            " ESCAPE " + self.render_literal_value(escape, sqltypes.STRINGTYPE)
            if escape
            else ""
        )

    def visit_notilike_op_binary(self, binary, operator, **kw):
        escape = binary.modifiers.get("escape", None)
        return "lower(%s) NOT LIKE lower(%s)" % (
            binary.left._compiler_dispatch(self, **kw),
            binary.right._compiler_dispatch(self, **kw),
        ) + (
            " ESCAPE " + self.render_literal_value(escape, sqltypes.STRINGTYPE)
            if escape
            else ""
        )

    def visit_between_op_binary(self, binary, operator, **kw):
        symmetric = binary.modifiers.get("symmetric", False)
        return self._generate_generic_binary(
            binary, " BETWEEN SYMMETRIC " if symmetric else " BETWEEN ", **kw
        )

    def visit_notbetween_op_binary(self, binary, operator, **kw):
        symmetric = binary.modifiers.get("symmetric", False)
        return self._generate_generic_binary(
            binary,
            " NOT BETWEEN SYMMETRIC " if symmetric else " NOT BETWEEN ",
            **kw
        )

    def visit_bindparam(
        self,
        bindparam,
        within_columns_clause=False,
        literal_binds=False,
        skip_bind_expression=False,
        literal_execute=False,
        render_postcompile=False,
        **kwargs
    ):

        if not skip_bind_expression:
            impl = bindparam.type.dialect_impl(self.dialect)
            if impl._has_bind_expression:
                bind_expression = impl.bind_expression(bindparam)
                return self.process(
                    bind_expression,
                    skip_bind_expression=True,
                    within_columns_clause=within_columns_clause,
                    literal_binds=literal_binds,
                    literal_execute=literal_execute,
                    **kwargs
                )

        if not literal_binds:
            literal_execute = (
                literal_execute
                or bindparam.literal_execute
                or (within_columns_clause and self.ansi_bind_rules)
            )
            post_compile = literal_execute or bindparam.expanding
        else:
            post_compile = False

        if not literal_execute and (literal_binds):
            ret = self.render_literal_bindparam(
                bindparam, within_columns_clause=True, **kwargs
            )
            if bindparam.expanding:
                ret = "(%s)" % ret
            return ret

        name = self._truncate_bindparam(bindparam)

        if name in self.binds:
            existing = self.binds[name]
            if existing is not bindparam:
                if (
                    existing.unique or bindparam.unique
                ) and not existing.proxy_set.intersection(bindparam.proxy_set):
                    raise exc.CompileError(
                        "Bind parameter '%s' conflicts with "
                        "unique bind parameter of the same name"
                        % bindparam.key
                    )
                elif existing._is_crud or bindparam._is_crud:
                    raise exc.CompileError(
                        "bindparam() name '%s' is reserved "
                        "for automatic usage in the VALUES or SET "
                        "clause of this "
                        "insert/update statement.   Please use a "
                        "name other than column name when using bindparam() "
                        "with insert() or update() (for example, 'b_%s')."
                        % (bindparam.key, bindparam.key)
                    )

        self.binds[bindparam.key] = self.binds[name] = bindparam
        if bindparam.isoutparam:
            self.has_out_parameters = True

        if post_compile:
            if render_postcompile:
                self._render_postcompile = True

            if literal_execute:
                self.literal_execute_params |= {bindparam}
            else:
                self.post_compile_params |= {bindparam}

        ret = self.bindparam_string(
            name,
            post_compile=post_compile,
            expanding=bindparam.expanding,
            **kwargs
        )
        if bindparam.expanding:
            ret = "(%s)" % ret
        return ret

    def render_literal_bindparam(
        self, bindparam, render_literal_value=NO_ARG, **kw
    ):
        if render_literal_value is not NO_ARG:
            value = render_literal_value
        else:
            if bindparam.value is None and bindparam.callable is None:
                raise exc.CompileError(
                    "Bind parameter '%s' without a "
                    "renderable value not allowed here." % bindparam.key
                )
            value = bindparam.effective_value

        if bindparam.expanding:
            leep = self._literal_execute_expanding_parameter_literal_binds
            to_update, replacement_expr = leep(bindparam, value)
            return replacement_expr
        else:
            return self.render_literal_value(value, bindparam.type)

    def render_literal_value(self, value, type_):
        """Render the value of a bind parameter as a quoted literal.

        This is used for statement sections that do not accept bind parameters
        on the target driver/database.

        This should be implemented by subclasses using the quoting services
        of the DBAPI.

        """

        processor = type_._cached_literal_processor(self.dialect)
        if processor:
            return processor(value)
        else:
            raise NotImplementedError(
                "Don't know how to literal-quote value %r" % value
            )

    def _truncate_bindparam(self, bindparam):
        if bindparam in self.bind_names:
            return self.bind_names[bindparam]

        bind_name = bindparam.key
        if isinstance(bind_name, elements._truncated_label):
            bind_name = self._truncated_identifier("bindparam", bind_name)

        # add to bind_names for translation
        self.bind_names[bindparam] = bind_name

        return bind_name

    def _truncated_identifier(self, ident_class, name):
        if (ident_class, name) in self.truncated_names:
            return self.truncated_names[(ident_class, name)]

        anonname = name.apply_map(self.anon_map)

        if len(anonname) > self.label_length - 6:
            counter = self.truncated_names.get(ident_class, 1)
            truncname = (
                anonname[0 : max(self.label_length - 6, 0)]
                + "_"
                + hex(counter)[2:]
            )
            self.truncated_names[ident_class] = counter + 1
        else:
            truncname = anonname
        self.truncated_names[(ident_class, name)] = truncname
        return truncname

    def _anonymize(self, name):
        return name % self.anon_map

    def bindparam_string(
        self,
        name,
        positional_names=None,
        post_compile=False,
        expanding=False,
        **kw
    ):
        if self.positional:
            if positional_names is not None:
                positional_names.append(name)
            else:
                self.positiontup.append(name)
        if post_compile:
            return "[POSTCOMPILE_%s]" % name
        else:
            return self.bindtemplate % {"name": name}

    def visit_cte(
        self,
        cte,
        asfrom=False,
        ashint=False,
        fromhints=None,
        visiting_cte=None,
        from_linter=None,
        **kwargs
    ):
        self._init_cte_state()

        kwargs["visiting_cte"] = cte
        if isinstance(cte.name, elements._truncated_label):
            cte_name = self._truncated_identifier("alias", cte.name)
        else:
            cte_name = cte.name

        is_new_cte = True
        embedded_in_current_named_cte = False

        if cte_name in self.ctes_by_name:
            existing_cte = self.ctes_by_name[cte_name]
            embedded_in_current_named_cte = visiting_cte is existing_cte

            # we've generated a same-named CTE that we are enclosed in,
            # or this is the same CTE.  just return the name.
            if cte in existing_cte._restates or cte is existing_cte:
                is_new_cte = False
            elif existing_cte in cte._restates:
                # we've generated a same-named CTE that is
                # enclosed in us - we take precedence, so
                # discard the text for the "inner".
                del self.ctes[existing_cte]
            else:
                raise exc.CompileError(
                    "Multiple, unrelated CTEs found with "
                    "the same name: %r" % cte_name
                )

        if asfrom or is_new_cte:
            if cte._cte_alias is not None:
                pre_alias_cte = cte._cte_alias
                cte_pre_alias_name = cte._cte_alias.name
                if isinstance(cte_pre_alias_name, elements._truncated_label):
                    cte_pre_alias_name = self._truncated_identifier(
                        "alias", cte_pre_alias_name
                    )
            else:
                pre_alias_cte = cte
                cte_pre_alias_name = None

        if is_new_cte:
            self.ctes_by_name[cte_name] = cte

            if (
                "autocommit" in cte.element._execution_options
                and "autocommit" not in self.execution_options
            ):
                self.execution_options = self.execution_options.union(
                    {
                        "autocommit": cte.element._execution_options[
                            "autocommit"
                        ]
                    }
                )

            if pre_alias_cte not in self.ctes:
                self.visit_cte(pre_alias_cte, **kwargs)

            if not cte_pre_alias_name and cte not in self.ctes:
                if cte.recursive:
                    self.ctes_recursive = True
                text = self.preparer.format_alias(cte, cte_name)
                if cte.recursive:
                    if isinstance(cte.element, selectable.Select):
                        col_source = cte.element
                    elif isinstance(cte.element, selectable.CompoundSelect):
                        col_source = cte.element.selects[0]
                    else:
                        assert False
                    recur_cols = [
                        c
                        for c in util.unique_list(col_source.inner_columns)
                        if c is not None
                    ]

                    text += "(%s)" % (
                        ", ".join(
                            self.preparer.format_column(ident)
                            for ident in recur_cols
                        )
                    )

                if self.positional:
                    kwargs["positional_names"] = self.cte_positional[cte] = []

                assert kwargs.get("subquery", False) is False
                text += " AS %s\n(%s)" % (
                    self._generate_prefixes(cte, cte._prefixes, **kwargs),
                    cte.element._compiler_dispatch(
                        self, asfrom=True, **kwargs
                    ),
                )

                if cte._suffixes:
                    text += " " + self._generate_prefixes(
                        cte, cte._suffixes, **kwargs
                    )

                self.ctes[cte] = text

        if asfrom:
            if from_linter:
                from_linter.froms[cte] = cte_name

            if not is_new_cte and embedded_in_current_named_cte:
                return self.preparer.format_alias(cte, cte_name)

            if cte_pre_alias_name:
                text = self.preparer.format_alias(cte, cte_pre_alias_name)
                if self.preparer._requires_quotes(cte_name):
                    cte_name = self.preparer.quote(cte_name)
                text += self.get_render_as_alias_suffix(cte_name)
                return text
            else:
                return self.preparer.format_alias(cte, cte_name)

    def visit_alias(
        self,
        alias,
        asfrom=False,
        ashint=False,
        iscrud=False,
        fromhints=None,
        subquery=False,
        lateral=False,
        enclosing_alias=None,
        from_linter=None,
        **kwargs
    ):
        if enclosing_alias is not None and enclosing_alias.element is alias:
            inner = alias.element._compiler_dispatch(
                self,
                asfrom=asfrom,
                ashint=ashint,
                iscrud=iscrud,
                fromhints=fromhints,
                lateral=lateral,
                enclosing_alias=alias,
                **kwargs
            )
            if subquery and (asfrom or lateral):
                inner = "(%s)" % (inner,)
            return inner
        else:
            enclosing_alias = kwargs["enclosing_alias"] = alias

        if asfrom or ashint:
            if isinstance(alias.name, elements._truncated_label):
                alias_name = self._truncated_identifier("alias", alias.name)
            else:
                alias_name = alias.name

        if ashint:
            return self.preparer.format_alias(alias, alias_name)
        elif asfrom:
            if from_linter:
                from_linter.froms[alias] = alias_name

            inner = alias.element._compiler_dispatch(
                self, asfrom=True, lateral=lateral, **kwargs
            )
            if subquery:
                inner = "(%s)" % (inner,)

            ret = inner + self.get_render_as_alias_suffix(
                self.preparer.format_alias(alias, alias_name)
            )
            if fromhints and alias in fromhints:
                ret = self.format_from_hint_text(
                    ret, alias, fromhints[alias], iscrud
                )

            return ret
        else:
            # note we cancel the "subquery" flag here as well
            return alias.element._compiler_dispatch(
                self, lateral=lateral, **kwargs
            )

    def visit_subquery(self, subquery, **kw):
        kw["subquery"] = True
        return self.visit_alias(subquery, **kw)

    def visit_lateral(self, lateral, **kw):
        kw["lateral"] = True
        return "LATERAL %s" % self.visit_alias(lateral, **kw)

    def visit_tablesample(self, tablesample, asfrom=False, **kw):
        text = "%s TABLESAMPLE %s" % (
            self.visit_alias(tablesample, asfrom=True, **kw),
            tablesample._get_method()._compiler_dispatch(self, **kw),
        )

        if tablesample.seed is not None:
            text += " REPEATABLE (%s)" % (
                tablesample.seed._compiler_dispatch(self, **kw)
            )

        return text

    def get_render_as_alias_suffix(self, alias_name_text):
        return " AS " + alias_name_text

    def _add_to_result_map(self, keyname, name, objects, type_):
        if keyname is None:
            self._ordered_columns = False
            self._textual_ordered_columns = True
        self._result_columns.append((keyname, name, objects, type_))

    def _label_select_column(
        self,
        select,
        column,
        populate_result_map,
        asfrom,
        column_clause_args,
        name=None,
        within_columns_clause=True,
        column_is_repeated=False,
        need_column_expressions=False,
    ):
        """produce labeled columns present in a select()."""

        impl = column.type.dialect_impl(self.dialect)

        if impl._has_column_expression and (
            need_column_expressions or populate_result_map
        ):
            col_expr = impl.column_expression(column)
        else:
            col_expr = column

        if populate_result_map:
            # pass an "add_to_result_map" callable into the compilation
            # of embedded columns.  this collects information about the
            # column as it will be fetched in the result and is coordinated
            # with cursor.description when the query is executed.
            add_to_result_map = self._add_to_result_map

            # if the SELECT statement told us this column is a repeat,
            # wrap the callable with one that prevents the addition of the
            # targets
            if column_is_repeated:
                _add_to_result_map = add_to_result_map

                def add_to_result_map(keyname, name, objects, type_):
                    _add_to_result_map(keyname, name, (), type_)

            # if we redefined col_expr for type expressions, wrap the
            # callable with one that adds the original column to the targets
            elif col_expr is not column:
                _add_to_result_map = add_to_result_map

                def add_to_result_map(keyname, name, objects, type_):
                    _add_to_result_map(
                        keyname, name, (column,) + objects, type_
                    )

        else:
            add_to_result_map = None

        if not within_columns_clause:
            result_expr = col_expr
        elif isinstance(column, elements.Label):
            if col_expr is not column:
                result_expr = _CompileLabel(
                    col_expr, column.name, alt_names=(column.element,)
                )
            else:
                result_expr = col_expr

        elif select is not None and name:
            result_expr = _CompileLabel(
                col_expr, name, alt_names=(column._key_label,)
            )
        elif (
            asfrom
            and isinstance(column, elements.ColumnClause)
            and not column.is_literal
            and column.table is not None
            and not isinstance(column.table, selectable.Select)
        ):
            result_expr = _CompileLabel(
                col_expr,
                coercions.expect(roles.TruncatedLabelRole, column.name),
                alt_names=(column.key,),
            )
        elif (
            not isinstance(column, elements.TextClause)
            and (
                not isinstance(column, elements.UnaryExpression)
                or column.wraps_column_expression
            )
            and (
                not hasattr(column, "name")
                or isinstance(column, functions.FunctionElement)
            )
        ):
            result_expr = _CompileLabel(col_expr, column.anon_label)
        elif col_expr is not column:
            # TODO: are we sure "column" has a .name and .key here ?
            # assert isinstance(column, elements.ColumnClause)
            result_expr = _CompileLabel(
                col_expr,
                coercions.expect(roles.TruncatedLabelRole, column.name),
                alt_names=(column.key,),
            )
        else:
            result_expr = col_expr

        column_clause_args.update(
            within_columns_clause=within_columns_clause,
            add_to_result_map=add_to_result_map,
        )
        return result_expr._compiler_dispatch(self, **column_clause_args)

    def format_from_hint_text(self, sqltext, table, hint, iscrud):
        hinttext = self.get_from_hint_text(table, hint)
        if hinttext:
            sqltext += " " + hinttext
        return sqltext

    def get_select_hint_text(self, byfroms):
        return None

    def get_from_hint_text(self, table, text):
        return None

    def get_crud_hint_text(self, table, text):
        return None

    def get_statement_hint_text(self, hint_texts):
        return " ".join(hint_texts)

    _default_stack_entry = util.immutabledict(
        [("correlate_froms", frozenset()), ("asfrom_froms", frozenset())]
    )

    def _display_froms_for_select(self, select, asfrom, lateral=False):
        # utility method to help external dialects
        # get the correct from list for a select.
        # specifically the oracle dialect needs this feature
        # right now.
        toplevel = not self.stack
        entry = self._default_stack_entry if toplevel else self.stack[-1]

        correlate_froms = entry["correlate_froms"]
        asfrom_froms = entry["asfrom_froms"]

        if asfrom and not lateral:
            froms = select._get_display_froms(
                explicit_correlate_froms=correlate_froms.difference(
                    asfrom_froms
                ),
                implicit_correlate_froms=(),
            )
        else:
            froms = select._get_display_froms(
                explicit_correlate_froms=correlate_froms,
                implicit_correlate_froms=asfrom_froms,
            )
        return froms

    def visit_select(
        self,
        select,
        asfrom=False,
        fromhints=None,
        compound_index=0,
        select_wraps_for=None,
        lateral=False,
        from_linter=None,
        **kwargs
    ):

        toplevel = not self.stack
        entry = self._default_stack_entry if toplevel else self.stack[-1]

        populate_result_map = need_column_expressions = (
            toplevel
            or entry.get("need_result_map_for_compound", False)
            or entry.get("need_result_map_for_nested", False)
        )

        if compound_index > 0:
            populate_result_map = False

        # this was first proposed as part of #3372; however, it is not
        # reached in current tests and could possibly be an assertion
        # instead.
        if not populate_result_map and "add_to_result_map" in kwargs:
            del kwargs["add_to_result_map"]

        froms = self._setup_select_stack(
            select, entry, asfrom, lateral, compound_index
        )

        column_clause_args = kwargs.copy()
        column_clause_args.update(
            {"within_label_clause": False, "within_columns_clause": False}
        )

        text = "SELECT "  # we're off to a good start !

        if select._hints:
            hint_text, byfrom = self._setup_select_hints(select)
            if hint_text:
                text += hint_text + " "
        else:
            byfrom = None

        if select._prefixes:
            text += self._generate_prefixes(select, select._prefixes, **kwargs)

        text += self.get_select_precolumns(select, **kwargs)
        # the actual list of columns to print in the SELECT column list.
        inner_columns = [
            c
            for c in [
                self._label_select_column(
                    select,
                    column,
                    populate_result_map,
                    asfrom,
                    column_clause_args,
                    name=name,
                    column_is_repeated=repeated,
                    need_column_expressions=need_column_expressions,
                )
                for name, column, repeated in select._columns_plus_names
            ]
            if c is not None
        ]

        if populate_result_map and select_wraps_for is not None:
            # if this select is a compiler-generated wrapper,
            # rewrite the targeted columns in the result map

            translate = dict(
                zip(
                    [
                        name
                        for (key, name, repeated) in select._columns_plus_names
                    ],
                    [
                        name
                        for (
                            key,
                            name,
                            repeated,
                        ) in select_wraps_for._columns_plus_names
                    ],
                )
            )

            self._result_columns = [
                (key, name, tuple(translate.get(o, o) for o in obj), type_)
                for key, name, obj, type_ in self._result_columns
            ]

        text = self._compose_select_body(
            text, select, inner_columns, froms, byfrom, toplevel, kwargs
        )

        if select._statement_hints:
            per_dialect = [
                ht
                for (dialect_name, ht) in select._statement_hints
                if dialect_name in ("*", self.dialect.name)
            ]
            if per_dialect:
                text += " " + self.get_statement_hint_text(per_dialect)

        if self.ctes and toplevel:
            text = self._render_cte_clause() + text

        if select._suffixes:
            text += " " + self._generate_prefixes(
                select, select._suffixes, **kwargs
            )

        self.stack.pop(-1)

        return text

    def _setup_select_hints(self, select):
        byfrom = dict(
            [
                (
                    from_,
                    hinttext
                    % {"name": from_._compiler_dispatch(self, ashint=True)},
                )
                for (from_, dialect), hinttext in select._hints.items()
                if dialect in ("*", self.dialect.name)
            ]
        )
        hint_text = self.get_select_hint_text(byfrom)
        return hint_text, byfrom

    def _setup_select_stack(
        self, select, entry, asfrom, lateral, compound_index
    ):
        correlate_froms = entry["correlate_froms"]
        asfrom_froms = entry["asfrom_froms"]

        if compound_index > 0:
            # note this is cached
            select_0 = entry["selectable"].selects[0]
            if select_0._is_select_container:
                select_0 = select_0.element
            numcols = len(select_0.selected_columns)
            # numcols = len(select_0._columns_plus_names)
            if len(select._columns_plus_names) != numcols:
                raise exc.CompileError(
                    "All selectables passed to "
                    "CompoundSelect must have identical numbers of "
                    "columns; select #%d has %d columns, select "
                    "#%d has %d"
                    % (
                        1,
                        numcols,
                        compound_index + 1,
                        len(select.selected_columns),
                    )
                )

        if asfrom and not lateral:
            froms = select._get_display_froms(
                explicit_correlate_froms=correlate_froms.difference(
                    asfrom_froms
                ),
                implicit_correlate_froms=(),
            )
        else:
            froms = select._get_display_froms(
                explicit_correlate_froms=correlate_froms,
                implicit_correlate_froms=asfrom_froms,
            )

        new_correlate_froms = set(selectable._from_objects(*froms))
        all_correlate_froms = new_correlate_froms.union(correlate_froms)

        new_entry = {
            "asfrom_froms": new_correlate_froms,
            "correlate_froms": all_correlate_froms,
            "selectable": select,
        }
        self.stack.append(new_entry)

        return froms

    def _compose_select_body(
        self, text, select, inner_columns, froms, byfrom, toplevel, kwargs
    ):
        text += ", ".join(inner_columns)

        if self.linting & COLLECT_CARTESIAN_PRODUCTS:
            from_linter = FromLinter({}, set())
            if toplevel:
                self.from_linter = from_linter
        else:
            from_linter = None

        if froms:
            text += " \nFROM "

            if select._hints:
                text += ", ".join(
                    [
                        f._compiler_dispatch(
                            self,
                            asfrom=True,
                            fromhints=byfrom,
                            from_linter=from_linter,
                            **kwargs
                        )
                        for f in froms
                    ]
                )
            else:
                text += ", ".join(
                    [
                        f._compiler_dispatch(
                            self,
                            asfrom=True,
                            from_linter=from_linter,
                            **kwargs
                        )
                        for f in froms
                    ]
                )
        else:
            text += self.default_from()

        if select._whereclause is not None:
            t = select._whereclause._compiler_dispatch(
                self, from_linter=from_linter, **kwargs
            )
            if t:
                text += " \nWHERE " + t

        if (
            self.linting & COLLECT_CARTESIAN_PRODUCTS
            and self.linting & WARN_LINTING
        ):
            from_linter.warn()

        if select._group_by_clause.clauses:
            text += self.group_by_clause(select, **kwargs)

        if select._having is not None:
            t = select._having._compiler_dispatch(self, **kwargs)
            if t:
                text += " \nHAVING " + t

        if select._order_by_clause.clauses:
            text += self.order_by_clause(select, **kwargs)

        if (
            select._limit_clause is not None
            or select._offset_clause is not None
        ):
            text += self.limit_clause(select, **kwargs)

        if select._for_update_arg is not None:
            text += self.for_update_clause(select, **kwargs)

        return text

    def _generate_prefixes(self, stmt, prefixes, **kw):
        clause = " ".join(
            prefix._compiler_dispatch(self, **kw)
            for prefix, dialect_name in prefixes
            if dialect_name is None or dialect_name == self.dialect.name
        )
        if clause:
            clause += " "
        return clause

    def _render_cte_clause(self):
        if self.positional:
            self.positiontup = (
                sum([self.cte_positional[cte] for cte in self.ctes], [])
                + self.positiontup
            )
        cte_text = self.get_cte_preamble(self.ctes_recursive) + " "
        cte_text += ", \n".join([txt for txt in self.ctes.values()])
        cte_text += "\n "
        return cte_text

    def get_cte_preamble(self, recursive):
        if recursive:
            return "WITH RECURSIVE"
        else:
            return "WITH"

    def get_select_precolumns(self, select, **kw):
        """Called when building a ``SELECT`` statement, position is just
        before column list.

        """
        return select._distinct and "DISTINCT " or ""

    def group_by_clause(self, select, **kw):
        """allow dialects to customize how GROUP BY is rendered."""

        group_by = select._group_by_clause._compiler_dispatch(self, **kw)
        if group_by:
            return " GROUP BY " + group_by
        else:
            return ""

    def order_by_clause(self, select, **kw):
        """allow dialects to customize how ORDER BY is rendered."""

        order_by = select._order_by_clause._compiler_dispatch(self, **kw)
        if order_by:
            return " ORDER BY " + order_by
        else:
            return ""

    def for_update_clause(self, select, **kw):
        return " FOR UPDATE"

    def returning_clause(self, stmt, returning_cols):
        raise exc.CompileError(
            "RETURNING is not supported by this "
            "dialect's statement compiler."
        )

    def limit_clause(self, select, **kw):
        text = ""
        if select._limit_clause is not None:
            text += "\n LIMIT " + self.process(select._limit_clause, **kw)
        if select._offset_clause is not None:
            if select._limit_clause is None:
                text += "\n LIMIT -1"
            text += " OFFSET " + self.process(select._offset_clause, **kw)
        return text

    def visit_table(
        self,
        table,
        asfrom=False,
        iscrud=False,
        ashint=False,
        fromhints=None,
        use_schema=True,
        from_linter=None,
        **kwargs
    ):
        if from_linter:
            from_linter.froms[table] = table.fullname

        if asfrom or ashint:
            effective_schema = self.preparer.schema_for_object(table)

            if use_schema and effective_schema:
                ret = (
                    self.preparer.quote_schema(effective_schema)
                    + "."
                    + self.preparer.quote(table.name)
                )
            else:
                ret = self.preparer.quote(table.name)
            if fromhints and table in fromhints:
                ret = self.format_from_hint_text(
                    ret, table, fromhints[table], iscrud
                )
            return ret
        else:
            return ""

    def visit_join(self, join, asfrom=False, from_linter=None, **kwargs):
        if from_linter:
            from_linter.edges.add((join.left, join.right))

        if join.full:
            join_type = " FULL OUTER JOIN "
        elif join.isouter:
            join_type = " LEFT OUTER JOIN "
        else:
            join_type = " JOIN "
        return (
            join.left._compiler_dispatch(
                self, asfrom=True, from_linter=from_linter, **kwargs
            )
            + join_type
            + join.right._compiler_dispatch(
                self, asfrom=True, from_linter=from_linter, **kwargs
            )
            + " ON "
            # TODO: likely need asfrom=True here?
            + join.onclause._compiler_dispatch(
                self, from_linter=from_linter, **kwargs
            )
        )

    def _setup_crud_hints(self, stmt, table_text):
        dialect_hints = dict(
            [
                (table, hint_text)
                for (table, dialect), hint_text in stmt._hints.items()
                if dialect in ("*", self.dialect.name)
            ]
        )
        if stmt.table in dialect_hints:
            table_text = self.format_from_hint_text(
                table_text, stmt.table, dialect_hints[stmt.table], True
            )
        return dialect_hints, table_text

    def visit_insert(self, insert_stmt, **kw):
        toplevel = not self.stack

        self.stack.append(
            {
                "correlate_froms": set(),
                "asfrom_froms": set(),
                "selectable": insert_stmt,
            }
        )

        crud_params = crud._setup_crud_params(
            self, insert_stmt, crud.ISINSERT, **kw
        )

        if (
            not crud_params
            and not self.dialect.supports_default_values
            and not self.dialect.supports_empty_insert
        ):
            raise exc.CompileError(
                "The '%s' dialect with current database "
                "version settings does not support empty "
                "inserts." % self.dialect.name
            )

        if insert_stmt._has_multi_parameters:
            if not self.dialect.supports_multivalues_insert:
                raise exc.CompileError(
                    "The '%s' dialect with current database "
                    "version settings does not support "
                    "in-place multirow inserts." % self.dialect.name
                )
            crud_params_single = crud_params[0]
        else:
            crud_params_single = crud_params

        preparer = self.preparer
        supports_default_values = self.dialect.supports_default_values

        text = "INSERT "

        if insert_stmt._prefixes:
            text += self._generate_prefixes(
                insert_stmt, insert_stmt._prefixes, **kw
            )

        text += "INTO "
        table_text = preparer.format_table(insert_stmt.table)

        if insert_stmt._hints:
            _, table_text = self._setup_crud_hints(insert_stmt, table_text)

        text += table_text

        if crud_params_single or not supports_default_values:
            text += " (%s)" % ", ".join(
                [preparer.format_column(c[0]) for c in crud_params_single]
            )

        if self.returning or insert_stmt._returning:
            returning_clause = self.returning_clause(
                insert_stmt, self.returning or insert_stmt._returning
            )

            if self.returning_precedes_values:
                text += " " + returning_clause
        else:
            returning_clause = None

        if insert_stmt.select is not None:
            select_text = self.process(self._insert_from_select, **kw)

            if self.ctes and toplevel and self.dialect.cte_follows_insert:
                text += " %s%s" % (self._render_cte_clause(), select_text)
            else:
                text += " %s" % select_text
        elif not crud_params and supports_default_values:
            text += " DEFAULT VALUES"
        elif insert_stmt._has_multi_parameters:
            text += " VALUES %s" % (
                ", ".join(
                    "(%s)" % (", ".join(c[1] for c in crud_param_set))
                    for crud_param_set in crud_params
                )
            )
        else:
            insert_single_values_expr = ", ".join([c[1] for c in crud_params])
            text += " VALUES (%s)" % insert_single_values_expr
            if toplevel:
                self.insert_single_values_expr = insert_single_values_expr

        if insert_stmt._post_values_clause is not None:
            post_values_clause = self.process(
                insert_stmt._post_values_clause, **kw
            )
            if post_values_clause:
                text += " " + post_values_clause

        if returning_clause and not self.returning_precedes_values:
            text += " " + returning_clause

        if self.ctes and toplevel and not self.dialect.cte_follows_insert:
            text = self._render_cte_clause() + text

        self.stack.pop(-1)

        return text

    def update_limit_clause(self, update_stmt):
        """Provide a hook for MySQL to add LIMIT to the UPDATE"""
        return None

    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw):
        """Provide a hook to override the initial table clause
        in an UPDATE statement.

        MySQL overrides this.

        """
        kw["asfrom"] = True
        return from_table._compiler_dispatch(self, iscrud=True, **kw)

    def update_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        """Provide a hook to override the generation of an
        UPDATE..FROM clause.

        MySQL and MSSQL override this.

        """
        raise NotImplementedError(
            "This backend does not support multiple-table "
            "criteria within UPDATE"
        )

    def visit_update(self, update_stmt, **kw):
        toplevel = not self.stack

        extra_froms = update_stmt._extra_froms
        is_multitable = bool(extra_froms)

        if is_multitable:
            # main table might be a JOIN
            main_froms = set(selectable._from_objects(update_stmt.table))
            render_extra_froms = [
                f for f in extra_froms if f not in main_froms
            ]
            correlate_froms = main_froms.union(extra_froms)
        else:
            render_extra_froms = []
            correlate_froms = {update_stmt.table}

        self.stack.append(
            {
                "correlate_froms": correlate_froms,
                "asfrom_froms": correlate_froms,
                "selectable": update_stmt,
            }
        )

        text = "UPDATE "

        if update_stmt._prefixes:
            text += self._generate_prefixes(
                update_stmt, update_stmt._prefixes, **kw
            )

        table_text = self.update_tables_clause(
            update_stmt, update_stmt.table, render_extra_froms, **kw
        )
        crud_params = crud._setup_crud_params(
            self, update_stmt, crud.ISUPDATE, **kw
        )

        if update_stmt._hints:
            dialect_hints, table_text = self._setup_crud_hints(
                update_stmt, table_text
            )
        else:
            dialect_hints = None

        text += table_text

        text += " SET "
        include_table = (
            is_multitable and self.render_table_with_column_in_update_from
        )
        text += ", ".join(
            c[0]._compiler_dispatch(self, include_table=include_table)
            + "="
            + c[1]
            for c in crud_params
        )

        if self.returning or update_stmt._returning:
            if self.returning_precedes_values:
                text += " " + self.returning_clause(
                    update_stmt, self.returning or update_stmt._returning
                )

        if extra_froms:
            extra_from_text = self.update_from_clause(
                update_stmt,
                update_stmt.table,
                render_extra_froms,
                dialect_hints,
                **kw
            )
            if extra_from_text:
                text += " " + extra_from_text

        if update_stmt._whereclause is not None:
            t = self.process(update_stmt._whereclause, **kw)
            if t:
                text += " WHERE " + t

        limit_clause = self.update_limit_clause(update_stmt)
        if limit_clause:
            text += " " + limit_clause

        if (
            self.returning or update_stmt._returning
        ) and not self.returning_precedes_values:
            text += " " + self.returning_clause(
                update_stmt, self.returning or update_stmt._returning
            )

        if self.ctes and toplevel:
            text = self._render_cte_clause() + text

        self.stack.pop(-1)

        return text

    @util.memoized_property
    def _key_getters_for_crud_column(self):
        return crud._key_getters_for_crud_column(self, self.statement)

    def delete_extra_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        """Provide a hook to override the generation of an
        DELETE..FROM clause.

        This can be used to implement DELETE..USING for example.

        MySQL and MSSQL override this.

        """
        raise NotImplementedError(
            "This backend does not support multiple-table "
            "criteria within DELETE"
        )

    def delete_table_clause(self, delete_stmt, from_table, extra_froms):
        return from_table._compiler_dispatch(self, asfrom=True, iscrud=True)

    def visit_delete(self, delete_stmt, **kw):
        toplevel = not self.stack

        crud._setup_crud_params(self, delete_stmt, crud.ISDELETE, **kw)

        extra_froms = delete_stmt._extra_froms

        correlate_froms = {delete_stmt.table}.union(extra_froms)
        self.stack.append(
            {
                "correlate_froms": correlate_froms,
                "asfrom_froms": correlate_froms,
                "selectable": delete_stmt,
            }
        )

        text = "DELETE "

        if delete_stmt._prefixes:
            text += self._generate_prefixes(
                delete_stmt, delete_stmt._prefixes, **kw
            )

        text += "FROM "
        table_text = self.delete_table_clause(
            delete_stmt, delete_stmt.table, extra_froms
        )

        if delete_stmt._hints:
            dialect_hints, table_text = self._setup_crud_hints(
                delete_stmt, table_text
            )
        else:
            dialect_hints = None

        text += table_text

        if delete_stmt._returning:
            if self.returning_precedes_values:
                text += " " + self.returning_clause(
                    delete_stmt, delete_stmt._returning
                )

        if extra_froms:
            extra_from_text = self.delete_extra_from_clause(
                delete_stmt,
                delete_stmt.table,
                extra_froms,
                dialect_hints,
                **kw
            )
            if extra_from_text:
                text += " " + extra_from_text

        if delete_stmt._whereclause is not None:
            t = delete_stmt._whereclause._compiler_dispatch(self, **kw)
            if t:
                text += " WHERE " + t

        if delete_stmt._returning and not self.returning_precedes_values:
            text += " " + self.returning_clause(
                delete_stmt, delete_stmt._returning
            )

        if self.ctes and toplevel:
            text = self._render_cte_clause() + text

        self.stack.pop(-1)

        return text

    def visit_savepoint(self, savepoint_stmt):
        return "SAVEPOINT %s" % self.preparer.format_savepoint(savepoint_stmt)

    def visit_rollback_to_savepoint(self, savepoint_stmt):
        return "ROLLBACK TO SAVEPOINT %s" % self.preparer.format_savepoint(
            savepoint_stmt
        )

    def visit_release_savepoint(self, savepoint_stmt):
        return "RELEASE SAVEPOINT %s" % self.preparer.format_savepoint(
            savepoint_stmt
        )


class StrSQLCompiler(SQLCompiler):
    """A :class:`.SQLCompiler` subclass which allows a small selection
    of non-standard SQL features to render into a string value.

    The :class:`.StrSQLCompiler` is invoked whenever a Core expression
    element is directly stringified without calling upon the
    :meth:`.ClauseElement.compile` method.   It can render a limited set
    of non-standard SQL constructs to assist in basic stringification,
    however for more substantial custom or dialect-specific SQL constructs,
    it will be necessary to make use of :meth:`.ClauseElement.compile`
    directly.

    .. seealso::

        :ref:`faq_sql_expression_string`

    """

    def _fallback_column_name(self, column):
        return "<name unknown>"

    def visit_getitem_binary(self, binary, operator, **kw):
        return "%s[%s]" % (
            self.process(binary.left, **kw),
            self.process(binary.right, **kw),
        )

    def visit_json_getitem_op_binary(self, binary, operator, **kw):
        return self.visit_getitem_binary(binary, operator, **kw)

    def visit_json_path_getitem_op_binary(self, binary, operator, **kw):
        return self.visit_getitem_binary(binary, operator, **kw)

    def visit_sequence(self, seq, **kw):
        return "<next sequence value: %s>" % self.preparer.format_sequence(seq)

    def returning_clause(self, stmt, returning_cols):
        columns = [
            self._label_select_column(None, c, True, False, {})
            for c in elements._select_iterables(returning_cols)
        ]

        return "RETURNING " + ", ".join(columns)

    def update_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        return "FROM " + ", ".join(
            t._compiler_dispatch(self, asfrom=True, fromhints=from_hints, **kw)
            for t in extra_froms
        )

    def delete_extra_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        return ", " + ", ".join(
            t._compiler_dispatch(self, asfrom=True, fromhints=from_hints, **kw)
            for t in extra_froms
        )

    def visit_empty_set_expr(self, type_):
        return "SELECT 1 WHERE 1!=1"


class DDLCompiler(Compiled):
    @util.memoized_property
    def sql_compiler(self):
        return self.dialect.statement_compiler(self.dialect, None)

    @util.memoized_property
    def type_compiler(self):
        return self.dialect.type_compiler

    def construct_params(self, params=None):
        return None

    def visit_ddl(self, ddl, **kwargs):
        # table events can substitute table and schema name
        context = ddl.context
        if isinstance(ddl.target, schema.Table):
            context = context.copy()

            preparer = self.preparer
            path = preparer.format_table_seq(ddl.target)
            if len(path) == 1:
                table, sch = path[0], ""
            else:
                table, sch = path[-1], path[0]

            context.setdefault("table", table)
            context.setdefault("schema", sch)
            context.setdefault("fullname", preparer.format_table(ddl.target))

        return self.sql_compiler.post_process_text(ddl.statement % context)

    def visit_create_schema(self, create):
        schema = self.preparer.format_schema(create.element)
        return "CREATE SCHEMA " + schema

    def visit_drop_schema(self, drop):
        schema = self.preparer.format_schema(drop.element)
        text = "DROP SCHEMA " + schema
        if drop.cascade:
            text += " CASCADE"
        return text

    def visit_create_table(self, create):
        table = create.element
        preparer = self.preparer

        text = "\nCREATE "
        if table._prefixes:
            text += " ".join(table._prefixes) + " "
        text += "TABLE " + preparer.format_table(table) + " "

        create_table_suffix = self.create_table_suffix(table)
        if create_table_suffix:
            text += create_table_suffix + " "

        text += "("

        separator = "\n"

        # if only one primary key, specify it along with the column
        first_pk = False
        for create_column in create.columns:
            column = create_column.element
            try:
                processed = self.process(
                    create_column, first_pk=column.primary_key and not first_pk
                )
                if processed is not None:
                    text += separator
                    separator = ", \n"
                    text += "\t" + processed
                if column.primary_key:
                    first_pk = True
            except exc.CompileError as ce:
                util.raise_(
                    exc.CompileError(
                        util.u("(in table '%s', column '%s'): %s")
                        % (table.description, column.name, ce.args[0])
                    ),
                    from_=ce,
                )

        const = self.create_table_constraints(
            table,
            _include_foreign_key_constraints=create.include_foreign_key_constraints,  # noqa
        )
        if const:
            text += separator + "\t" + const

        text += "\n)%s\n\n" % self.post_create_table(table)
        return text

    def visit_create_column(self, create, first_pk=False):
        column = create.element

        if column.system:
            return None

        text = self.get_column_specification(column, first_pk=first_pk)
        const = " ".join(
            self.process(constraint) for constraint in column.constraints
        )
        if const:
            text += " " + const

        return text

    def create_table_constraints(
        self, table, _include_foreign_key_constraints=None
    ):

        # On some DB order is significant: visit PK first, then the
        # other constraints (engine.ReflectionTest.testbasic failed on FB2)
        constraints = []
        if table.primary_key:
            constraints.append(table.primary_key)

        all_fkcs = table.foreign_key_constraints
        if _include_foreign_key_constraints is not None:
            omit_fkcs = all_fkcs.difference(_include_foreign_key_constraints)
        else:
            omit_fkcs = set()

        constraints.extend(
            [
                c
                for c in table._sorted_constraints
                if c is not table.primary_key and c not in omit_fkcs
            ]
        )

        return ", \n\t".join(
            p
            for p in (
                self.process(constraint)
                for constraint in constraints
                if (
                    constraint._create_rule is None
                    or constraint._create_rule(self)
                )
                and (
                    not self.dialect.supports_alter
                    or not getattr(constraint, "use_alter", False)
                )
            )
            if p is not None
        )

    def visit_drop_table(self, drop):
        return "\nDROP TABLE " + self.preparer.format_table(drop.element)

    def visit_drop_view(self, drop):
        return "\nDROP VIEW " + self.preparer.format_table(drop.element)

    def _verify_index_table(self, index):
        if index.table is None:
            raise exc.CompileError(
                "Index '%s' is not associated " "with any table." % index.name
            )

    def visit_create_index(
        self, create, include_schema=False, include_table_schema=True
    ):
        index = create.element
        self._verify_index_table(index)
        preparer = self.preparer
        text = "CREATE "
        if index.unique:
            text += "UNIQUE "
        if index.name is None:
            raise exc.CompileError(
                "CREATE INDEX requires that the index have a name"
            )
        text += "INDEX %s ON %s (%s)" % (
            self._prepared_index_name(index, include_schema=include_schema),
            preparer.format_table(
                index.table, use_schema=include_table_schema
            ),
            ", ".join(
                self.sql_compiler.process(
                    expr, include_table=False, literal_binds=True
                )
                for expr in index.expressions
            ),
        )
        return text

    def visit_drop_index(self, drop):
        index = drop.element

        if index.name is None:
            raise exc.CompileError(
                "DROP INDEX requires that the index have a name"
            )
        return "\nDROP INDEX " + self._prepared_index_name(
            index, include_schema=True
        )

    def _prepared_index_name(self, index, include_schema=False):
        if index.table is not None:
            effective_schema = self.preparer.schema_for_object(index.table)
        else:
            effective_schema = None
        if include_schema and effective_schema:
            schema_name = self.preparer.quote_schema(effective_schema)
        else:
            schema_name = None

        index_name = self.preparer.format_index(index)

        if schema_name:
            index_name = schema_name + "." + index_name
        return index_name

    def visit_add_constraint(self, create):
        return "ALTER TABLE %s ADD %s" % (
            self.preparer.format_table(create.element.table),
            self.process(create.element),
        )

    def visit_set_table_comment(self, create):
        return "COMMENT ON TABLE %s IS %s" % (
            self.preparer.format_table(create.element),
            self.sql_compiler.render_literal_value(
                create.element.comment, sqltypes.String()
            ),
        )

    def visit_drop_table_comment(self, drop):
        return "COMMENT ON TABLE %s IS NULL" % self.preparer.format_table(
            drop.element
        )

    def visit_set_column_comment(self, create):
        return "COMMENT ON COLUMN %s IS %s" % (
            self.preparer.format_column(
                create.element, use_table=True, use_schema=True
            ),
            self.sql_compiler.render_literal_value(
                create.element.comment, sqltypes.String()
            ),
        )

    def visit_drop_column_comment(self, drop):
        return "COMMENT ON COLUMN %s IS NULL" % self.preparer.format_column(
            drop.element, use_table=True
        )

    def visit_create_sequence(self, create):
        text = "CREATE SEQUENCE %s" % self.preparer.format_sequence(
            create.element
        )
        if create.element.increment is not None:
            text += " INCREMENT BY %d" % create.element.increment
        if create.element.start is not None:
            text += " START WITH %d" % create.element.start
        if create.element.minvalue is not None:
            text += " MINVALUE %d" % create.element.minvalue
        if create.element.maxvalue is not None:
            text += " MAXVALUE %d" % create.element.maxvalue
        if create.element.nominvalue is not None:
            text += " NO MINVALUE"
        if create.element.nomaxvalue is not None:
            text += " NO MAXVALUE"
        if create.element.cache is not None:
            text += " CACHE %d" % create.element.cache
        if create.element.order is True:
            text += " ORDER"
        if create.element.cycle is not None:
            text += " CYCLE"
        return text

    def visit_drop_sequence(self, drop):
        return "DROP SEQUENCE %s" % self.preparer.format_sequence(drop.element)

    def visit_drop_constraint(self, drop):
        constraint = drop.element
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
        else:
            formatted_name = None

        if formatted_name is None:
            raise exc.CompileError(
                "Can't emit DROP CONSTRAINT for constraint %r; "
                "it has no name" % drop.element
            )
        return "ALTER TABLE %s DROP CONSTRAINT %s%s" % (
            self.preparer.format_table(drop.element.table),
            formatted_name,
            drop.cascade and " CASCADE" or "",
        )

    def get_column_specification(self, column, **kwargs):
        colspec = (
            self.preparer.format_column(column)
            + " "
            + self.dialect.type_compiler.process(
                column.type, type_expression=column
            )
        )
        default = self.get_column_default_string(column)
        if default is not None:
            colspec += " DEFAULT " + default

        if column.computed is not None:
            colspec += " " + self.process(column.computed)

        if not column.nullable:
            colspec += " NOT NULL"
        return colspec

    def create_table_suffix(self, table):
        return ""

    def post_create_table(self, table):
        return ""

    def get_column_default_string(self, column):
        if isinstance(column.server_default, schema.DefaultClause):
            if isinstance(column.server_default.arg, util.string_types):
                return self.sql_compiler.render_literal_value(
                    column.server_default.arg, sqltypes.STRINGTYPE
                )
            else:
                return self.sql_compiler.process(
                    column.server_default.arg, literal_binds=True
                )
        else:
            return None

    def visit_table_or_column_check_constraint(self, constraint, **kw):
        if constraint.is_column_level:
            return self.visit_column_check_constraint(constraint)
        else:
            return self.visit_check_constraint(constraint)

    def visit_check_constraint(self, constraint):
        text = ""
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
            if formatted_name is not None:
                text += "CONSTRAINT %s " % formatted_name
        text += "CHECK (%s)" % self.sql_compiler.process(
            constraint.sqltext, include_table=False, literal_binds=True
        )
        text += self.define_constraint_deferrability(constraint)
        return text

    def visit_column_check_constraint(self, constraint):
        text = ""
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
            if formatted_name is not None:
                text += "CONSTRAINT %s " % formatted_name
        text += "CHECK (%s)" % self.sql_compiler.process(
            constraint.sqltext, include_table=False, literal_binds=True
        )
        text += self.define_constraint_deferrability(constraint)
        return text

    def visit_primary_key_constraint(self, constraint):
        if len(constraint) == 0:
            return ""
        text = ""
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
            if formatted_name is not None:
                text += "CONSTRAINT %s " % formatted_name
        text += "PRIMARY KEY "
        text += "(%s)" % ", ".join(
            self.preparer.quote(c.name)
            for c in (
                constraint.columns_autoinc_first
                if constraint._implicit_generated
                else constraint.columns
            )
        )
        text += self.define_constraint_deferrability(constraint)
        return text

    def visit_foreign_key_constraint(self, constraint):
        preparer = self.preparer
        text = ""
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
            if formatted_name is not None:
                text += "CONSTRAINT %s " % formatted_name
        remote_table = list(constraint.elements)[0].column.table
        text += "FOREIGN KEY(%s) REFERENCES %s (%s)" % (
            ", ".join(
                preparer.quote(f.parent.name) for f in constraint.elements
            ),
            self.define_constraint_remote_table(
                constraint, remote_table, preparer
            ),
            ", ".join(
                preparer.quote(f.column.name) for f in constraint.elements
            ),
        )
        text += self.define_constraint_match(constraint)
        text += self.define_constraint_cascades(constraint)
        text += self.define_constraint_deferrability(constraint)
        return text

    def define_constraint_remote_table(self, constraint, table, preparer):
        """Format the remote table clause of a CREATE CONSTRAINT clause."""

        return preparer.format_table(table)

    def visit_unique_constraint(self, constraint):
        if len(constraint) == 0:
            return ""
        text = ""
        if constraint.name is not None:
            formatted_name = self.preparer.format_constraint(constraint)
            if formatted_name is not None:
                text += "CONSTRAINT %s " % formatted_name
        text += "UNIQUE (%s)" % (
            ", ".join(self.preparer.quote(c.name) for c in constraint)
        )
        text += self.define_constraint_deferrability(constraint)
        return text

    def define_constraint_cascades(self, constraint):
        text = ""
        if constraint.ondelete is not None:
            text += " ON DELETE %s" % self.preparer.validate_sql_phrase(
                constraint.ondelete, FK_ON_DELETE
            )
        if constraint.onupdate is not None:
            text += " ON UPDATE %s" % self.preparer.validate_sql_phrase(
                constraint.onupdate, FK_ON_UPDATE
            )
        return text

    def define_constraint_deferrability(self, constraint):
        text = ""
        if constraint.deferrable is not None:
            if constraint.deferrable:
                text += " DEFERRABLE"
            else:
                text += " NOT DEFERRABLE"
        if constraint.initially is not None:
            text += " INITIALLY %s" % self.preparer.validate_sql_phrase(
                constraint.initially, FK_INITIALLY
            )
        return text

    def define_constraint_match(self, constraint):
        text = ""
        if constraint.match is not None:
            text += " MATCH %s" % constraint.match
        return text

    def visit_computed_column(self, generated):
        text = "GENERATED ALWAYS AS (%s)" % self.sql_compiler.process(
            generated.sqltext, include_table=False, literal_binds=True
        )
        if generated.persisted is True:
            text += " STORED"
        elif generated.persisted is False:
            text += " VIRTUAL"
        return text


class GenericTypeCompiler(TypeCompiler):
    def visit_FLOAT(self, type_, **kw):
        return "FLOAT"

    def visit_REAL(self, type_, **kw):
        return "REAL"

    def visit_NUMERIC(self, type_, **kw):
        if type_.precision is None:
            return "NUMERIC"
        elif type_.scale is None:
            return "NUMERIC(%(precision)s)" % {"precision": type_.precision}
        else:
            return "NUMERIC(%(precision)s, %(scale)s)" % {
                "precision": type_.precision,
                "scale": type_.scale,
            }

    def visit_DECIMAL(self, type_, **kw):
        if type_.precision is None:
            return "DECIMAL"
        elif type_.scale is None:
            return "DECIMAL(%(precision)s)" % {"precision": type_.precision}
        else:
            return "DECIMAL(%(precision)s, %(scale)s)" % {
                "precision": type_.precision,
                "scale": type_.scale,
            }

    def visit_INTEGER(self, type_, **kw):
        return "INTEGER"

    def visit_SMALLINT(self, type_, **kw):
        return "SMALLINT"

    def visit_BIGINT(self, type_, **kw):
        return "BIGINT"

    def visit_TIMESTAMP(self, type_, **kw):
        return "TIMESTAMP"

    def visit_DATETIME(self, type_, **kw):
        return "DATETIME"

    def visit_DATE(self, type_, **kw):
        return "DATE"

    def visit_TIME(self, type_, **kw):
        return "TIME"

    def visit_CLOB(self, type_, **kw):
        return "CLOB"

    def visit_NCLOB(self, type_, **kw):
        return "NCLOB"

    def _render_string_type(self, type_, name):

        text = name
        if type_.length:
            text += "(%d)" % type_.length
        if type_.collation:
            text += ' COLLATE "%s"' % type_.collation
        return text

    def visit_CHAR(self, type_, **kw):
        return self._render_string_type(type_, "CHAR")

    def visit_NCHAR(self, type_, **kw):
        return self._render_string_type(type_, "NCHAR")

    def visit_VARCHAR(self, type_, **kw):
        return self._render_string_type(type_, "VARCHAR")

    def visit_NVARCHAR(self, type_, **kw):
        return self._render_string_type(type_, "NVARCHAR")

    def visit_TEXT(self, type_, **kw):
        return self._render_string_type(type_, "TEXT")

    def visit_BLOB(self, type_, **kw):
        return "BLOB"

    def visit_BINARY(self, type_, **kw):
        return "BINARY" + (type_.length and "(%d)" % type_.length or "")

    def visit_VARBINARY(self, type_, **kw):
        return "VARBINARY" + (type_.length and "(%d)" % type_.length or "")

    def visit_BOOLEAN(self, type_, **kw):
        return "BOOLEAN"

    def visit_large_binary(self, type_, **kw):
        return self.visit_BLOB(type_, **kw)

    def visit_boolean(self, type_, **kw):
        return self.visit_BOOLEAN(type_, **kw)

    def visit_time(self, type_, **kw):
        return self.visit_TIME(type_, **kw)

    def visit_datetime(self, type_, **kw):
        return self.visit_DATETIME(type_, **kw)

    def visit_date(self, type_, **kw):
        return self.visit_DATE(type_, **kw)

    def visit_big_integer(self, type_, **kw):
        return self.visit_BIGINT(type_, **kw)

    def visit_small_integer(self, type_, **kw):
        return self.visit_SMALLINT(type_, **kw)

    def visit_integer(self, type_, **kw):
        return self.visit_INTEGER(type_, **kw)

    def visit_real(self, type_, **kw):
        return self.visit_REAL(type_, **kw)

    def visit_float(self, type_, **kw):
        return self.visit_FLOAT(type_, **kw)

    def visit_numeric(self, type_, **kw):
        return self.visit_NUMERIC(type_, **kw)

    def visit_string(self, type_, **kw):
        return self.visit_VARCHAR(type_, **kw)

    def visit_unicode(self, type_, **kw):
        return self.visit_VARCHAR(type_, **kw)

    def visit_text(self, type_, **kw):
        return self.visit_TEXT(type_, **kw)

    def visit_unicode_text(self, type_, **kw):
        return self.visit_TEXT(type_, **kw)

    def visit_enum(self, type_, **kw):
        return self.visit_VARCHAR(type_, **kw)

    def visit_null(self, type_, **kw):
        raise exc.CompileError(
            "Can't generate DDL for %r; "
            "did you forget to specify a "
            "type on this Column?" % type_
        )

    def visit_type_decorator(self, type_, **kw):
        return self.process(type_.type_engine(self.dialect), **kw)

    def visit_user_defined(self, type_, **kw):
        return type_.get_col_spec(**kw)


class StrSQLTypeCompiler(GenericTypeCompiler):
    def __getattr__(self, key):
        if key.startswith("visit_"):
            return self._visit_unknown
        else:
            raise AttributeError(key)

    def _visit_unknown(self, type_, **kw):
        return "%s" % type_.__class__.__name__


class IdentifierPreparer(object):

    """Handle quoting and case-folding of identifiers based on options."""

    reserved_words = RESERVED_WORDS

    legal_characters = LEGAL_CHARACTERS

    illegal_initial_characters = ILLEGAL_INITIAL_CHARACTERS

    schema_for_object = schema._schema_getter(None)

    def __init__(
        self,
        dialect,
        initial_quote='"',
        final_quote=None,
        escape_quote='"',
        quote_case_sensitive_collations=True,
        omit_schema=False,
    ):
        """Construct a new ``IdentifierPreparer`` object.

        initial_quote
          Character that begins a delimited identifier.

        final_quote
          Character that ends a delimited identifier. Defaults to
          `initial_quote`.

        omit_schema
          Prevent prepending schema name. Useful for databases that do
          not support schemae.
        """

        self.dialect = dialect
        self.initial_quote = initial_quote
        self.final_quote = final_quote or self.initial_quote
        self.escape_quote = escape_quote
        self.escape_to_quote = self.escape_quote * 2
        self.omit_schema = omit_schema
        self.quote_case_sensitive_collations = quote_case_sensitive_collations
        self._strings = {}
        self._double_percents = self.dialect.paramstyle in (
            "format",
            "pyformat",
        )

    def _with_schema_translate(self, schema_translate_map):
        prep = self.__class__.__new__(self.__class__)
        prep.__dict__.update(self.__dict__)
        prep.schema_for_object = schema._schema_getter(schema_translate_map)
        return prep

    def _escape_identifier(self, value):
        """Escape an identifier.

        Subclasses should override this to provide database-dependent
        escaping behavior.
        """

        value = value.replace(self.escape_quote, self.escape_to_quote)
        if self._double_percents:
            value = value.replace("%", "%%")
        return value

    def _unescape_identifier(self, value):
        """Canonicalize an escaped identifier.

        Subclasses should override this to provide database-dependent
        unescaping behavior that reverses _escape_identifier.
        """

        return value.replace(self.escape_to_quote, self.escape_quote)

    def validate_sql_phrase(self, element, reg):
        """keyword sequence filter.

        a filter for elements that are intended to represent keyword sequences,
        such as "INITIALLY", "INITIALLY DEFERRED", etc.   no special characters
        should be present.

        .. versionadded:: 1.3

        """

        if element is not None and not reg.match(element):
            raise exc.CompileError(
                "Unexpected SQL phrase: %r (matching against %r)"
                % (element, reg.pattern)
            )
        return element

    def quote_identifier(self, value):
        """Quote an identifier.

        Subclasses should override this to provide database-dependent
        quoting behavior.
        """

        return (
            self.initial_quote
            + self._escape_identifier(value)
            + self.final_quote
        )

    def _requires_quotes(self, value):
        """Return True if the given identifier requires quoting."""
        lc_value = value.lower()
        return (
            lc_value in self.reserved_words
            or value[0] in self.illegal_initial_characters
            or not self.legal_characters.match(util.text_type(value))
            or (lc_value != value)
        )

    def _requires_quotes_illegal_chars(self, value):
        """Return True if the given identifier requires quoting, but
        not taking case convention into account."""
        return not self.legal_characters.match(util.text_type(value))

    def quote_schema(self, schema, force=None):
        """Conditionally quote a schema name.


        The name is quoted if it is a reserved word, contains quote-necessary
        characters, or is an instance of :class:`.quoted_name` which includes
        ``quote`` set to ``True``.

        Subclasses can override this to provide database-dependent
        quoting behavior for schema names.

        :param schema: string schema name
        :param force: unused

            .. deprecated:: 0.9

                The :paramref:`.IdentifierPreparer.quote_schema.force`
                parameter is deprecated and will be removed in a future
                release.  This flag has no effect on the behavior of the
                :meth:`.IdentifierPreparer.quote` method; please refer to
                :class:`.quoted_name`.

        """
        if force is not None:
            # not using the util.deprecated_params() decorator in this
            # case because of the additional function call overhead on this
            # very performance-critical spot.
            util.warn_deprecated(
                "The IdentifierPreparer.quote_schema.force parameter is "
                "deprecated and will be removed in a future release.  This "
                "flag has no effect on the behavior of the "
                "IdentifierPreparer.quote method; please refer to "
                "quoted_name()."
            )

        return self.quote(schema)

    def quote(self, ident, force=None):
        """Conditionally quote an identfier.

        The identifier is quoted if it is a reserved word, contains
        quote-necessary characters, or is an instance of
        :class:`.quoted_name` which includes ``quote`` set to ``True``.

        Subclasses can override this to provide database-dependent
        quoting behavior for identifier names.

        :param ident: string identifier
        :param force: unused

            .. deprecated:: 0.9

                The :paramref:`.IdentifierPreparer.quote.force`
                parameter is deprecated and will be removed in a future
                release.  This flag has no effect on the behavior of the
                :meth:`.IdentifierPreparer.quote` method; please refer to
                :class:`.quoted_name`.

        """
        if force is not None:
            # not using the util.deprecated_params() decorator in this
            # case because of the additional function call overhead on this
            # very performance-critical spot.
            util.warn_deprecated(
                "The IdentifierPreparer.quote.force parameter is "
                "deprecated and will be removed in a future release.  This "
                "flag has no effect on the behavior of the "
                "IdentifierPreparer.quote method; please refer to "
                "quoted_name()."
            )

        force = getattr(ident, "quote", None)

        if force is None:
            if ident in self._strings:
                return self._strings[ident]
            else:
                if self._requires_quotes(ident):
                    self._strings[ident] = self.quote_identifier(ident)
                else:
                    self._strings[ident] = ident
                return self._strings[ident]
        elif force:
            return self.quote_identifier(ident)
        else:
            return ident

    def format_collation(self, collation_name):
        if self.quote_case_sensitive_collations:
            return self.quote(collation_name)
        else:
            return collation_name

    def format_sequence(self, sequence, use_schema=True):
        name = self.quote(sequence.name)

        effective_schema = self.schema_for_object(sequence)

        if (
            not self.omit_schema
            and use_schema
            and effective_schema is not None
        ):
            name = self.quote_schema(effective_schema) + "." + name
        return name

    def format_label(self, label, name=None):
        return self.quote(name or label.name)

    def format_alias(self, alias, name=None):
        return self.quote(name or alias.name)

    def format_savepoint(self, savepoint, name=None):
        # Running the savepoint name through quoting is unnecessary
        # for all known dialects.  This is here to support potential
        # third party use cases
        ident = name or savepoint.ident
        if self._requires_quotes(ident):
            ident = self.quote_identifier(ident)
        return ident

    @util.dependencies("sqlalchemy.sql.naming")
    def format_constraint(self, naming, constraint, _alembic_quote=True):
        if isinstance(constraint.name, elements._defer_name):
            name = naming._constraint_name_for_table(
                constraint, constraint.table
            )

            if name is None:
                if isinstance(constraint.name, elements._defer_none_name):
                    return None
                else:
                    name = constraint.name
        else:
            name = constraint.name

        if isinstance(name, elements._truncated_label):
            if constraint.__visit_name__ == "index":
                max_ = (
                    self.dialect.max_index_name_length
                    or self.dialect.max_identifier_length
                )
            else:
                max_ = self.dialect.max_identifier_length
            if len(name) > max_:
                name = name[0 : max_ - 8] + "_" + util.md5_hex(name)[-4:]
        else:
            self.dialect.validate_identifier(name)

        if not _alembic_quote:
            return name
        else:
            return self.quote(name)

    def format_index(self, index):
        return self.format_constraint(index)

    def format_table(self, table, use_schema=True, name=None):
        """Prepare a quoted table and schema name."""

        if name is None:
            name = table.name
        result = self.quote(name)

        effective_schema = self.schema_for_object(table)

        if not self.omit_schema and use_schema and effective_schema:
            result = self.quote_schema(effective_schema) + "." + result
        return result

    def format_schema(self, name):
        """Prepare a quoted schema name."""

        return self.quote(name)

    def format_column(
        self,
        column,
        use_table=False,
        name=None,
        table_name=None,
        use_schema=False,
    ):
        """Prepare a quoted column name."""

        if name is None:
            name = column.name
        if not getattr(column, "is_literal", False):
            if use_table:
                return (
                    self.format_table(
                        column.table, use_schema=use_schema, name=table_name
                    )
                    + "."
                    + self.quote(name)
                )
            else:
                return self.quote(name)
        else:
            # literal textual elements get stuck into ColumnClause a lot,
            # which shouldn't get quoted

            if use_table:
                return (
                    self.format_table(
                        column.table, use_schema=use_schema, name=table_name
                    )
                    + "."
                    + name
                )
            else:
                return name

    def format_table_seq(self, table, use_schema=True):
        """Format table name and schema as a tuple."""

        # Dialects with more levels in their fully qualified references
        # ('database', 'owner', etc.) could override this and return
        # a longer sequence.

        effective_schema = self.schema_for_object(table)

        if not self.omit_schema and use_schema and effective_schema:
            return (
                self.quote_schema(effective_schema),
                self.format_table(table, use_schema=False),
            )
        else:
            return (self.format_table(table, use_schema=False),)

    @util.memoized_property
    def _r_identifiers(self):
        initial, final, escaped_final = [
            re.escape(s)
            for s in (
                self.initial_quote,
                self.final_quote,
                self._escape_identifier(self.final_quote),
            )
        ]
        r = re.compile(
            r"(?:"
            r"(?:%(initial)s((?:%(escaped)s|[^%(final)s])+)%(final)s"
            r"|([^\.]+))(?=\.|$))+"
            % {"initial": initial, "final": final, "escaped": escaped_final}
        )
        return r

    def unformat_identifiers(self, identifiers):
        """Unpack 'schema.table.column'-like strings into components."""

        r = self._r_identifiers
        return [
            self._unescape_identifier(i)
            for i in [a or b for a, b in r.findall(identifiers)]
        ]
