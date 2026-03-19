import time
from selene import browser, be, have

def test_enable_button():
    browser.open('/dynamic-properties')

    enable_button = browser.element('#enableAfter')
    enable_button.should(be.visible)
    enable_button.should(be.disabled)

    time.sleep(5)

    enable_button.should(be.clickable)


def test_change_button():
    browser.open('/dynamic-properties')

    change_button = browser.element('#colorChange')
    change_button.should(be.visible)
    change_button.should(be.clickable)
    change_button.should(have.no.css_class('text-danger'))

    time.sleep(5)

    change_button.should(have.css_class('text-danger'))


def test_visible_button():
    browser.open('/dynamic-properties')

    visible_button = browser.element('#visibleAfter')
    visible_button.should(be.not_.present)

    time.sleep(5)

    visible_button.should(be.visible)
    visible_button.should(be.clickable)

def test_complite_button():
    browser.open('/dynamic-properties')

    enable_button = browser.element('#enableAfter')
    enable_button.should(be.visible)
    enable_button.should(be.disabled)

    change_button = browser.element('#colorChange')
    change_button.should(be.visible)
    change_button.should(be.clickable)
    change_button.should(have.no.css_class('text-danger'))

    visible_button = browser.element('#visibleAfter')
    visible_button.should(be.not_.present)

    time.sleep(5)

    enable_button.should(be.clickable)

    change_button.should(have.css_class('text-danger'))

    visible_button.should(be.visible)
    visible_button.should(be.clickable)