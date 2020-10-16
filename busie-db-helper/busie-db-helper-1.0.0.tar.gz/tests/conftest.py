import pytest
from os.path import join, dirname, abspath

@pytest.fixture
def root_dir():
    return join(dirname(abspath(__file__)), '../')

@pytest.fixture
def async_mock(mocker):
    return lambda mod: lambda loc, **kwargs: mocker.patch(f"{loc}.{mod}", **kwargs)

@pytest.fixture
def mock_sql_alchemy(async_mock):
    return async_mock('SQLAlchemy')

@pytest.fixture
def mock_flask(async_mock):
    return async_mock('Flask')
