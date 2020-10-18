__all__ = (
    'InvalidArgs',
    'InvalidImageURL',
    'ResponseError',
    'InvalidToken'
)


class InvalidArgs(Exception):
    def __init__(self, message="You have passed in invalid arguments! Please refer to the documentation for more info:"
                               "https://dagpi.docs.apiary.io/#reference/images-api"):
        self.message = message

    def __str__(self):
        return self.message


class InvalidImageURL(Exception):
    def __init__(self, message="You have passed in an incorrect image url!"):
        self.message = message

    def __str__(self):
        return self.message


class ResponseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidToken(Exception):
    def __init__(self, message="You have passed in an incorrect token"):
        self.message = message

    def __str__(self):
        return self.message
