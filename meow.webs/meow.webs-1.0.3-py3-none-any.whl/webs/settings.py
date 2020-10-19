import typing
import importlib
from meow.validators import Container, Validator, Object, ValidationError
from . import Component
from .utils import import_string


class EventHook(typing.Protocol):
    def on_request(self, *args: object, **kwargs: object) -> object:
        ...  # pragma: nocover

    def on_response(self, *args: object, **kwargs: object) -> object:
        ...  # pragma: nocover

    def on_error(self, *args: object, **kwargs: object) -> object:
        ...  # pragma: nocover


class Settings:
    __slots__ = ()
    ROUTES: str = "routes.routes"
    STATIC_URL: str = "/static"
    DEBUG: bool = True
    PROPAGATE_EXCEPTIONS: typing.Optional[bool] = None
    COMPONENTS: typing.Tuple[Component, ...] = ()
    EVENT_HOOKS: typing.Tuple[EventHook, ...] = ()
    TEMPLATE_DIRS: typing.Tuple[typing.Union[str, typing.Dict[str, str]], ...] = ()
    STATIC_DIRS: typing.Tuple[typing.Union[str, typing.Dict[str, str]], ...] = ()

    def __getitem__(self, item: str) -> typing.Any:  # pragma: nocover
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)


def _get_instance(obj: typing.Union[str, object]) -> object:
    if isinstance(obj, str):
        value = import_string(obj, type)
        return value()
    else:
        return obj


class ComponentInstanceValidator(Validator[Component]):
    errors = {"type": "Must be an instance of Component class", "import": "{error}"}

    def validate(self, value: object, allow_coerce: bool = False) -> Component:
        try:
            inst = _get_instance(value)
        except (ImportError, TypeError, ValueError) as e:
            self.error("import", error=str(e))
        if not isinstance(inst, Component):
            self.error("type")
        return inst


class EventHookValidator(Validator[EventHook]):
    errors = {
        "type": "Must be compatible with EventHook protocol",
        "import": "{error}",
    }

    def validate(self, value: object, allow_coerce: bool = False) -> EventHook:
        try:
            inst = _get_instance(value)
        except (ImportError, TypeError, ValueError) as e:
            self.error("import", error=str(e))
        if not any(
            [
                hasattr(inst, "on_request"),
                hasattr(inst, "on_response"),
                hasattr(inst, "on_error"),
            ]
        ):
            self.error("type")
        return inst  # type: ignore


def load_settings(settings_module: str) -> Settings:
    module = importlib.import_module(settings_module)

    def default(
        tp: typing.Type[object], *args: object
    ) -> typing.Callable[..., Validator[typing.Any]]:
        if tp is Component:
            return ComponentInstanceValidator
        if tp is EventHook:
            return EventHookValidator
        raise TypeError()  # pragma: nocover

    validators = Container(default=default)
    config_dict: typing.Dict[str, object] = {"__slots__": ()}
    to_validate = {}
    properties = {}
    for setting in dir(module):
        if setting.isupper():
            value = getattr(module, setting)
            if setting in Settings.__annotations__:
                to_validate[setting] = value
                properties[setting] = validators[Settings.__annotations__[setting]]
            else:
                config_dict[setting] = value
    try:
        validated_conf: typing.Mapping[str, typing.Any] = Object(
            properties=properties
        ).validate(to_validate)
    except ValidationError as exc:
        raise ValidationError({"Improperly configured": exc.detail}) from None

    config_dict.update(validated_conf)
    return type("Settings", (Settings,), config_dict)()  # type: ignore
