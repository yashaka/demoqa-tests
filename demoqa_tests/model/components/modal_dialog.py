from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls.table import Table


class ModalDialog:
    def __init__(self):
        self.element = browser.element('.modal-dialog')
        self.table = Table(self.element.element('.table'))

    def should_have_row_with_exact_texts(self, *values):
        self.table.cells_of_row(1).should(have.exact_texts('Student Name', 'Harry Potter'))
