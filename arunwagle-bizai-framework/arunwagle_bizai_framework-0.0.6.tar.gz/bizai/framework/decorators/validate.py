import json
import functools

from jsonschema import validate
from jsonschema.exceptions import SchemaError, ValidationError, ErrorTree

# import jsonschema


def validate_input(schema):

    def _validate(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            """
            Get the attributes to validate
            """
            # print("validate_input::*args::{}".format(args))
            # print("validate_input::**kwargs::{}".format(kwargs))
            # input = args[0]._input
            input = kwargs
            # print("validate_input::input::{}".format(input))
            # print("validate_input::schema::{}".format(schema))
            result = None
            try:
                # json_obj = json.loads(input)
                validate(instance=input, schema=schema)
                result = func(*args, **kwargs)
            except SchemaError as e:
                raise Exception(
                    "There is an error with the schema {} for function {} ".format(e.message, func.__name__)) 
            except ValidationError as e:
                print("Validation Error {} in function {} ".format(
                    e.message, func.__name__))

                raise Exception(
                    "Validation Error {} in function {} ".format(e.message, func.__name__))

            return result

        return func_wrapper

    return _validate
