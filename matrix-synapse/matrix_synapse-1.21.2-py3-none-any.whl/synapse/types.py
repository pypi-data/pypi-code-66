# -*- coding: utf-8 -*-
# Copyright 2014-2016 OpenMarket Ltd
# Copyright 2019 The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import abc
import re
import string
import sys
from collections import namedtuple
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
)

import attr
from signedjson.key import decode_verify_key_bytes
from unpaddedbase64 import decode_base64

from synapse.api.errors import Codes, SynapseError

if TYPE_CHECKING:
    from synapse.storage.databases.main import DataStore

# define a version of typing.Collection that works on python 3.5
if sys.version_info[:3] >= (3, 6, 0):
    from typing import Collection
else:
    from typing import Container, Iterable, Sized

    T_co = TypeVar("T_co", covariant=True)

    class Collection(Iterable[T_co], Container[T_co], Sized):  # type: ignore
        __slots__ = ()


# Define a state map type from type/state_key to T (usually an event ID or
# event)
T = TypeVar("T")
StateKey = Tuple[str, str]
StateMap = Mapping[StateKey, T]
MutableStateMap = MutableMapping[StateKey, T]

# the type of a JSON-serialisable dict. This could be made stronger, but it will
# do for now.
JsonDict = Dict[str, Any]


class Requester(
    namedtuple(
        "Requester",
        [
            "user",
            "access_token_id",
            "is_guest",
            "shadow_banned",
            "device_id",
            "app_service",
        ],
    )
):
    """
    Represents the user making a request

    Attributes:
        user (UserID):  id of the user making the request
        access_token_id (int|None):  *ID* of the access token used for this
            request, or None if it came via the appservice API or similar
        is_guest (bool):  True if the user making this request is a guest user
        shadow_banned (bool):  True if the user making this request has been shadow-banned.
        device_id (str|None):  device_id which was set at authentication time
        app_service (ApplicationService|None):  the AS requesting on behalf of the user
    """

    def serialize(self):
        """Converts self to a type that can be serialized as JSON, and then
        deserialized by `deserialize`

        Returns:
            dict
        """
        return {
            "user_id": self.user.to_string(),
            "access_token_id": self.access_token_id,
            "is_guest": self.is_guest,
            "shadow_banned": self.shadow_banned,
            "device_id": self.device_id,
            "app_server_id": self.app_service.id if self.app_service else None,
        }

    @staticmethod
    def deserialize(store, input):
        """Converts a dict that was produced by `serialize` back into a
        Requester.

        Args:
            store (DataStore): Used to convert AS ID to AS object
            input (dict): A dict produced by `serialize`

        Returns:
            Requester
        """
        appservice = None
        if input["app_server_id"]:
            appservice = store.get_app_service_by_id(input["app_server_id"])

        return Requester(
            user=UserID.from_string(input["user_id"]),
            access_token_id=input["access_token_id"],
            is_guest=input["is_guest"],
            shadow_banned=input["shadow_banned"],
            device_id=input["device_id"],
            app_service=appservice,
        )


def create_requester(
    user_id,
    access_token_id=None,
    is_guest=False,
    shadow_banned=False,
    device_id=None,
    app_service=None,
):
    """
    Create a new ``Requester`` object

    Args:
        user_id (str|UserID):  id of the user making the request
        access_token_id (int|None):  *ID* of the access token used for this
            request, or None if it came via the appservice API or similar
        is_guest (bool):  True if the user making this request is a guest user
        shadow_banned (bool):  True if the user making this request is shadow-banned.
        device_id (str|None):  device_id which was set at authentication time
        app_service (ApplicationService|None):  the AS requesting on behalf of the user

    Returns:
        Requester
    """
    if not isinstance(user_id, UserID):
        user_id = UserID.from_string(user_id)
    return Requester(
        user_id, access_token_id, is_guest, shadow_banned, device_id, app_service
    )


def get_domain_from_id(string):
    idx = string.find(":")
    if idx == -1:
        raise SynapseError(400, "Invalid ID: %r" % (string,))
    return string[idx + 1 :]


def get_localpart_from_id(string):
    idx = string.find(":")
    if idx == -1:
        raise SynapseError(400, "Invalid ID: %r" % (string,))
    return string[1:idx]


