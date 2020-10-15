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
from .AmountDto import AmountDto
from .EntityTypeDto import EntityTypeDto
from .KeyDto import KeyDto
from .LinkActionDto import LinkActionDto
from .NetworkTypeDto import NetworkTypeDto
from .NodeKeyLinkTransactionBodyBuilder import NodeKeyLinkTransactionBodyBuilder
from .SignatureDto import SignatureDto
from .TimestampDto import TimestampDto
from .TransactionBuilder import TransactionBuilder


class NodeKeyLinkTransactionBuilder(TransactionBuilder):
    """Binary layout for a non-embedded node key link transaction.

    Attributes:
        nodeKeyLinkTransactionBody: Node key link transaction body.
    """

    def __init__(self, size: int, signature: SignatureDto, signerPublicKey: KeyDto, version: int, network: NetworkTypeDto, type: EntityTypeDto, fee: AmountDto, deadline: TimestampDto, linkedPublicKey: KeyDto, linkAction: LinkActionDto):
        """Constructor.
        Args:
            size: Entity size.
            signature: Entity signature.
            signerPublicKey: Entity signer's public key.
            version: Entity version.
            network: Entity network.
            type: Entity type.
            fee: Transaction fee.
            deadline: Transaction deadline.
            linkedPublicKey: Linked public key.
            linkAction: Link action.
        """
        super().__init__(size, signature, signerPublicKey, version, network, type, fee, deadline)
        self.nodeKeyLinkTransactionBody = NodeKeyLinkTransactionBodyBuilder(linkedPublicKey, linkAction)

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> NodeKeyLinkTransactionBuilder:
        """Creates an instance of NodeKeyLinkTransactionBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of NodeKeyLinkTransactionBuilder.
        """
        bytes_ = bytes(payload)
        superObject = TransactionBuilder.loadFromBinary(bytes_)
        bytes_ = bytes_[superObject.getSize():]
        nodeKeyLinkTransactionBody = NodeKeyLinkTransactionBodyBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[nodeKeyLinkTransactionBody.getSize():]
        return NodeKeyLinkTransactionBuilder(superObject.size, superObject.signature, superObject.signerPublicKey, superObject.version, superObject.network, superObject.type, superObject.fee, superObject.deadline, nodeKeyLinkTransactionBody.linkedPublicKey, nodeKeyLinkTransactionBody.linkAction)

    def getLinkedPublicKey(self) -> KeyDto:
        """Gets linked public key.
        Returns:
            Linked public key.
        """
        return self.nodeKeyLinkTransactionBody.getLinkedPublicKey()

    def getLinkAction(self) -> LinkActionDto:
        """Gets link action.
        Returns:
            Link action.
        """
        return self.nodeKeyLinkTransactionBody.getLinkAction()

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = super().getSize()
        size += self.nodeKeyLinkTransactionBody.getSize()
        return size

    def getBody(self) -> NodeKeyLinkTransactionBodyBuilder:
        """Gets the body builder of the object.
        Returns:
            Body builder.
        """
        return self.nodeKeyLinkTransactionBody

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, super().serialize())
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.nodeKeyLinkTransactionBody.serialize())  # kind:CUSTOM
        return bytes_
