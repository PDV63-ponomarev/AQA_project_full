from selene import have, be
import allure

full_name = 'Иванов Иван'
email = 'ivanov@gmail.com'
address = 'Some adress'

@allure.title("Successful check radio buttons")
def test_radio_buttons(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/radio-button')

    with allure.step('Нажатия кнопки YES'):
        radio_yes = browser.element('#yesRadio')
        radio_yes_text = (radio_yes.element('./..//label[contains(@class, "form-check-label")]')
                          .locate().text)

        radio_yes.should(have.attribute('type', 'radio'))
        radio_yes.click()

    with allure.step('Передача кнопки в поле выбора'):
        browser.element('.text-success').should(have.text(radio_yes_text))

    with allure.step('Нажатия кнопки YES'):
        radio_impressive = browser.element('#impressiveRadio')
        radio_impressive_text = (radio_impressive.element('./..//label[contains(@class, "form-check-label")]')
                                 .locate().text)

        radio_impressive.should(have.attribute('type', 'radio'))
        radio_impressive.click()

    with allure.step('Передача кнопки в поле выбора'):
        browser.element('.text-success').should(have.text(radio_impressive_text))


    with allure.step('Кнопка NO не доступна'):
        radio_no = browser.element('#noRadio')
        radio_no.should(have.attribute('type', 'radio'))
        radio_no.should(be.disabled)