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


class VotingKeyDto:
    """Voting key.

    Attributes:
        votingKey: Voting key.
    """

    def __init__(self, votingKey: bytes):
        """Constructor.

        Args:
            votingKey: Voting key.
        """
        self.votingKey = votingKey

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> VotingKeyDto:
        """Creates an instance of VotingKeyDto from binary payload.

        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of VotingKeyDto.
        """
        bytes_ = bytes(payload)
        votingKey = GeneratorUtils.getBytes(bytes_, 48)
        return VotingKeyDto(votingKey)

    @classmethod
    def getSize(cls) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        return 48

    def getVotingKey(self) -> bytes:
        """Gets Voting key.

        Returns:
            Voting key.
        """
        return self.votingKey

    def serialize(self) -> bytes:
        """Serializes self to bytes.

        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.votingKey)
        return bytes_
