from selene.support.shared import browser
from selene import command, have


def test_submit_text_box_form():
    browser.open('https://demoqa.com/text-box')
    browser.all(
        '[id^=google_ads_iframe_][id$=__container__]'
    ).should(have.size_greater_than_or_equal(2)).perform(command.js.remove)
    '''
    # just examples of other options showing javascript usage
    # ...
    # remove one element via executing java script
    browser.element('[id^=google_ads_iframe_][id$=__container__]').execute_script('element.remove()')
    # remove all elements via executing java script that finds and removes element by itself
    browser.execute_script(
        'document.querySelectorAll("[id^=google_ads_iframe_][id$=__container__]").forEach(element => element.remove())'
    )
    # find all elements by selene and then remove EACH by javascript on element
    for element in browser.all(
        '[id^=google_ads_iframe_][id$=__container__]'
    ):
        element.execute_script('element.remove()')
    # find all elements by selene and then remove EACH by javascript on browser
    for element in browser.all(
        '[id^=google_ads_iframe_][id$=__container__]'
    ):
        browser.execute_script('arguments[0].remove()', element.locate())

    # find all elements by selene and then remove ALL by javascript
    browser.execute_script(
        'arguments[0].forEach(element => element.remove())',
        browser.all('[id^=google_ads_iframe_][id$=__container__]').locate()
    )
    '''

    browser.element('#userName').type('yashaka')
    ''' 
    # raw webdriver version:
    from selenium.webdriver.common.by import By
    browser.driver.find_element(By.CSS_SELECTOR, '#userName').send_keys('yashaka')
    '''
    # was not shown at lesson, but here how this test may finish:
    browser.element('#userEmail').type('yashaka@gmail.com')
    browser.element('#currentAddress').type('Earth')
    browser.element('#permanentAddress').type('Universe & abroad')
    browser.element('#submit').click()

    browser.all('#output p').should(have.texts(
        'yasha',
        'yashaka@gmail.com',
        'Earth',
        'Universe & abroad',
    ))


'''
# example of more complex extra commands (via raw selenium webdriver):
from selenium.webdriver import ActionChains
ActionChains(browser.driver).drag_and_drop(browser.element('from').locate(), browser.element('to').locate())
'''
