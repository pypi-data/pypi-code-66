import google.cloud.speech_v1p1beta1 as cloud_speech

from mod9.asr.common import (
    long_running_recognize,
    recognize,
    streaming_recognize,
)

# Copy Google's types into this namespace.
# Not all are used/implemented by Mod9 ASR; they may be silently ignored.
LongRunningRecognizeMetadata = cloud_speech.LongRunningRecognizeMetadata
LongRunningRecognizeRequest = cloud_speech.LongRunningRecognizeRequest
LongRunningRecognizeResponse = cloud_speech.LongRunningRecognizeResponse
RecognitionAudio = cloud_speech.RecognitionAudio
RecognitionConfig = cloud_speech.RecognitionConfig
RecognitionMetadata = cloud_speech.RecognitionMetadata
RecognizeRequest = cloud_speech.RecognizeRequest
RecognizeResponse = cloud_speech.RecognizeResponse
SpeakerDiarizationConfig = cloud_speech.SpeakerDiarizationConfig
SpeechContext = cloud_speech.SpeechContext
SpeechRecognitionAlternative = cloud_speech.SpeechRecognitionAlternative
SpeechRecognitionResult = cloud_speech.SpeechRecognitionResult
StreamingRecognitionConfig = cloud_speech.StreamingRecognitionConfig
StreamingRecognitionResult = cloud_speech.StreamingRecognitionResult
StreamingRecognizeRequest = cloud_speech.StreamingRecognizeRequest
StreamingRecognizeResponse = cloud_speech.StreamingRecognizeResponse
WordInfo = cloud_speech.WordInfo


class Mod9ASREngineTransport(object):
    """Duck-typed SpeechTransport"""
    _wrapped_methods = {}

    def __init__(self):
        self._wrapped_methods[self.recognize] = recognize
        self._wrapped_methods[self.streaming_recognize] = streaming_recognize

    def long_running_recognize(self, *args, **kwargs):
        return long_running_recognize(*args, **kwargs)

    def recognize(self, *args, **kwargs):
        return recognize(*args, **kwargs)

    def streaming_recognize(self, *args, **kwargs):
        return streaming_recognize(*args, **kwargs)


class SpeechClient(cloud_speech.SpeechClient):
    """OVERRIDE: this is a drop-in replacement for Google Cloud Speech"""

    def __init__(self, *args, **kwargs):
        """OVERRIDE: ignore all arguments, and set Mod9's custom transport."""
        self._transport = Mod9ASREngineTransport()
