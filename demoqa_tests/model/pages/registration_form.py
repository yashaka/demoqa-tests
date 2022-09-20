from typing import Tuple

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, modal
from tests.test_data.users import Subject

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def set_state(value: str):
    dropdown.select(state, value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
