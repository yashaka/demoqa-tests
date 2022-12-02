from selene.support.shared import browser
from selene import be, have, by


def test_finds_selene():
    browser.open('https://www.google.com/ncr').should(have.title('Google'))
    browser.element('[name=q]').type('selene').press_enter()
    '''
    # OR:
    browser.element(by.name('q')).type('selene').press_enter()
    # OR with assertion of empty value or text + set_value command that does clear + type at once:
    browser.element('[name=q]').should(be.blank).set_value('selene').press_enter()
    '''
    browser.element('#search').should(have.text('User-oriented Web UI browser tests'))
    '''
    # OR:
    browser.element(by.id('search')).should(have.text('User-oriented Web UI browser tests'))
    # but using # as shortcut for "by id" in css selector - is more concise, yet natural in frontend world
    '''

    results = browser.all('#rso>div')
    results.should(have.size_greater_than_or_equal(6))


def test_finds_selene_with_refined_query():
    browser.open('https://www.google.com/ncr')
    browser.element('[name=q]').type('selene').press_enter()
    '''
    # compare to XPath
    browser.element('//*[name="q"]').type('selene').press_enter()
    '''

    results = browser.all('#rso>div')
    '''
    # compare to XPath
    results = browser.all('//*[@id="rso"]/div')
    '''
    results.should(have.size_greater_than_or_equal(6))

    browser.element('[name=q]').type(' yashaka github').press_enter()
    results.should(have.size_greater_than_or_equal(6))
    results.first.element('h3').click()
    browser.should(have.title_containing('yashaka/selene'))

