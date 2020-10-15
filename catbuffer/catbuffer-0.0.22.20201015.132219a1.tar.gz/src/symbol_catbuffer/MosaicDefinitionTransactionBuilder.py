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
from typing import List
from .GeneratorUtils import GeneratorUtils
from .AmountDto import AmountDto
from .BlockDurationDto import BlockDurationDto
from .EntityTypeDto import EntityTypeDto
from .KeyDto import KeyDto
from .MosaicDefinitionTransactionBodyBuilder import MosaicDefinitionTransactionBodyBuilder
from .MosaicFlagsDto import MosaicFlagsDto
from .MosaicIdDto import MosaicIdDto
from .MosaicNonceDto import MosaicNonceDto
from .NetworkTypeDto import NetworkTypeDto
from .SignatureDto import SignatureDto
from .TimestampDto import TimestampDto
from .TransactionBuilder import TransactionBuilder


class MosaicDefinitionTransactionBuilder(TransactionBuilder):
    """Binary layout for a non-embedded mosaic definition transaction.

    Attributes:
        mosaicDefinitionTransactionBody: Mosaic definition transaction body.
    """

    def __init__(self, size: int, signature: SignatureDto, signerPublicKey: KeyDto, version: int, network: NetworkTypeDto, type: EntityTypeDto, fee: AmountDto, deadline: TimestampDto, id: MosaicIdDto, duration: BlockDurationDto, nonce: MosaicNonceDto, flags: List[MosaicFlagsDto], divisibility: int):
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
            id: Mosaic identifier.
            duration: Mosaic duration.
            nonce: Mosaic nonce.
            flags: Mosaic flags.
            divisibility: Mosaic divisibility.
        """
        super().__init__(size, signature, signerPublicKey, version, network, type, fee, deadline)
        self.mosaicDefinitionTransactionBody = MosaicDefinitionTransactionBodyBuilder(id, duration, nonce, flags, divisibility)

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> MosaicDefinitionTransactionBuilder:
        """Creates an instance of MosaicDefinitionTransactionBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of MosaicDefinitionTransactionBuilder.
        """
        bytes_ = bytes(payload)
        superObject = TransactionBuilder.loadFromBinary(bytes_)
        bytes_ = bytes_[superObject.getSize():]
        mosaicDefinitionTransactionBody = MosaicDefinitionTransactionBodyBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[mosaicDefinitionTransactionBody.getSize():]
        return MosaicDefinitionTransactionBuilder(superObject.size, superObject.signature, superObject.signerPublicKey, superObject.version, superObject.network, superObject.type, superObject.fee, superObject.deadline, mosaicDefinitionTransactionBody.id, mosaicDefinitionTransactionBody.duration, mosaicDefinitionTransactionBody.nonce, mosaicDefinitionTransactionBody.flags, mosaicDefinitionTransactionBody.divisibility)

    def getId(self) -> MosaicIdDto:
        """Gets mosaic identifier.
        Returns:
            Mosaic identifier.
        """
        return self.mosaicDefinitionTransactionBody.getId()

    def getDuration(self) -> BlockDurationDto:
        """Gets mosaic duration.
        Returns:
            Mosaic duration.
        """
        return self.mosaicDefinitionTransactionBody.getDuration()

    def getNonce(self) -> MosaicNonceDto:
        """Gets mosaic nonce.
        Returns:
            Mosaic nonce.
        """
        return self.mosaicDefinitionTransactionBody.getNonce()

    def getFlags(self) -> List[MosaicFlagsDto]:
        """Gets mosaic flags.
        Returns:
            Mosaic flags.
        """
        return self.mosaicDefinitionTransactionBody.getFlags()

    def getDivisibility(self) -> int:
        """Gets mosaic divisibility.
        Returns:
            Mosaic divisibility.
        """
        return self.mosaicDefinitionTransactionBody.getDivisibility()

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = super().getSize()
        size += self.mosaicDefinitionTransactionBody.getSize()
        return size

    def getBody(self) -> MosaicDefinitionTransactionBodyBuilder:
        """Gets the body builder of the object.
        Returns:
            Body builder.
        """
        return self.mosaicDefinitionTransactionBody

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, super().serialize())
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.mosaicDefinitionTransactionBody.serialize())  # kind:CUSTOM
        return bytes_
