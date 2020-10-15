#!/usr/bin/python
"""
    Copyright (c) 2016-present,
    Jaguar0625, gimre, BloodyRookie, Tech Bureau, Corp. All rights reserved.

    This file is part of Catapult.

    Catapult is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Catapult is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Catapult. If not, see <http://www.gnu.org/licenses/>.
"""

# pylint: disable=W0622,W0612,C0301,R0904

from __future__ import annotations
from .GeneratorUtils import GeneratorUtils
from .AccountKeyLinkTransactionBodyBuilder import AccountKeyLinkTransactionBodyBuilder
from .EmbeddedTransactionBuilder import EmbeddedTransactionBuilder
from .EntityTypeDto import EntityTypeDto
from .KeyDto import KeyDto
from .LinkActionDto import LinkActionDto
from .NetworkTypeDto import NetworkTypeDto


class EmbeddedAccountKeyLinkTransactionBuilder(EmbeddedTransactionBuilder):
    """Binary layout for an embedded account key link transaction.

    Attributes:
        accountKeyLinkTransactionBody: Account key link transaction body.
    """

    def __init__(self, size: int, signerPublicKey: KeyDto, version: int, network: NetworkTypeDto, type: EntityTypeDto, linkedPublicKey: KeyDto, linkAction: LinkActionDto):
        """Constructor.
        Args:
            size: Entity size.
            signerPublicKey: Entity signer's public key.
            version: Entity version.
            network: Entity network.
            type: Entity type.
            linkedPublicKey: Linked public key.
            linkAction: Link action.
        """
        super().__init__(size, signerPublicKey, version, network, type)
        self.accountKeyLinkTransactionBody = AccountKeyLinkTransactionBodyBuilder(linkedPublicKey, linkAction)

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> EmbeddedAccountKeyLinkTransactionBuilder:
        """Creates an instance of EmbeddedAccountKeyLinkTransactionBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of EmbeddedAccountKeyLinkTransactionBuilder.
        """
        bytes_ = bytes(payload)
        superObject = EmbeddedTransactionBuilder.loadFromBinary(bytes_)
        bytes_ = bytes_[superObject.getSize():]
        accountKeyLinkTransactionBody = AccountKeyLinkTransactionBodyBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[accountKeyLinkTransactionBody.getSize():]
        return EmbeddedAccountKeyLinkTransactionBuilder(superObject.size, superObject.signerPublicKey, superObject.version, superObject.network, superObject.type, accountKeyLinkTransactionBody.linkedPublicKey, accountKeyLinkTransactionBody.linkAction)

    def getLinkedPublicKey(self) -> KeyDto:
        """Gets linked public key.
        Returns:
            Linked public key.
        """
        return self.accountKeyLinkTransactionBody.getLinkedPublicKey()

    def getLinkAction(self) -> LinkActionDto:
        """Gets link action.
        Returns:
            Link action.
        """
        return self.accountKeyLinkTransactionBody.getLinkAction()

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = super().getSize()
        size += self.accountKeyLinkTransactionBody.getSize()
        return size

    def getBody(self) -> AccountKeyLinkTransactionBodyBuilder:
        """Gets the body builder of the object.
        Returns:
            Body builder.
        """
        return self.accountKeyLinkTransactionBody

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, super().serialize())
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.accountKeyLinkTransactionBody.serialize())  # kind:CUSTOM
        return bytes_
