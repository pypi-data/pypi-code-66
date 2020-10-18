import re

from dagpipy.exceptions import InvalidImageURL

__all__ = (
    'ImageURL'
)


class ImageURL(str):
    def __init__(self, c):
        super().__init__()
        regex = re.compile(
            r"^(?:http|ftp)s?://"
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            r"(?::\d+)?"
            r"(?:/?|[/?]\S+)$", re.IGNORECASE)
        if not re.match(regex, c):
            raise InvalidImageURL()
        else:
            if not any(a in c for a in ['.png', '.jpg', '.jpeg', '.gif']):
                raise InvalidImageURL()
