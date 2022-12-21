from datetime import date, datetime

from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model import controls
from demoqa_tests.model.controls import dropdown, radio, checkboxes, datepicker

'''
submit = browser.element('#submit')
'''

# _submit = browser.element('#submit')
_validations = browser.all('.validation')

def given_opened():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
    '''
    # might be also needed:
    '''
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    ads.perform(command.js.remove)

'''
def select_gender(gender):
    browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
'''

gender = 'gender'
hobbies = browser.all('[for^=hobbies-checkbox]')

def select_gender(gender):
    radio.select('gender', by_value=gender)


def select_hobbies(*texts: str):
    checkboxes.select(hobbies, by_texts=texts)


def submit():
    browser.element('#submit').click()


def submit_data(first_name, last_name, hobbies):
    """todo: implement"""
    # select_hobbies(hobbies)
    # radio.select(...)
    # checkboxes.select(..)
    # datepicker.select(...)


def select_birthday(*, month, year, day):
    datepicker.select('#dateOfBirthInput', month=month, year=year, day=day)


def should_have_validations_of_number(number: int):
    _validations.should(have.size(number))


def should_have_validation_errors():
    _validations.should(have.size_greater_than(0))


def select_state(value):
    dropdown.select('#state', by_text=value)
