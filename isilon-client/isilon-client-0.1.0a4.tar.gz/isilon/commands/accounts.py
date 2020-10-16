import asyncio
import json

from cleo import Command

from isilon.client import IsilonClient


class AccountsCommand(Command):
    """
    Accounts.

    accounts
        {account : Account name.}
        {--headers=* : HTTP headers.}
        {--s|show : Create or replace object.}
        {--u|update : Create, update or delete account metadata.}
        {--m|metadata : Show account metadata.}
    """

    def handle(self):
        client = IsilonClient()
        account_name = str(self.argument("account"))
        headers = dict()
        for header in self.option("headers"):
            headers.update(json.loads(header))
        if self.option("show"):
            resp = asyncio.run(client.accounts.show(account_name, headers))
            self.line(f"{resp}")
        elif self.option("update"):
            asyncio.run(client.accounts.update(account_name, headers))
            self.line("<options=bold>metadata updated.</>")
        elif self.option("metadata"):
            resp = asyncio.run(client.accounts.metadata(account_name, headers))
            for meta_key, meta_value in resp.items():
                self.line(f"<options=bold>{meta_key}</>: {meta_value}")
