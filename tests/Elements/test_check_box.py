import time

import allure

@allure.title("Successful fill check box")
def test_simple_form(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/checkbox')

    with allure.step('Раскрытие ветки'):
        browser.element('.rc-tree-switcher_close').click()
        for element in browser.elements('.rc-tree-switcher_close'):
            element.click()
        time.sleep(5)