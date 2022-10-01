import datetime

from selene import have
from selene.support.conditions.have import *  # noqa
from selene.support.conditions.be import *  # noqa

import demoqa_tests


def date(value: datetime.date):  # noqa
    return have.value(value.strftime(demoqa_tests.config.datetime_input_format))
