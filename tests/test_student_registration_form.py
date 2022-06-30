from typing import Optional

from selene import have, command
from selene.core.entity import SeleneElement
from selene.support.shared import browser


def given_student_registration_form_opened():
    browser.open('/automation-practice-form')
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]').with_(timeout=10)
        .should(have.size_greater_than_or_equal(2))
        .perform(command.js.remove)
    )


def select(element: SeleneElement, /, *, option: str):  # todo: consider option_text
    element.click()
    element.all('option').element_by(have.exact_text(option)).click()


def autocomplete(element: SeleneElement, /, *, from_: str, to: Optional[str] = None):
    element.type(from_)
    browser.all(
        '.subjects-auto-complete__option'
    ).element_by(have.text(to or from_)).click()


def resource(relative_path):
    import demoqa_tests
    from pathlib import Path
    return (
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )


def test_register_student():
    given_student_registration_form_opened()

    # WHEN
    browser.element('#firstName').type('Harry')
    browser.element('#lastName').type('Potter')
    browser.element('#userEmail').type('theboywholived@hogwarts.edu')

    browser.element('#genterWrapper').all(
        '.custom-radio'
    ).element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    # browser.element('#dateOfBirthInput').setValue('31 Jul 1980')
    browser.element('#dateOfBirthInput').click()
    select(browser.element('.react-datepicker__month-select'), option='July')
    select(browser.element('.react-datepicker__year-select'), option='1980')
    browser.element(f'.react-datepicker__day--0{31}').click()

    autocomplete(browser.element('#subjectsInput'), from_='Chem', to='Chemistry')
    autocomplete(browser.element('#subjectsInput'), from_='Maths')

    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()
    browser.all('.custom-checkbox').element_by(have.exact_text('Music')).click()
    '''
    # OR
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.text('Sports')).click()
    # OR
    sports_hobby = browser.element('[for=hobbies-checkbox-1]')
    sports_hobby.click()

    ...
    '''

    browser.element('#uploadPicture').send_keys(
        resource('pexels-vinicius-vieira-ft-3151954.jpg')
    )

    browser.element('#currentAddress').type('4 Privet Drive')

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text('Uttar Pradesh')).click()
    browser.element('#city').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text('Lucknow')).click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    def cells_of_row(index):
        return browser.element('.modal-content .table').all('tbody tr')[index].all('td')

    cells_of_row(0).should(have.texts('Student Name', 'Harry Potter'))
    cells_of_row(1).should(have.texts('Student Email', 'theboywholived@hogwarts.edu'))
    cells_of_row(2).should(have.texts('Gender', 'Male'))
    cells_of_row(3).should(have.texts('Mobile', '1234567890'))
    cells_of_row(4).should(have.texts('Date of Birth', '31 July,1980'))
    cells_of_row(5).should(have.texts('Subjects', 'Chemistry, Maths'))
    cells_of_row(6).should(have.texts('Hobbies', 'Sports, Reading, Music'))
    cells_of_row(7).should(have.texts('Picture', 'pexels-vinicius-vieira-ft-3151954.jpg'))
    cells_of_row(8).should(have.texts('Address', '4 Privet Drive'))
    cells_of_row(9).should(have.texts('State and City', 'Uttar Pradesh Lucknow'))
