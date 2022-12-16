from selene import have
from selene.support.shared import browser


def select(selector, /, *, by_text):
    browser.element(selector).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(by_text)
    ).click()
