import pytest
from selene import browser

from project import Config
from project import get_driver


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    config = Config()

    # driver = get_driver(config.driver_name)

    browser.config.base_url = config.base_url
    browser.config.driver = get_driver(config.driver_name)
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield

    # Закрываем браузер после теста
    if not config.hold_driver_at_exit:
        browser.quit()