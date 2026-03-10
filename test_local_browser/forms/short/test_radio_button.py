import time

from selene import browser, have, be


def test_simple_form():

    browser.open('/radio-button')

    radio_yes = browser.element('#yesRadio')
    radio_yes_text = (radio_yes.element('./..//label[contains(@class, "form-check-label")]')
                      .locate().text)

    radio_yes.should(have.attribute('type', 'radio'))
    radio_yes.click()
    browser.element('.text-success').should(have.text(radio_yes_text))


    radio_impressive = browser.element('#impressiveRadio')
    radio_impressive_text = (radio_impressive.element('./..//label[contains(@class, "form-check-label")]')
                             .locate().text)

    radio_impressive.should(have.attribute('type', 'radio'))
    radio_impressive.click()
    browser.element('.text-success').should(have.text(radio_impressive_text))


    radio_no = browser.element('#noRadio')
    radio_no.should(have.attribute('type', 'radio'))
    radio_no.should(be.disabled)
