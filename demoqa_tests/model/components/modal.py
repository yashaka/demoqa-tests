from selene.support.shared import browser

from demoqa_tests.model.controls import table

dialog = browser.element('.modal-content')
rows = table.rows(inside=dialog)
