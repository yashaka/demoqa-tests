import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 3
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'  # or 'firefox' or 'edge' or 'opera'
    browser.config.window_width = 1200
    browser.config.window_height = 900

    yield
