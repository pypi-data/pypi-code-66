import sys

import google.cloud.speech_v1p1beta1 as cloud_speech
from google.protobuf import duration_pb2 as duration
import proto

from mod9.asr import common

# Used to compile protobufs into Python classes.
__protobuf__ = proto.module(
    package='mod9.asr.speech_mod9',
    manifest={
        "LongRunningRecognizeMetadata",
        "LongRunningRecognizeRequest",
        "LongRunningRecognizeResponse",
        "RecognitionAudio",                    # Held by subclass
        "RecognitionConfig",                   # Mod9-only attribute(s)
        "RecognitionMetadata",
        "RecognizeRequest",                    # Holds subclass with Mod9-only attribute(s)
        "RecognizeResponse",                   # Holds subclass with Mod9-only attribute(s)
        "SpeakerDiarizationConfig",
        "SpeechContext",
        "SpeechRecognitionAlternative",
        'SpeechRecognitionPhrase',             # Mod9-only message
        'SpeechRecognitionPhraseAlternative',  # Mod9-only message
        "SpeechRecognitionResult",             # Mod9-only attribute(s)
        "StreamingRecognitionConfig",          # Holds subclass with Mod9-only attribute(s)
        "StreamingRecognitionResult",          # Mod9-only attribute(s)
        "StreamingRecognizeRequest",
        "StreamingRecognizeResponse",          # Holds subclass with Mod9-only attribute(s)
        "WordInfo",
    },
)


# Copy Google's types into this namespace.
# Not all are used/implemented by Mod9 ASR; they may be silently ignored.
LongRunningRecognizeMetadata = cloud_speech.LongRunningRecognizeMetadata
LongRunningRecognizeRequest = cloud_speech.LongRunningRecognizeRequest
LongRunningRecognizeResponse = cloud_speech.LongRunningRecognizeResponse
RecognitionAudio = cloud_speech.RecognitionAudio
RecognitionMetadata = cloud_speech.RecognitionMetadata
SpeakerDiarizationConfig = cloud_speech.SpeakerDiarizationConfig
SpeechContext = cloud_speech.SpeechContext
SpeechRecognitionAlternative = cloud_speech.SpeechRecognitionAlternative
StreamingRecognizeRequest = cloud_speech.StreamingRecognizeRequest
WordInfo = cloud_speech.WordInfo


# Subclass Google's types required to extend
#  functionality to include Mod9-only options.
# Mod9-only message
class SpeechRecognitionPhrase(proto.Message):
    am = proto.Field(proto.FLOAT, number=1)
    lm = proto.Field(proto.FLOAT, number=2)
    phrase = proto.Field(proto.STRING, number=3)


# Mod9-only message
class SpeechRecognitionPhraseAlternative(proto.Message):
    alternatives = proto.RepeatedField(SpeechRecognitionPhrase, number=1)
    start_time = proto.Field(duration.Duration, number=2)
    end_time = proto.Field(duration.Duration, number=3)
    phrase = proto.Field(proto.STRING, number=4)


class SpeechRecognitionResult(proto.Message):
    alternatives = proto.RepeatedField(SpeechRecognitionAlternative, number=1)
    channel_tag = proto.Field(proto.INT32, number=2)
    language_code = proto.Field(proto.STRING, number=5)
    # Mod9-only attribute
    phrases = proto.RepeatedField(SpeechRecognitionPhraseAlternative, number=901)


class RecognizeResponse(proto.Message):
    results = proto.RepeatedField(SpeechRecognitionResult, number=2)


class StreamingRecognitionResult(proto.Message):
    alternatives = proto.RepeatedField(SpeechRecognitionAlternative, number=1)
    is_final = proto.Field(proto.BOOL, number=2)
    stability = proto.Field(proto.FLOAT, number=3)
    result_end_time = proto.Field(duration.Duration, number=4)
    channel_tag = proto.Field(proto.INT32, number=5)
    language_code = proto.Field(proto.STRING, number=6)
    # Mod9-only attribute
    phrases = proto.RepeatedField(SpeechRecognitionPhraseAlternative, number=901)


class StreamingRecognizeResponse(proto.Message):
    class SpeechEventType(proto.Enum):
        SPEECH_EVENT_UNSPECIFIED = 0
        END_OF_SINGLE_UTTERANCE = 1

    # error = proto.Field(proto.MESSAGE, number=1, message=status.Status,)
    results = proto.RepeatedField(StreamingRecognitionResult, number=2)
    # speech_event_type = proto.Field(proto.ENUM, number=4, enum=SpeechEventType,)


class RecognitionConfig(proto.Message):
    class AudioEncoding(proto.Enum):
        ENCODING_UNSPECIFIED = 0
        LINEAR16 = 1
        MULAW = 3
        # Mod9-only option
        ALAW = 901

    encoding = proto.Field(proto.ENUM, number=1, enum=AudioEncoding,)
    sample_rate_hertz = proto.Field(proto.INT32, number=2)
    language_code = proto.Field(proto.STRING, number=3)
    max_alternatives = proto.Field(proto.INT32, number=4)
    enable_word_time_offsets = proto.Field(proto.BOOL, number=8)
    enable_word_confidence = proto.Field(proto.BOOL, number=15)
    enable_automatic_punctuation = proto.Field(proto.BOOL, number=11)
    # Mod9-only option
    max_phrase_alternatives = proto.Field(proto.INT32, number=901)


class StreamingRecognitionConfig(proto.Message):
    config = proto.Field(RecognitionConfig, number=1)
    single_utterance = proto.Field(proto.BOOL, number=2)
    interim_results = proto.Field(proto.BOOL, number=3)


class RecognitionAudio(proto.Message):
    content = proto.Field(proto.BYTES, number=1, oneof="audio_source")
    uri = proto.Field(proto.STRING, number=2, oneof="audio_source")


class RecognizeRequest(proto.Message):
    config = proto.Field(RecognitionConfig, number=1)
    audio = proto.Field(RecognitionAudio, number=2)


class SpeechClient(object):
    """A duck-typed extension of google.cloud.speech.SpeechClient"""

    def long_running_recognize(self, request=None, *, config=None, audio=None, **kwargs):
        # TODO: similar logic to recognize for handling various input types.
        return common.long_running_recognize(request, **kwargs)

    def recognize(self, request=None, *, config=None, audio=None, **kwargs):
        # Replicate the logic for handling various input types.
        has_flattened_params = any([config, audio])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )
        if not isinstance(request, RecognizeRequest):
            request = RecognizeRequest(**request)
        return common.recognize(request, module=sys.modules[__name__], **kwargs)

    def streaming_recognize(self, config, requests, **kwargs):
        # Replicate the logic of google.cloud.speech_v1.helpers.SpeechHelpers.
        return common.streaming_recognize(
            self._streaming_request_iterable(config, requests),
            module=sys.modules[__name__],
            **kwargs,
        )

    def _streaming_request_iterable(self, config, requests):
        # Replicate the logic of google.cloud.speech_v1.helpers.SpeechHelpers.
        yield {'streaming_config': config}
        for request in requests:
            yield request


# Used to compile protobufs into Python classes.
__all__ = tuple(sorted(__protobuf__.manifest))
