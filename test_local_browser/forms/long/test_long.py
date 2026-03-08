import time

from selene import be, have, by, browser
from selenium.webdriver import Keys
import allure

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

    browser.open('/automation-practice-form')

    browser.execute_script("document.body.style.zoom='80%'")

    browser.element('#firstName').should(be.blank).type(firstName)
    browser.element('#lastName').should(be.blank).type(lastName)
    browser.element('#userEmail').should(be.blank).type(mail)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(number)

    browser.element('#dateOfBirthInput').click().send_keys(
        Keys.CONTROL + 'a',
        Keys.NULL,
        '01 Jan 2020',
        Keys.ENTER,
    )

    browser.element('#dateOfBirthInput').should(have.value('01 Jan 2020'))

    browser.element('#subjectsInput').type(predmet1).send_keys(Keys.ENTER)
    browser.element('#subjectsInput').type(predmet2)
    browser.element('.subjects-auto-complete__option').click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#currentAddress').type(addres)


    browser.all('[class="css-19bb58m"]').first.click()
    browser.element(by.text(state)).click()

    browser.all('[class="css-19bb58m"]').second.click()
    browser.element(by.text(city)).click()

    browser.element('#submit').click()



    browser.element('[class="modal-content"').should(be.visible)
    browser.element('[class="table-responsive"]').should(have.text(f'{firstName} {lastName}'))
    browser.element('[class="table-responsive"]').should(have.text(mail))
    browser.element('[class="table-responsive"]').should(have.text(number))
    browser.element('[class="table-responsive"]').should(have.text('01 January,2020'))
    browser.element('[class="table-responsive"]').should(have.text(predmet1 + ', ' + predmet2))
    browser.element('[class="table-responsive"]').should(have.text(addres))
    browser.element('[class="table-responsive"]').should(have.text(state + ' ' + city))
