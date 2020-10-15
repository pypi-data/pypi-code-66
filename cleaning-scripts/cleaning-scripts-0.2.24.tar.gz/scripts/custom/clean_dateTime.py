import datetime
import re

from scripts import utils


def clean_dateTime(raw_input):  # noqa: C901
    if not isinstance(raw_input, str):
        raw_input = str(raw_input)
    if utils.is_empty(raw_input):
        return ""

    date = None

    # Correct format
    try:
        pattern = re.compile(
            r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)"
            r"(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1])(T([01][0-9]|2[0-3])"
            r":[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):"
            r"[0-5][0-9]|14:00)))?)?)?"
        )
        date = re.fullmatch(pattern, raw_input).group(0)
        result = date
    except AttributeError:
        pass

    # Handle YYYY
    try:
        date = datetime.datetime.strptime(raw_input, "%Y")
        result = date.strftime("%Y")
    except ValueError:
        pass

    # Handle YYYY-MM
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m")
        result = date.strftime("%Y-%m")
    except ValueError:
        pass

    # Handle YYYYMM
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m")
        result = date.strftime("%Y-%m")
    except ValueError:
        pass

    # Handle YYYY-MM-DD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d")
        result = date.strftime("%Y-%m-%d")
    except ValueError:
        pass

    # Handle YYYYMMDD
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d")
        result = date.strftime("%Y-%m-%d")
    except ValueError:
        pass

    # Handle YYYYMMDDHHMM
    try:
        date = datetime.datetime.strptime(raw_input, "%Y%m%d%H%M")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DD H:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%d %H:%M:%S")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S+zz:zz
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S+%z")
        result = date.strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        pass

    # Handle YYYY-MM-DDTH:M:S-zz:zz
    try:
        date = datetime.datetime.strptime(raw_input, "%Y-%m-%dT%H:%M:%S-%z")
        result = date.strftime("%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        pass

    # Handle RFC 1123 format
    try:
        date = datetime.datetime.strptime(raw_input, "%a, %d %b %Y %H:%M:%S GMT")
        result = date.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    except ValueError:
        pass

    if date is None:
        return raw_input

    return result
