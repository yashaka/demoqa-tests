from selene import have, command
from selene.support.shared import browser


def given_opened_text_box_page():
    browser.open('/text-box')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)
        '''
        # more low level version:
        browser.execute_script('document.querySelectorAll("[id^=google_ads_][id$=container__]").forEach(element => element.remove())')
        '''
