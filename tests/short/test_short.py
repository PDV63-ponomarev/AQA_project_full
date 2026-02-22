from selene import have, browser
import allure
from selenium.webdriver import Keys

full_name = 'Иванов Иван'
email = 'ivanov@gmail.com'
address = 'Some adress'


@allure.title("Successful fill form")
def test_simple_form(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/')
        browser.execute_script("document.body.style.zoom='75%'")

    with allure.step('Заполнение полей'):

        browser.element('#userName').type(full_name)
        browser.element('#userEmail').type(email)
        browser.element('#currentAddress').type(address)

        browser.element('#submit').click()

    with allure.step('Проверка заполнености'):
        output = browser.element('#output')
        output.should(have.text(f'Name:{full_name}'))
        output.should(have.text(f'Email:{email}'))
        output.should(have.text(f'Current Address :{address}'))

