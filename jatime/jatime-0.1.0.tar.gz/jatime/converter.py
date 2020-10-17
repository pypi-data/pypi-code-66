import datetime
from typing import Callable, Dict, Optional, Tuple, Union


def ja_num_to_int(num: Union[int, str]) -> Optional[int]:
    """Convert the Japanese numerical expression to int.

    Notes
    -----
    * "半" is specially converted to 30.
    * This function supports expressions with 4 or fewer digits, not including
      "百" and "千".

    Parameters
    ----------
    num : int or str
        Japanese numerical expression.

    Returns
    -------
    int or None
        The int value corresponding to ``num``, or None if `it cannot be converted.

    Examples
    --------
    >>> [ja_num_to_int(n) for n in (1, "零", "六七", "八十九", "二〇二〇", "半", "あ")]
    [1, 0, 67, 89, 2020, 30, None]
    """
    if type(num) == int:
        return num

    num = str(num)
    if len(num) == 0:
        return None

    specials = {"零": 0, "元": 1, "十": 10, "拾": 10, "半": 30}
    if num in specials.keys():
        return specials[num]

    num = num[:-1] + num[-1].replace("十", "0").replace("拾", "0")
    num = num[0] + num[1:].replace("十", "").replace("拾", "")
    num = num.translate(str.maketrans("〇一二三四五六七八九十拾", "012345678911"))

    try:
        return int(num)
    except ValueError:
        return None


def jp_year_to_ad_year(jp_year: str) -> Optional[int]:
    """Convert the Japanese year to the Western calendar.

    Notes
    -----
    If a year beyond the final year is given, return None.

    Parameters
    ----------
    jp_year : str
        Japanese year.

    Returns
    -------
    int or None
        The Western calendar corresponding to ``jp_year``, or None if it cannot be
        converted.

    Examples
    --------
    >>> [jp_year_to_ad_year(y) for y in ("昭和二十", "平成4", "令和元", "あ")]
    [1945, 1992, 2019, None]

    Note that the 昭和 era is up to '64.

    >>> assert jp_year_to_ad_year("昭和65") is None
    """
    era = jp_year[:2]
    year = jp_year[2:]
    data = {
        # 年号: (最終年, 最終年に対応する西暦年)
        "明治": (45, 1912),
        "大正": (15, 1926),
        "昭和": (64, 1989),
        "平成": (31, 2019),
        "令和": (50, 2068),
    }
    if era not in data.keys():
        return None
    year = ja_num_to_int(year)
    if year is None:
        return None
    diff = data[era][0] - year
    if diff < 0:
        return None
    return data[era][1] - diff


def _relative_to_absolute(data: Dict[str, int]) -> Callable[[str, int], Optional[int]]:
    def converter(relative_expression: str, base: int) -> Optional[int]:
        assert type(base) == int
        if relative_expression not in data.keys():
            return None
        return base + data[relative_expression]

    return converter


def relative_year_into_absolute(relative_year: str, base_year: int) -> Optional[int]:
    """Convert a relative expression of the year into an absolute one.

    Parameters
    ----------
    relative_year : str
        Relative year expression.
    base_year : int
        Base year.

    Returns
    -------
    int or None
        The western calendar corresponding to ``relative_year`` based on ``base_year``,
        or None if it cannot be converted.

    Examples
    --------
    >>> relative_year_into_absolute("来年", 2020)
    2021

    >>> relative_year_into_absolute("一昨年", 2020)
    2018
    """
    data = {
        "一昨年": -2,
        "昨年": -1,
        "去年": -1,
        "今年": 0,
        "来年": 1,
        "再来年": 2,
    }
    return _relative_to_absolute(data)(relative_year, base_year)


def relative_month_into_absolute(
    relative_month: str, base_year: int, base_month: int
) -> Optional[Tuple[int, int]]:
    """Convert a relative expression of the month into an absolute one.

    Parameters
    ----------
    relative_month : str
        Relative month expression.
    base_year : int
        Base year.
    base_month : int
        Base month.

    Returns
    -------
    tuple of int
        The absolute year and month corresponding to ``relative_month`` based on
        ``base_year`` and ``base_month`, or None if it cannot be converted.

    Examples
    --------
    >>> relative_month_into_absolute("先月", 2021, 1)
    (2020, 12)

    >>> relative_month_into_absolute("今月", 2021, 1)
    (2021, 1)

    >>> relative_month_into_absolute("再来月", 2020, 12)
    (2021, 2)
    """
    assert type(base_year) == int
    data = {
        "先々月": -2,
        "先月": -1,
        "今月": 0,
        "来月": 1,
        "再来月": 2,
    }
    month = _relative_to_absolute(data)(relative_month, base_month)
    if month is None:
        return None
    if month < 1:
        return base_year - 1, month + 12
    elif month <= 12:
        return base_year, month
    else:
        return base_year + 1, month - 12


def relative_day_into_absolute(
    relative_day: str, base_year: int, base_month: int, base_day: int
) -> Optional[Tuple[int, int, int]]:
    """Convert a relative expression of the day into an absolute one.

    Parameters
    ----------
    relative_day : str
        Relative day expression.
    base_year : int
        Base year.
    base_month : int
        Base month.
    base_day : int
        Base day.

    Returns
    -------
    tuple of int
        The absolute year, month and day corresponding to ``relative_day`` based on
        ``base_year``, ``base_month`` and ``base_day``, or None if it cannot be
        converted.

    Examples
    --------
    >>> relative_day_into_absolute("明日", 2020, 10, 17)
    (2020, 10, 18)

    >>> relative_day_into_absolute("昨日", 2020, 3, 1)
    (2020, 2, 29)

    >>> relative_day_into_absolute("昨日", 2021, 3, 1)
    (2021, 2, 28)
    """
    data = {"一昨日": -2, "昨日": -1, "今日": 0, "本日": 0, "明日": 1, "明後日": 2}
    if relative_day not in data.keys():
        return None
    base = datetime.date(base_year, base_month, base_day)
    date = base + datetime.timedelta(days=data[relative_day])
    return date.year, date.month, date.day


def ja_hour_to_24_hour(ampm: str, hour: int) -> int:
    """Unify the expression of hour with 24-hour clock.

    Parameters
    ----------
    ampm : str
        A string representing AM or PM.
    hour : int
        Hour.

    Returns
    -------
        24-hour.

    Examples
    --------
    >>> ja_hour_to_24_hour("午前", 9)
    9

    >>> ja_hour_to_24_hour("午後", 9)
    21

    >>> ja_hour_to_24_hour("AM", 10)
    10

    >>> ja_hour_to_24_hour("PM", 10)
    22
    """
    if "午後" in ampm or ampm.startswith(("p", "ｐ", "P", "Ｐ")):
        hour += 12
    return hour
