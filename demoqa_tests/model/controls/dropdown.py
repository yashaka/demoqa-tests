from selene.support.shared import browser
from selene import be, have


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').element_by(
        have.exact_text(f'{option}')
    ).click()
