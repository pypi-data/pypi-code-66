'''The MIT License (MIT)

Copyright (c) 2020 Raj Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import aiohttp
from .exceptions import InvalidOption,\
                        InvalidToken,\
                        RateLimited,\
                        ServerError,\
                        UnknownError


class Http:
    """Base aiodagpi http class
    """
    def __init__(self, token) -> None:
        self.token = token
        self.session = None
        self.basedata = 'https://api.dagpi.xyz/data/'
        self.baseimg = 'https://api.dagpi.xyz/image/'
        self.codes = {
            401: InvalidToken,
            403: InvalidToken,
            404: InvalidOption,
            429: RateLimited,
            500: ServerError
        }
        self.headers = {
            'Authorization': self.token
        }
        self.singparams = {
            'url': 'url'
        }

    async def createsession(self) -> None:
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def closesession(self) -> None:
        if self.session:
            await self.session.close()
            self.session = None

    async def dataget(self, endpoint: str) -> dict:
        await self.createsession()
        url = self.basedata + endpoint
        async with self.session.get(url, headers=self.headers) as client_resp:
            if client_resp.status == 200:
                try:
                    return await client_resp.json()
                except aiohttp.ContentTypeError:
                    return await client_resp.text()
            if client_resp.status in self.codes:
                exception = self.codes[client_resp.status]
                raise exception()
            raise UnknownError(code=client_resp.status,
                               error=client_resp.reason)

    async def sing_img(self, endpoint: str, imgurl: str) -> bytes:
        await self.createsession()
        url = self.baseimg + endpoint + '/'
        params = self.singparams
        params['url'] = imgurl
        async with self.session.get(url, headers=self.headers,
                                    params=params) as client_resp:
            if client_resp.status == 200:
                return await client_resp.read()
            if client_resp.status in self.codes:
                exception = self.codes[client_resp.status]
                raise exception()
            raise UnknownError(code=client_resp.status,
                               error=client_resp.reason)
