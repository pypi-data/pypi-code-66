from typing import Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Tokens(APIBase):
    def create(self, permanent: bool = False) -> Response:
        data = {"permanent": permanent}

        return self.client.post(url="/v1/tokens/", json=data)

    def list(
        self, permanent: bool = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"permanent": permanent, "limit": limit, "offset": offset}

        return self.client.get(url="/v1/tokens/", params=data)

    def get(self, token_id_or_key: Union[int, str]) -> Response:
        return self.client.get(url=f"/v1/tokens/{token_id_or_key}/")

    def update(
        self, token_id_or_key: Union[int, str], is_active: bool
    ) -> Response:
        return self.client.patch(
            url=f"/v1/tokens/{token_id_or_key}/", data={"is_active": is_active}
        )

    def delete_list(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None

        return self.client.delete(url="/v1/tokens/", params=data)

    def delete(self, token_id_or_key: Union[int, str]) -> Response:
        return self.client.delete(url=f"/v1/tokens/{token_id_or_key}/")


class TokensAsync(APIBaseAsync):
    async def create(self, permanent: bool = False) -> Response:
        data = {"permanent": permanent}

        return await self.client.post(url="/v1/tokens/", json=data)

    async def list(
        self, permanent: bool = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"permanent": permanent, "limit": limit, "offset": offset}

        return await self.client.get(url="/v1/tokens/", params=data)

    async def get(self, token_id_or_key: Union[int, str]) -> Response:
        return await self.client.get(url=f"/v1/tokens/{token_id_or_key}/")

    async def update(
        self, token_id_or_key: Union[int, str], is_active: bool
    ) -> Response:
        return await self.client.patch(
            url=f"/v1/tokens/{token_id_or_key}/", data={"is_active": is_active}
        )

    async def delete_list(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None

        return await self.client.delete(url="/v1/tokens/", params=data)

    async def delete(self, token_id_or_key: Union[int, str]) -> Response:
        return await self.client.delete(url=f"/v1/tokens/{token_id_or_key}/")
