import os
import typing

import pytest

from horkos import errors
from horkos import schemaomatic

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCE_PATH = os.path.join(DIR_PATH, 'resources')


def test_schema_from_yaml():
    """Should be able to create a schema from a yaml file without error."""
    yaml_path = os.path.join(RESOURCE_PATH, 'sample.yaml')

    schemaomatic.schema_from_yaml(yaml_path)


def test_schema_process():
    """Should be able to process a record with the schema."""
    raw_schema = {
        'name': 'foobar',
        'description': 'The details',
        'fields': {
            'first_field': {
                'type': 'string',
                'description': 'This is a description',
                'checks': [
                    {'name': 'regex', 'args': {'regex': r'\d+'}}
                ]
            },
            'second_field': {
                'type': 'string',
                'description': 'Some description',
                'required': False,
                'nullable': True,
                'checks': [
                    'json'
                ]
            }
        }
    }
    schema = schemaomatic.schema_from_dict(raw_schema)

    result = schema.process({'first_field': 123456})

    assert result['first_field'] == '123456'
    assert result['second_field'] == None


def test_schema_process_with_errors():
    """Should get all check errors at once."""
    raw_schema = {
        'name': 'foobar',
        'description': 'The details',
        'fields': {
            'first_field': {
                'type': 'string',
                'description': 'This is a description',
                'checks': [
                    {'name': 'regex', 'args': {'regex': r'\d+'}}
                ]
            },
            'second_field': {
                'type': 'string',
                'description': 'Some description',
                'nullable': True,
                'checks': [
                    'json'
                ]
            }
        }
    }
    schema = schemaomatic.schema_from_dict(raw_schema)

    with pytest.raises(ValueError) as err:
        schema.process({'first_field': 'foobar', 'second_field': 'fizz'})

    err_msg = 'value of "foobar" in first_field did not pass regex check'
    assert err_msg in str(err.value)
    err_msg = 'value of "fizz" in second_field did not pass json check'
    assert err_msg in str(err.value)


SCENARIOS = [
    ({}, '"prefix.name" is required'),
    ({'name': []}, '"prefix.name" must be a string'),
    ({'name': 'something', 'args': []}, '"prefix.args" must be a dictionary'),
    ([], '"prefix" must be a string or dictionary'),
]


@pytest.mark.parametrize('check, msg', SCENARIOS)
def test_standardize_check_errors(check: typing.Any, msg: str):
    """If given a bad check an error should be raised."""
    with pytest.raises(errors.SchemaValidationError) as err:
        schemaomatic._standardize_check(check, 'prefix')

    assert msg in str(err.value)


SCENARIOS = [
    ({'type': 'string'}, '"fields.field_id.description" is required'),
    (
        {'type': 'bool', 'description': 'foo', 'labels': []},
        '"fields.field_id.labels" must be of type dict'
    ),
]


@pytest.mark.parametrize('field, msg', SCENARIOS)
def test_standardize_field_errors(field: typing.Any, msg: str):
    """If given a bad field an error should be raised."""
    with pytest.raises(errors.SchemaValidationError) as err:
        schemaomatic._standardize_field(field, 'field_id')

    assert msg in str(err.value)


SCENARIOS = [
    ({}, '"name" is required'),
    ({'name': {}}, '"name" must be of type str'),
]


@pytest.mark.parametrize('schema, msg', SCENARIOS)
def test_standardize_schema_errors(schema: typing.Any, msg: str):
    """If given a bad schema an error should be raised."""
    with pytest.raises(errors.SchemaValidationError) as err:
        schemaomatic._standardize_schema(schema)

    assert msg in str(err.value)
