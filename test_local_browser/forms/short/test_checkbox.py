import time
from selene import browser, be, have
import allure


def test_simple_form():

    browser.open('/checkbox')

    current_count = len(browser.all('.rc-tree-switcher_close'))
    while current_count > 0 and current_count != -1:
        for folder in browser.all('.rc-tree-switcher_close'):
            if folder.matching(be.visible):
                folder.click()

        current_count = len(browser.all('.rc-tree-switcher_close'))

def open_box(browser):
    current_count = len(browser.all('.rc-tree-switcher_close'))
    while current_count > 0 and current_count != -1:
        for folder in browser.all('.rc-tree-switcher_close'):
            if folder.matching(be.visible):
                folder.click()
        current_count = len(browser.all('.rc-tree-switcher_close'))


@allure.title("Successful check in check box")
def test_check_boxes():


    with allure.step('Открытие сайта'):
        browser.open('/checkbox')

    with allure.step('Раскрытие ветки'):
        open_box(browser)

    with allure.step('Выбор общей папки'):
        browser.element('[aria-label="Select Home"]').click()

    with allure.step('Проверка выбора всех папок'):
        for element in browser.all('.rc-tree-checkbox'):
            element.should(have.css_class('rc-tree-checkbox-checked'))

    with allure.step('Проверка поля результат'):
        selected_checkboxes = browser.all('.rc-tree-checkbox-checked')
        selected_texts = []

        # достаем текст чекбоксов
        for checkbox in selected_checkboxes:
            text_element = checkbox.element('./..//span[contains(@class, "rc-tree-title")]')
            text = text_element.locate().text
            if text ==  'Word File.doc':
                selected_texts.append('wordFile')
            elif text == 'Excel File.doc':
                selected_texts.append('excelFile')
            else:
                selected_texts.append(text.lower())
        # преобразуем текст в строку
        expected_text = ' '.join(selected_texts)

        # сравнение выбранного с полем отображения
        browser.element('#result').should(have.text(expected_text))





