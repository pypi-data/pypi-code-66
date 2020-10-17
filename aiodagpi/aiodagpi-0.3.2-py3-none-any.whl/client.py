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

from typing import Union
from .http import Http
from .objects import Object, Make_Object


class AioDagpiClient:
    """The main AioDagpi user client
    """
    def __init__(self, token: str) -> None:
        """init

        Args:
            token (str): Your Dagpi API token
        """
        self.http = Http(token)
        self.token = token

    async def createsession(self) -> None:
        """Creates an aiohttp client session
        """
        await self.http.createsession()

    async def closesession(self) -> None:
        """Closes the existing aiohttp client session
        """
        await self.http.closesession()

    async def data(self,
                   option: str,
                   _object: bool = False) -> Union[dict, Object]:
        """Collects a response from dagpi's data endpoint

        Args:
            option (str): The endpoint to choose from, options are documented
            object (bool, optional): Whether or not to convert into object
            output

        Returns:
            Union[dict, Object]: Either a dictionary or an object, depending
            on the object param
        """
        response = await self.http.dataget(option)
        await self.closesession()
        if _object:
            return Make_Object(response)
        return response
