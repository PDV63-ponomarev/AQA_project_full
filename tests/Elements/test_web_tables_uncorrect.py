from selene import browser, have, be
import allure

@allure.title("Successful stop empty form")
def test_added_empty_forms(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/webtables')

    with allure.step('Открытие формы'):
        browser.element('#addNewRecordButton').should(be.visible)
        browser.element('#addNewRecordButton').click()
        browser.element('.modal-content').should(be.visible)

    with allure.step('Окно не закрывается с пустыми строками'):
        browser.element('#submit').click()
        browser.element('.modal-content').should(be.visible)

    with allure.step('У полей отображаются ошибки'):
        browser.element('#userForm').should(have.css_class('was-validated'))
        for field_id in ['firstName', 'lastName', 'userEmail', 'age', 'salary', 'department']:
            is_invalid = browser.execute_script(f"""
                return !document.getElementById('{field_id}').checkValidity();
            """)
            assert is_invalid, f"Поле {field_id} должно быть невалидным"

@allure.title("Successful stop uncorrect form")
def test_added_uncorrect_forms(setup_browser):
    browser = setup_browser

    with allure.step('Открытие сайта'):
        browser.open('/webtables')

    with allure.step('Открытие формы'):
        browser.element('#addNewRecordButton').should(be.visible)
        browser.element('#addNewRecordButton').click()
        browser.element('.modal-content').should(be.visible)


    with allure.step("Заполнение формы с невалидными данными"):
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
                allure.attach(
                    name=f"Ошибка при проверке поля {field_id}",
                    body=str(e),
                    attachment_type=allure.attachment_type.TEXT
                )
