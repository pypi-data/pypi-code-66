import itertools
import re
from typing import Generator

# 括弧
_OPEN = r"[(（「『【〔［]"
_CLOSE = r"[)）」』】〕］]"

# 日付表記のセパレータ
_SEP = r"/／"

# 西暦4桁表記
_AD_YEAR = r"(?P<ad_year>[12１２一二][\d〇一二三四五六七八九]{3})"

# 和暦表記
_JP_YEAR = (
    r"(?P<jp_year>(明治|大正|昭和|平成|令和)("
    + "|".join(
        [
            r"\d{1,2}",
            r"[二三四五六][十拾]?[一二三四五六七八九]",
            r"[拾十一][一二三四五六七八九]",
            r"[二三四五六][〇十拾]",
            r"一〇",
            r"[一二三四五六七八九十拾]",
            r"元",
        ]
    )
    + "))"
)

# 相対的な年表現
_RELATIVE_YEAR = r"(?P<relative_year>(一昨年|昨年|去年|今年|再来年|来年))"

# 年表現のパターン一覧
_YEAR = [
    [_JP_YEAR, r"年", _OPEN, _AD_YEAR, r"年?", _CLOSE],
    [_JP_YEAR, _OPEN, _AD_YEAR, _CLOSE, r"年?"],
    [_AD_YEAR, r"年", _OPEN, _JP_YEAR, r"年?", _CLOSE],
    [_AD_YEAR, _OPEN, _JP_YEAR, _CLOSE, r"年?"],
    [_JP_YEAR, r"年"],
    [_AD_YEAR, r"年"],
    [_RELATIVE_YEAR],
]
YEAR = [r"\s*".join(y) for y in _YEAR]

MONTH = [
    r"(?P<month>("
    + "|".join(
        [
            r"[1１][012０１２]",
            r"[十一拾][一二]",
            r"一〇",
            r"[一二三四五六七八九十拾]",
            r"[1-9]",
            r"[１-９]",
        ]
    )
    + r"))\s*月",
    r"(?P<relative_month>(先月|今月|再来月|来月))",
]

DAY = [
    r"(?P<day>("
    + "|".join(
        [
            r"[3３][01０１]",
            r"[12１２]\d",
            r"[1-9１-９]",
            r"三[十拾]?一",
            r"二[十拾]?[一二三四五六七八九]",
            r"[拾十一][一二三四五六七八九]",
            r"[二三][十拾〇]",
            r"一〇",
            r"[一二三四五六七八九十拾]",
        ]
    )
    + r"))\s*日",
    r"(?P<relative_day>(一昨日|昨日|今日|本日|明日|明後日))",
]

# 曜日
DOW = [
    r"\s*".join([_OPEN, r"(?P<dow>[月火水木金土日])(曜日|曜|)", _CLOSE]),
    r"(?P<dow>[月火水木金土日])(曜日|曜)",
]

# 時
_HOUR = (
    r"(?P<ampm>(午前|午後|[aａAＡpｐPＰ]\.?[mｍMＭ]\.?|))"
    + r"\s*"
    + r"(?P<hour>("
    + "|".join(
        [
            r"[012０１２]?\d",
            r"二[十拾]?[一二三四五六七八九]",
            r"[拾十一][一二三四五六七八九]",
            r"[二][〇十]",
            r"一〇",
            r"[零〇一二三四五六七八九十拾]",
        ]
    )
    + r"))"
)
# 分
_MINUTE = (
    r"(?P<minute>("
    + "|".join(
        [
            r"[0-5０-５]?\d",
            r"[二三四五][十拾]?[一二三四五六七八九]",
            r"[拾十一][一二三四五六七八九]",
            r"[二三四五][〇十]",
            r"一〇",
            r"[零〇一二三四五六七八九十拾]",
        ]
    )
    + r"))"
)
_TIME = [
    [_HOUR, "[:：]", _MINUTE],
    [_HOUR, "時", _MINUTE, "分"],
    [_HOUR, "時", r"(?P<minute>半?)"],
]
TIME = [r"\s*".join(t) for t in _TIME]


# 優先順位付けられた日付表現のリスト
_ORDERED_PATTERNS = [
    (YEAR, MONTH, DAY, DOW, TIME),
    (YEAR, MONTH, DAY, TIME),
    (YEAR, MONTH, DAY, DOW),
    (YEAR, MONTH, DAY),
    (YEAR, MONTH),
    (YEAR,),
    (MONTH, DAY, DOW, TIME),
    (MONTH, DAY, TIME),
    (MONTH, DAY, DOW),
    (MONTH, DAY),
    (MONTH,),
    (DAY, DOW, TIME),
    (DAY, TIME),
    (DAY, DOW),
    (DAY,),
    (DOW, TIME),
    (TIME,),
    (DOW,),
]


def datetime_patterns() -> Generator:
    for time_repr in _ORDERED_PATTERNS:
        for pattern_tuple in itertools.product(*time_repr):
            yield re.compile(r"\s*の?\s*".join(pattern_tuple))
