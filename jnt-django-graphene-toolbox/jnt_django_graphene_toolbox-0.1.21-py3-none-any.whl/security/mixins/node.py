from typing import Optional

from django.db.models import Model
from graphql import ResolveInfo

from jnt_django_graphene_toolbox.helpers.generics import (
    get_object_or_not_found,
)
from jnt_django_graphene_toolbox.security.permissions import AllowAny


class AuthNode:
    """
    Permission mixin for queries (nodes).

    Allows for simple configuration of access to nodes via class system.
    """

    permission_classes = (AllowAny,)

    @classmethod
    def get_node(
        cls, info: ResolveInfo, obj_id: str,  # noqa: WPS110
    ) -> Optional[Model]:
        """Get node."""
        has_node_permission = all(
            (
                perm().has_node_permission(info, obj_id)
                for perm in cls.permission_classes
            ),
        )

        if has_node_permission:
            return get_object_or_not_found(
                cls.get_queryset(cls._meta.model.objects, info),  # type: ignore
                id=obj_id,
            )

        return None
