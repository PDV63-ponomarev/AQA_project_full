from selene import have, browser, be, by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

def test_link_open_new_tab():

    browser.open('/links')

    link = browser.element('#simpleLink')

    link.should(be.visible)
    link.should(have.tag('a'))
    link.should(have.attribute('href')
                .value_containing('https://demoqa.com'))

    # запоминаем тек вкладку
    original_windows = browser.driver.window_handles

    link.click()

    # появление новой вкладки
    WebDriverWait(browser.driver, 10).until(
        EC.number_of_windows_to_be(len(original_windows) + 1)
    )

    # ПЕРЕКЛЮЧАЕМСЯ НА ПОСЛЕДНЮЮ ВКЛАДКУ
    browser.driver.switch_to.window(browser.driver.window_handles[-1])

    # проверка текущей вкладки
    browser.should(have.url_containing('demoqa.com'))

    browser.close()


def test_dynamic_link_open_new_tab_for_text():

    browser.open('/links')

    link = (browser.element('#dynamicLink')
            .should(have.text('Home')))

    link.should(be.visible)
    link.should(have.tag('a'))
    link.should(have.attribute('href')
                .value_containing('https://demoqa.com'))

    # запоминаем тек вкладку
    original_windows = browser.driver.window_handles

    link.click()

    # появление новой вкладки
    WebDriverWait(browser.driver, 10).until(
        EC.number_of_windows_to_be(len(original_windows) + 1)
    )

    # проверка текущей вкладки
    browser.should(have.url_containing('demoqa.com'))

    # ПЕРЕКЛЮЧАЕМСЯ НА ПОСЛЕДНЮЮ ВКЛАДКУ
    browser.driver.switch_to.window(browser.driver.window_handles[-1])
    browser.close()


def test_links_spend_api():

    response = requests.get('https://demoqa.com/created')
    assert response.status_code == 201

    response = requests.get('https://demoqa.com/no-content')
    assert response.status_code == 204

    response = requests.get('https://demoqa.com/moved')
    assert response.status_code == 301

    response = requests.get('https://demoqa.com/unauthorized')
    assert response.status_code == 401

    response = requests.get('https://demoqa.com/forbidden')
    assert response.status_code == 403

    response = requests.get('https://demoqa.com/invalid-url')
    assert response.status_code == 404