DS = TypeVar("DS", bound="DomainSpecificString")


class DomainSpecificString(
    namedtuple("DomainSpecificString", ("localpart", "domain")), metaclass=abc.ABCMeta
):
    """Common base class among ID/name strings that have a local part and a
    domain name, prefixed with a sigil.

    Has the fields:

        'localpart' : The local part of the name (without the leading sigil)
        'domain' : The domain part of the name
    """

    SIGIL = abc.abstractproperty()  # type: str  # type: ignore

    # Deny iteration because it will bite you if you try to create a singleton
    # set by:
    #    users = set(user)
    def __iter__(self):
        raise ValueError("Attempted to iterate a %s" % (type(self).__name__,))

    # Because this class is a namedtuple of strings and booleans, it is deeply
    # immutable.
    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

    @classmethod
    def from_string(cls: Type[DS], s: str) -> DS:
        """Parse the string given by 's' into a structure object."""
        if len(s) < 1 or s[0:1] != cls.SIGIL:
            raise SynapseError(
                400,
                "Expected %s string to start with '%s'" % (cls.__name__, cls.SIGIL),
                Codes.INVALID_PARAM,
            )

        parts = s[1:].split(":", 1)
        if len(parts) != 2:
            raise SynapseError(
                400,
                "Expected %s of the form '%slocalname:domain'"
                % (cls.__name__, cls.SIGIL),
                Codes.INVALID_PARAM,
            )

        domain = parts[1]

        # This code will need changing if we want to support multiple domain
        # names on one HS
        return cls(localpart=parts[0], domain=domain)

    def to_string(self) -> str:
        """Return a string encoding the fields of the structure object."""
        return "%s%s:%s" % (self.SIGIL, self.localpart, self.domain)

    @classmethod
    def is_valid(cls: Type[DS], s: str) -> bool:
        try:
            cls.from_string(s)
            return True
        except Exception:
            return False

    __repr__ = to_string


class UserID(DomainSpecificString):
    """Structure representing a user ID."""

    SIGIL = "@"


class RoomAlias(DomainSpecificString):
    """Structure representing a room name."""

    SIGIL = "#"


class RoomID(DomainSpecificString):
    """Structure representing a room id. """

    SIGIL = "!"


class EventID(DomainSpecificString):
    """Structure representing an event id. """

    SIGIL = "$"


class GroupID(DomainSpecificString):
    """Structure representing a group ID."""

    SIGIL = "+"

    @classmethod
    def from_string(cls: Type[DS], s: str) -> DS:
        group_id = super().from_string(s)  # type: DS # type: ignore

        if not group_id.localpart:
            raise SynapseError(400, "Group ID cannot be empty", Codes.INVALID_PARAM)

        if contains_invalid_mxid_characters(group_id.localpart):
            raise SynapseError(
                400,
                "Group ID can only contain characters a-z, 0-9, or '=_-./'",
                Codes.INVALID_PARAM,
            )

        return group_id


mxid_localpart_allowed_characters = set(
    "_-./=" + string.ascii_lowercase + string.digits
)


def contains_invalid_mxid_characters(localpart):
    """Check for characters not allowed in an mxid or groupid localpart

    Args:
        localpart (basestring): the localpart to be checked

    Returns:
        bool: True if there are any naughty characters
    """
    return any(c not in mxid_localpart_allowed_characters for c in localpart)


UPPER_CASE_PATTERN = re.compile(b"[A-Z_]")

# the following is a pattern which matches '=', and bytes which are not allowed in a mxid
# localpart.
#
# It works by:
#  * building a string containing the allowed characters (excluding '=')
#  * escaping every special character with a backslash (to stop '-' being interpreted as a
#    range operator)
#  * wrapping it in a '[^...]' regex
#  * converting the whole lot to a 'bytes' sequence, so that we can use it to match
#    bytes rather than strings
#
NON_MXID_CHARACTER_PATTERN = re.compile(
    ("[^%s]" % (re.escape("".join(mxid_localpart_allowed_characters - {"="})),)).encode(
        "ascii"
    )
)


