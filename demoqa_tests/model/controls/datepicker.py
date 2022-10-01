import datetime

import selene
from selenium.webdriver.common.keys import Keys
from demoqa_tests.model.data import user
import sys


def set_date(element: selene.Element, date: datetime.date):
    modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    element.send_keys(
        modifier_key + 'a' + Keys.NULL,
        user.format_input_date(date),
    ).press_enter()


# def assert_value(element: selene.Element, date: datetime.date):
#     """
#     just an example for advocates of including assertions into PageObjects
#     see https://martinfowler.com/bliki/PageObject.html for more details
#     """
#     element.should(have.value(user.format_date(date)))
