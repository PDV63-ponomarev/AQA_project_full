from selene import browser, have, be
import allure
from faker import Faker
from selenium.webdriver import Keys

fake = Faker()
users = None

def check_empty_forms():
    browser.element('#firstName').should(be.blank)
    browser.element('#lastName').should(be.blank)
    browser.element('#userEmail').should(be.blank)
    browser.element('#age').should(be.blank)
    browser.element('#salary').should(be.blank)
    browser.element('#department').should(be.blank)
    browser.element('#submit').should(be.visible)

def completion_random_form():
    user = {
        'First Name': fake.first_name(),
        'Last Name': fake.last_name(),
        'Email': fake.email(),
        'Age': fake.random_int(0, 99),
        'Salary': fake.random_int(500, 20000),
        'Department': fake.random_element([
            'QA', 'Developer', 'Marketing',
            'Legal', 'Insurance', 'Compliance'])
    }
    browser.element('#firstName').type(user['First Name'])
    browser.element('#lastName').type(user['Last Name'])
    browser.element('#userEmail').type(user['Email'])
    browser.element('#age').type(user['Age'])
    browser.element('#salary').type(user['Salary'])
    browser.element('#department').type(user['Department'])
    global users
    users = user


@allure.title("Successful add form")
def test_add_form(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/webtables')

    with allure.step('Открытие формы'):
        browser.element('#addNewRecordButton').should(be.visible)
        browser.element('#addNewRecordButton').click()
        browser.element('.modal-content').should(be.visible)

    with allure.step('Заполнение полей'):
        check_empty_forms()
        completion_random_form()

    with allure.step('Поле закрылось'):
        browser.element('#submit').click()
        browser.element('.modal-content').should(be.absent)

@allure.title("Successful find visible table")
def test_added_user_in_tables():
    with allure.step('Обнаружение таблицы'):
        tables = browser.element('.table-bordered')
        tables.should(be.visible)

    with allure.step('В таблице созданный юзер'):
        for value in users:
            tables.should(have.text(str(value)))

@allure.title("Successful work search")
def test_check_search():
    word = users['Last Name']

    with allure.step("Ввод в поиск имени"):
        search = browser.element('#searchBox')
        (search
         .should(be.visible)
         .should(be.blank)
         .click()
         .type(word)
         )

    with allure.step("Проверка работы поиска"):
        rows = browser.all('.table-bordered tbody tr')
        rows.should(have.size_greater_than(0))
        for row in rows:
            row.should(have.text(word))
        search.send_keys(Keys.CONTROL + 'a').send_keys(Keys.DELETE)

@allure.title("Successful show quantity users in tables")
def test_quantity_show_in_table():
    with allure.step('Обнаружение таблицы'):
        browser.element('#addNewRecordButton').should(be.visible)

    with allure.step('Добавление 15 пользователей'):
        i = 0
        while i < 15:
            browser.element('#addNewRecordButton').click()
            completion_random_form()
            browser.element('#submit').click()
            i += 1

    with allure.step('Проверка пользователей в таблице не больше 10'):
        rows = browser.all('.table-bordered tbody tr')
        rows.should(have.size_less_than_or_equal(10))

    with allure.step('Выбор отображения 20 пользователей'):
        browser.element('.pagination .form-control').click()
        browser.element('[value="20"]').click()

    with allure.step('Проверка пользователей в таблице больше 10 и не больше 20'):
        rows.should(have.size_greater_than_or_equal(10))
        rows.should(have.size_less_than_or_equal(20))
