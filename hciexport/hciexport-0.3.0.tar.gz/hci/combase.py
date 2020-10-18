# The MIT License (MIT)
#
# Copyright (c) 2020 Thorsten Simons (sw@snomis.eu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import httpx
import ssl
import json
import sys
from typing import List


class ApiConBase():
    """
    A class representing a virtual session with HCI.
    Use to subclass for your specific needs.
    """
    def __init__(self, hci: str, grant_type: str, user: str, password: str,
                 client_secret: str, client_id: str, realm: str,
                 pkgname: str='', pkgdesc: str='') -> None:
        """
        param hci:  the HCIs FQDN
        """
        self.hci = hci
        self.grant_type = grant_type
        self.user = user
        self.password = password
        self.client_secret = client_secret
        self.client_id = client_id
        self.realm = realm
        self.pkgname = pkgname
        self.pkgdesc = pkgdesc

        self.__connect()
        self.__authenticate()

    def __connect(self):
        """
        Open a requests Session towards HCI.
        """

        # setup a non-verifying SSL-context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.verify_mode = ssl.CERT_NONE
        context.check_hostname = False

        self.client = httpx.Client(base_url=self.hci,
                                   verify=context,
                                   timeout=60.0,
                                   headers={'Accept': 'application/json',
                                            'Content-Type': 'application/x-www-form-urlencoded'}
                                   )


    def __authenticate(self) -> None:
        """
        Connect to the given HCI.
        (Create an access token)
        """
        printstep('\tauthentication', 40)

        r = self.client.post('/auth/oauth',
                                 params={'grant_type': self.grant_type,
                                         'username': self.user,
                                         'password': self.password,
                                         'client_secret': self.client_secret,
                                         'client_id': self.client_id,
                                         'realm': self.realm}
                                 )

        if r.status_code == 200:
            self.client.headers['Authorization'] = f'Bearer {r.json()["access_token"]}'
            self.client.headers['Content-Type'] = 'application/json'
            print('OK')
        else:
            print()
            sys.exit(f'fatal: acquiring an access token failed - http {r.status_code}')


def printstep(txt, width):
    """
    Print a text, filling with spaces to width and no LF.
    """
    print(f'{txt+":":{width}} ', end='')