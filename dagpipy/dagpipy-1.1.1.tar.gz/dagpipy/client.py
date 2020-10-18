from typing import Union

from requests import get
from io import BytesIO

from .models import *
from .enums import ImageOptions, Games
from .exceptions import *

__all__ = (
    'Client'
)

URL = "https://api.dagpi.xyz/{type}/{option}"
ERRORS = {
    403: InvalidToken(),
    413: InvalidArgs('The image you passed in was too large!'),
    422: InvalidArgs(),
    429: ResponseError('You are being rate limited!'),
    500: ResponseError('Server error. Try again later.')

}
# Constants


class Client:
    def __init__(
            self,
            token: str,
    ):
        self.auth = token

    def get_image(
            self,
            option: ImageOptions,
            url: Union[ImageURL, str],
            **kwargs  # other stuff
    ) -> BytesIO:
        response = get(
            url=URL.format(type="image", option=option),
            params=dict(url=str(ImageURL(url)), **kwargs),
            headers={'Authorization': self.auth}
        )
        error = ERRORS.get(response.status_code)
        if error:
            raise error
        return BytesIO(response.content)

    def get_game(
            self,
            option: Games
    ) -> Union[Pokemon,
               LogoGame,
               Roast,
               YoMama,
               PickupLine,
               Joke,
               Waifu]:
        response = get(
            url=URL.format(type="data", option=option),
            headers={"Authorization": self.auth}
        )
        error = ERRORS.get(response.status_code)
        if error:
            raise error
        lookup = {
            "wtp": Pokemon,
            "logo": LogoGame,
            "roast": Roast,
            "yomama": YoMama,
            "pickupline": PickupLine,
            "joke": Joke,
            "waifu": Waifu
        }
        model = lookup.get(str(option))
        return model(response.json())