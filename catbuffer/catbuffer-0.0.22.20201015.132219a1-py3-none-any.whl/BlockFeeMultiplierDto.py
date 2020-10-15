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


class BlockFeeMultiplierDto:
    """Block fee multiplier.

    Attributes:
        blockFeeMultiplier: Block fee multiplier.
    """

    def __init__(self, blockFeeMultiplier: int):
        """Constructor.

        Args:
            blockFeeMultiplier: Block fee multiplier.
        """
        self.blockFeeMultiplier = blockFeeMultiplier

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> BlockFeeMultiplierDto:
        """Creates an instance of BlockFeeMultiplierDto from binary payload.

        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of BlockFeeMultiplierDto.
        """
        bytes_ = bytes(payload)
        blockFeeMultiplier = GeneratorUtils.bufferToUint(GeneratorUtils.getBytes(bytes_, 4))
        return BlockFeeMultiplierDto(blockFeeMultiplier)

    @classmethod
    def getSize(cls) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        return 4

    def getBlockFeeMultiplier(self) -> int:
        """Gets Block fee multiplier.

        Returns:
            Block fee multiplier.
        """
        return self.blockFeeMultiplier

    def serialize(self) -> bytes:
        """Serializes self to bytes.

        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, GeneratorUtils.uintToBuffer(self.getBlockFeeMultiplier(), 4))
        return bytes_
