from selene.support.shared import browser
from selene import have
from selene import command
from demoqa_tests import resource
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Olga').fill_last_name('YA')
    browser.element('#userEmail').type('name@example.com')

    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()

    browser.element('#userNumber').type('1234567891')

    registration_page.fill_date_of_birth('1999', 'May', '11')

    browser.element('#subjectsInput').type('Computer Science').press_enter()

    browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

    browser.element('#uploadPicture').set_value(resource.path('foto.jpg'))

    browser.element('#currentAddress').type('Moscowskaya Street 18')

    registration_page.fill_state('NCR')

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.should_registered_user_with(
        'Olga YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )
    '''
    # example of implementing assertion-free pageobjects
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
    '''
