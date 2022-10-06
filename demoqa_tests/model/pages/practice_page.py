from selene.support.shared import browser

from demoqa_tests import utils
from demoqa_tests.model import google
from demoqa_tests.model.controls import (
    dropdown,
    radio_button,
    checkbox,
    file_input,
)
from demoqa_tests.model.components import modal
from selene import command, have

from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.data import user
import datetime
from demoqa_tests import have
from demoqa_tests.utils.selene import command


class PracticePage:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))

    def open(self):  # noqa
        browser.open('/automation-practice-form')
        google.remove_ads(amount=3, timeout=6)
        google.remove_ads(amount=1, timeout=2)
        return self

    def fill_name(self, firstname: str, lastname: str):
        browser.element('#firstName').type(firstname)
        browser.element('#lastName').type(lastname)
        return self

    def fill_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def fill_phone(self, phone: str):
        browser.element('#userNumber').type(phone)
        return self

    def fill_subjects(self, *subjects: str):
        for item in subjects:
            browser.element('#subjectsInput').type(item).press_enter()
        return self

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)
        return self

    def select_state(self, state: str):
        utils.browser.scroll_one_page()
        dropdown.select(browser.element('#state'), state)
        return self

    def select_city(self, city: str):
        dropdown.select(browser.element('#city'), city)
        return self

    def submit_form(self, ):
        # utils.browser.scroll_one_page()
        # browser.element('#submit').click()
        browser.element('#submit').perform(command.js.click)
        return self

    def assert_form_sent(self, *data):
        for name, value in data:
            value = (
                user.format_view_date(value) if isinstance(value, datetime.date) else value
            )
            modal.rows.element_by(have.text(name)).all('td')[1].should(
                have.exact_text(value)
            )
        return self

    def fill_gender(self, value: user.Gender):
        radio_button.set_option('gender', value.value)  # noqa
        return self

    def fill_birthday(self, date: datetime.date):
        self.birthday.set_date(date)
        return self

    def assert_filled_birthday(self, date: datetime.date):
        # birthday.should(have.date(date))
        self.birthday.assert_value(date)
        # """
        # just an example for advocates of including assertions into PageObjects
        # see https://martinfowler.com/bliki/PageObject.html for more details
        # """
        return self

    def fill_hobbies(self, *options: user.Hobby):
        checkbox.check_options(
            browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
        )
        return self

    def select_picture(self, relative_path):
        file_input.upload('../resources/picture.png')
        return self
