import time

from selene import  browser, be
from selenium.webdriver.support import expected_conditions as EC

def test_button_to_alert():
    browser.open('/alerts')

    button_alert = browser.element('#alertButton')
    button_alert.should(be.visible)
    button_alert.should(be.clickable)

    button_alert.click()

    assert EC.alert_is_present()

    browser.driver.switch_to.alert.accept()


