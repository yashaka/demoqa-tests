from typing import Optional, Union

from selene.core.entity import Element
from selene.support.shared import browser


class Cell:

    def __init__(self, element: Element):
        self.element = element

    def start_editing(self):
        self.element.double_click()
        return self

    @property
    def input(self):
        return self.element.element('.input')

    def set(self, value):
        self.input.set_value(value)
        return self

    def save(self):
        self.input.press_enter()
        return self


class Table:

    def __init__(self, element: Element = ...):
        self.element = element if element is not ... else browser.element('.table')
        '''
        # OR if default is None
        self.element = element if element else browser.element('.table')
        self.element = element or browser.element('.table')
        '''

    def cell(self, row_index: int, column_index: int):
        return Cell(self.cells_of_row(row_index)[column_index])

    def cells_of_row(self, index):
        return self.rows[index].all('td')

    @property
    def rows(self):
        return self.element.all('tr')

    # def __getitem__(
    #     self, index_or_slice: int | slice
    # ) -> Element:
    #     if isinstance(index_or_slice, slice):
    #         return self.cell(
    #             index_or_slice.start, index_or_slice.stop
    #         )
    #
    #     return self.rows[index_or_slice]
