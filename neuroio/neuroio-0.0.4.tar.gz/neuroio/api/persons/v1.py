from typing import BinaryIO, Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import EntryResult, sentinel
from neuroio.utils import request_dict_processing, request_form_processing


class Persons(APIBase):
    def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: Union[int, object] = sentinel,
        create_on_ha: Union[bool, object] = sentinel,
        create_on_junk: Union[bool, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image"])
        files = {"image": image}

        return self.client.post(url="/v1/persons/", data=data, files=files)

    def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        return self.client.post(url="/v1/persons/entry/", json=data)

    def reinit(self, id: int) -> Response:
        return self.client.post(url="/v1/persons/reinit/", json={"id": id})

    def reinit_by_photo(
        self,
        pid: str,
        image: BinaryIO,
        source: str,
        facesize: Union[int, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
        result: str = EntryResult.HA,
    ) -> Response:
        data = request_form_processing(locals())
        files = {"image": image}

        return self.client.post(
            url=f"/v1/persons/reinit/{pid}/", data=data, files=files
        )

    def search(self, image: BinaryIO, identify_asm: bool = False) -> Response:
        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}

        return self.client.post(
            url="/v1/persons/search/", data=data, files=files
        )

    def delete(self, pid: str) -> Response:
        return self.client.delete(url=f"/v1/persons/{pid}/")


class PersonsAsync(APIBaseAsync):
    async def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: Union[int, object] = sentinel,
        create_on_ha: Union[bool, object] = sentinel,
        create_on_junk: Union[bool, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image"])
        files = {"image": image}

        return await self.client.post(
            url="/v1/persons/", data=data, files=files
        )

    async def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        return await self.client.post(url="/v1/persons/entry/", json=data)

    async def reinit(self, id: int) -> Response:
        return await self.client.post(
            url="/v1/persons/reinit/", json={"id": id}
        )

    async def reinit_by_photo(
        self,
        pid: str,
        image: BinaryIO,
        source: str,
        facesize: Union[int, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
        result: str = EntryResult.HA,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image", "pid"])
        files = {"image": image}

        return await self.client.post(
            url=f"/v1/persons/reinit/{pid}/", data=data, files=files
        )

    async def search(
        self, image: BinaryIO, identify_asm: bool = False
    ) -> Response:
        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}

        return await self.client.post(
            url="/v1/persons/search/", data=data, files=files
        )

    async def delete(self, pid: str) -> Response:
        return await self.client.delete(url=f"/v1/persons/{pid}/")
