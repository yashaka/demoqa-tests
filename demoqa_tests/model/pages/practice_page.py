from selene.support.shared import browser

import demoqa_tests
from demoqa_tests import utils
from demoqa_tests.model import google
from demoqa_tests.model.controls import (
    dropdown,
    radio_button,
    datepicker,
    checkbox,
    file_input,
)
from demoqa_tests.model.components import modal
from selene import command, have

from demoqa_tests.model.data import user
import datetime
from demoqa_tests import have
from demoqa_tests.utils.selene import command

birthday = browser.element('#dateOfBirthInput')


def open():  # noqa
    browser.open('/automation-practice-form')
    google.remove_ads(amount=3, timeout=6)
    google.remove_ads(amount=1, timeout=2)


def fill_name(firstname: str, lastname: str):
    browser.element('#firstName').type(firstname)
    browser.element('#lastName').type(lastname)


def fill_email(value: str):
    browser.element('#userEmail').type(value)


def fill_phone(phone: str):
    browser.element('#userNumber').type(phone)


def fill_subjects(*subjects: str):
    for item in subjects:
        browser.element('#subjectsInput').type(item).press_enter()


def fill_address(address):
    browser.element('#currentAddress').type(address)


def select_state(state: str):
    utils.browser.scroll_one_page()
    dropdown.select(browser.element('#state'), state)


def select_city(city: str):
    dropdown.select(browser.element('#city'), city)


def submit_form():
    # utils.browser.scroll_one_page()
    # browser.element('#submit').click()
    browser.element('#submit').perform(command.js.click)


def assert_form_sent(*data):
    for name, value in data:
        value = (
            user.format_view_date(value) if isinstance(value, datetime.date) else value
        )
        modal.rows.element_by(have.text(name)).all('td')[1].should(
            have.exact_text(value)
        )


def fill_gender(value: user.Gender):
    radio_button.set_option('gender', value.value)  # noqa


def fill_birthday(date: datetime.date):
    datepicker.set_date(birthday, date)


def assert_filled_birthday(date: datetime.date):
    birthday.should(have.date(date))
    # datepicker.assert_value(birthday, date)
    # """
    # just an example for advocates of including assertions into PageObjects
    # see https://martinfowler.com/bliki/PageObject.html for more details
    # """


def fill_hobbies(*options: user.Hobby):
    checkbox.check_options(
        browser.all('[for^=hobbies-checkbox]'), *[option.value for option in options]
    )


def select_picture(relative_path):
    file_input.upload('../resources/picture.png')
