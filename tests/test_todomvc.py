from selene import have, be
from selene.support.shared import browser


def test_completes_and_clear_todo():
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').should(be.blank).type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    '''
    # xpath version
    browser.element('//*[@id="todo-list"]/li[.//*[text()="b"]]//*[contains(concat(" ",normalize-space(@class)," ")," toggle ")]').click()
    '''
    browser.all('#todo-list>li').by(have.css_class('completed')).should(have.exact_texts('b'))
    browser.all('#todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))
    '''
    # compare to version without «selector break down for faster error analysis»
    # that is more concise but will be harder to maintain on failures (find error cause)
    browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))
    '''

    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))


def test_todos_storage_is_not_shared_between_browsers(with_new_browser):
    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser2 = with_new_browser()
    browser2.open('https://todomvc.com/examples/emberjs/')
    browser2.element('#new-todo').type('d').press_enter()

    browser2.all('#todo-list>li').should(have.exact_texts('d'))
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser3 = with_new_browser('firefox')
    browser3.open('https://todomvc.com/examples/emberjs/')
    browser3.element('#new-todo').type('e').press_enter()

    browser3.all('#todo-list>li').should(have.exact_texts('e'))
    browser2.all('#todo-list>li').should(have.exact_texts('d'))
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))
