from selene.support.shared import browser
from selene import have, command, by, be

from demoqa_tests.utils import path
from demoqa_tests.utils.common import flatten
from tests.test_data.users import yuri


def test_fail_to_submit_form():
    given_opened_form()

    # todo: implement


def test_submit_student_registration_form():

    given_opened_form()

    # WHEN

    browser.element('#firstName').type(yuri.name)
    browser.element('#lastName').type(yuri.last_name)
    browser.element('#userEmail').type(yuri.email)

    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()

    browser.all('[for^=gender-radio]').by(
        have.exact_text(yuri.gender.value)
    ).first.click()
    '''
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('[id^=gender-radio][value=Male]').element(
        './following-sibling::*'
    ).click()
    # OR better:
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    # OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
    '''
    browser.element('#userNumber').type(yuri.user_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(yuri.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(yuri.birth_year)
    browser.element(
        f'.react-datepicker__day--0{yuri.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    for subject in yuri.subjects:
        browser.element('#subjectsInput').type(subject.value).press_tab()

    for hobby in yuri.hobbies:
        '''
        # not good
        browser.element(f'//label[contains(.,"{hobby.value}")]').click()
        # better
        browser.element(by.text(hobby.value, tag='label')).click()
        # often the best would be closer to:
        '''
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()

    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(yuri.picture_file)
    )

    browser.element('#currentAddress').type(yuri.current_address)
    state = browser.element('#state')

    state.perform(command.js.scroll_into_view)

    select_dropdown(state, yuri.state)

    state.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(yuri.state)
    ).first.click()

    select_dropdown(browser.element('#city'), yuri.city)

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(yuri.city)
    ).first.click()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
    '''
    # OR (if you allow yourself to check app texts)
    browser.element('[id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form')
    )
    '''

    should_have_dialog_results(
        ('Student Name', f'{yuri.name} {yuri.last_name}'),
        ('Student Email', yuri.email),
        ('Gender', yuri.gender.value),
        ('Mobile', yuri.user_number),
        ('Date of Birth', f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}'),
        ('Subjects', ', '.join([subject.value for subject in yuri.subjects])),
        ('Hobbies', ', '.join([hobby.name for hobby in yuri.hobbies])),
        ('Picture', yuri.picture_file),
        ('Address', yuri.current_address),
        ('State and City', f'{yuri.state} {yuri.city}'),
    )
    '''
    # option 1 without helper
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(
            'Student Name',
            f'{yuri.name} {yuri.last_name}',
            'Student Email',
            yuri.email,
            'Gender',
            yuri.gender.value,
            'Mobile',
            yuri.user_number,
            'Date of Birth',
            f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}',
            'Subjects',
            ', '.join([subject.value for subject in yuri.subjects]),
            'Hobbies',
            ', '.join([hobby.name for hobby in yuri.hobbies]),
            'Picture',
            yuri.picture_file,
            'Address',
            yuri.current_address,
            'State and City',
            f'{yuri.state} {yuri.city}',
        )
    )
    
    # option 1.2 without helper for assertion but with helper to flatten "table" to list
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(
            *flatten(
                ('Student Name', f'{yuri.name} {yuri.last_name}'),
                ('Student Email', yuri.email),
                ('Gender', yuri.gender.value),
                ('Mobile', yuri.user_number),
                ('Date of Birth', f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}'),
                ('Subjects', ', '.join([subject.value for subject in yuri.subjects])),
                ('Hobbies', ', '.join([hobby.name for hobby in yuri.hobbies])),
                ('Picture', yuri.picture_file),
                ('Address', yuri.current_address),
                ('State and City', f'{yuri.state} {yuri.city}'),
            )
        )
    )

    # option 2 without helper
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').even.should(
        have.exact_texts(
            f'{yuri.name} {yuri.last_name}',
            yuri.email,
            yuri.gender.value,
            yuri.user_number,
            f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}',
            ', '.join([subject.value for subject in yuri.subjects]),
            ', '.join([hobby.name for hobby in yuri.hobbies]),
            yuri.picture_file,
            yuri.current_address,
            f'{yuri.state} {yuri.city}',
        )
    )
    '''


def given_opened_form():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)


def select_dropdown(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()


def should_have_dialog_results(*data):
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    for name, value in data:
        rows.element_by(have.text(name)).all('td')[1].should(have.exact_text(value))
    '''
    # just one more option to implement it, partially using XPath
    for name, value in data:
        rows.all('td').element_by(have.exact_text(name)).element(
            './following-sibling::td'
        ).should(have.exact_text(value))
    # more precise implementation, corresponding to fn name (if fn was named as should_have_table):
    for index, (name, value) in enumerate(data):
        row_cells = rows[index].all('td')
        row_cells[0].should(have.exact_text(name))
        row_cells[1].should(have.exact_text(value))
    # precise and KISS version:
    flatten_data = [name_or_value for row in data for name_or_value in row]
    rows.all('td').should(have.exact_texts(*flatten_data))
    # pretty KISS but skipping field names to check...
    # (here we should rename fn at least to something like `should_have_table_with(data)`)
    values = [value for row in data for value in row[1::2]]
    rows.all('td').even.should(have.exact_texts(*values))
    # same but more self-documented:
    even = slice(1, None, 2)
    values = [value for row in data for value in row[even]]
    rows.all('td').even.should(have.exact_texts(*values))
    # or with helper 
    from demoqa_test.utils.common import flatten
    rows.all('td').even.should(have.exact_texts(*flatten(data)))
    '''
