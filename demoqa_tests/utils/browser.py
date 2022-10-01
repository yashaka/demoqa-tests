from selene.support.shared import browser

from demoqa_tests.utils.selene import command


def scroll_one_page():
    browser.perform(command.js.scroll_one_page)
