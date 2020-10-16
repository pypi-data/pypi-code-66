import json
import sys

from . import common
from . import speech_mod9
from .reformat import mod9

reformat = mod9.ReformatMod9()


class SpeechClient:
    def recognize(self, request):
        return common.recognize(request, module=speech_mod9, reformat=reformat)

    def streaming_recognize(self, config, requests):
        return common.streaming_recognize(
            self._streaming_request_iterable(config, requests),
            module=speech_mod9,
            reformat=reformat,
        )

    def _streaming_request_iterable(self, config, requests):
        yield {'streaming_config': config}
        for request in requests:
            yield request
