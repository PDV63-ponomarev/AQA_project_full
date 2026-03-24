import time
from selene import be, have
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

def click_alert(browser):
    try:
        browser.driver.switch_to.alert.accept()
        return True
    except:
        return False

@allure.title("Successful see alert after click button")
def test_button_to_alert(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/alerts')

    with allure.step('Нахождение кнопки'):
        button_alert = browser.element('#alertButton')
        button_alert.should(be.visible)
        button_alert.should(be.clickable)

    with allure.step('Нажатие кнопки'):
        button_alert.click()

    with allure.step('Проверка появления диалогового окна'):
        WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    with allure.step('Закрытие диалогового окна'):
        click_alert(browser)

@allure.title("Successful see alert after click button with delay 5 sec")
def test_button_to_alert_after_5_seconds(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/alerts')

    with allure.step('Нахождение кнопки'):
        delay_button_alert = browser.element('#timerAlertButton')
        delay_button_alert.should(be.visible)
        delay_button_alert.should(be.clickable)

    with allure.step('Нажатие кнопки'):
        delay_button_alert.click()

    with allure.step('Проверка каждые 5 сек, диалогового окна нет'):
        t = 0
        while t < 5:
            assert not click_alert(browser)
            t += 1
            time.sleep(1)

    with allure.step('Проверка появления диалогового окна'):
        WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    with allure.step('Закрытие диалогового окна'):
        click_alert(browser)

@allure.title("Successful see confirm after click button")
def test_button_to_confirm(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/alerts')

    with allure.step('Нахождение кнопки'):
        button_confirm = browser.element('#confirmButton')
        button_confirm.should(be.visible)
        button_confirm.should(be.clickable)

    with allure.step('Нажатие кнопки'):
        button_confirm.click()

    with allure.step('Проверка появления диалогового окна'):
        WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    with allure.step('Закрытие диалогового окна'):
        click_alert(browser)

    with allure.step('Проверка текста после ОК'):
        browser.element('#confirmResult').should(have.text('You selected Ok'))

    with allure.step('Нажатие кнопки'):
        button_confirm.click()

    with allure.step('Проверка появления диалогового окна'):
        WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    with allure.step('Закрытие диалогового окна'):
        browser.driver.switch_to.alert.dismiss()

    with allure.step('Проверка текста после CANCEL'):
        browser.element('#confirmResult').should(have.text('You selected Cancel'))

@allure.title("Successful see prompt after click button")
def test_button_to_prompt(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/alerts')

    with allure.step('Нахождение кнопки'):
        button_prompt = browser.element('#promtButton')
        button_prompt.should(be.visible)
        button_prompt.should(be.clickable)

    with allure.step('Нажатие кнопки'):
        button_prompt.click()

    with allure.step('Проверка появления диалогового окна'):
         WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    with allure.step('Ввод текста в диалоговое окно'):
        text = 'Some text'
        browser.driver.switch_to.alert.send_keys(text)

    with allure.step('Закрытие диалогового окна'):
        click_alert(browser)

    with allure.step('Проверка передачи текста из диалогового окна в сообщение'):
        browser.element('#promptResult').should(have.text(f'You entered {text}'))