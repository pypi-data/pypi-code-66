import datetime
from typing import Generator, Optional, Tuple

from jatime.errors import NotFoundError


def _years_close_to(
    base_year: int, max_diff: Optional[int] = None
) -> Generator[int, None, None]:
    if max_diff is None:
        max_diff = 50

    year = base_year
    for i in range(max_diff * 2):
        if i % 2 == 0:
            year -= i
        else:
            year += i
        yield year


def year_from_month_day_dow(
    month: int, day: int, dow: int, base_year: Optional[int] = None
) -> int:
    """Find the closest year that meets the requirements for a given month,
    day and day of the week.

    Parameters
    ----------
    month : int
        Month.
    day : int
        Day.
    dow : int
        Day of the week as an integer, where Monday is 0 and Sunday is 6.
    base_year : int, optional
        The base year of the search (the default is the year at runtime).

    Returns
    -------
    int
        The the closest year that meets
        ``datetime(year, month, day).weekday() == dow```.

    Raises
    ------
    NotFoundError
        If the year is not found.

    Notes
    -----
    Given a combination of month, day and day of the week that exist, the year is
    always found.

    Examples
    --------
    October 17, 2018 is a Wednesday (dow = 2).

    >>> year_from_month_day_dow(10, 17, 2, 2020)
    2018

    Note that October 17, 2029 is also a Wednesday, but 2018 will be adopted because
    it is closer to 2020.
    """
    if base_year is None:
        base_year = datetime.date.today().year

    for year in _years_close_to(base_year):
        # MEMO: It is always found within +-40 from the base year.
        try:
            date = datetime.date(year, month, day)
            if date.weekday() == dow:
                return year
        except ValueError:
            # February 29th of a non-leap year.
            continue

    raise NotFoundError(
        f"could not find the year: ({month}, {day}, {dow}; {base_year})"
    )


def _years_months_close_to(
    base_year: int, base_month: int, max_diff: Optional[int] = None
) -> Generator[Tuple[int, int], None, None]:
    if max_diff is None:
        max_diff = 50

    month = base_month
    for m in range(max_diff * 2):
        if m % 2 == 0:
            month -= m
        else:
            month += m
        q, r = divmod(month, 12)
        if r != 0:
            next_year = base_year + q
            next_month = r
        else:
            next_year = base_year + q - 1
            next_month = 12
        yield next_year, next_month


def year_month_from_day_dow(
    day: int,
    dow: int,
    base_year: Optional[int] = None,
    base_month: Optional[int] = None,
) -> Tuple[int, int]:
    """Find the closest year and month that meets the requirements for a given day and
    day of the week.

    Parameters
    ----------
    day : int
        Day.
    dow : int
        Day of the week as an integer, where Monday is 0 and Sunday is 6.
    base_year : int, optional
        The base year of the search (the default is the year at runtime).
    base_month : int, optional
        The base month of the search (the default is the month at runtime).

    Returns
    -------
    int
        The the closest year and month that meets
        ``datetime(year, month, day).weekday() == dow```.

    Raises
    ------
    NotFoundError
        If the year or month is not found.

    Notes
    -----
    Given a combination of day and day of the week that exist, the year and month are
    always found.

    Examples
    --------
    February 17, 2021 is a Wednesday (dow = 2).

    >>> year_month_from_day_dow(17, 2, 2020, 12)
    (2021, 2)

    Note that June 17, 2020 is also a Wednesday, but February 2021 will be adopted
    because it is closer to December 2020.
    """
    if base_year is None:
        base_year = datetime.date.today().year
    if base_month is None:
        base_month = datetime.date.today().month

    for year, month in _years_months_close_to(base_year, base_month):
        # MEMO: It is always found within +-20 from the base year and base month.
        try:
            if datetime.date(year, month, day).weekday() == dow:
                return year, month
        except ValueError:
            # February 29th of a non-leap year.
            continue

    raise NotFoundError(
        f"could not find the year and month: ({day}, {dow}; {base_year}, {base_month})"
    )