def map_username_to_mxid_localpart(username, case_sensitive=False):
    """Map a username onto a string suitable for a MXID

    This follows the algorithm laid out at
    https://matrix.org/docs/spec/appendices.html#mapping-from-other-character-sets.

    Args:
        username (unicode|bytes): username to be mapped
        case_sensitive (bool): true if TEST and test should be mapped
            onto different mxids

    Returns:
        unicode: string suitable for a mxid localpart
    """
    if not isinstance(username, bytes):
        username = username.encode("utf-8")

    # first we sort out upper-case characters
    if case_sensitive:

        def f1(m):
            return b"_" + m.group().lower()

        username = UPPER_CASE_PATTERN.sub(f1, username)
    else:
        username = username.lower()

    # then we sort out non-ascii characters
    def f2(m):
        g = m.group()[0]
        if isinstance(g, str):
            # on python 2, we need to do a ord(). On python 3, the
            # byte itself will do.
            g = ord(g)
        return b"=%02x" % (g,)

    username = NON_MXID_CHARACTER_PATTERN.sub(f2, username)

    # we also do the =-escaping to mxids starting with an underscore.
    username = re.sub(b"^_", b"=5f", username)

    # we should now only have ascii bytes left, so can decode back to a
    # unicode.
    return username.decode("ascii")


@attr.s(frozen=True, slots=True)
class RoomStreamToken:
    """Tokens are positions between events. The token "s1" comes after event 1.

            s0    s1
            |     |
        [0] V [1] V [2]

    Tokens can either be a point in the live event stream or a cursor going
    through historic events.

    When traversing the live event stream events are ordered by when they
    arrived at the homeserver.

    When traversing historic events the events are ordered by their depth in
    the event graph "topological_ordering" and then by when they arrived at the
    homeserver "stream_ordering".

    Live tokens start with an "s" followed by the "stream_ordering" id of the
    event it comes after. Historic tokens start with a "t" followed by the
    "topological_ordering" id of the event it comes after, followed by "-",
    followed by the "stream_ordering" id of the event it comes after.
    """

    topological = attr.ib(
        type=Optional[int],
        validator=attr.validators.optional(attr.validators.instance_of(int)),
    )
    stream = attr.ib(type=int, validator=attr.validators.instance_of(int))

    @classmethod
    async def parse(cls, store: "DataStore", string: str) -> "RoomStreamToken":
        try:
            if string[0] == "s":
                return cls(topological=None, stream=int(string[1:]))
            if string[0] == "t":
                parts = string[1:].split("-", 1)
                return cls(topological=int(parts[0]), stream=int(parts[1]))
        except Exception:
            pass
        raise SynapseError(400, "Invalid token %r" % (string,))

    @classmethod
    def parse_stream_token(cls, string: str) -> "RoomStreamToken":
        try:
            if string[0] == "s":
                return cls(topological=None, stream=int(string[1:]))
        except Exception:
            pass
        raise SynapseError(400, "Invalid token %r" % (string,))

    def copy_and_advance(self, other: "RoomStreamToken") -> "RoomStreamToken":
        """Return a new token such that if an event is after both this token and
        the other token, then its after the returned token too.
        """

        if self.topological or other.topological:
            raise Exception("Can't advance topological tokens")

        max_stream = max(self.stream, other.stream)

        return RoomStreamToken(None, max_stream)

    def as_tuple(self) -> Tuple[Optional[int], int]:
        return (self.topological, self.stream)

    async def to_string(self, store: "DataStore") -> str:
        if self.topological is not None:
            return "t%d-%d" % (self.topological, self.stream)
        else:
            return "s%d" % (self.stream,)


