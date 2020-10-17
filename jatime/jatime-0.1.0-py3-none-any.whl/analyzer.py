import datetime
import re
from typing import Dict, List, Optional, Union

from jatime.errors import InvalidValueError
from jatime.patterns import datetime_patterns
from jatime.times import DateTime


def _split(string: str, pattern) -> List:
    pieces = []
    i = 0
    for m in re.finditer(pattern, string):
        pieces.append(string[i : m.span()[0]])
        pieces.append(m)
        i = m.span()[1]
    if string[i:] != "":
        pieces.append(string[i:])
    return pieces


def split(string: str, patterns) -> List:
    pieces = [string]
    for pattern in patterns:
        new_pieces = []
        for p in pieces:
            if type(p) == str:
                new_pieces += _split(p, pattern)
            else:
                new_pieces.append(p)
        pieces = new_pieces
    return pieces


def analyze(
    string: str, base: Optional[datetime.datetime] = None
) -> List[Union[str, Dict]]:
    if base is None:
        base = datetime.datetime.now()

    result = []
    pieces = split(string, datetime_patterns())
    for p in pieces:
        if type(p) == str:
            result.append(p)
            continue

        dic = {"string": p.group()}
        try:
            dt = DateTime(base=base, **p.groupdict())
            dic.update(dt.to_dict())
        except InvalidValueError as e:
            dic["error"] = str(e)
        result.append(dic)
        # TODO: update base time (?)
    return result
