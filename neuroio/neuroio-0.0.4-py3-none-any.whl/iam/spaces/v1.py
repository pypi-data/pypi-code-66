import httpx
from httpx import URL, Response

from neuroio import constants
from neuroio.api.base import APIBase, APIBaseAsync


class Spaces(APIBase):
    def create(self, name: str) -> Response:
        data = {"name": name}

        return self.client.post(url="/v1/spaces/", json=data)

    def list(
        self, q: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": q, "limit": limit, "offset": offset}

        return self.client.get(url="/v1/spaces/", params=data)

    def get(self, id: int) -> Response:
        return self.client.get(url=f"/v1/spaces/{id}/")

    def update(self, id: int, name: str) -> Response:
        data = {"name": name}

        return self.client.patch(url=f"/v1/spaces/{id}/", json=data)

    def delete(self, id: int) -> Response:
        return self.client.delete(url=f"/v1/spaces/{id}/")

    def token(self, id: int, permanent: bool = False) -> Response:
        data = {"permanent": permanent}

        return self.client.post(url=f"/v1/spaces/{id}/tokens/", json=data)


class SpacesAsync(APIBaseAsync):
    def __init__(self, client: httpx.AsyncClient):
        client.base_url = URL(constants.IAM_BASE_URL)
        super().__init__(client=client)

    async def create(self, name: str) -> Response:
        data = {"name": name}

        return await self.client.post(url="/v1/spaces/", json=data)

    async def list(
        self, q: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": q, "limit": limit, "offset": offset}

        return await self.client.get(url="/v1/spaces/", params=data)

    async def get(self, id: int) -> Response:
        return await self.client.get(url=f"/v1/spaces/{id}/")

    async def update(self, id: int, name: str) -> Response:
        data = {"name": name}

        return await self.client.patch(url=f"/v1/spaces/{id}/", json=data)

    async def delete(self, id: int) -> Response:
        return await self.client.delete(url=f"/v1/spaces/{id}/")

    async def token(self, id: int, permanent: bool = False) -> Response:
        data = {"permanent": permanent}
        return await self.client.post(
            url=f"/v1/spaces/{id}/tokens/", json=data
        )
