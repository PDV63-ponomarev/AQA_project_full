import pytest
from selene import browser
# import pydantic
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url: str = 'https://demoqa.com/text-box'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: str = '2048'
    window_height: str = '1024'
    timeout: float = 3.0


config = Config()



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Отключить ожидание полной загрузки страницы
    chrome_options.page_load_strategy = 'eager'

    driver = webdriver.Chrome(options=chrome_options)

    # Настраиваем Selene
    browser.config.driver = driver

    browser.config.base_url = config.base_url
    browser.config.driver_name = config.driver_name
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout


    yield browser

    browser.quit()