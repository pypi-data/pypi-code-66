# standard imports
import logging

# third-party imports
import http_hoba_auth

logg = logging.getLogger()


class HobaFilter(http_hoba_auth.Hoba):
    """Provider a filter to generate signature material specified for HOBA specified in RFC 7496.

    :param s: Value to transform
    :type s: bytes
    :raises ValueError: If supplied value does not match the stored the challenge already stored in the hoba instance. This is an interface anomaly, and should probably be revisited.
    :return: Transformed value
    :rtype: bytes
    """
    def filter(self, s):
        if self.challenge != s:
            logg.error('challenge mismatch {} != {}'.format(self.challenge.hex(), s.hex()))
            raise ValueError('challenge mismatch')
        tbs = self.to_be_signed()
        logg.debug('hoba filter {} -> {}'.format(s, tbs))
        return tbs.encode('utf-8')
