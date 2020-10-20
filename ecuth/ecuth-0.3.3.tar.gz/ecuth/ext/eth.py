# standard imports
import logging

# third-party imports
import eth_keys

# local imports
from ecuth.challenge import ChallengeRetriever, source_hash

logg = logging.getLogger()


def signature_patch_v(signature_bytes):
    """Python package eth-keys returns recovery byte 00-01 instead of the eth standard 27-28. This patches any incoming 'correct' signature to the local 'incorrect' one.

    :params signature_bytes: Raw signature
    :type signature_bytes: bytes
    :return: Patched signature
    :rtype: Bytes
    """
    m = signature_bytes[64] % 27
    patched_signature_bytes = signature_bytes[:64] + bytes([m])
    return patched_signature_bytes


class EthereumRetriever(ChallengeRetriever):
    """A single-url retriever for the ACL list.

    Will attempt to retrieve an ACL list from a file matching the 0x-prefixed hex string at the base_url given at construction time.

    """
    def __init__(self, fetcher, parser):
        super(EthereumRetriever, self).__init__(fetcher, parser, self._address_from_challenge_response)
   

    def _address_from_challenge_response(self, challenge, signature):
        """Verifies and recovers public key and address for the signature and challenge. 

        :param challenge: Challenge data signed by user
        :type challenge: bytes
        :param signature: Challenge signature 
        :type signature: bytes
        :return: Recovered address
        :rtype: bytes
        """
        # Make sure signature has v byte understood by eth-keys package
        signature_patched_bytes = signature_patch_v(signature)
        signature_patched = eth_keys.datatypes.Signature(signature_bytes=signature_patched_bytes)

        pubkey = signature_patched.recover_public_key_from_msg(challenge)
        address = pubkey.to_checksum_address()
        logg.debug('address >>>>>>> {}'.format(address))
        address_bytes = bytes.fromhex(address[2:])
        return address_bytes
