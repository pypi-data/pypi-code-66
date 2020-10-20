# standard import
import unittest
import logging
import os
import time

# third-party imports
import gnupg
import confini
import eth_keys

# local imports
from ecuth.filter.hoba import HobaFilter
import ecuth
from ecuth.error import ChallengeError
from ecuth.challenge import AuthChallenge, source_hash
from ecuth.acl.yaml import YAMLAcl
from ecuth.ext.eth import EthereumRetriever

logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()

auth_example = 'APAeYTSy7MGaALMr+hm1OzdHdAzA4se26p9WHMHXyVE=.5xIfu0aBxBPHS/31wf9i2mxR098=.MyliXAfcRKy/NO/QnhumoMWNhSvce+Sq8MQefVOlgNY=.TlzNAnX6fPX+MEV2wb+yl+M7HldmZ12wS7flIIZBbrQl41WoTB+E0qM4wB3I8sbIXaQx+gfLuKLx1Mb+k5pg3Bw='
root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
gpg_dir = os.path.join(root_dir, '.gnupg')
logg.debug('gpg dir {}'.format(gpg_dir))
gpg = gnupg.GPG(gnupghome=gpg_dir)


# fetch from file for test
def fetcher(address=None):
    f = open(os.path.join(root_dir, 'test', 'data', address.hex()), 'rb')
    d = f.read(1024*1024)
    f.close()
    return decrypter(d)


# GNUPG data pluggable test decrypter
def decrypter(data):
    d = gpg.decrypt(data, passphrase='tralala')
    if d.trust_level < d.TRUST_FULLY:
        raise ValueError('untrusted data')
    logg.debug('trust {}'.format(d.trust_level))
    return str(d)



class TestHoba(unittest.TestCase):

    config = confini.Config(os.path.join(root_dir, 'config'))

    def setUp(self):
        self.config.process()
        self.config.require('BASE_URL', 'ECUTH')
        self.config.require('AUTH_REALM', 'HTTP')
        self.config.require('AUTH_ORIGIN', 'HTTP')
        self.config.validate()


    def test_hoba(self):
        r = EthereumRetriever(fetcher, YAMLAcl)
        hoba = HobaFilter('http://localhost:5555', 'GE', 'secp256k1')
        hoba.parse(auth_example)
        r.add_filter(hoba.filter, 'hoba')

        pk_bytes = bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000005')
        pk = eth_keys.keys.PrivateKey(pk_bytes)
        address = pk.public_key.to_checksum_address() # 0xe1AB8145F7E55DC933d51a18c793F901A3A0b276

        # wrong challenge
        ip = '127.0.0.1'
        (c, expire) = r.challenge(ip)
        challenge_key = source_hash(ip, c)   
        r.auth[challenge_key].challenge = pk_bytes
        signature = pk.sign_msg(c)
        with self.assertRaises(ValueError):
            a = r.validate(ip, c, signature)

        k = source_hash(ip, hoba.challenge)
        r.auth[k] = AuthChallenge(ip, r.challenge_filter)
        r.auth[k].challenge = hoba.challenge
        r.auth[k].challenge_expire = time.time() + 1
        tosign = hoba.to_be_signed()
        signature = pk.sign_msg(tosign.encode('utf-8'))
        logg.debug('tosign {} challenge {}'.format(signature, c))
        a = r.validate(ip, hoba.challenge, signature)
        r.load(a)


if __name__ == '__main__':
    unittest.main()
