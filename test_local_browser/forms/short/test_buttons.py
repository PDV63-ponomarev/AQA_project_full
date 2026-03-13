import time
from selene import have, browser, by, be

def test_double_click():

    browser.open('/buttons')
    browser.element('#doubleClickMessage').should(be.absent)

    # двойное нажатие
    double_click_btn = browser.element('#doubleClickBtn')
    double_click_btn.should(be.visible)
    double_click_btn.should(be.clickable)

    double_click_btn.double_click()

    time.sleep(3)
    browser.element('#doubleClickMessage').should(be.visible)


def test_right_click():
    browser.open('/buttons')
    browser.element('#rightClickMessage').should(be.absent)

    right_click_btn = browser.element('#rightClickBtn')
    right_click_btn.should(be.visible)
    right_click_btn.should(be.clickable)

    right_click_btn.context_click()

    time.sleep(3)
    browser.element('#rightClickMessage').should(be.visible)