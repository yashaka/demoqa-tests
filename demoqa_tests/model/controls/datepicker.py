import datetime

import selene
from selenium.webdriver.common.keys import Keys
from demoqa_tests.model.data import user
import sys


class DatePicker:
    # formatting = '%d %b %Y'

    def __init__(self, element: selene.Element):
        self.element = element

    def set_date(self, date: datetime.date):
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(
            modifier_key + 'a' + Keys.NULL,
            user.format_input_date(date),
            # date.strftime(DatePicker.formatting)
        ).press_enter()
        return self

    def assert_value(self, date: datetime.date):
        """
        just an example for advocates of including assertions into PageObjects
        see https://martinfowler.com/bliki/PageObject.html for more details
        """
        self.element.should(selene.have.value(user.format_input_date(date)))
        return self

