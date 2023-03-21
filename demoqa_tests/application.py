from selene.support.shared import browser

from demoqa_tests.model.components import Panel
from demoqa_tests.model.pages.profile_page import ProfilePage
from demoqa_tests.model.pages.simple_user_registration_page import (
    SimpleUserRegistrationPage,
)


class Application:
    def __init__(self):
        self.simple_registration = SimpleUserRegistrationPage()
        self.profile = ProfilePage()
        self.panel = Panel()

    def open(self):
        browser.open('/')
        return self


app = Application()
