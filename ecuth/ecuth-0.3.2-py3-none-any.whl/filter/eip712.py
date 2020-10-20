# standard imports
import logging

# third-party imports
import eip712_structs

logg = logging.getLogger()


class Challenge(eip712_structs.EIP712Struct):
    """Overloaded EIP712Struct class, to define a single 'challenge' schema item of type 'Bytes'
    """
    challenge = eip712_structs.Bytes()


class EIP712Filter:
    """Provides a filter to the SimpleResolver implmentation, in order to transform a challenge to signature material wrapped by the EIP712 standard.

    :param name: The EIP712 name parameter
    :type name: str
    :param version: The EIP712 version parameter
    :type version: str
    :param chain_id: The EIP712 chainId parameter
    :type chain_id: str
    """
    def __init__(self, name, version, chain_id):
        self.name = name
        self.version = version
        self.chain_id = chain_id


    def filter(self, s):
        """Filter to execute on the challengedata

        :param s: Challenge data
        :type s: bytes
        :return: Transformed challenge data
        :rtype: bytes
        """
        c = Challenge()
        c['challenge'] = s
        d = eip712_structs.make_domain(
                name=self.name,
                version=self.version,
                chainId=self.chain_id,
                )
        z = c.signable_bytes(d)
        logg.debug('eip712 filter {} -> {}'.format(s.hex(), z.hex()))
        return z
