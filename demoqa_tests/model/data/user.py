import datetime
from dataclasses import dataclass
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


'''
class User:

    def __init__(self, *, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
'''


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
