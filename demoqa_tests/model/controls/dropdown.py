from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


def select(element: Element, /, *, option: str):  # todo: consider option_text
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def autocomplete(element: Element, /, *, option: str):  # todo: consider option_text
    element.element(
        '[id^=react-select-][id*=-input]'
    ).type(option).press_tab()
