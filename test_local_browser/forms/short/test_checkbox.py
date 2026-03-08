import time
from selene import browser
import allure



def test_simple_form():
    browser.open('/checkbox')


    browser.element('.rc-tree-switcher_close').click()
    for element in browser.elements('.rc-tree-switcher_close'):
        element.click()
    time.sleep(5)