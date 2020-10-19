import json
import typing
from io import BytesIO
from werkzeug.formparser import FormDataParser
from werkzeug.http import parse_options_header
from werkzeug.urls import url_decode
from .http import Headers, FormData
from .exceptions import NoCodecAvailable, DecodeError


class Codec:
    media_type: str

    def decode(
        self, bytestring: bytes, headers: typing.Optional[Headers] = None
    ) -> object:
        raise NoCodecAvailable()  # pragma: nocover


class JSONCodec(Codec):
    media_type = "application/json"

    def decode(
        self, bytestring: bytes, headers: typing.Optional[Headers] = None
    ) -> object:
        try:
            data = json.loads(bytestring.decode("utf-8"))
        except ValueError as exc:
            raise DecodeError("Malformed JSON. %s" % exc) from None
        if not isinstance(data, dict):
            raise DecodeError("Malformed JSON. Object expected.")
        return data


class MultiPartCodec(Codec):
    media_type = "multipart/form-data"

    def decode(
        self, bytestring: bytes, headers: typing.Optional[Headers] = None
    ) -> object:
        content_length = None
        mime_type = ""
        mime_options: typing.Dict[str, str] = {}
        if headers is not None:
            try:
                content_length = max(0, int(headers["content-length"]))
            except (KeyError, ValueError, TypeError):  # pragma: nocover
                pass
            try:
                mime_type, mime_options = parse_options_header(headers["content-type"])  # type: ignore
            except KeyError:  # pragma: nocover
                pass

        body_file = BytesIO(bytestring)
        parser = FormDataParser(cls=list)
        stream, form, files = parser.parse(
            body_file, mime_type, content_length, mime_options
        )
        return FormData(form + files)


class TextCodec(Codec):
    media_type = "text/*"

    def decode(
        self, bytestring: bytes, headers: typing.Optional[Headers] = None
    ) -> str:
        return bytestring.decode("utf-8")


class URLEncodedCodec(Codec):
    media_type = "application/x-www-form-urlencoded"

    def decode(
        self, bytestring: bytes, headers: typing.Optional[Headers] = None
    ) -> object:
        return url_decode(bytestring, cls=FormData)
