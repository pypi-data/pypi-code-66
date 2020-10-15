# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy
__all__ = [
    "Location",
    "Zone",
    "ZoneAddLocationAction",
    "ZoneChangeNameAction",
    "ZoneDraft",
    "ZonePagedQueryResponse",
    "ZoneReference",
    "ZoneRemoveLocationAction",
    "ZoneResourceIdentifier",
    "ZoneSetDescriptionAction",
    "ZoneSetKeyAction",
    "ZoneUpdate",
    "ZoneUpdateAction",
]


class Location(_BaseType):
    #: :class:`str`
    country: "str"
    #: Optional :class:`str`
    state: typing.Optional[str]

    def __init__(self, *, country: "str", state: typing.Optional[str] = None) -> None:
        self.country = country
        self.state = state
        super().__init__()

    def __repr__(self) -> str:
        return "Location(country=%r, state=%r)" % (self.country, self.state)


class Zone(BaseResource):
    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: str
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: List of :class:`commercetools.types.Location`
    locations: typing.List["Location"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        name: str,
        locations: typing.List["Location"],
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        description: typing.Optional[str] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "Zone(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r, description=%r, locations=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
                self.description,
                self.locations,
            )
        )


class ZoneDraft(_BaseType):
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: str
    #: Optional :class:`str`
    description: typing.Optional[str]
    #: List of :class:`commercetools.types.Location`
    locations: typing.List["Location"]

    def __init__(
        self,
        *,
        name: str,
        locations: typing.List["Location"],
        key: typing.Optional[str] = None,
        description: typing.Optional[str] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.locations = locations
        super().__init__()

    def __repr__(self) -> str:
        return "ZoneDraft(key=%r, name=%r, description=%r, locations=%r)" % (
            self.key,
            self.name,
            self.description,
            self.locations,
        )


class ZonePagedQueryResponse(_BaseType):
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.Zone`
    results: typing.Sequence["Zone"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        offset: int,
        results: typing.Sequence["Zone"],
        total: typing.Optional[int] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ZonePagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class ZoneReference(Reference):
    #: Optional :class:`commercetools.types.Zone`
    obj: typing.Optional["Zone"]

    def __init__(self, *, id: str, obj: typing.Optional["Zone"] = None) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.ZONE, id=id)

    def __repr__(self) -> str:
        return "ZoneReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class ZoneResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.ZONE, id=id, key=key)

    def __repr__(self) -> str:
        return "ZoneResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ZoneUpdate(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int, actions: list) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ZoneUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class ZoneUpdateAction(_BaseType):
    #: :class:`str`
    action: str

    def __init__(self, *, action: str) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ZoneUpdateAction(action=%r)" % (self.action,)


class ZoneAddLocationAction(ZoneUpdateAction):
    #: :class:`commercetools.types.Location`
    location: "Location"

    def __init__(self, *, location: "Location") -> None:
        self.location = location
        super().__init__(action="addLocation")

    def __repr__(self) -> str:
        return "ZoneAddLocationAction(action=%r, location=%r)" % (
            self.action,
            self.location,
        )


class ZoneChangeNameAction(ZoneUpdateAction):
    #: :class:`str`
    name: str

    def __init__(self, *, name: str) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ZoneChangeNameAction(action=%r, name=%r)" % (self.action, self.name)


class ZoneRemoveLocationAction(ZoneUpdateAction):
    #: :class:`commercetools.types.Location`
    location: "Location"

    def __init__(self, *, location: "Location") -> None:
        self.location = location
        super().__init__(action="removeLocation")

    def __repr__(self) -> str:
        return "ZoneRemoveLocationAction(action=%r, location=%r)" % (
            self.action,
            self.location,
        )


class ZoneSetDescriptionAction(ZoneUpdateAction):
    #: Optional :class:`str`
    description: typing.Optional[str]

    def __init__(self, *, description: typing.Optional[str] = None) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "ZoneSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ZoneSetKeyAction(ZoneUpdateAction):
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ZoneSetKeyAction(action=%r, key=%r)" % (self.action, self.key)
