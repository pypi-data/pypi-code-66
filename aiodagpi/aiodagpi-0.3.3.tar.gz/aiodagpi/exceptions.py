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


class AioDagpiException(Exception):
    """The base AioDagpi exception class
    """


class UnknownError(AioDagpiException):
    """When an unknown error occurs
    """
    def __init__(self, code, error) -> None:
        self.error = error
        self.code = code

    def __str__(self) -> str:
        return f'{self.code} received: {self.error}'


class InvalidToken(AioDagpiException):
    """When an unkown token is passed
    """
    def __init__(self, error='Invalid dagpi token passed, check to\
                            make sure it is correct.') -> None:
        self.error = error

    def __str__(self) -> str:
        return self.error


class InvalidOption(AioDagpiException):
    """When an invalid option is passed
    """
    def __init__(self, error='Invalid option selected, check for typos\
                            and make sure it exists.') -> None:
        self.error = error

    def __str__(self) -> str:
        return self.error


class RateLimited(AioDagpiException):
    """When you are being ratelimited
    """
    def __init__(self, error='You are being ratelimited for consistent usage,\
                            slow it down.') -> None:
        self.error = error

    def __str__(self) -> str:
        return self.error


class ServerError(AioDagpiException):
    """When there is an internal server error
    """
    def __init__(self, error='The server raised an error but could not be more\
                           specific of its origin. Check back later.') -> None:
        self.error = error

    def __str__(self) -> str:
        return self.error
