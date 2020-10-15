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
from .EmbeddedTransactionHeaderBuilder import EmbeddedTransactionHeaderBuilder
from .EntityTypeDto import EntityTypeDto
from .KeyDto import KeyDto
from .NetworkTypeDto import NetworkTypeDto


class EmbeddedTransactionBuilder(EmbeddedTransactionHeaderBuilder):
    """Binary layout for an embedded transaction.

    Attributes:
        signerPublicKey: Entity signer's public key.
        entityBody_Reserved1: Reserved padding to align end of EntityBody on 8-byte boundary.
        version: Entity version.
        network: Entity network.
        type: Entity type.
    """

    def __init__(self, size: int, signerPublicKey: KeyDto, version: int, network: NetworkTypeDto, type: EntityTypeDto):
        """Constructor.
        Args:
            size: Entity size.
            signerPublicKey: Entity signer's public key.
            version: Entity version.
            network: Entity network.
            type: Entity type.
        """
        super().__init__(size)
        self.signerPublicKey = signerPublicKey
        self.entityBody_Reserved1 = 0
        self.version = version
        self.network = network
        self.type = type

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> EmbeddedTransactionBuilder:
        """Creates an instance of EmbeddedTransactionBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of EmbeddedTransactionBuilder.
        """
        bytes_ = bytes(payload)
        superObject = EmbeddedTransactionHeaderBuilder.loadFromBinary(bytes_)
        bytes_ = bytes_[superObject.getSize():]
        signerPublicKey = KeyDto.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[signerPublicKey.getSize():]
        entityBody_Reserved1 = GeneratorUtils.bufferToUint(GeneratorUtils.getBytes(bytes_, 4))  # kind:SIMPLE
        bytes_ = bytes_[4:]
        version = GeneratorUtils.bufferToUint(GeneratorUtils.getBytes(bytes_, 1))  # kind:SIMPLE
        bytes_ = bytes_[1:]
        network = NetworkTypeDto.loadFromBinary(bytes_)  # kind:CUSTOM2
        bytes_ = bytes_[network.getSize():]
        type = EntityTypeDto.loadFromBinary(bytes_)  # kind:CUSTOM2
        bytes_ = bytes_[type.getSize():]
        return EmbeddedTransactionBuilder(superObject.size, signerPublicKey, version, network, type)

    def getSignerPublicKey(self) -> KeyDto:
        """Gets entity signer's public key.
        Returns:
            Entity signer's public key.
        """
        return self.signerPublicKey

    def getEntityBody_Reserved1(self) -> int:
        """Gets reserved padding to align end of EntityBody on 8-byte boundary.
        Returns:
            Reserved padding to align end of EntityBody on 8-byte boundary.
        """
        return self.entityBody_Reserved1

    def getVersion(self) -> int:
        """Gets entity version.
        Returns:
            Entity version.
        """
        return self.version

    def getNetwork(self) -> NetworkTypeDto:
        """Gets entity network.
        Returns:
            Entity network.
        """
        return self.network

    def getType(self) -> EntityTypeDto:
        """Gets entity type.
        Returns:
            Entity type.
        """
        return self.type

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = super().getSize()
        size += self.signerPublicKey.getSize()
        size += 4  # entityBody_Reserved1
        size += 1  # version
        size += self.network.getSize()
        size += self.type.getSize()
        return size

    def getBody(self) -> None:
        """Gets the body builder of the object.
        Returns:
            Body builder.
        """
        return None

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, super().serialize())
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.signerPublicKey.serialize())  # kind:CUSTOM
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, GeneratorUtils.uintToBuffer(self.getEntityBody_Reserved1(), 4))  # kind:SIMPLE
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, GeneratorUtils.uintToBuffer(self.getVersion(), 1))  # kind:SIMPLE
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.network.serialize())  # kind:CUSTOM
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.type.serialize())  # kind:CUSTOM
        return bytes_
