from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Auth(APIBase):
    def login(self, username: str, password: str) -> Response:
        data = {"username": username, "password": password}

        return self.client.post(url="/v1/login/", json=data)

    def password_change(
        self, old_password: str, new_password: str, reset_tokens: bool = False
    ) -> Response:
        data = {
            "old_password": old_password,
            "password": new_password,
            "password2": new_password,
            "reset_tokens": reset_tokens,
        }

        return self.client.post(url="/v1/auth/password/change/", json=data)


class AuthAsync(APIBaseAsync):
    async def login(self, username: str, password: str) -> Response:
        data = {"username": username, "password": password}

        return await self.client.post(url="/v1/login/", json=data)

    async def password_change(
        self, old_password: str, new_password: str, reset_tokens: bool = False
    ) -> Response:
        data = {
            "old_password": old_password,
            "password": new_password,
            "password2": new_password,
            "reset_tokens": reset_tokens,
        }

        return await self.client.post(
            url="/v1/auth/password/change/", json=data
        )
