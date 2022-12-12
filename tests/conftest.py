import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    '''
    # consider checking that everything will work in ff too
    browser.config.browser_name = 'firefox'
    # to find bugs when input fields are covered by other elements when typing
    browser.config.wait_for_no_overlap_found_by_js = True
    '''

    yield

    browser.quit()
