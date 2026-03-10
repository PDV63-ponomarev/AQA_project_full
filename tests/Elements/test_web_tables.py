import allure


@allure.title("Successful fill text box")
def test_simple_form(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/webtables')
