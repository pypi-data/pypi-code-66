import asyncio
import json

from cleo import Command

from isilon.client import IsilonClient


class DiscoverabilityCommand(Command):
    """
    Discoverability.

    discoverability
    """

    def handle(self):
        client = IsilonClient()
        resp = asyncio.run(client.discoverability.info())
        self.line(f"{json.dumps(resp, indent=4, sort_keys=True)}")
