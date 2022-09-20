from selene.support.shared import browser

from demoqa_tests.model.controls import dropdown


def test_save_document():
    # documents_dashboard.given_opened()

    ...

    dropdown.select(browser.element('#document-type'), 'pdf')

    ...
