import asyncio

from cleo import Command

from isilon.client import IsilonClient


class EndpointsCommand(Command):
    """
    Endpoints.

    endpoints
    """

    def handle(self):
        client = IsilonClient()
        resp = asyncio.run(client.endpoints())
        self.line(f"{resp}")
