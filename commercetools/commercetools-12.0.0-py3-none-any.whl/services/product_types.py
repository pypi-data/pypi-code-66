# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._product_type import (
    ProductTypeDraftSchema,
    ProductTypePagedQueryResponseSchema,
    ProductTypeSchema,
    ProductTypeUpdateSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._product_type import (
    ProductType,
    ProductTypeDraft,
    ProductTypePagedQueryResponse,
    ProductTypeUpdate,
    ProductTypeUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ProductTypeQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _ProductTypeUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _ProductTypeDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class ProductTypeService(abstract.AbstractService):
    """Product Types are used to describe common characteristics, most importantly
    common custom attributes,

    of many concrete products.
    """

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> ProductType:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"product-types/{id}", params=params, schema_cls=ProductTypeSchema
        )

    def get_by_key(self, key: str, *, expand: OptionalListStr = None) -> ProductType:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"product-types/key={key}",
            params=params,
            schema_cls=ProductTypeSchema,
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
    ) -> ProductTypePagedQueryResponse:
        """Product Types are used to describe common characteristics, most
        importantly common custom attributes, of many concrete products.
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
            _ProductTypeQuerySchema,
        )
        return self._client._get(
            endpoint="product-types",
            params=params,
            schema_cls=ProductTypePagedQueryResponseSchema,
        )

    def create(
        self, draft: ProductTypeDraft, *, expand: OptionalListStr = None
    ) -> ProductType:
        """Product Types are used to describe common characteristics, most
        importantly common custom attributes, of many concrete products.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="product-types",
            params=params,
            data_object=draft,
            request_schema_cls=ProductTypeDraftSchema,
            response_schema_cls=ProductTypeSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ProductTypeUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ProductType:
        params = self._serialize_params({"expand": expand}, _ProductTypeUpdateSchema)
        update_action = ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=ProductTypeUpdateSchema,
            response_schema_cls=ProductTypeSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[ProductTypeUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> ProductType:
        params = self._serialize_params({"expand": expand}, _ProductTypeUpdateSchema)
        update_action = ProductTypeUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"product-types/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=ProductTypeUpdateSchema,
            response_schema_cls=ProductTypeSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ProductType:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ProductTypeDeleteSchema
        )
        return self._client._delete(
            endpoint=f"product-types/{id}",
            params=params,
            response_schema_cls=ProductTypeSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> ProductType:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _ProductTypeDeleteSchema
        )
        return self._client._delete(
            endpoint=f"product-types/key={key}",
            params=params,
            response_schema_cls=ProductTypeSchema,
            force_delete=force_delete,
        )
