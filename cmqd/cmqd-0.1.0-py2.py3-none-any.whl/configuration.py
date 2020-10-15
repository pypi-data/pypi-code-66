from pathlib import PurePath
import logging


class Configuration:
    username = None

    password = None

    credentials = None

    url = "https://api.clearmacro.com"

    logger = logging.getLogger("clearmacro")

    # True, False or path to CA Bundle file
    ssl_verify = True

    # None or a single file (containing the private key and
    # the certificate) or as a tuple of both files’ paths
    cert_file = None

    debug = False

    timeout = 30

    def __init__(self, **config):
        for key, value in config.items():
            setattr(self, key, value)

    def request_params(self):
        auth = {}

        if (self.credentials is not None):
            auth = {
                'authorization': 'Bearer {}'.format(self.credentials.get('access_token'))
            }

        params = {
            'timeout': self.timeout,
            'verify': self.ssl_verify,
            'headers': {
                **auth,
                'content-type': 'application/json',
                'accept': 'application/json',
            }
        }

        if self.cert_file:
            params['cert'] = self.cert_file

        return params
