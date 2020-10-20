# standard imports
import logging
import hashlib

from ecuth.session import Session

logg = logging.getLogger(__name__)


def source_hash(ip, data):
    """Creates a unique index value for a combination of (client) ip and challenge data.

    :param ip: IP address in text format, translated to bytes
    :type ip: bytes
    :param data: The data represented by the index
    :type data: bytes
    :return: Preimage of ip and data
    :rtype: bytes
    """
    h = hashlib.sha256()
    h.update(ip.encode('utf-8'))
    h.update(data)
    k = h.digest()
    return k


class Retriever:
    """Base implementation of ACL retriever

    :param fetcher: Retrieves authentication info for authentication digest
    :type fetcher: function
    :param parser: Object capable of parsing authentication info returned from fetcher to return an ACL object
    :type parser: class
    """
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.session = {}
        self.session_reverse = {}
        self.parser = parser


    def clear(self, identity):
        """Clear session from registry

        :param identity: Authorization digest of user
        :type identity: bytes
        """
        if self.session.get(identity) != None:
            del self.session[identity]


    def load(self, identity):
        """Retrieves ACL, initializes session and stores session in registry.

        :param identity: Authorization digest of user
        :type identity: bytes
        :return: New session
        :rtype: ecuth.Session
        """
        data = self.fetcher(identity)
        acl = self.parser(data)
       
        session = Session(identity, acl)
        self.session[identity] = session
        self.session_reverse[session.auth] = session
        self.renew(identity, session.refresh)

        logg.debug('added session {}'.format(session))

        return session


    def renew(self, address, refresh_token):
        """Renews an expired auth token.

        :param address: Ethereum address of user
        :type address: str, 0x-hex
        :raises ecuth.error.SessionExpiredError: Refresh token expired (must restart challenge)
        :return: New auth token
        :rtype: bytes
        """
        old_token = self.session[address].auth
        new_token = self.session[address].renew(refresh_token)
        self.session_reverse[new_token] = address
        if old_token != None:
            del self.session_reverse[old_token]
        return new_token 


    def check(self, address):
        return self.session_reverse[address]
