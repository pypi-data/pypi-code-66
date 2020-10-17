import typing

from horkos import definitions


def _int(value: typing.Any) -> int:
    """Convert the given value into an integer."""
    if isinstance(value, float) and (int(value) - value) != 0:
        raise ValueError('Cannot losslessly convert to an integer')
    return int(value)


def _bool(value: typing.Any) -> bool:
    """Convert the given value to a boolean"""
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() == 'true':
        return True
    if isinstance(value, str) and value.lower() == 'false':
        return False
    if isinstance(value, int) and value == 0:
        return False
    if isinstance(value, int) and value == 1:
        return True
    raise ValueError(f'Cannot convert {value} to a boolean')


def cast(record: dict, field_map: typing.Dict[str, definitions.Field]) -> dict:
    """
    Cast the fields on the given record to the expected types.

    :param record:
        The record on which to check for incorrect types. It is expected to be
        a dictionary mapping field names to values.
    :param field_map:
        A dictionary mapping field names to their field objects.
    :return:
        A dictionary representing the record with each value converted to
        the expected type.
    """
    cast_map = {
        'boolean': _bool,
        'float': float,
        'integer': _int,
        'string': str,
    }

    errors = []
    result = {}
    for field_name, field in field_map.items():
        if field_name not in record and field.required:
            errors.append(f'{field_name} is required')
            continue
        value = record.get(field_name)
        if value is None and not field.nullable:
            errors.append(f'{field_name} cannot be null')
            continue
        if value is None:
            result[field_name] = value
            continue
        try:
            result[field_name] = cast_map[field.type_](value)
        except (TypeError, ValueError):
            errors.append(
                f'value of "{value}" for {field_name} '
                f'could not be cast to {field.type_}'
            )
    if errors:
        raise ValueError(f'Casting errors - {", ".join(errors)}')
    return result
