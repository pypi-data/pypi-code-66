import json

from pathlib import Path
from jsonschema import validate, ValidationError

def assert_schema(json_dict: dict, schema_name: str, path='json-schema') -> None:
    """
    Assert that a dictionnary respect a specific json-schema.

    See more about json schema syntax at: https://json-schema.org/

    :param dict json_dict: dictionnary to assert against schema
    :param str schema_name: schema name in path
    :param str path: path where schema_name will be searched

    :raise ValidationError: if the schema is not respected
    """
    path = Path(path)
    schema_path = path.joinpath(schema_name)

    try:
        schema = open(schema_path)
        schema_loaded = json.load(schema)
        convert_relative_ref_to_absolute(schema_loaded, schema_path)
        # Validate json
        validate(instance=json_dict, schema=schema_loaded)
    except FileNotFoundError as error:
        raise Exception(f"Couldn't load json-schema at: {schema_path}") from error
    finally:
        schema.close()

def __convert_to_absolute(relative_path_uri, relative_root, uri_scheme):
    if not relative_path_uri[:len(uri_scheme)] == uri_scheme:
        return relative_path_uri

    # Clean path
    path = relative_path_uri.replace(uri_scheme, '')
    if path[0] == ':':
        path = path[1::]

    # Extract JPointer (things that is after #)
    exploded = path.split('#')
    # This should (if this uri is valid) be 1 or 2
    jpointer = f"#{exploded[1]}" if len(exploded) == 2 else ''

    # Ensure they are Path instance
    path = Path(path)
    relative_root = Path(relative_root).parent

    full_path = relative_root.joinpath(path).absolute()

    # Reconstruct uri
    uri = f"file:{full_path}{jpointer}"

    return uri

def convert_relative_ref_to_absolute(obj, schema_path, uri_scheme='relative_file'):
    """
    Convert all value associated to $ref and having:
    relative_file:<path_to_file_relative_to_schema_file>
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(key, str):
                if key == "$ref":
                    uri = __convert_to_absolute(value, schema_path, uri_scheme)
                    obj[key] = uri
            if isinstance(value, dict):
                convert_relative_ref_to_absolute(value, schema_path, uri_scheme)
