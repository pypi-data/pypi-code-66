from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Whoami(APIBase):
    def me(self) -> Response:
        return self.client.get(url="/v1/whoami/")


class WhoamiAsync(APIBaseAsync):
    async def me(self) -> Response:
        return await self.client.get(url="/v1/whoami/")
