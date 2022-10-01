import os

import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def change_test_dir_to_project_root(request, monkeypatch):
    """
    see https://stackoverflow.com/questions/62044541/change-pytest-working-directory-to-test-case-directory
    """
    monkeypatch.chdir(request.fspath.dirname)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '1080'
    yield
