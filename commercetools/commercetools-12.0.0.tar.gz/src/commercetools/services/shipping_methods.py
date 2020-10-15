# DO NOT EDIT! This file is automatically generated
import typing

import marshmallow
from marshmallow import fields

from commercetools._schemas._shipping_method import (
    ShippingMethodDraftSchema,
    ShippingMethodPagedQueryResponseSchema,
    ShippingMethodSchema,
    ShippingMethodUpdateSchema,
)
from commercetools.helpers import OptionalList, RemoveEmptyValuesMixin
from commercetools.types._shipping_method import (
    ShippingMethod,
    ShippingMethodDraft,
    ShippingMethodPagedQueryResponse,
    ShippingMethodUpdate,
    ShippingMethodUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ShippingMethodQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ShippingMethodUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ShippingMethodDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class _ShippingMethodMatching_CartSchema(traits.ExpandableSchema):
    cart_id = OptionalList(fields.String(), data_key="cartId")


class _ShippingMethodMatching_LocationSchema(traits.ExpandableSchema):
    country = OptionalList(fields.String())
    state = OptionalList(fields.String(), required=False)
    currency = OptionalList(fields.String(), required=False)


class _ShippingMethodMatching_OrdereditSchema(
    marshmallow.Schema, RemoveEmptyValuesMixin
):
    order_edit_id = OptionalList(fields.String(), data_key="orderEditId")
    country = OptionalList(fields.String())
    state = OptionalList(fields.String(), required=False)


class ShippingMethodService(abstract.AbstractService):
    """Shipping Methods define where orders can be shipped and what the costs are."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> ShippingMethod:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"shipping-methods/{id}",
            params=params,
            schema_cls=ShippingMethodSchema,
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> ShippingMethod:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"shipping-methods/key={key}",
            params=params,
            schema_cls=ShippingMethodSchema,
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> ShippingMethodPagedQueryResponse:
        """Shipping Methods define where orders can be shipped and what the costs
        are.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _ShippingMethodQuerySchema,
        )
        return self._client._get(
            endpoint="shipping-methods",
            params=params,
            schema_cls=ShippingMethodPagedQueryResponseSchema,
        )

    def create(
        self, draft: ShippingMethodDraft, *, expand: OptionalListStr = None
    ) -> ShippingMethod:
        """Shipping Methods define where orders can be shipped and what the costs
        are.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="shipping-methods",
            params=params,
            data_object=draft,
            request_schema_cls=ShippingMethodDraftSchema,
            response_schema_cls=ShippingMethodSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ShippingMethodUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ShippingMethod:
        params = self._serialize_params({"expand": expand}, _ShippingMethodUpdateSchema)
        update_action = ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shipping-methods/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=ShippingMethodUpdateSchema,
            response_schema_cls=ShippingMethodSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[ShippingMethodUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ShippingMethod:
        params = self._serialize_params({"expand": expand}, _ShippingMethodUpdateSchema)
        update_action = ShippingMethodUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"shipping-methods/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=ShippingMethodUpdateSchema,
            response_schema_cls=ShippingMethodSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ShippingMethod:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ShippingMethodDeleteSchema
        )
        return self._client._delete(
            endpoint=f"shipping-methods/{id}",
            params=params,
            response_schema_cls=ShippingMethodSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ShippingMethod:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ShippingMethodDeleteSchema
        )
        return self._client._delete(
            endpoint=f"shipping-methods/key={key}",
            params=params,
            response_schema_cls=ShippingMethodSchema,
            force_delete=force_delete,
        )

    def matching_cart(
        self, cart_id: str, *, expand: OptionalListStr = None
    ) -> ShippingMethodPagedQueryResponse:
        """Get ShippingMethods for a cart
        """
        params = self._serialize_params(
            {"expand": expand, "cart_id": cart_id}, _ShippingMethodMatching_CartSchema
        )
        return self._client._get(
            endpoint="shipping-methods/matching-cart",
            params=params,
            schema_cls=ShippingMethodPagedQueryResponseSchema,
        )

    def matching_location(
        self,
        country: str,
        *,
        expand: OptionalListStr = None,
        state: str = None,
        currency: str = None,
    ) -> ShippingMethodPagedQueryResponse:
        """Get ShippingMethods for a location
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "country": country,
                "state": state,
                "currency": currency,
            },
            _ShippingMethodMatching_LocationSchema,
        )
        return self._client._get(
            endpoint="shipping-methods/matching-location",
            params=params,
            schema_cls=ShippingMethodPagedQueryResponseSchema,
        )

    def matching_orderedit(
        self, order_edit_id: str, country: str, *, state: str = None
    ) -> ShippingMethodPagedQueryResponse:
        """Get ShippingMethods for an order edit
        """
        params = self._serialize_params(
            {"order_edit_id": order_edit_id, "country": country, "state": state},
            _ShippingMethodMatching_OrdereditSchema,
        )
        return self._client._get(
            endpoint="shipping-methods/matching-orderedit",
            params=params,
            schema_cls=ShippingMethodPagedQueryResponseSchema,
        )
