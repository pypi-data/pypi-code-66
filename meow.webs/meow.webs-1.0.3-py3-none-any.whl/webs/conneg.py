import typing
from .codecs import Codec
from . import exceptions


def negotiate_content_type(
    codecs: typing.List[Codec], content_type: typing.Optional[str] = None
) -> Codec:
    """
    Given the value of a 'Content-Type' header, return the appropriate
    codec for decoding the request content.
    """
    if content_type is None:
        return codecs[0]  # pragma: nocover

    content_type = content_type.split(";")[0].strip().lower()
    main_type = content_type.split("/")[0] + "/*"
    wildcard_type = "*/*"

    for codec in codecs:
        if codec.media_type in (content_type, main_type, wildcard_type):
            return codec

    msg = f"Unsupported media in Content-Type header '{content_type}'"
    raise exceptions.NoCodecAvailable(msg)
