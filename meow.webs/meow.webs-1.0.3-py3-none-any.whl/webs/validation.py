import inspect
import enum
import datetime
import uuid
import dataclasses
from meow.validators import get_validator, ValidationError
from .router import Route
from .conneg import negotiate_content_type
from .datastructures import MultiMapping
from . import Component, codecs, exceptions, http


class RequestDataComponent(Component):
    def __init__(self) -> None:
        self.codecs = [
            codecs.JSONCodec(),
            codecs.MultiPartCodec(),
            codecs.URLEncodedCodec(),
            codecs.TextCodec(),
        ]

    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation is http.RequestData

    def resolve(
        self, route: Route, content: http.Body, headers: http.Headers
    ) -> object:
        if not content:
            return None

        content_type = headers.get("Content-Type")
        try:
            codec = negotiate_content_type(self.codecs, content_type)
        except exceptions.NoCodecAvailable:
            raise exceptions.UnsupportedMediaType()

        try:
            return codec.decode(content, headers=headers)
        except exceptions.DecodeError as exc:
            raise exceptions.BadRequest(exc.detail)


PRIMITIVE_TYPES = frozenset(
    [str, float, int, bool, datetime.datetime, datetime.time, datetime.date, uuid.UUID]
)


class PrimitiveParamComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return parameter.annotation in PRIMITIVE_TYPES or (
            isinstance(parameter.annotation, type)
            and issubclass(parameter.annotation, enum.Enum)
        )

    def resolve(
        self,
        parameter: inspect.Parameter,
        path_params: http.PathParams,
        query_params: http.QueryParams,
    ) -> object:
        if parameter.name in path_params:
            validator = get_validator(parameter.annotation)
            try:
                return validator.validate(
                    path_params[parameter.name], allow_coerce=True
                )
            except ValidationError as exc:
                raise exceptions.NotFound({parameter.name: exc.detail})
        else:
            try:
                value = query_params[parameter.name]
            except KeyError:
                if parameter.default is parameter.empty:
                    raise exceptions.BadRequest(
                        {parameter.name: "Parameter is required"}
                    )
                return parameter.default

            validator = get_validator(parameter.annotation)

            try:
                return validator.validate(value, allow_coerce=True)
            except ValidationError as exc:
                raise exceptions.BadRequest({parameter.name: exc.detail})


class CompositeParamComponent(Component):
    def can_handle_parameter(self, parameter: inspect.Parameter) -> bool:
        return isinstance(parameter.annotation, type) and dataclasses.is_dataclass(
            parameter.annotation
        )

    def resolve(
        self,
        route: Route,
        parameter: inspect.Parameter,
        query_params: http.QueryParams,
        request_data: http.RequestData,
    ) -> object:
        validator = get_validator(parameter.annotation)
        if route.support_request_data:
            try:
                allow_coerce = isinstance(request_data, MultiMapping)
                return validator.validate(request_data, allow_coerce=allow_coerce)
            except ValidationError as exc:
                raise exceptions.BadRequest(exc.as_dict())
        else:
            try:
                return validator.validate(dict(query_params), allow_coerce=True)
            except ValidationError as exc:
                raise exceptions.BadRequest(exc.as_dict())


VALIDATION_COMPONENTS = [
    RequestDataComponent(),
    PrimitiveParamComponent(),
    CompositeParamComponent(),
]
