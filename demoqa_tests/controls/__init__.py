from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
        return self
