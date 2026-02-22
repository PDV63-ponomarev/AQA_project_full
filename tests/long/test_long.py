import time
from selene import browser, be, have, by
from selenium.webdriver import Keys

firstName = 'Иван'
lastName = 'Иванов'
mail = 'random@mail.ru'
number = '8800123456'
date = '01 Jan 2026'
addres = 'Россия, г. Мытищи, Ленинская ул., д. 16 кв.194'
predmet1 = 'English'
predmet2 = 'Biology'
state = 'Haryana'
city = 'Karnal'

def test_form_ru():

    browser.open('/')

    # Ввод первого имени
    browser.element('#firstName').should(be.blank).type(firstName)

    # ввод второго имени
    browser.element('#lastName').should(be.blank).type(lastName)

    # ввод почты
    browser.element('#userEmail').should(be.blank).type(mail)

    # Нажатие кнопки (перекрыто label, нажатие через него)
    browser.element('[for="gender-radio-1"]').click()

    # ввод номера
    browser.element('#userNumber').type(number)

    # ввод даты вручную
    browser.element('#dateOfBirthInput').send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01.01.2020',
        Keys.ENTER,
    )

    # проверка сохранения даты
    browser.element('#dateOfBirthInput').should(have.value('01 Jan 2020'))

    # ввод даты нажатием
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(
        '[value="2026"]'
    ).click()
    browser.element('.react-datepicker__month-select').click().element(
        '[value="0"]'
    ).click()
    browser.element(
        '[class="react-datepicker__day react-datepicker__day--001"]'
    ).click()

    # проверка сохранения даты
    browser.element('#dateOfBirthInput').should(have.value(date))

    # выбор предметов
    # полный ввод текста
    browser.element('#subjectsInput').type(predmet1).send_keys(Keys.ENTER)
    # выбор
    browser.element('#subjectsInput').type(predmet2)
    browser.element('.subjects-auto-complete__option').click()

    # прожатие чекбоксов хобби
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    # ввод адреса
    browser.element('#currentAddress').type(addres)

    # выбор штата
    browser.all('[class=" css-1wy0on6"]').first.click()
    browser.element(by.text(state)).click()

    # выбор города
    browser.all('[class=" css-1wy0on6"]').second.click()
    browser.element(by.text(city)).click()

    # # подтверждения
    browser.element('#submit').click()

    # проверка заполнености
    browser.element('[class="modal-content"').should(be.visible)
    browser.element('[class="table-responsive"]').should(have.text(f'{firstName} {lastName}'))
    browser.element('[class="table-responsive"]').should(have.text(mail))
    browser.element('[class="table-responsive"]').should(have.text(number))
    browser.element('[class="table-responsive"]').should(have.text(predmet1 + ', ' + predmet2))
    browser.element('[class="table-responsive"]').should(have.text(addres))
    browser.element('[class="table-responsive"]').should(have.text(state + ' ' + city))
