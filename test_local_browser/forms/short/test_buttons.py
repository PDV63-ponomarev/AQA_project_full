from selene import have, browser, be

def test_double_click():

    browser.open('/buttons')
    browser.element('#doubleClickMessage').should(be.absent)

    double_click_btn = browser.element('#doubleClickBtn')
    double_click_btn.should(be.visible)
    double_click_btn.should(be.clickable)

    double_click_btn.double_click()

    browser.element('#doubleClickMessage').should(be.visible)


def test_right_click():
    browser.open('/buttons')
    browser.element('#rightClickMessage').should(be.absent)

    right_click_btn = browser.element('#rightClickBtn')
    right_click_btn.should(be.visible)
    right_click_btn.should(be.clickable)

    right_click_btn.context_click()

    browser.element('#rightClickMessage').should(be.visible)


def test_dynamic_click():
    browser.open('/buttons')
    browser.element('#dynamicClickMessage').should(be.absent)

    button = (browser.all('.btn.btn-primary')
              .element_by(have.exact_text('Click Me')))
    button.should(be.visible)
    button.should(be.clickable)

    button.click()

    browser.element('#dynamicClickMessage').should(be.visible)
