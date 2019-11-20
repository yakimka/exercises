import datetime
from enum import IntEnum
from itertools import count, takewhile


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year: int, month: int, nth: int = 4, weekday: int = 3) -> datetime.date:
    nth = nth - 1 if nth > 0 else nth
    date = datetime.date(year=year, month=month, day=1)
    first_day_weekday = date.weekday()
    first_day = 1 + weekday - first_day_weekday
    if first_day < 1:
        first_day += 7
    all_days = all_days_of_weekday(first_day, last_day_of_month(date))
    return datetime.date(year=year, month=month, day=all_days[nth])


def all_days_of_weekday(start: int, stop: int) -> list:
    return list(takewhile(lambda x: x <= stop, count(start, 7)))


def last_day_of_month(any_day: datetime.date) -> int:
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return (next_month - datetime.timedelta(days=next_month.day)).day