@attr.s(slots=True, frozen=True)
class StreamToken:
    room_key = attr.ib(
        type=RoomStreamToken, validator=attr.validators.instance_of(RoomStreamToken)
    )
    presence_key = attr.ib(type=int)
    typing_key = attr.ib(type=int)
    receipt_key = attr.ib(type=int)
    account_data_key = attr.ib(type=int)
    push_rules_key = attr.ib(type=int)
    to_device_key = attr.ib(type=int)
    device_list_key = attr.ib(type=int)
    groups_key = attr.ib(type=int)

    _SEPARATOR = "_"
    START = None  # type: StreamToken

    @classmethod
    async def from_string(cls, store: "DataStore", string: str) -> "StreamToken":
        try:
            keys = string.split(cls._SEPARATOR)
            while len(keys) < len(attr.fields(cls)):
                # i.e. old token from before receipt_key
                keys.append("0")
            return cls(
                await RoomStreamToken.parse(store, keys[0]), *(int(k) for k in keys[1:])
            )
        except Exception:
            raise SynapseError(400, "Invalid Token")

    async def to_string(self, store: "DataStore") -> str:
        return self._SEPARATOR.join(
            [
                await self.room_key.to_string(store),
                str(self.presence_key),
                str(self.typing_key),
                str(self.receipt_key),
                str(self.account_data_key),
                str(self.push_rules_key),
                str(self.to_device_key),
                str(self.device_list_key),
                str(self.groups_key),
            ]
        )

    @property
    def room_stream_id(self):
        return self.room_key.stream

    def copy_and_advance(self, key, new_value) -> "StreamToken":
        """Advance the given key in the token to a new value if and only if the
        new value is after the old value.
        """
        if key == "room_key":
            new_token = self.copy_and_replace(
                "room_key", self.room_key.copy_and_advance(new_value)
            )
            return new_token

        new_token = self.copy_and_replace(key, new_value)
        new_id = int(getattr(new_token, key))
        old_id = int(getattr(self, key))

        if old_id < new_id:
            return new_token
        else:
            return self

    def copy_and_replace(self, key, new_value) -> "StreamToken":
        return attr.evolve(self, **{key: new_value})


StreamToken.START = StreamToken(RoomStreamToken(None, 0), 0, 0, 0, 0, 0, 0, 0, 0)


@attr.s(slots=True, frozen=True)
class PersistedEventPosition:
    """Position of a newly persisted event with instance that persisted it.

    This can be used to test whether the event is persisted before or after a
    RoomStreamToken.
    """

    instance_name = attr.ib(type=str)
    stream = attr.ib(type=int)

    def persisted_after(self, token: RoomStreamToken) -> bool:
        return token.stream < self.stream

    def to_room_stream_token(self) -> RoomStreamToken:
        """Converts the position to a room stream token such that events
        persisted in the same room after this position will be after the
        returned `RoomStreamToken`.

        Note: no guarentees are made about ordering w.r.t. events in other
        rooms.
        """
        # Doing the naive thing satisfies the desired properties described in
        # the docstring.
        return RoomStreamToken(None, self.stream)


class ThirdPartyInstanceID(
    namedtuple("ThirdPartyInstanceID", ("appservice_id", "network_id"))
):
    # Deny iteration because it will bite you if you try to create a singleton
    # set by:
    #    users = set(user)
    def __iter__(self):
        raise ValueError("Attempted to iterate a %s" % (type(self).__name__,))

    # Because this class is a namedtuple of strings, it is deeply immutable.
    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

    @classmethod
    def from_string(cls, s):
        bits = s.split("|", 2)
        if len(bits) != 2:
            raise SynapseError(400, "Invalid ID %r" % (s,))

        return cls(appservice_id=bits[0], network_id=bits[1])

    def to_string(self):
        return "%s|%s" % (self.appservice_id, self.network_id)

    __str__ = to_string

    @classmethod
    def create(cls, appservice_id, network_id):
        return cls(appservice_id=appservice_id, network_id=network_id)


@attr.s(slots=True)
class ReadReceipt:
    """Information about a read-receipt"""

    room_id = attr.ib()
    receipt_type = attr.ib()
    user_id = attr.ib()
    event_ids = attr.ib()
    data = attr.ib()


def get_verify_key_from_cross_signing_key(key_info):
    """Get the key ID and signedjson verify key from a cross-signing key dict

    Args:
        key_info (dict): a cross-signing key dict, which must have a "keys"
            property that has exactly one item in it

    Returns:
        (str, VerifyKey): the key ID and verify key for the cross-signing key
    """
    # make sure that exactly one key is provided
    if "keys" not in key_info:
        raise ValueError("Invalid key")
    keys = key_info["keys"]
    if len(keys) != 1:
        raise ValueError("Invalid key")
    # and return that one key
    for key_id, key_data in keys.items():
        return (key_id, decode_verify_key_bytes(key_id, decode_base64(key_data)))
