import pytest


def test_construction():
    with pytest.raises(Exception):
        therm = Thermostat(host="notahost")
