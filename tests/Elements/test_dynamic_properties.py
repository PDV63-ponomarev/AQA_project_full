import time
from selene import be, have
import allure

@allure.title("Successful button enable before 5 seconds")
def test_enable_button(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск кнопки'):
        enable_button = browser.element('#enableAfter')
        enable_button.should(be.visible)

    with allure.step('Кнопка неактивна'):
        enable_button.should(be.disabled)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Проверка активации цнопки'):
        enable_button.should(be.clickable)

@allure.title("Successful button change color before 5 seconds")
def test_change_button(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск кнопки'):
        change_button = browser.element('#colorChange')
        change_button.should(be.visible)

    with allure.step('Кнопка активна'):
        change_button.should(be.clickable)

    with allure.step('Кнопка не имеет спец цвета'):
        change_button.should(have.no.css_class('text-danger'))

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Кнопка имеет спец цвет'):
        change_button.should(have.css_class('text-danger'))

@allure.title("Successful button visible before 5 seconds")
def test_visible_button(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Кнопка отсутствует в DOM'):
        visible_button = browser.element('#visibleAfter')
        visible_button.should(be.not_.present)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Кнопка появилась'):
        visible_button.should(be.visible)
        visible_button.should(be.clickable)

@allure.title("Successful buttons complite before 5 seconds")
def test_complite_button(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск неактивной кнопки'):
        enable_button = browser.element('#enableAfter')
        enable_button.should(be.visible)
        enable_button.should(be.disabled)

    with allure.step('Поиск кнопки со сменой цвета'):
        change_button = browser.element('#colorChange')
        change_button.should(be.visible)
        change_button.should(be.clickable)
        change_button.should(have.no.css_class('text-danger'))

    with allure.step('Поиск отсутствующей кнопки'):
        visible_button = browser.element('#visibleAfter')
        visible_button.should(be.not_.present)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Проверка активации цнопки'):
      enable_button.should(be.clickable)

    with allure.step('Кнопка имеет спец цвет'):
        change_button.should(have.css_class('text-danger'))

    with allure.step('Кнопка появилась'):
        visible_button.should(be.visible)
        visible_button.should(be.clickable)