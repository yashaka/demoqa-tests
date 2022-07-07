from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:

    @staticmethod
    def by_name(value):
        return TagsInput(browser.element(
            f'#{value},[name={value}],[name*={value}],[id*={value}],.{value},[testID={value}'
        ))

    def __init__(self, element: Element):
        self.element = element
        self.container = self.element.element(
            './ancestor::*[contains(@id, "Wrapper")]'
        )
        '''
        yep:) here goes xpath:)
        but... better would be completely to refactor our control page-object
        to accept in __init__ the element that is a container of all elements
        not an inner input ;)
        then we can separately find the an input inside a container and values
        think on how to refactor this code;)
        '''
        self.value_labels = self.container.all(
            '[class*=-auto-complete__multi-value__label]'
        )

    # @property
    # def element(self):
    #     return browser.element(self.selector)

    def should_have_texts(self, *values):
        self.value_labels.should(have.exact_texts(*values))

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
        return self

    def autocomplete(self, *values):
        for value in values:
            self.element.type(value).press_tab()


'''
# example of usage:
TagsInput(browser.element('#subjectsInput'))

TagsInput.by_name('subjects')
'''
