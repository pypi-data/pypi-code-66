import os
from unittest.mock import patch

import pytest

from query_factory import SQLQueryFactory
from query_factory import exceptions


@pytest.fixture()
def template_path():
    return os.path.join(os.path.dirname(__file__), "data", "sql_template_with_defaults.yaml")


def test_init(template_path):
    _ = SQLQueryFactory(template_path)


@patch("jinjasql.JinjaSql.prepare_query", return_value=("%s, %s", [1, 2]))
def test_get_query_with(prepare_query_mock, template_path):
    factory = SQLQueryFactory(template_path)
    factory.get_query_with(start_date="1", end_date="2", category_id="cat", market="pro")
    factory._jinjasql.prepare_query.assert_called_once_with(
        factory._query, data={
            "start_date": "1",
            "end_date": "2",
            "category_id": "cat",
            "market": "pro"
        }
    )


@patch("jinjasql.JinjaSql.prepare_query", return_value=("%s, %s", [1, 2]))
def test_get_query_with_defaults(prepare_query_mock, template_path):
    factory = SQLQueryFactory(template_path)
    factory.get_query_with(start_date="1", end_date="2")
    factory._jinjasql.prepare_query.assert_called_once_with(
        factory._query, data={
            "start_date": "1",
            "end_date": "2",
            "category_id": None,
            "market": "part"
        }
    )


def test_get_query_with_raises_extra(template_path):
    factory = SQLQueryFactory(template_path)
    with pytest.raises(exceptions.MissingOrExtraVariableException):
        factory.get_query_with(wrong_arg="1")


def test_get_query_with_raises_missing(template_path):
    factory = SQLQueryFactory(template_path)
    with pytest.raises(exceptions.MissingOrExtraVariableException):
        factory.get_query_with()


@patch("yaml.load", return_value={"wrong_key": "value"})
def test_malformed_raise(load_mock, template_path):
    with pytest.raises(exceptions.MalformedTemplate):
        _ = SQLQueryFactory(template_path)


@patch("yaml.load", return_value={"query_template": "", "variables": {}})
def test_raise_on_empty_query(load_mock, template_path):
    with pytest.raises(exceptions.NoOrEmptyQueryException):
        _ = SQLQueryFactory(template_path)


def test_factory_describe(template_path):
    factory = SQLQueryFactory(template_path)
    description = factory.describe("start_date")
    assert description == "UTC datetime string to gather data from (inclusive)"
