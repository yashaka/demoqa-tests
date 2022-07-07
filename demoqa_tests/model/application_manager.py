from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.components.modal_dialog import ModalDialog
from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm


class ApplicationManager:
    def __init__(self):
        self.form = StudentRegistrationForm()
        self.results = ModalDialog()


    def given_student_registration_form_opened(self):
        browser.open('/automation-practice-form')
        (
            browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
            .with_(timeout=10)
            .should(have.size_greater_than_or_equal(3))
            .perform(command.js.remove)
        )
        return self


app = ApplicationManager()
