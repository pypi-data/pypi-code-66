import pydantic


class GymDiscreteError(pydantic.PydanticValueError):
    msg_template = 'value: "{value}" not within range [0, {n})'
