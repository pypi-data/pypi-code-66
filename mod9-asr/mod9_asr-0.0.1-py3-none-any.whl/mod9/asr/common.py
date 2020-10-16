import google.cloud.speech_v1p1beta1 as cloud_speech

from mod9.reformat.utils import get_transcripts_mod9
from mod9.reformat import google as reformat


class Mod9NotImplementedError(Exception):
    pass


def long_running_recognize(
    request,
    retry=None,
    timeout=None,
    metadata=None,
    module=cloud_speech,
    *args,
    **kwargs,
):
    raise Mod9NotImplementedError('Refer to the REST wrapper for long-running recognition.')


def recognize(
    request,
    retry=None,
    timeout=None,
    metadata=None,
    module=cloud_speech,
    *args,
    **kwargs,
):
    if retry or timeout or metadata:
        # NOTE: Mod9 ASR Python SDK wrapper does not support retry,
        #  timeout, or metadata arguments, which are currently ignored.
        # TODO: Add support for retry and timeout arguments.
        pass

    # Parse inputs to ensure they are the expected encoding, have allowed arguments.
    options, requests = reformat.input_to_mod9(
        {'config': request.config, 'audio': request.audio},
        module=module,
    )

    # Read Engine responses.
    mod9_results = get_transcripts_mod9(options, requests)

    # Convert Mod9 style to Google style.
    google_result_dicts = reformat.result_from_mod9(mod9_results)

    # Convert Mod9 type to Google type.
    google_results = reformat.google_type_result_from_dict(
        google_result_dicts,
        google_result_type=module.SpeechRecognitionResult,
        module=module,
    )

    # Yield the expected response object.
    response = module.RecognizeResponse()
    for google_result in google_results:
        response.results.append(google_result)

    return response


def streaming_recognize(
    requests,
    retry=None,
    timeout=None,
    metadata=None,
    module=cloud_speech,
    *args,
    **kwargs,
):
    if retry or timeout or metadata:
        # NOTE: Mod9 ASR Python SDK wrapper does not support retry,
        #  timeout, or metadata arguments, which are currently ignored.
        # TODO: Add support for retry and timeout arguments.
        pass

    # The first request should have the config and no audio.
    request = next(requests)

    # Parse inputs to ensure they are the expected encoding, have allowed arguments.
    options, _ = reformat.input_to_mod9({'config': request['streaming_config']}, module=module)

    # Read Engine responses.
    audio_requests = (request.audio_content for request in requests)
    mod9_results = get_transcripts_mod9(options, audio_requests)

    # Convert Mod9 style to Google style.
    google_result_dicts = reformat.result_from_mod9(mod9_results)

    # Convert Mod9 type to Google type.
    google_results = reformat.google_type_result_from_dict(
        google_result_dicts,
        google_result_type=module.StreamingRecognitionResult,
        module=module,
    )

    # Yield the expected response object.
    for google_result in google_results:
        response = module.StreamingRecognizeResponse()
        response.results.append(google_result)
        yield response
