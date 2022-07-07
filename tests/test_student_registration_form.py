from selene import have, command
from selene.support.shared import browser
from demoqa_tests.data import User
from demoqa_tests.model.application_manager import app
from demoqa_tests.model.controls import dropdown
from demoqa_tests import utils

'''
# Just an example of Fluent PageObject application:
# BAD (with returning main_page from de_login):
sign_in_page.do_login('drako.malfoy@gmail.com', 'Cruc1@tu$').add_post('Potter!!!! you must die!!!')
# GOOD (without Fluent PageObject):
sign_in_page.do_login('drako.malfoy@gmail.com', 'Cruc1@tu$')
main_page.add_post('Potter!!!! you must die!!!')
'''


def test_register_student():
    app.given_student_registration_form_opened()
    harry_potter = User(
        first_name='Harry',
        last_name='Potter',
        subjects=['Chemistry', 'Maths', 'Physics'],
    )

    # WHEN
    app.form.fill_form(harry_potter)
    '''
    # OR:
    app.form.set_first_name('Harry').set_last_name('Potter')
    # somewhere later:
    app.results.should_have_row_with_exact_texts(...)
    '''

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
    
    # Some ideas:
    class Months(Enum):
        September = 8
        Aug = 7

    DatePicker(browser.element('#dateOfBirthInput')).open().select_month(Months.Aug).select_year(1999).select_day(30)
    form.set_birth_date(30, Months.Aug, 1999)
    '''

    '''
    subjects = object.__new__(TagsInput)
    TagsInput.__init__(subjects, browser.element('#subjectsInput'))
    TagsInput.add(subjects, 'Maths')
    '''

    app.form.add_subjects('Chemistry', 'Maths', 'Physics')
    app.form.should_have_subjects('Chemistry', 'Maths', 'Physics')
    '''
    # other versions (but locators are wrong below):
    app.form.subjects.element.should(have.text(''.join(['Chemistry', 'Maths', 'Physics'])))
    app.form.subjects.should_have_texts('Chemistry', 'Maths', 'Physics')
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
        utils.paths.resource('pexels-vinicius-vieira-ft-3151954.jpg')
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

    app.form.submit()

    # THEN
    app.results.should_have_row_with_exact_texts('Student Name', 'Harry Potter')
    '''
    results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    '''

    '''
    # Just an example of cell(1, 2) returning another Cell page-object
    results.cell(1, 2).start_editing().set('new value').save()
    '''

    app.results.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
    app.results.table.cells_of_row(2).should(have.exact_texts('Student Email', 'theboywholived@hogwarts.edu'))
    app.results.table.cells_of_row(3).should(have.exact_texts('Gender', 'Male'))
    app.results.table.cells_of_row(4).should(have.exact_texts('Mobile', '1234567890'))
    app.results.table.cells_of_row(5).should(have.exact_texts('Date of Birth', '31 July,1980'))
    app.results.table.cells_of_row(6).should(have.exact_texts('Subjects', 'Chemistry, Maths, Physics'))
    app.results.table.cells_of_row(7).should(have.exact_texts('Hobbies', 'Sports, Reading, Music'))
    app.results.table.cells_of_row(8).should(have.exact_texts('Picture', 'pexels-vinicius-vieira-ft-3151954.jpg'))
    app.results.table.cells_of_row(9).should(have.exact_texts('Address', '4 Privet Drive'))
    app.results.table.cells_of_row(10).should(have.exact_texts('State and City', 'Uttar Pradesh Lucknow'))


