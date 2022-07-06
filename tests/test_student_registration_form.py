from selene import have, command
from selene.support.shared import browser
from demoqa_tests.controls import dropdown, TagsInput


# from demoqa_tests.controls import tags_input


def given_student_registration_form_opened():
    browser.open('/automation-practice-form')
    (
        browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
        .with_(timeout=10)
        .should(have.size_greater_than_or_equal(3))
        .perform(command.js.remove)
    )


def test_register_student():
    given_student_registration_form_opened()

    # WHEN
    browser.element('#firstName').type('Harry')
    browser.element('#lastName').type('Potter')
    browser.element('#userEmail').type('theboywholived@hogwarts.edu')

    gender = browser.element('#genterWrapper')
    gender.all('.custom-radio').element_by(have.exact_text('Male')).click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element(
        '.react-datepicker__month-select'
    ).all('option').element_by(have.exact_text('July')).click()
    browser.element(
        '.react-datepicker__year-select'
    ).all('option').element_by(have.exact_text('1980')).click()
    browser.element(f'.react-datepicker__day--0{31}').click()
    '''
    # OR:
    browser.element('#dateOfBirthInput').perform(command.js.set_value('31 Jul 1980'))
    '''

    subjects = TagsInput(browser.element('#subjectsInput'))

    subjects.add('Chem', autocomplete='Chemistry').add('Maths')
    '''
    # OR:
    subjects = browser.element('#subjectsInput')
    tags_input.add(subjects, from_='Chem', autocomplete='Chemistry')
    tags_input.add(subjects, from_='Maths')
    '''

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

    browser.element(
        '#currentAddress'
    ).type('4 Privet Drive').perform(command.js.scroll_into_view)

    dropdown.autocomplete(browser.element('#state'), option='Uttar Pradesh')
    dropdown.autocomplete(browser.element('#city'), option='Lucknow')
    '''
    # OR (future version):
    Dropdown(browser.element('#state')).select('Uttar Pradesh')
    Dropdown(browser.element('#city')).select('Lucknow')
    
    # OR (first version):
    select.by_choose(browser.element('#state'), option='Uttar Pradesh')
    select.by_autocomplete(browser.element('#city'), option='Lucknow')
    '''

    subjects.add('Physics')

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(
        have.text('Thanks for submitting the form')
    )

    def cells_of_row(index):
        return browser.element(
            '.modal-content .table'
        ).all('tbody tr')[index].all('td')

    cells_of_row(0).should(have.exact_texts('Student Name', 'Harry Potter'))
    cells_of_row(1).should(have.exact_texts('Student Email', 'theboywholived@hogwarts.edu'))
    cells_of_row(2).should(have.exact_texts('Gender', 'Male'))
    cells_of_row(3).should(have.exact_texts('Mobile', '1234567890'))
    cells_of_row(4).should(have.exact_texts('Date of Birth', '31 July,1980'))
    cells_of_row(5).should(have.exact_texts('Subjects', 'Chemistry, Maths, Physics'))
    cells_of_row(6).should(have.exact_texts('Hobbies', 'Sports, Reading, Music'))
    cells_of_row(7).should(have.exact_texts('Picture', 'pexels-vinicius-vieira-ft-3151954.jpg'))
    cells_of_row(8).should(have.exact_texts('Address', '4 Privet Drive'))
    cells_of_row(9).should(have.exact_texts('State and City', 'Uttar Pradesh Lucknow'))


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
