from selene.support.shared import browser


def set_option(label_prefix: str, number: int):
    browser.element(f'[for={label_prefix}-radio-{number}]').click()
    # browser.all(f'[for^=gender-radio]').element_by(have.text(value)).click()
