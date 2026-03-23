from selene import have, browser, be, by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import allure

@allure.title("Successful link open new tab")
def un_test_link_open_new_tab():

    with allure.step('Открытие сайта'):
        browser.open('/links')

    with allure.step('Проверка ссылки'):
        link = browser.element('#simpleLink')
        link.should(be.visible)
        link.should(have.tag('a'))
        link.should(have.attribute('href')
                    .value_containing('https://demoqa.com'))

    with allure.step('Появление новой вкладки'):
        original_windows = browser.driver.window_handles
        link.click()
        WebDriverWait(browser.driver, 10).until(
            EC.number_of_windows_to_be(len(original_windows) + 1)
        )
    with allure.step('Переход на новую вкладку'):
        browser.should(have.url_containing('demoqa.com'))

    with allure.step('Закрытие вкладка'):
        browser.driver.switch_to.window(browser.driver.window_handles[-1])
        browser.close()

@allure.title("Successful dynamic link open new tab")
def un_test_dynamic_link_open_new_tab_for_text():

    with allure.step('Открытие сайта'):
        browser.open('/links')

    with allure.step('Проверка ссылки'):
        link = (browser.element('#dynamicLink')
                .should(have.text('Home')))
        link.should(be.visible)
        link.should(have.tag('a'))
        link.should(have.attribute('href')
                    .value_containing('https://demoqa.com'))

    with allure.step('Появление новой вкладки'):
        original_windows = browser.driver.window_handles
        link.click()
        WebDriverWait(browser.driver, 10).until(
            EC.number_of_windows_to_be(len(original_windows) + 1)
        )

    with allure.step('Переход на новую вкладку'):
        browser.should(have.url_containing('demoqa.com'))

    with allure.step('Закрытие вкладка'):
        browser.driver.switch_to.window(browser.driver.window_handles[-1])
        browser.close()


@allure.title("Successful link give api")
def test_links_spend_api():

    with allure.step('Получение кода 201'):
        response = requests.get('https://demoqa.com/created')
        assert response.status_code == 201

    with allure.step('Получение кода 204'):
        response = requests.get('https://demoqa.com/no-content')
        assert response.status_code == 204

    with allure.step('Получение кода 301'):
        response = requests.get('https://demoqa.com/moved')
        assert response.status_code == 301

    with allure.step('Получение кода 401'):
        response = requests.get('https://demoqa.com/unauthorized')
        assert response.status_code == 401

    with allure.step('Получение кода 403'):
        response = requests.get('https://demoqa.com/forbidden')
        assert response.status_code == 403

    with allure.step('Получение кода 404'):
        response = requests.get('https://demoqa.com/invalid-url')
        assert response.status_code == 404

