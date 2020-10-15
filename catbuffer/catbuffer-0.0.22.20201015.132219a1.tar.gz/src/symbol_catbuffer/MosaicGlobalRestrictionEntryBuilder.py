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
from .GlobalKeyValueSetBuilder import GlobalKeyValueSetBuilder
from .MosaicIdDto import MosaicIdDto


class MosaicGlobalRestrictionEntryBuilder:
    """Binary layout for a mosaic restriction.

    Attributes:
        mosaicId: Identifier of the mosaic to which the restriction applies.
        keyPairs: Global key value restriction set.
    """

    def __init__(self, mosaicId: MosaicIdDto, keyPairs: GlobalKeyValueSetBuilder):
        """Constructor.
        Args:
            mosaicId: Identifier of the mosaic to which the restriction applies.
            keyPairs: Global key value restriction set.
        """
        self.mosaicId = mosaicId
        self.keyPairs = keyPairs

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> MosaicGlobalRestrictionEntryBuilder:
        """Creates an instance of MosaicGlobalRestrictionEntryBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of MosaicGlobalRestrictionEntryBuilder.
        """
        bytes_ = bytes(payload)
        mosaicId = MosaicIdDto.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[mosaicId.getSize():]
        keyPairs = GlobalKeyValueSetBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[keyPairs.getSize():]
        return MosaicGlobalRestrictionEntryBuilder(mosaicId, keyPairs)

    def getMosaicId(self) -> MosaicIdDto:
        """Gets identifier of the mosaic to which the restriction applies.
        Returns:
            Identifier of the mosaic to which the restriction applies.
        """
        return self.mosaicId

    def getKeyPairs(self) -> GlobalKeyValueSetBuilder:
        """Gets global key value restriction set.
        Returns:
            Global key value restriction set.
        """
        return self.keyPairs

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = 0
        size += self.mosaicId.getSize()
        size += self.keyPairs.getSize()
        return size

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.mosaicId.serialize())  # kind:CUSTOM
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.keyPairs.serialize())  # kind:CUSTOM
        return bytes_
