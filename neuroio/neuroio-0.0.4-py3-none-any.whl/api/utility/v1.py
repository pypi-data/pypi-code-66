from typing.io import BinaryIO

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import EntryResult


class Utility(APIBase):
    def compare(
        self, image1: BinaryIO, image2: BinaryIO, result: str = EntryResult.HA
    ) -> Response:
        files = {"image1": image1, "image2": image2}
        data = {"result": result}

        return self.client.post(
            url="/v1/utility/compare/", data=data, files=files
        )

    def asm(self, image: BinaryIO) -> Response:
        files = {"image": image}

        return self.client.post(url="/v1/utility/asm/", files=files)


class UtilityAsync(APIBaseAsync):
    async def compare(
        self, image1: BinaryIO, image2: BinaryIO, result: str = EntryResult.HA
    ) -> Response:
        files = {"image1": image1, "image2": image2}
        data = {"result": result}

        return await self.client.post(
            url="/v1/utility/compare/", data=data, files=files
        )

    async def asm(self, image: BinaryIO) -> Response:
        files = {"image": image}

        return await self.client.post(url="/v1/utility/asm/", files=files)
