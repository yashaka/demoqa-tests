from selene.support.shared import browser
from selene import have
import os
import tests
import demoqa_tests.model.controls.dropdown
from demoqa_tests.model.pages import practice_form
from demoqa_tests.model.controls.dropdown import select


def test_student_registration_form():
    practice_form.given_opened()

    # WHEN
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('YA')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    '''
    # some other variations to do the same
    browser.all('[name=gender]').element_by(have.value('Female')).element(
        './following-sibling::*'
    ).click()
    browser.element('[name=gender][value=Female]+label').click()
    browser.element('[name=gender][value=Female]').element('..').click()
    browser.element('[value=Female]+label').click()
    browser.element('[value=Female]').element('..').click()
    browser.all('.custom-radio').element_by(have.text('Female')).click()
    browser.all('[for^=gender-radio]').element_by(have.text('Female')).click()
    browser.all('[for^=gender-radio]').element_by(have.exact_text('Female')).click()
    '''
    browser.element('#userNumber').type('1234567891')
    browser.element('#userEmail').type('name@example.com')

    # todo: consider refactoring the order of the following steps
    #       to be more straightforward (one by one from top to bottom)
    #       and so more natural in context of «happy path»

    # todo: refactor to select by text proper checkbox
    browser.element('[for=hobbies-checkbox-2]').click()
    '''
    # not needed when scaling:
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    '''

    browser.element('#currentAddress').type('Moscowskaya Street 18')
    '''
    # just an example of using by_js ;)
    browser.element('#currentAddress').with_(set_value_by_js=True).set_value('Moscowskaya Street 18')
    browser.element('#currentAddress').perform(command.js.set_value('Moscowskaya Street 18'))
    '''

    practice_form.select_state('NCR')
    select('#city', 'Delhi')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    '''
    # will not work in firefox
    browser.element('.react-datepicker__month-select').type('May')
    '''
    browser.element('.react-datepicker__month-select').all('option').element_by(
        have.exact_text('May')
    ).click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').all('option').element_by(
        have.exact_text('1999')
    ).click()
    '''
    # will not work in firefox
    browser.element('.react-datepicker__year-select').type('1999')
    '''
    browser.element(f'.react-datepicker__day--0{11}').click()
    '''
    # potentially more stable:
    browser.element(
        f'.react-datepicker__day--0{11}:not(.react-datepicker__day--outside-month)'
    ).click()
    # potentially more optimal:
    from selenium.webdriver import Keys
    browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND, 'a').type(
        '11 May 1999'
    ).press_enter()
    # even more versatile:
    import sys
    browser.element('#dateOfBirthInput').send_keys(
        Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a'
    ).type('11 May 1999').press_enter()
    '''

    browser.element('#subjectsInput').type('Computer Science')
    '''
    # if we want to test that correct partial phrase will be auto-completed
    browser.element('#subjectsInput').type('Compu')
    '''
    browser.all('.subjects-auto-complete__option').element_by(
        have.exact_text('Computer Science')
    ).click()
    # browser.element('#uploadPicture').set_value(resource.path('foto.jpg'))
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )
    '''
    # Using pathlib module:
    browser.element('#uploadPicture').set_value(
        str(Path(tests.__file__).parent.joinpath('resources/foto.jpg').absolute())
    )
    browser.element('#uploadPicture').set_value(
        str(Path(resources.__file__).joinpath('foto.jpg').absolute())
    )
    # BAD versions (because tightly coupled with dir from where the test was started):
    browser.element('#uploadPicture').set_value(os.path.abspath('../resources/foto.jpg'))
    '''

    practice_form.submit()
    '''
    # not needed when scaling:
    browser.element('#submit').press_enter()
    # as this also:
    # OR maybe more obvious:
    browser.element('#submit').perform(command.js.click)
    '''

    # THEN
    '''
    # can be considered as additional check:
    browser.element('[id=example-modal-sizes-title-lg]').should(be.visible)
    # OR (if you allow yourself to check app texts)
    browser.element('[id=example-modal-sizes-title-lg]').should(
        have.text('Thanks for submitting the form')
    )
    '''
    browser.element('.table').all('td').even.should(
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
    # same but harder to debug errors ##########################################
    # because the selector is not broken down into smaller pieces
    browser.all('.table td:nth-of-type(2)').should(
        have.texts(
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
    # pay also attention to the difference 
    # between have.texts and have.exact_texts
    # exact_texts is more strict, and sometimes better in context of Test Design
    ############################################################################
    
    # The most detailed assertion, ##########################################
    # checking also relevance of the data to the field name
    # but unfortunately tightly coupled with TEXT from UI, 
    # that might be more unstable in context of functional testing
    browser.element('.table').all('td').should(
        have.texts(
            ('Student Name', 'Olga YA'),
            ('Student Email', 'name@example.com'),
            ('Gender', 'Female'),
            ('Mobile', '1234567891'),
            ('Date of Birth', '11 May,1999'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Reading'),
            ('Picture', 'foto.jpg'),
            ('Address', 'Moscowskaya Street 18'),
            ('State and City', 'NCR Delhi'),
        )
    )
    #########################################################################
    
    # can have problems with formatting by tools like black;) ###############
    browser.element('.table').all('td').should(have.texts(
        'Student Name', 'Olga YA',
        'Student Email', 'name@example.com',
        'Gender', 'Female',
        'Mobile', '1234567891',
        'Date of Birth', '11 May,1999',
        'Subjects', 'Computer Science',
        'Hobbies', 'Reading',
        'Picture', 'foto.jpg',
        'Address', 'Moscowskaya Street 18',
        'State and City', 'NCR Delhi'
    ))
    #########################################################################
        
    # INVALID: ##############################################################
    browser.element('.table').should(
        have.text(
            'Olga YA'
            and 'name@example.com'
            and 'Female'
            and '1234567891'
            and '11 May,1999'
            and 'Computer Science'
            and 'Reading'
            and 'foto.jpg'
            and 'Moscowskaya Street 18'
            and 'NCR Delhi'
        )
    )
    # !!! because any ('one' and 'two' and 'three' and 'so on') 
    # will result in the only last string, i.e. 'so on' from the last example
    #########################################################################
    # But shis should work OK:
    browser.element('.table').should(
        have.text('Olga YA')
        .and_(have.text('name@example.com'))
        .and_(have.text('Female'))
        .and_(have.text(1234567891))
        .and_(have.text('11 May,1999'))
        .and_(have.text('Computer Science'))
        .and_(have.text('Reading'))
        .and_(have.text('foto.jpg'))
        .and_(have.text('Moscowskaya Street 18'))
        .and_(have.text('NCR Delhi'))
    )
    # just keep in mind that it will not check the correct order 
    # and place of the text inside the table...
    #########################################################################
    
    # maybe in future we can be more precise on what we check: #################
    browser.element('.modal-content').element('.table').all('tr').should(...)
    browser.element('.modal-content').element('.table').all('tr').all('td').should(...)
    ############################################################################
    '''
    demoqa_tests.model.controls.dropdown.select


