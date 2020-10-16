import os

import attr

from isilon.api import Accounts, Containers, Discoverability, Endpoints, Objects
from isilon.creds import Credentials
from isilon.http import Http


@attr.s
class IsilonClient:
    address = attr.ib(
        type=str,
        default=os.getenv("ISILON_ADDRESS", "http://localhost:8080"),
        validator=attr.validators.instance_of(str),
    )
    account = attr.ib(
        type=str,
        default=os.getenv("ISILON_ACCOUNT", "test"),
        validator=attr.validators.instance_of(str),
    )
    user = attr.ib(
        type=str,
        default=os.getenv("ISILON_USER", "tester"),
        validator=attr.validators.instance_of(str),
    )
    password = attr.ib(
        type=str,
        default=os.getenv("ISILON_PASSWORD", "testing"),
        validator=attr.validators.instance_of(str),
    )

    def __attrs_post_init__(self):
        http = Http()
        self.credentials = Credentials(http, self.account, self.user, self.password)
        self.objects = Objects(http, self.address, self.credentials)
        self.discoverability = Discoverability(http, self.address, self.credentials)
        self.containers = Containers(http, self.address, self.credentials)
        self.endpoints = Endpoints(http, self.address, self.credentials)
        self.accounts = Accounts(http, self.address, self.credentials)
