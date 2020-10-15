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
from .MosaicRestrictionTypeDto import MosaicRestrictionTypeDto


class RestrictionRuleBuilder:
    """Binary layout of restriction rule being applied.

    Attributes:
        referenceMosaicId: Identifier of the mosaic providing the restriction key.
        restrictionValue: Restriction value.
        restrictionType: Restriction type.
    """

    def __init__(self, referenceMosaicId: MosaicIdDto, restrictionValue: int, restrictionType: MosaicRestrictionTypeDto):
        """Constructor.
        Args:
            referenceMosaicId: Identifier of the mosaic providing the restriction key.
            restrictionValue: Restriction value.
            restrictionType: Restriction type.
        """
        self.referenceMosaicId = referenceMosaicId
        self.restrictionValue = restrictionValue
        self.restrictionType = restrictionType

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> RestrictionRuleBuilder:
        """Creates an instance of RestrictionRuleBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of RestrictionRuleBuilder.
        """
        bytes_ = bytes(payload)
        referenceMosaicId = MosaicIdDto.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[referenceMosaicId.getSize():]
        restrictionValue = GeneratorUtils.bufferToUint(GeneratorUtils.getBytes(bytes_, 8))  # kind:SIMPLE
        bytes_ = bytes_[8:]
        restrictionType = MosaicRestrictionTypeDto.loadFromBinary(bytes_)  # kind:CUSTOM2
        bytes_ = bytes_[restrictionType.getSize():]
        return RestrictionRuleBuilder(referenceMosaicId, restrictionValue, restrictionType)

    def getReferenceMosaicId(self) -> MosaicIdDto:
        """Gets identifier of the mosaic providing the restriction key.
        Returns:
            Identifier of the mosaic providing the restriction key.
        """
        return self.referenceMosaicId

    def getRestrictionValue(self) -> int:
        """Gets restriction value.
        Returns:
            Restriction value.
        """
        return self.restrictionValue

    def getRestrictionType(self) -> MosaicRestrictionTypeDto:
        """Gets restriction type.
        Returns:
            Restriction type.
        """
        return self.restrictionType

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = 0
        size += self.referenceMosaicId.getSize()
        size += 8  # restrictionValue
        size += self.restrictionType.getSize()
        return size

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.referenceMosaicId.serialize())  # kind:CUSTOM
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, GeneratorUtils.uintToBuffer(self.getRestrictionValue(), 8))  # kind:SIMPLE
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.restrictionType.serialize())  # kind:CUSTOM
        return bytes_
