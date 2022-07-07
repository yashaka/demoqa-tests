from selene import command, have
from selene.support.shared import browser

from demoqa_tests.data import User
from demoqa_tests.model.controls import TagsInput


class StudentRegistrationForm:

    '''
    # Also possible but one can shoot in his leg;) so be careful with this style
    first_name = browser.element('#firstName')
    last_name = browser.element('#lastName')
    subjects = TagsInput('subjectsInput')
    submit = browser.element('#submit')
    '''

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.subjects = TagsInput.by_name('subjectsInput')
        self.submit_button = browser.element('#submit')

    '''
    def set_first_name(self, value):
        browser.element('#firstName').type('Harry')
        return self

    def set_last_name(self, value):
        browser.element('#lastName').type('Potter')
        return self
    '''

    def add_subjects(self, *names):
        for name in names:
            self.subjects.add(name)
        return self

    def should_have_subjects(self, *names):
        """
        # look how this step-method already looks as redundant
        subjects.should_have_texts(*names)
        # is already a good code to be used in test;)
        """
        self.subjects.should_have_texts(*names)
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)

    def fill_form(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        '''
        # could be like this too (yet might be considered as over-engineering):
        self.set_first_name(first_name).set_last_name(last_name).addSubjects(*subjects)
        '''

        # self.subjects.autocomplete(*user.subjects)

        # todo: finish implementation

        return self
