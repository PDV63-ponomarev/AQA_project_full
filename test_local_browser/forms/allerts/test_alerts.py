import time
from selene import browser, be, have
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click_alert():
    try:
        browser.driver.switch_to.alert.accept()
        return True
    except:
        return False

def test_button_to_alert():
    browser.open('/alerts')

    button_alert = browser.element('#alertButton')
    button_alert.should(be.visible)
    button_alert.should(be.clickable)

    button_alert.click()

    WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    click_alert()

def test_button_to_alert_after_5_seconds():
    browser.open('/alerts')

    delay_button_alert = browser.element('#timerAlertButton')
    delay_button_alert.should(be.visible)
    delay_button_alert.should(be.clickable)

    delay_button_alert.click()

    t = 0
    while t < 5:
        assert not click_alert()
        t += 1
        time.sleep(1)

    assert EC.alert_is_present()

    click_alert()

def test_button_to_confirm():
    browser.open('/alerts')

    button_confirm = browser.element('#confirmButton')
    button_confirm.should(be.visible)
    button_confirm.should(be.clickable)

    button_confirm.click()

    WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    click_alert()

    browser.element('#confirmResult').should(have.text('You selected Ok'))

    button_confirm.click()

    WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    browser.driver.switch_to.alert.dismiss()

    browser.element('#confirmResult').should(have.text('You selected Cancel'))

def test_button_to_promt():
    browser.open('/alerts')

    button_promt = browser.element('#promtButton')
    button_promt.should(be.visible)
    button_promt.should(be.clickable)

    button_promt.click()

    WebDriverWait(browser.driver, 2).until(EC.alert_is_present())

    text = 'Some text'
    browser.driver.switch_to.alert.send_keys(text)
    click_alert()
    browser.element('#promptResult').should(have.text(f'You entered {text}'))