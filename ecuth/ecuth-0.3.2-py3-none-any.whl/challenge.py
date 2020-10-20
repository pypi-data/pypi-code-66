# standard imports
import uuid
import logging
import time
import eth_keys
import hashlib

# third-party imports
from ecuth.base import Retriever, source_hash
from ecuth.error import ChallengeError

logg = logging.getLogger()

DEFAULT_CHALLENGE_EXPIRE = 10


class AuthChallenge:
    """Minimal convenience object representing an authentication challenge.

    :param ip: IP address of client
    :type p: str
    :param filters: List of filter methods to be executed on a challenge when apply_filters is called.
    :type filters: function, taking a single byte-string argument, returning a byte-string.
    """
    def __init__(self, ip, filters):
        self.ip = ip
        self.challenge = None
        self.challenge_expire = 0
        self.filter = filters


    def request(self):
        """Creates a new challenge.

        :return: Challenge value
        :rtype: bytes
        """
        uu = uuid.uuid4()
        self.challenge = uu.bytes
        self.challenge_expire = time.time() + DEFAULT_CHALLENGE_EXPIRE
        return (self.challenge, self.challenge_expire,)


    # TODO: the filters should be applied on the stored challenge. If a stateless transformation is needed, this method should be made static instead.
    def apply_filters(self, s):
        """Executes the challenge transformation filters on the given challenge.

        This does not modify the original challenge already stored in the instance.
        
        :param s: Challenge to transform.
        :type s: bytes
        :return: Fitered challenge value
        :rtype: bytes
        """
        for f in self.filter:
            logg.debug('applying filter {}'.format(f[0]))
            s = f[1](s)
        return s


    def clear(self):
        """Clears existing challenge data.
        """
        self.challenge = None
        self.challenge_expire = 0



class ChallengeRetriever(Retriever):
    """Extension of retirever implementing public-key challenge response.

    Provides stackable transformation filters to match challenge transformations on client end.

    :param fetcher: Retrieves authentication info for authentication digest
    :type fetcher: function
    :param parser: Object capable of parsing authentication info returned from fetcher to return an ACL object
    :type parser: class
    :param resolver: Retrieves authentication digest from challenge and signature.
    :type resolver: function
    """
    def __init__(self, fetcher, parser, resolver):
        super(ChallengeRetriever, self).__init__(fetcher, parser)
        self.challenge_filter = []
        self.challenge_filter_index = {}
        self.auth = {}
        self.resolver = resolver


    def clear(self, address):
        """Remove all session data.

        :param address: Ethereum address of user
        :type address: str, 0x-hex
        """
        if self.auth.get(address) != None:
            del self.auth[address]
        super(ChallengeRetriever, self).clear(address)


    def add_filter(self, filter, name=None):
        """Add a challenge transformation filter.

        :param filter: Filter method  to add
        :type filter: function
        :param name: Arbitrary filter name
        :type name: str
        """
        if not callable(filter):
            raise ValueError('filter must be callable')
        if name == None:
            name = filter.__name__
        if self.challenge_filter_index.get(name) != None:
            idx = self.challenge_filter_index[name]
            logg.info('resetting challenge filter {} on index {}'.format(name, idx))
            self.challenge_filter[idx][1] = filter
        else:
            self.challenge_filter_index[name] = len(self.challenge_filter)
            self.challenge_filter.append((name, filter,))


    def challenge(self, ip):
        """Generate a new challenge string for user address. This must be signed by the corresponding private key of the address.

        :param address: Ethereum address of user
        :type address: str, 0x-hex
        :return: Challenge token
        """
        c = AuthChallenge(ip, self.challenge_filter)
        (nonce, expire) = c.request()
        k = source_hash(ip, nonce)
        self.auth[k] = c
        logg.info('generated new challenge {} expires {}'.format(nonce.hex(), expire))
        return (nonce, expire,)


    def validate(self, ip, challenge_user, signature):
        """Validation of challenge signature. Passes the provided and original (unfiltered) challenge to the resolver. Note that it is the resolver's 

        :param challenge: Actual challenge data signed by user
        :type challenge: bytes
        :param signature: Challenge signature 
        :type signature: bytes
        :raises ecuth.error.ChallengeError: Challenge not found for address, or signature could not be verified.
        :raises urllib.error.URLError: Invalid fetch URL 
        :raises http.client.RemoteDisconnected: HTTP Connection exception
        :return: Refresh token and authentication token, respectively
        :rtype: tuple of bytestrings
        """
        # retrieve the challenge value
        challenge_key = source_hash(ip, challenge_user)
        challenge_object = self.auth[challenge_key]

        challenge_compare = challenge_object.apply_filters(challenge_user)
        challenge_correct = challenge_object.challenge
        if challenge_correct == None:
            raise ChallengeError('no challenge exists for address {}'.format(address))
        if challenge_correct != challenge_user:
            raise ChallengeError('challenge mismatch')

        address = self.resolver(challenge_compare, signature)
        logg.debug('challenge: {} address {}'.format(challenge_user.hex(), address.hex()))

        # at this point successful authentication, challenge can be removed.
        self.auth[challenge_key].clear()
        return address
