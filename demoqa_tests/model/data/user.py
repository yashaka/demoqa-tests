import datetime
from enum import Enum

import demoqa_tests


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3


class Hobby(Enum):
    Music = 'Music'
    Reading = 'Reading'
    Sports = 'Sports'


def format_input_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_input_format)


def format_view_date(value: datetime.date):
    return value.strftime(demoqa_tests.config.datetime_view_format)
