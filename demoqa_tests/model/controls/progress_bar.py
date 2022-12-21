from selene import be
from selene.support.shared import browser


def wait_for_loading():
    browser.element('#loading').should(be.not_.visible)
