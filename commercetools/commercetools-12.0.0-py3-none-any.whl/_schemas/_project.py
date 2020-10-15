# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types

__all__ = [
    "CartClassificationTypeSchema",
    "CartScoreTypeSchema",
    "CartValueTypeSchema",
    "CartsConfigurationSchema",
    "ExternalOAuthSchema",
    "ProjectChangeCountriesActionSchema",
    "ProjectChangeCountryTaxRateFallbackEnabledActionSchema",
    "ProjectChangeCurrenciesActionSchema",
    "ProjectChangeLanguagesActionSchema",
    "ProjectChangeMessagesConfigurationActionSchema",
    "ProjectChangeMessagesEnabledActionSchema",
    "ProjectChangeNameActionSchema",
    "ProjectSchema",
    "ProjectSetExternalOAuthActionSchema",
    "ProjectSetShippingRateInputTypeActionSchema",
    "ProjectUpdateActionSchema",
    "ProjectUpdateSchema",
    "ShippingRateInputTypeSchema",
]


class CartsConfigurationSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.CartsConfiguration`."""

    country_tax_rate_fallback_enabled = marshmallow.fields.Bool(
        allow_none=True, missing=None, data_key="countryTaxRateFallbackEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CartsConfiguration(**data)


class ExternalOAuthSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ExternalOAuth`."""

    url = marshmallow.fields.String(allow_none=True)
    authorization_header = marshmallow.fields.String(
        allow_none=True, data_key="authorizationHeader"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ExternalOAuth(**data)


class ProjectSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Project`."""

    version = marshmallow.fields.Integer(allow_none=True)
    key = marshmallow.fields.String(allow_none=True)
    name = marshmallow.fields.String(allow_none=True)
    countries = marshmallow.fields.List(marshmallow.fields.String())
    currencies = marshmallow.fields.List(marshmallow.fields.String())
    languages = marshmallow.fields.List(marshmallow.fields.String())
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    trial_until = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="trialUntil"
    )
    messages = helpers.LazyNestedField(
        nested="commercetools._schemas._message.MessageConfigurationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rate_input_type = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": "commercetools._schemas._project.CartClassificationTypeSchema",
            "CartScore": "commercetools._schemas._project.CartScoreTypeSchema",
            "CartValue": "commercetools._schemas._project.CartValueTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="shippingRateInputType",
    )
    external_oauth = helpers.LazyNestedField(
        nested="commercetools._schemas._project.ExternalOAuthSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="externalOAuth",
    )
    carts = helpers.LazyNestedField(
        nested="commercetools._schemas._project.CartsConfigurationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Project(**data)


class ProjectUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProjectUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectUpdateAction(**data)


class ProjectUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ProjectUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCountries": "commercetools._schemas._project.ProjectChangeCountriesActionSchema",
                "changeCountryTaxRateFallbackEnabled": "commercetools._schemas._project.ProjectChangeCountryTaxRateFallbackEnabledActionSchema",
                "changeCurrencies": "commercetools._schemas._project.ProjectChangeCurrenciesActionSchema",
                "changeLanguages": "commercetools._schemas._project.ProjectChangeLanguagesActionSchema",
                "changeMessagesConfiguration": "commercetools._schemas._project.ProjectChangeMessagesConfigurationActionSchema",
                "changeMessagesEnabled": "commercetools._schemas._project.ProjectChangeMessagesEnabledActionSchema",
                "changeName": "commercetools._schemas._project.ProjectChangeNameActionSchema",
                "setExternalOAuth": "commercetools._schemas._project.ProjectSetExternalOAuthActionSchema",
                "setShippingRateInputType": "commercetools._schemas._project.ProjectSetShippingRateInputTypeActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ProjectUpdate(**data)


class ShippingRateInputTypeSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShippingRateInputType`."""

    type = marshmallow_enum.EnumField(types.ShippingRateTierType, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.ShippingRateInputType(**data)


class CartClassificationTypeSchema(ShippingRateInputTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.CartClassificationType`."""

    values = marshmallow.fields.List(
        helpers.LazyNestedField(
            nested="commercetools._schemas._type.CustomFieldLocalizedEnumValueSchema",
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartClassificationType(**data)


class CartScoreTypeSchema(ShippingRateInputTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.CartScoreType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartScoreType()


class CartValueTypeSchema(ShippingRateInputTypeSchema):
    """Marshmallow schema for :class:`commercetools.types.CartValueType`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CartValueType()


class ProjectChangeCountriesActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeCountriesAction`."""

    countries = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeCountriesAction(**data)


class ProjectChangeCountryTaxRateFallbackEnabledActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeCountryTaxRateFallbackEnabledAction`."""

    country_tax_rate_fallback_enabled = marshmallow.fields.Bool(
        allow_none=True, data_key="countryTaxRateFallbackEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeCountryTaxRateFallbackEnabledAction(**data)


class ProjectChangeCurrenciesActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeCurrenciesAction`."""

    currencies = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeCurrenciesAction(**data)


class ProjectChangeLanguagesActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeLanguagesAction`."""

    languages = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeLanguagesAction(**data)


class ProjectChangeMessagesConfigurationActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeMessagesConfigurationAction`."""

    messages_configuration = helpers.LazyNestedField(
        nested="commercetools._schemas._message.MessageConfigurationDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="messagesConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeMessagesConfigurationAction(**data)


class ProjectChangeMessagesEnabledActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeMessagesEnabledAction`."""

    messages_enabled = marshmallow.fields.Bool(
        allow_none=True, data_key="messagesEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeMessagesEnabledAction(**data)


class ProjectChangeNameActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectChangeNameAction`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectChangeNameAction(**data)


class ProjectSetExternalOAuthActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectSetExternalOAuthAction`."""

    external_oauth = helpers.LazyNestedField(
        nested="commercetools._schemas._project.ExternalOAuthSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="externalOAuth",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectSetExternalOAuthAction(**data)


class ProjectSetShippingRateInputTypeActionSchema(ProjectUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ProjectSetShippingRateInputTypeAction`."""

    shipping_rate_input_type = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": "commercetools._schemas._project.CartClassificationTypeSchema",
            "CartScore": "commercetools._schemas._project.CartScoreTypeSchema",
            "CartValue": "commercetools._schemas._project.CartValueTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="shippingRateInputType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ProjectSetShippingRateInputTypeAction(**data)
