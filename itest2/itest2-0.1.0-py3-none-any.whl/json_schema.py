# -*- coding: utf-8 -*-

import json
from os import path
import jsonschema
from genson import SchemaBuilder


def generate_to_file(json_obj, schema_file_path: str):
    """
    generate json schema from json obj and write to file

    :param json_obj: json obj
    :param schema_file_path: the file to record json schema
    """

    with open(schema_file_path, 'w+') as f:
        json.dump(generate(json_obj), f, indent=4, ensure_ascii=False)


def generate(json_obj) -> dict:
    """
    generate json schema from json obj

    :param json_obj: json obj
    """
    builder = SchemaBuilder(schema_uri='http://json-schema.org/draft-07/schema#')
    builder.add_object(json_obj)
    return builder.to_schema()


def validate(instance, schema):
    """
    validate json string with json schema

    :param json: json
    :param schema: json schema string
    :raises jsonschema.ValidationError: if json string does not match json schema
    """

    jsonschema.validate(instance, schema)


def validate_from_file(instance , schema_file_path: str):
    """
    validate json string with getting json schema from file

    :param json: json
    :param schema_file_path: json schema file path
    """

    validate(instance, _get_schema_from_file(schema_file_path))


def _get_schema_from_file(schema_file_path: str):
    """
    get json schema from file

    :param schema_file_path: json schema file path
    :raises FileNotFoundError: if file not found
    :return: json schema
    :rtype: str
    """

    if not path.exists(schema_file_path):
        raise FileNotFoundError(f'{schema_file_path} not found')
    with open(schema_file_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    try:
        return json.loads(schema)
    except TypeError:
        return schema