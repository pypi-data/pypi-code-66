# DO NOT EDIT! This file is automatically generated
import marshmallow

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    LocalizedStringField,
    ReferenceSchema,
    ResourceIdentifierSchema,
)
from commercetools._schemas._type import FieldContainerField

__all__ = [
    "MyShoppingListSchema",
    "ShoppingListAddLineItemActionSchema",
    "ShoppingListAddTextLineItemActionSchema",
    "ShoppingListChangeLineItemQuantityActionSchema",
    "ShoppingListChangeLineItemsOrderActionSchema",
    "ShoppingListChangeNameActionSchema",
    "ShoppingListChangeTextLineItemNameActionSchema",
    "ShoppingListChangeTextLineItemQuantityActionSchema",
    "ShoppingListChangeTextLineItemsOrderActionSchema",
    "ShoppingListDraftSchema",
    "ShoppingListLineItemDraftSchema",
    "ShoppingListLineItemSchema",
    "ShoppingListPagedQueryResponseSchema",
    "ShoppingListReferenceSchema",
    "ShoppingListRemoveLineItemActionSchema",
    "ShoppingListRemoveTextLineItemActionSchema",
    "ShoppingListResourceIdentifierSchema",
    "ShoppingListSchema",
    "ShoppingListSetAnonymousIdActionSchema",
    "ShoppingListSetCustomFieldActionSchema",
    "ShoppingListSetCustomTypeActionSchema",
    "ShoppingListSetCustomerActionSchema",
    "ShoppingListSetDeleteDaysAfterLastModificationActionSchema",
    "ShoppingListSetDescriptionActionSchema",
    "ShoppingListSetKeyActionSchema",
    "ShoppingListSetLineItemCustomFieldActionSchema",
    "ShoppingListSetLineItemCustomTypeActionSchema",
    "ShoppingListSetSlugActionSchema",
    "ShoppingListSetTextLineItemCustomFieldActionSchema",
    "ShoppingListSetTextLineItemCustomTypeActionSchema",
    "ShoppingListSetTextLineItemDescriptionActionSchema",
    "ShoppingListUpdateActionSchema",
    "ShoppingListUpdateSchema",
    "TextLineItemDraftSchema",
    "TextLineItemSchema",
]


class MyShoppingListSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.MyShoppingList`."""

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
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
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
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.ShoppingListLineItemSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.TextLineItemSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.MyShoppingList(**data)


class ShoppingListDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListDraft`."""

    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.ShoppingListLineItemDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.TextLineItemDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShoppingListDraft(**data)


class ShoppingListLineItemDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListLineItemDraft`."""

    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    sku = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShoppingListLineItemDraft(**data)


class ShoppingListLineItemSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListLineItem`."""

    added_at = marshmallow.fields.DateTime(allow_none=True, data_key="addedAt")
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    deactivated_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="deactivatedAt"
    )
    id = marshmallow.fields.String(allow_none=True)
    name = LocalizedStringField(allow_none=True)
    product_id = marshmallow.fields.String(allow_none=True, data_key="productId")
    product_slug = LocalizedStringField(
        allow_none=True, missing=None, data_key="productSlug"
    )
    product_type = helpers.LazyNestedField(
        nested="commercetools._schemas._product_type.ProductTypeReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="productType",
    )
    quantity = marshmallow.fields.Integer(allow_none=True)
    variant = helpers.LazyNestedField(
        nested="commercetools._schemas._product.ProductVariantSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShoppingListLineItem(**data)


class ShoppingListPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.ShoppingListSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShoppingListPagedQueryResponse(**data)


class ShoppingListReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.ShoppingListSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ShoppingListReference(**data)


class ShoppingListResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ShoppingListResourceIdentifier(**data)


class ShoppingListSchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingList`."""

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
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
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
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.ShoppingListLineItemSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="lineItems",
    )
    name = LocalizedStringField(allow_none=True)
    slug = LocalizedStringField(allow_none=True, missing=None)
    text_line_items = helpers.LazyNestedField(
        nested="commercetools._schemas._shopping_list.TextLineItemSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="textLineItems",
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ShoppingList(**data)


class ShoppingListUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListUpdateAction(**data)


class ShoppingListUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addLineItem": "commercetools._schemas._shopping_list.ShoppingListAddLineItemActionSchema",
                "addTextLineItem": "commercetools._schemas._shopping_list.ShoppingListAddTextLineItemActionSchema",
                "changeLineItemQuantity": "commercetools._schemas._shopping_list.ShoppingListChangeLineItemQuantityActionSchema",
                "changeLineItemsOrder": "commercetools._schemas._shopping_list.ShoppingListChangeLineItemsOrderActionSchema",
                "changeName": "commercetools._schemas._shopping_list.ShoppingListChangeNameActionSchema",
                "changeTextLineItemName": "commercetools._schemas._shopping_list.ShoppingListChangeTextLineItemNameActionSchema",
                "changeTextLineItemQuantity": "commercetools._schemas._shopping_list.ShoppingListChangeTextLineItemQuantityActionSchema",
                "changeTextLineItemsOrder": "commercetools._schemas._shopping_list.ShoppingListChangeTextLineItemsOrderActionSchema",
                "removeLineItem": "commercetools._schemas._shopping_list.ShoppingListRemoveLineItemActionSchema",
                "removeTextLineItem": "commercetools._schemas._shopping_list.ShoppingListRemoveTextLineItemActionSchema",
                "setAnonymousId": "commercetools._schemas._shopping_list.ShoppingListSetAnonymousIdActionSchema",
                "setCustomField": "commercetools._schemas._shopping_list.ShoppingListSetCustomFieldActionSchema",
                "setCustomType": "commercetools._schemas._shopping_list.ShoppingListSetCustomTypeActionSchema",
                "setCustomer": "commercetools._schemas._shopping_list.ShoppingListSetCustomerActionSchema",
                "setDeleteDaysAfterLastModification": "commercetools._schemas._shopping_list.ShoppingListSetDeleteDaysAfterLastModificationActionSchema",
                "setDescription": "commercetools._schemas._shopping_list.ShoppingListSetDescriptionActionSchema",
                "setKey": "commercetools._schemas._shopping_list.ShoppingListSetKeyActionSchema",
                "setLineItemCustomField": "commercetools._schemas._shopping_list.ShoppingListSetLineItemCustomFieldActionSchema",
                "setLineItemCustomType": "commercetools._schemas._shopping_list.ShoppingListSetLineItemCustomTypeActionSchema",
                "setSlug": "commercetools._schemas._shopping_list.ShoppingListSetSlugActionSchema",
                "setTextLineItemCustomField": "commercetools._schemas._shopping_list.ShoppingListSetTextLineItemCustomFieldActionSchema",
                "setTextLineItemCustomType": "commercetools._schemas._shopping_list.ShoppingListSetTextLineItemCustomTypeActionSchema",
                "setTextLineItemDescription": "commercetools._schemas._shopping_list.ShoppingListSetTextLineItemDescriptionActionSchema",
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
        return types.ShoppingListUpdate(**data)


class TextLineItemDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TextLineItemDraft`."""

    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    name = LocalizedStringField(allow_none=True)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TextLineItemDraft(**data)


class TextLineItemSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TextLineItem`."""

    added_at = marshmallow.fields.DateTime(allow_none=True, data_key="addedAt")
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    description = LocalizedStringField(allow_none=True, missing=None)
    id = marshmallow.fields.String(allow_none=True)
    name = LocalizedStringField(allow_none=True)
    quantity = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TextLineItem(**data)


class ShoppingListAddLineItemActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListAddLineItemAction`."""

    sku = marshmallow.fields.String(allow_none=True, missing=None)
    product_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="productId"
    )
    variant_id = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="variantId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
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
        del data["action"]
        return types.ShoppingListAddLineItemAction(**data)


class ShoppingListAddTextLineItemActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListAddTextLineItemAction`."""

    name = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)
    added_at = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="addedAt"
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
        del data["action"]
        return types.ShoppingListAddTextLineItemAction(**data)


class ShoppingListChangeLineItemQuantityActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeLineItemQuantityAction`."""

    line_item_id = marshmallow.fields.String(allow_none=True, data_key="lineItemId")
    quantity = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeLineItemQuantityAction(**data)


class ShoppingListChangeLineItemsOrderActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeLineItemsOrderAction`."""

    line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="lineItemOrder"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeLineItemsOrderAction(**data)


class ShoppingListChangeNameActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeNameAction`."""

    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeNameAction(**data)


class ShoppingListChangeTextLineItemNameActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeTextLineItemNameAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeTextLineItemNameAction(**data)


class ShoppingListChangeTextLineItemQuantityActionSchema(
    ShoppingListUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeTextLineItemQuantityAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeTextLineItemQuantityAction(**data)


class ShoppingListChangeTextLineItemsOrderActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListChangeTextLineItemsOrderAction`."""

    text_line_item_order = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), data_key="textLineItemOrder"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListChangeTextLineItemsOrderAction(**data)


class ShoppingListRemoveLineItemActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListRemoveLineItemAction`."""

    line_item_id = marshmallow.fields.String(allow_none=True, data_key="lineItemId")
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListRemoveLineItemAction(**data)


class ShoppingListRemoveTextLineItemActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListRemoveTextLineItemAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
    quantity = marshmallow.fields.Integer(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListRemoveTextLineItemAction(**data)


class ShoppingListSetAnonymousIdActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetAnonymousIdAction`."""

    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetAnonymousIdAction(**data)


class ShoppingListSetCustomFieldActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetCustomFieldAction`."""

    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetCustomFieldAction(**data)


class ShoppingListSetCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetCustomTypeAction`."""

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
        return types.ShoppingListSetCustomTypeAction(**data)


class ShoppingListSetCustomerActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetCustomerAction`."""

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
        return types.ShoppingListSetCustomerAction(**data)


class ShoppingListSetDeleteDaysAfterLastModificationActionSchema(
    ShoppingListUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetDeleteDaysAfterLastModificationAction`."""

    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="deleteDaysAfterLastModification"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetDeleteDaysAfterLastModificationAction(**data)


class ShoppingListSetDescriptionActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetDescriptionAction`."""

    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetDescriptionAction(**data)


class ShoppingListSetKeyActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetKeyAction(**data)


class ShoppingListSetLineItemCustomFieldActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetLineItemCustomFieldAction`."""

    line_item_id = marshmallow.fields.String(allow_none=True, data_key="lineItemId")
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetLineItemCustomFieldAction(**data)


class ShoppingListSetLineItemCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetLineItemCustomTypeAction`."""

    line_item_id = marshmallow.fields.String(allow_none=True, data_key="lineItemId")
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
        return types.ShoppingListSetLineItemCustomTypeAction(**data)


class ShoppingListSetSlugActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetSlugAction`."""

    slug = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetSlugAction(**data)


class ShoppingListSetTextLineItemCustomFieldActionSchema(
    ShoppingListUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetTextLineItemCustomFieldAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
    name = marshmallow.fields.String(allow_none=True)
    value = marshmallow.fields.Raw(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetTextLineItemCustomFieldAction(**data)


class ShoppingListSetTextLineItemCustomTypeActionSchema(ShoppingListUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetTextLineItemCustomTypeAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
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
        return types.ShoppingListSetTextLineItemCustomTypeAction(**data)


class ShoppingListSetTextLineItemDescriptionActionSchema(
    ShoppingListUpdateActionSchema
):
    """Marshmallow schema for :class:`commercetools.types.ShoppingListSetTextLineItemDescriptionAction`."""

    text_line_item_id = marshmallow.fields.String(
        allow_none=True, data_key="textLineItemId"
    )
    description = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.ShoppingListSetTextLineItemDescriptionAction(**data)
