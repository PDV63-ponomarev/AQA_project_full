from selene import have, browser

full_name = 'Иванов Иван'
email = 'ivanov@gmail.com'
address = 'Some adress'

'''
запуск
$env:DRIVER_NAME = "chrome"; pytest tests
'''

def test_simple_form():
    browser.open('/')

    browser.element('#userName').type(full_name)
    browser.element('#userEmail').type(email)
    browser.element('#currentAddress').type(address)

    browser.element('#submit').click()

    output = browser.element('#output')
    output.should(have.text(f'Name:{full_name}'))
    output.should(have.text(f'Email:{email}'))
    output.should(have.text(f'Current Address :{address}'))

