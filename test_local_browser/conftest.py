import pytest
from selene import browser

from project import Config
from project import get_driver


@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    config = Config()

    # driver = get_driver(config.driver_name)
    browser.config.hold_browser_open = True
    browser.config.base_url = config.base_url
    browser.config.driver = get_driver(config.driver_name)
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield browser

    # Восстанавливаем состояние браузера
    # try:
    #     # Если открыто несколько вкладок, закрываем все лишние
    #     if len(browser.driver.window_handles) > 1:
    #         main_window = browser.driver.window_handles[0]
    #         for handle in browser.driver.window_handles[1:]:
    #             browser.driver.switch_to.window(handle)
    #             browser.driver.close()
    #         browser.driver.switch_to.window(main_window)
    # except Exception:
    #     pass

    # Закрываем браузер после теста
    if not config.hold_driver_at_exit:
        browser.quit()