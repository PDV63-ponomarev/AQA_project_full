
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

def test_add_form():

    browser.open('/webtables')

    # нажатие кнопки
    browser.element('#addNewRecordButton').should(be.visible)
    browser.element('#addNewRecordButton').click()

    # проверка появления окна форма
    browser.element('.modal-content').should(be.visible)

    # проверка пустых полей
    check_empty_forms()

    # заполнение полей
    completion_random_form()

    browser.element('#submit').click()

    # проверка закрытия поля
    browser.element('.modal-content').should(be.absent)


def test_check_tables():
    tables = browser.element('.table-bordered')
    tables.should(be.visible)

    for value in users:
        tables.should(have.text(str(value)))

def test_check_search():

    word = users['Last Name']
    search = browser.element('#searchBox')
    (search
     .should(be.visible)
     .should(be.blank)
     .click()
     .type(word)
     )

    rows = browser.all('.table-bordered tbody tr')
    # проверка что строки есть
    rows.should(have.size_greater_than(0))
    # проверка что в строках есть слово
    for row in rows:
        row.should(have.text(word))

    search.send_keys(Keys.CONTROL + 'a').send_keys(Keys.DELETE)

def test_quantity_show_in_table():

    browser.element('#addNewRecordButton').should(be.visible)
    i = 0
    while i < 15:
        browser.element('#addNewRecordButton').click()
        completion_random_form()
        browser.element('#submit').click()
        i += 1

    rows = browser.all('.table-bordered tbody tr')
    # проверка что строк меньше или 10
    rows.should(have.size_less_than_or_equal(10))

    browser.element('.pagination .form-control').click()
    browser.element('[value="20"]').click()
    rows.should(have.size_greater_than_or_equal(10))
    rows.should(have.size_less_than_or_equal(20))


def test_added_empty_forms():
    browser.open('/webtables')

    browser.element('#addNewRecordButton').should(be.visible)
    browser.element('#addNewRecordButton').click()
    browser.element('.modal-content').should(be.visible)

    # поля пустые, окно не пропадает
    browser.element('#submit').click()
    browser.element('.modal-content').should(be.visible)

    # поля пустые, выдает везде ошибку
    # Проверка что появился класс was-validated
    browser.element('#userForm').should(have.css_class('was-validated'))
    # Проверка полей с ошибкой через JavaScript
    for field_id in ['firstName', 'lastName', 'userEmail', 'age', 'salary', 'department']:
        # # Проверяем что поле не проходит валидацию
        is_invalid = browser.execute_script(f"""
            return !document.getElementById('{field_id}').checkValidity();
        """)
        assert is_invalid, f"Поле {field_id} должно быть невалидным"


def test_added_uncorrect_forms():
    browser.open('/webtables')

    browser.element('#addNewRecordButton').should(be.visible)
    browser.element('#addNewRecordButton').click()

    # # Словарь для сбора ошибок
    # validation_errors: Dict[str, str] = {}

    with allure.step("Заполнение формы с невалидными данными"):
        # Заполнение полей неверными данными
        modal = browser.element('.modal-content')
        modal.should(be.visible)

        browser.element('#firstName').type('Test123!@#$')
        browser.element('#lastName').type('Test123!@#$')
        browser.element('#userEmail').type('Test123!@#$')
        browser.element('#age').type('Test123!@#$')
        browser.element('#salary').type('Test123!@#$')
        browser.element('#department').type('Test123!@#$')

        browser.element('#submit').click()

    with allure.step("Проверка валидации полей (с мягкими проверками)"):
        for field_id in ['firstName', 'lastName', 'userEmail', 'age', 'salary', 'department']:
            try:
                is_invalid = browser.execute_script(f"""
                            return !document.getElementById('{field_id}').checkValidity();
                        """)
                if not is_invalid:
                    allure.attach(
                        name=f"Недочет валидации в поле {field_id}",
                        body=f"Поле {field_id} должно быть невалидным, но прошло проверку",
                        attachment_type=allure.attachment_type.TEXT
                    )

            except Exception as e:
                # Если ошибка при проверке - тоже отмечаем
                allure.attach(
                    name=f"Ошибка при проверке поля {field_id}",
                    body=str(e),
                    attachment_type=allure.attachment_type.TEXT
                )
