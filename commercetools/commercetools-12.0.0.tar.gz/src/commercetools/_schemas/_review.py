# DO NOT EDIT! This file is automatically generated
import marshmallow

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools._schemas._type import FieldContainerField

__all__ = [
    "ReviewDraftSchema",
    "ReviewPagedQueryResponseSchema",
    "ReviewRatingStatisticsSchema",
    "ReviewReferenceSchema",
    "ReviewResourceIdentifierSchema",
    "ReviewSchema",
    "ReviewSetAuthorNameActionSchema",
    "ReviewSetCustomFieldActionSchema",
    "ReviewSetCustomTypeActionSchema",
    "ReviewSetCustomerActionSchema",
    "ReviewSetKeyActionSchema",
    "ReviewSetLocaleActionSchema",
    "ReviewSetRatingActionSchema",
    "ReviewSetTargetActionSchema",
    "ReviewSetTextActionSchema",
    "ReviewSetTitleActionSchema",
    "ReviewTransitionStateActionSchema",
    "ReviewUpdateActionSchema",
    "ReviewUpdateSchema",
]


class ReviewDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ReviewDraft`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)
    uniqueness_value = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="uniquenessValue"
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    author_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    text = marshmallow.fields.String(allow_none=True, missing=None)
    target = helpers.LazyNestedField(
        nested="commercetools._schemas._product.ProductResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    state = helpers.LazyNestedField(
        nested="commercetools._schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    rating = marshmallow.fields.Integer(allow_none=True, missing=None)
    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ReviewDraft(**data)


class ReviewPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ReviewPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._review.ReviewSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ReviewPagedQueryResponse(**data)


class ReviewRatingStatisticsSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ReviewRatingStatistics`."""

    average_rating = marshmallow.fields.Integer(
        allow_none=True, data_key="averageRating"
    )
    highest_rating = marshmallow.fields.Integer(
        allow_none=True, data_key="highestRating"
    )
    lowest_rating = marshmallow.fields.Integer(allow_none=True, data_key="lowestRating")
    count = marshmallow.fields.Integer(allow_none=True)
    ratings_distribution = marshmallow.fields.Dict(
        allow_none=True, data_key="ratingsDistribution"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ReviewRatingStatistics(**data)


class ReviewReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._review.ReviewSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ReviewReference(**data)


class ReviewResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ReviewResourceIdentifier(**data)


class ReviewSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.Review`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)
    uniqueness_value = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="uniquenessValue"
    )
    locale = marshmallow.fields.String(allow_none=True, missing=None)
    author_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorName"
    )
    title = marshmallow.fields.String(allow_none=True, missing=None)
    text = marshmallow.fields.String(allow_none=True, missing=None)
    target = helpers.LazyNestedField(
        nested="commercetools._schemas._product.ProductReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    included_in_statistics = marshmallow.fields.Bool(
        allow_none=True, data_key="includedInStatistics"
    )
    rating = marshmallow.fields.Integer(allow_none=True, missing=None)
    state = helpers.LazyNestedField(
        nested="commercetools._schemas._state.StateReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Review(**data)


class ReviewUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ReviewUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewUpdateAction(**data)


class ReviewUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ReviewUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "setAuthorName": "commercetools._schemas._review.ReviewSetAuthorNameActionSchema",
                "setCustomField": "commercetools._schemas._review.ReviewSetCustomFieldActionSchema",
                "setCustomType": "commercetools._schemas._review.ReviewSetCustomTypeActionSchema",
                "setCustomer": "commercetools._schemas._review.ReviewSetCustomerActionSchema",
                "setKey": "commercetools._schemas._review.ReviewSetKeyActionSchema",
                "setLocale": "commercetools._schemas._review.ReviewSetLocaleActionSchema",
                "setRating": "commercetools._schemas._review.ReviewSetRatingActionSchema",
                "setTarget": "commercetools._schemas._review.ReviewSetTargetActionSchema",
                "setText": "commercetools._schemas._review.ReviewSetTextActionSchema",
                "setTitle": "commercetools._schemas._review.ReviewSetTitleActionSchema",
                "transitionState": "commercetools._schemas._review.ReviewTransitionStateActionSchema",
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
        return types.ReviewUpdate(**data)


class ReviewSetAuthorNameActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetAuthorNameAction`."""

    author_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="authorName"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetAuthorNameAction(**data)


class ReviewSetCustomFieldActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetCustomFieldAction(**data)


class ReviewSetCustomTypeActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetCustomTypeAction`."""

    type = helpers.LazyNestedField(
        nested="commercetools._schemas._type.TypeResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    fields = FieldContainerField(allow_none=True, missing=None)  # type: ignore

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetCustomTypeAction(**data)


class ReviewSetCustomerActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetCustomerAction`."""

    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetCustomerAction(**data)


class ReviewSetKeyActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetKeyAction(**data)


class ReviewSetLocaleActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetLocaleAction`."""

    locale = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetLocaleAction(**data)


class ReviewSetRatingActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetRatingAction`."""

    rating = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetRatingAction(**data)


class ReviewSetTargetActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetTargetAction`."""

    target = helpers.LazyNestedField(
        nested="commercetools._schemas._product.ProductResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetTargetAction(**data)


class ReviewSetTextActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetTextAction`."""

    text = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetTextAction(**data)


class ReviewSetTitleActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewSetTitleAction`."""

    title = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewSetTitleAction(**data)


class ReviewTransitionStateActionSchema(ReviewUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ReviewTransitionStateAction`."""

    state = helpers.LazyNestedField(
        nested="commercetools._schemas._state.StateResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    force = marshmallow.fields.Bool(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ReviewTransitionStateAction(**data)
