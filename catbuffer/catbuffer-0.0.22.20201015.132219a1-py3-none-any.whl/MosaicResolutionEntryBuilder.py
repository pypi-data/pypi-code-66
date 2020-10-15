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
from .MosaicIdDto import MosaicIdDto
from .ReceiptSourceBuilder import ReceiptSourceBuilder


class MosaicResolutionEntryBuilder:
    """Binary layout for mosaic resolution entry.

    Attributes:
        source: Source of resolution within block.
        resolved: Resolved value.
    """

    def __init__(self, source: ReceiptSourceBuilder, resolved: MosaicIdDto):
        """Constructor.
        Args:
            source: Source of resolution within block.
            resolved: Resolved value.
        """
        self.source = source
        self.resolved = resolved

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> MosaicResolutionEntryBuilder:
        """Creates an instance of MosaicResolutionEntryBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of MosaicResolutionEntryBuilder.
        """
        bytes_ = bytes(payload)
        source = ReceiptSourceBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[source.getSize():]
        resolved = MosaicIdDto.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[resolved.getSize():]
        return MosaicResolutionEntryBuilder(source, resolved)

    def getSource(self) -> ReceiptSourceBuilder:
        """Gets source of resolution within block.
        Returns:
            Source of resolution within block.
        """
        return self.source

    def getResolved(self) -> MosaicIdDto:
        """Gets resolved value.
        Returns:
            Resolved value.
        """
        return self.resolved

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = 0
        size += self.source.getSize()
        size += self.resolved.getSize()
        return size

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.source.serialize())  # kind:CUSTOM
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.resolved.serialize())  # kind:CUSTOM
        return bytes_
