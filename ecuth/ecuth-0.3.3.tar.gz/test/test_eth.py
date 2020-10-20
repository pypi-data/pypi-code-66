# standard imports
import os
import unittest
import logging
import hashlib

# third-party imports
import gnupg
import eth_keys
import confini

# local imports
import ecuth
from ecuth.error import ChallengeError
from ecuth.error import TokenExpiredError
from ecuth.error import SessionExpiredError
from ecuth.error import SessionError
#from ecuth.digest import DigestRetriever
from ecuth.ext.eth import EthereumRetriever
from ecuth.challenge import source_hash
from ecuth.filter.eip712 import EIP712Filter
from ecuth.acl.yaml import YAMLAcl

logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
gpg_dir = os.path.join(root_dir, '.gnupg')
logg.debug('gpg dir {}'.format(gpg_dir))
gpg = gnupg.GPG(gnupghome=gpg_dir)


def sha1filter(s):
    logg.debug('object {}'.format(s))
    h = hashlib.sha1()
    h.update(s)
    z = h.digest()
    logg.debug('shafilter {} -> {}'.format(s.hex(), z.hex()))
    return z


# GNUPG data pluggable test decrypter
def decrypter(data):
    d = gpg.decrypt(data, passphrase='tralala')
    if d.trust_level < d.TRUST_FULLY:
        raise ValueError('untrusted data')
    logg.debug('trust {}'.format(d.trust_level))
    return str(d)


# fetch from file for test
def fetcher(address=None):
    f = open(os.path.join(root_dir, 'test', 'data', address.hex()), 'rb')
    d = f.read(1024*1024)
    f.close()
    return decrypter(d)


class TestCore(unittest.TestCase):

    config = confini.Config(os.path.join(root_dir, 'config'))

    def setUp(self):
        self.config.process()
        self.config.require('NAME', 'EIP712')
        self.config.require('VERSION', 'EIP712')
        self.config.require('BASE_URL', 'ECUTH')
        self.config.require('CHAIN_ID', 'ECUTH')
        self.config.validate()


    def tearDown(self):
        pass


    def test_basic(self):
        r = EthereumRetriever(fetcher, YAMLAcl)
        pk_bytes = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000005')
        pk = eth_keys.keys.PrivateKey(pk_bytes)
        address = pk.public_key.to_checksum_address() # 0xe1AB8145F7E55DC933d51a18c793F901A3A0b276

        # wrong challenge
        ip = '127.0.0.1'
        (c, expire) = r.challenge(ip)
        challenge_key = source_hash(ip, c)
        r.auth[challenge_key].challenge = pk_bytes
        signature = pk.sign_msg(c)
        with self.assertRaises(ChallengeError):
            r.validate(ip, c, signature)

        # correct challenge
        (c, expire) = r.challenge(ip)
        signature = pk.sign_msg(c)
        auth = r.validate(ip, c, signature)
        session = r.load(auth)
        self.assertTrue(session.read('ussd.session'))
        self.assertFalse(session.write('ussd.session'))
        self.assertFalse(session.read('ussd.pin'))
        self.assertTrue(session.write('ussd.pin'))

        # verify reverse lookup
        r.check(session.auth)

        # invalidate auth token
        session.auth_expire = 0
        with self.assertRaises(TokenExpiredError):
            self.assertTrue(session.read('ussd.session'))

        token = r.renew(auth, session.refresh)
        self.assertTrue(session.read('ussd.session'))

        # invalidate refresh token
        session.refresh_expire = 0
        session.auth_expire = 0
        with self.assertRaises(SessionExpiredError):
            r.renew(auth, session.refresh)
             

    def test_eip712(self):
        r = EthereumRetriever(fetcher, YAMLAcl)
        eip712_filter = EIP712Filter(self.config.get('EIP712_NAME'), self.config.get('EIP712_VERSION'), self.config.get('ECUTH_CHAIN_ID'))
        r.add_filter(eip712_filter.filter, 'eip712')

        pk_bytes = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000005')
        pk = eth_keys.keys.PrivateKey(pk_bytes)
        address = pk.public_key.to_checksum_address()

        ip = '127.0.0.1'
        (c, expire) = r.challenge(ip)
        k = source_hash(ip, c)

        # signing the nonce only will not work
        eip712_c = eip712_filter.filter(c)
        signature = pk.sign_msg(c)
        a = r.validate(ip, c, signature)
        with self.assertRaises(FileNotFoundError):
            r.load(a)

        # signing the eip712 structure is ok
        (c, expire) = r.challenge(ip)
        k = source_hash(ip, c)
        eip712_c = eip712_filter.filter(c)
        signature = pk.sign_msg(eip712_c)
        a = r.validate(ip, c, signature)
        s = r.load(a)

    
    @unittest.skip('needs update after refactor')
    def test_multi_filters(self):
        r = DigestRetriever(fetcher, YAMLAcl)
        r.add_filter(sha1filter, 'sha1')
        eip712_filter = EIP712Filter(self.config.get('EIP712_NAME'), self.config.get('EIP712_VERSION'), self.config.get('ECUTH_CHAIN_ID'))
        r.add_filter(eip712_filter.filter, 'eip712')

        pk_bytes = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000005')
        pk = eth_keys.keys.PrivateKey(pk_bytes)
        address = pk.public_key.to_checksum_address()

        ip = '127.0.0.1'
        (c, expire) = r.challenge(ip)
        k = source_hash(ip, c)
        signature = pk.sign_msg(c)
        a = r.validate(ip, c, signature)
        with self.assertRaises(FileNotFoundError):
            r.load(a)

        (c, expire) = r.challenge(ip)
        k = source_hash(ip, c)
        logg.debug('challenge {}'.format(c))
        filtered_c = sha1filter(c)
        signature = pk.sign_msg(filtered_c)

        with self.assertRaises(FileNotFoundError):
            r.load(ip, c, signature)

        (c, expire) = r.challenge(ip)
        k = source_hash(ip.encode('utf-8'), c)
        logg.debug('challenge {}'.format(c))
        first_filtered_c = sha1filter(c)
        second_filtered_c = eip712_filter.filter(first_filtered_c)
        signature = pk.sign_msg(second_filtered_c)
        (refresh, auth, expire) = r.load(ip, c, signature)


if __name__ == '__main__':
    unittest.main()
