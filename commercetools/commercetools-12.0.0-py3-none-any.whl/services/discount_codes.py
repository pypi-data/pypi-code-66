# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._discount_code import (
    DiscountCodeDraftSchema,
    DiscountCodePagedQueryResponseSchema,
    DiscountCodeSchema,
    DiscountCodeUpdateSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._discount_code import (
    DiscountCode,
    DiscountCodeDraft,
    DiscountCodePagedQueryResponse,
    DiscountCodeUpdate,
    DiscountCodeUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _DiscountCodeQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _DiscountCodeUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _DiscountCodeDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.DataErasureSchema
):
    pass


class DiscountCodeService(abstract.AbstractService):
    """Discount codes can be added to a discount-code to enable certain discount-
    code discounts."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> DiscountCode:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"discount-codes/{id}",
            params=params,
            schema_cls=DiscountCodeSchema,
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
    ) -> DiscountCodePagedQueryResponse:
        """Discount codes can be added to a discount-code to enable certain
        discount-code discounts.
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
            _DiscountCodeQuerySchema,
        )
        return self._client._get(
            endpoint="discount-codes",
            params=params,
            schema_cls=DiscountCodePagedQueryResponseSchema,
        )

    def create(
        self, draft: DiscountCodeDraft, *, expand: OptionalListStr = None
    ) -> DiscountCode:
        """Discount codes can be added to a discount-code to enable certain
        discount-code discounts.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="discount-codes",
            params=params,
            data_object=draft,
            request_schema_cls=DiscountCodeDraftSchema,
            response_schema_cls=DiscountCodeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[DiscountCodeUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> DiscountCode:
        params = self._serialize_params({"expand": expand}, _DiscountCodeUpdateSchema)
        update_action = DiscountCodeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"discount-codes/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=DiscountCodeUpdateSchema,
            response_schema_cls=DiscountCodeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        data_erasure: bool = None,
        force_delete: bool = False,
    ) -> DiscountCode:
        params = self._serialize_params(
            {"version": version, "expand": expand, "data_erasure": data_erasure},
            _DiscountCodeDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"discount-codes/{id}",
            params=params,
            response_schema_cls=DiscountCodeSchema,
            force_delete=force_delete,
        )
