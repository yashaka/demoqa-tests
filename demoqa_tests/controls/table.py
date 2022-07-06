from typing import Optional, Union

from selene.core.entity import Element
from selene.support.shared import browser


class Table:

    def __init__(self, element: Element = ...):
        self.element = element if element is not ... else browser.element('.table')
        '''
        # OR if default is None
        self.element = element if element else browser.element('.table')
        self.element = element or browser.element('.table')
        '''

    def cell(self, row_index: int, column_index: int):
        return self.cells_of_row(row_index)[column_index]

    def cells_of_row(self, index):
        return self.rows[index].all('td')

    @property
    def rows(self):
        return self.element.all('tr')

    def __getitem__(
        self, index_or_slice: int | slice
    ) -> Element:
        if isinstance(index_or_slice, slice):
            return self.cell(
                index_or_slice.start, index_or_slice.stop
            )

        return self.rows[index_or_slice]
