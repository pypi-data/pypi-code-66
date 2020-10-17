import datetime
from typing import Dict, Optional, Tuple

from jatime.converter import (
    ja_hour_to_24_hour,
    ja_num_to_int,
    jp_year_to_ad_year,
    relative_day_into_absolute,
    relative_month_into_absolute,
    relative_year_into_absolute,
)
from jatime.errors import InvalidValueError
from jatime.finder import year_from_month_day_dow, year_month_from_day_dow


class DateTime(object):
    ATTRS = ["year", "month", "day", "dow", "hour", "minute"]
    DOW = "月火水木金土日"

    def __init__(self, base: Optional[datetime.datetime] = None, **kwargs) -> None:
        self.base = datetime.datetime.now() if base is None else base

        self.year = self._given_year(**kwargs)
        self.month = self._given_month(**kwargs)
        self.day = self._given_day(**kwargs)
        self.dow = self._given_dow(**kwargs)
        self.hour = self._given_hour(**kwargs)
        self.minute = self._given_minute(**kwargs)

        self._estimate()

    def _relative_year(self, **kwargs) -> Optional[int]:
        if "relative_year" not in kwargs.keys():
            return None

        year = relative_year_into_absolute(kwargs["relative_year"], self.base.year)
        if year is None:
            return None

        return year

    def _given_year(self, **kwargs) -> Optional[int]:
        year = self._relative_year(**kwargs)
        if year is not None:
            return year

        year_ad = ja_num_to_int(kwargs.get("ad_year", None))

        if "jp_year" not in kwargs.keys():
            return year_ad

        year_jp = jp_year_to_ad_year(kwargs["jp_year"])
        if year_jp is None:
            return year_ad
        elif year_ad is None:
            return year_jp

        if year_jp == year_ad:
            return year_jp
        else:
            raise InvalidValueError(
                f"{kwargs['jp_year']} is not {year_ad}, but {year_jp}."
            )

    def _relative_month(self, **kwargs) -> Optional[Tuple[int, int]]:
        if "relative_month" not in kwargs.keys():
            return None

        year_month = relative_month_into_absolute(
            kwargs["relative_month"], self.base.year, self.base.month
        )
        if year_month is None:
            return None

        return year_month

    def _given_month(self, **kwargs) -> Optional[int]:
        year_month = self._relative_month(**kwargs)
        if year_month is not None:
            self.year = year_month[0]
            return year_month[1]

        month = ja_num_to_int(kwargs.get("month", None))
        if month is None:
            return None
        if month < 1 or 12 < month:
            raise InvalidValueError(f"month must be in 1..12, but {month} was given.")

        return month

    def _relative_day(self, **kwargs) -> Optional[Tuple[int, int, int]]:
        if "relative_day" not in kwargs.keys():
            return None

        year_month_day = relative_day_into_absolute(
            kwargs["relative_day"], self.base.year, self.base.month, self.base.day
        )
        if year_month_day is None:
            return None

        return year_month_day

    def _given_day(self, **kwargs) -> Optional[int]:
        year_month_day = self._relative_day(**kwargs)
        if year_month_day is not None:
            self.year = year_month_day[0]
            self.month = year_month_day[1]
            return year_month_day[2]

        day = ja_num_to_int(kwargs.get("day", None))
        if day is None:
            return None
        if day < 1 or 31 < day:
            raise InvalidValueError(f"day must be in 1..31, but {day} was given.")
        return day

    def _given_dow(self, **kwargs) -> Optional[int]:
        if self.year is not None and self.month is not None and self.day is not None:
            date = datetime.date(self.year, self.month, self.day)
            calculated_dow = date.weekday()
        else:
            date = None
            calculated_dow = None

        if "dow" not in kwargs.keys():
            return calculated_dow

        dow = self.DOW.index(kwargs["dow"])
        if calculated_dow is None or dow == calculated_dow:
            return dow

        raise InvalidValueError(
            f"day of the week on {date} is not {dow}, but {calculated_dow}."
        )

    @staticmethod
    def _given_hour(**kwargs) -> Optional[int]:
        hour = ja_num_to_int(kwargs.get("hour", None))
        if hour is None:
            return None
        if "ampm" in kwargs.keys():
            hour = ja_hour_to_24_hour(kwargs["ampm"], hour)
        if hour < 0 or 29 < hour:
            raise InvalidValueError(f"hour must be in 0..29, but {hour} was given.")
        return hour

    @staticmethod
    def _given_minute(**kwargs) -> Optional[int]:
        minute = ja_num_to_int(kwargs.get("minute", None))
        if minute is None:
            return None
        if minute < 0 or 59 < minute:
            raise InvalidValueError(f"minute must be in 0..59, but {minute} was given.")
        return minute

    def _estimate(self) -> None:
        if (
            self.year is None
            and self.month is not None
            and self.day is not None
            and self.dow is not None
        ):
            self.year = year_from_month_day_dow(
                self.month, self.day, self.dow, self.base.year
            )

        if (
            self.year is None
            and self.month is None
            and self.day is not None
            and self.dow is not None
        ):
            self.year, self.month = year_month_from_day_dow(
                self.day, self.dow, self.base.year, self.base.month
            )

    def to_dict(self) -> Dict:
        return {key: getattr(self, key) for key in self.ATTRS}
