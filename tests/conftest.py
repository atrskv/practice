import pytest

from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    # browser.config.hold_browser_open = True


    yield

    browser.quit()

