import pytest
from typing import List
from hypothesis import given, strategies as st
from pampy import match, _

from fslash.core import Result, Ok, Error, Result_
from fslash.builders import result
from .utils import CustomException, throw


def test_result_ok():
    xs = Ok(42)

    assert isinstance(xs, Result_)
    assert xs.is_ok()
    assert not xs.is_error(

    )
    res = match(xs,
                Ok, lambda ok: ok.value,
                Error, lambda error: throw(error.error))
    assert res == 42


def test_result_ok_iterate():
    for x in Ok(42):
        assert x == 42


def test_result_error():
    xs = Error(CustomException("d'oh!"))

    assert isinstance(xs, Result_)
    assert not xs.is_ok()
    assert xs.is_error()

    with pytest.raises(CustomException):
        match(xs,
              Ok, lambda ok: ok.value,
              Error, lambda error: throw(error.error))


def test_result_error_iterate():
    with pytest.raises(Error) as excinfo:
        for x in Error("err"):
            assert x == 42

    assert excinfo.value.error == "err"


@given(st.integers(), st.integers())
def test_result_map_piped(x, y):
    xs = Ok(x)
    mapper = lambda x: x + y

    ys = xs.pipe(Result.map(mapper))
    res = match(ys,
                Ok, lambda ok: ok.value,
                Error, lambda error: throw(error.error))
    assert res == mapper(x)


@given(st.integers(), st.integers())
def test_result_map_ok_fluent(x, y):
    xs = Ok(x)
    mapper = lambda x: x + y

    ys = xs.map(mapper)
    res = match(ys,
                Ok, lambda ok: ok.value,
                Error, lambda error: throw(error.error))
    assert res == mapper(x)


@given(st.integers(), st.integers())
def test_result_ok_chained_map(x, y):
    xs = Ok(x)
    mapper1 = lambda x: x + y
    mapper2 = lambda x: x * 10

    ys = xs.map(mapper1).map(mapper2)
    res = match(ys,
                Ok, lambda ok: ok.value,
                Error, lambda error: throw(error.error))
    assert res == mapper2(mapper1(x))


@given(st.text(), st.integers())
def test_result_map_error_piped(msg, y):
    xs = Error(msg)
    mapper = lambda x: x + y

    ys = xs.pipe(Result.map(mapper))

    with pytest.raises(CustomException) as ex:
        match(ys,
              Ok, lambda ok: ok.value,
              Error, lambda error: throw(CustomException(error.error)))
    assert ex.value.message == msg


@given(st.text(), st.integers())
def test_result_map_error_fluent(msg, y):
    xs = Error(msg)
    mapper = lambda x: x + y

    ys = xs.map(mapper)
    with pytest.raises(CustomException) as ex:
        match(ys,
              Ok, lambda ok: ok.value,
              Error, lambda error: throw(CustomException(error.error)))
    assert ex.value.message == msg


@given(st.text(), st.integers())
def test_result_error_chained_map(msg, y):
    xs = Error(msg)
    mapper1 = lambda x: x + y
    mapper2 = lambda x: x * 10

    ys = xs.map(mapper1).map(mapper2)
    with pytest.raises(CustomException) as ex:
        ys.match(
            Ok, lambda ok: ok.value,
            Error, lambda error: throw(CustomException(error.error))
        )
    assert ex.value.message == msg


@given(st.integers(), st.integers())
def test_result_bind_piped(x, y):
    xs = Ok(x)
    mapper = lambda x: Ok(x + y)

    ys = xs.pipe(Result.bind(mapper))
    res = ys.match(
        Ok, lambda ok: ok.value,
        Error, lambda error: throw(error.error)
    )
    assert Ok(res) == mapper(x)


@given(st.lists(st.integers()))
def test_result_traverse_ok(xs):
    ys: List[Result_[int, str]] = [Ok(x) for x in xs]
    zs = Result.sequence(ys)
    res = zs.match(
        Ok, lambda ok: sum(ok.value),
        Error, lambda error: throw(error.error)
    )

    assert res == sum(xs)


@given(st.lists(st.integers(), min_size=5))
def test_result_traverse_error(xs):
    error = "Do'h"
    ys: List[Result_[int, str]] = [Ok(x) if i == 3 else Error(error) for x, i in enumerate(xs)]

    zs = Result.sequence(ys)
    res = zs.match(
        Ok, lambda ok: "",
        Error, lambda error: error.error
    )

    assert res == error


def test_result_builder_zero():
    @result
    def fn():
        yield

    with pytest.raises(NotImplementedError):
        fn()


def test_result_builder_yield_ok():
    @result
    def fn():
        yield 42

    xs = fn()
    assert 42 == xs.match(
        Ok, lambda ok: ok.value,
        _, None
    )


def test_result_builder_return_ok():
    @result
    def fn():
        x = yield 42
        return x

    xs = fn()
    assert 42 == xs.match(
        Ok, lambda ok: ok.value,
        _, None
    )


def test_result_builder_yield_from_ok():
    @result
    def fn():
        x = yield from Ok(42)
        return x + 1

    xs = fn()
    assert 43 == xs.match(
        Ok, lambda some: some.value,
        _, None
    )


def test_result_builder_yield_from_error():
    error = "Do'h"

    @result
    def fn():
        x = yield from Error(error)
        return x

    xs = fn()
    assert xs.match(
        Ok, lambda some: some.value,
        Error, lambda error: error.error
    ) == error


def test_result_builder_multiple_ok():
    @result
    def fn():
        x = yield 42
        y = yield from Ok(43)

        return x + y

    xs = fn()
    assert 85 == xs.match(
        Ok, lambda ok: ok.value,
        _, None
    )
