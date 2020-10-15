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
from .AccountOperationRestrictionTransactionBodyBuilder import AccountOperationRestrictionTransactionBodyBuilder
from .AccountRestrictionFlagsDto import AccountRestrictionFlagsDto
from .AmountDto import AmountDto
from .EntityTypeDto import EntityTypeDto
from .KeyDto import KeyDto
from .NetworkTypeDto import NetworkTypeDto
from .SignatureDto import SignatureDto
from .TimestampDto import TimestampDto
from .TransactionBuilder import TransactionBuilder


class AccountOperationRestrictionTransactionBuilder(TransactionBuilder):
    """Binary layout for a non-embedded account operation restriction transaction.

    Attributes:
        accountOperationRestrictionTransactionBody: Account operation restriction transaction body.
    """

    def __init__(self, size: int, signature: SignatureDto, signerPublicKey: KeyDto, version: int, network: NetworkTypeDto, type: EntityTypeDto, fee: AmountDto, deadline: TimestampDto, restrictionFlags: List[AccountRestrictionFlagsDto], restrictionAdditions: List[EntityTypeDto], restrictionDeletions: List[EntityTypeDto]):
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
            restrictionFlags: Account restriction flags.
            restrictionAdditions: Account restriction additions.
            restrictionDeletions: Account restriction deletions.
        """
        super().__init__(size, signature, signerPublicKey, version, network, type, fee, deadline)
        self.accountOperationRestrictionTransactionBody = AccountOperationRestrictionTransactionBodyBuilder(restrictionFlags, restrictionAdditions, restrictionDeletions)

    @classmethod
    def loadFromBinary(cls, payload: bytes) -> AccountOperationRestrictionTransactionBuilder:
        """Creates an instance of AccountOperationRestrictionTransactionBuilder from binary payload.
        Args:
            payload: Byte payload to use to serialize the object.
        Returns:
            Instance of AccountOperationRestrictionTransactionBuilder.
        """
        bytes_ = bytes(payload)
        superObject = TransactionBuilder.loadFromBinary(bytes_)
        bytes_ = bytes_[superObject.getSize():]
        accountOperationRestrictionTransactionBody = AccountOperationRestrictionTransactionBodyBuilder.loadFromBinary(bytes_)  # kind:CUSTOM1
        bytes_ = bytes_[accountOperationRestrictionTransactionBody.getSize():]
        return AccountOperationRestrictionTransactionBuilder(superObject.size, superObject.signature, superObject.signerPublicKey, superObject.version, superObject.network, superObject.type, superObject.fee, superObject.deadline, accountOperationRestrictionTransactionBody.restrictionFlags, accountOperationRestrictionTransactionBody.restrictionAdditions, accountOperationRestrictionTransactionBody.restrictionDeletions)

    def getRestrictionFlags(self) -> List[AccountRestrictionFlagsDto]:
        """Gets account restriction flags.
        Returns:
            Account restriction flags.
        """
        return self.accountOperationRestrictionTransactionBody.getRestrictionFlags()

    def getRestrictionAdditions(self) -> List[EntityTypeDto]:
        """Gets account restriction additions.
        Returns:
            Account restriction additions.
        """
        return self.accountOperationRestrictionTransactionBody.getRestrictionAdditions()

    def getRestrictionDeletions(self) -> List[EntityTypeDto]:
        """Gets account restriction deletions.
        Returns:
            Account restriction deletions.
        """
        return self.accountOperationRestrictionTransactionBody.getRestrictionDeletions()

    def getSize(self) -> int:
        """Gets the size of the object.
        Returns:
            Size in bytes.
        """
        size = super().getSize()
        size += self.accountOperationRestrictionTransactionBody.getSize()
        return size

    def getBody(self) -> AccountOperationRestrictionTransactionBodyBuilder:
        """Gets the body builder of the object.
        Returns:
            Body builder.
        """
        return self.accountOperationRestrictionTransactionBody

    def serialize(self) -> bytes:
        """Serializes self to bytes.
        Returns:
            Serialized bytes.
        """
        bytes_ = bytes()
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, super().serialize())
        bytes_ = GeneratorUtils.concatTypedArrays(bytes_, self.accountOperationRestrictionTransactionBody.serialize())  # kind:CUSTOM
        return bytes_
