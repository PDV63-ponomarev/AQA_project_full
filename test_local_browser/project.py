from pydantic_settings import BaseSettings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Config(BaseSettings):
    base_url: str = 'https://demoqa.com/text-box'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: str = '1024'
    window_height: str = '1024'
    timeout: float = 3.0


def get_driver(driver_name='chrome'):

    driver_name = driver_name.lower()

    if driver_name == 'chrome':
        options = ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.page_load_strategy = 'eager'

        service = webdriver.chrome.service.Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Дополнительно для Chrome
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    elif driver_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.page_load_strategy = 'eager'

        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference('useAutomationExtension', False)

        options.set_preference("app.update.enabled", False)

        service = webdriver.firefox.service.Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Браузер {driver_name} не поддерживается")

    return driver

