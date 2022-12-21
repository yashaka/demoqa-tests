from selene import have, Element
from selene.support.shared import browser

from demoqa_tests.utils import string


def select(elements_or_selector_or_name: str | Element, *, by_texts: tuple | list[str]):
    if string.is_word_with_dashes_underscores_or_numbers(elements_or_selector_or_name):
        elements = browser.all(f'[name={elements_or_selector_or_name}],[id={elements_or_selector_or_name}]')
    elif isinstance(elements_or_selector_or_name, str):
        elements = browser.all(elements_or_selector_or_name)
    else:
        elements = elements_or_selector_or_name

    for by_text in by_texts:
        elements.element_by(have.text(by_text)).click()
