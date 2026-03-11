# from selene import browser
#
# browser.open('https://demoqa.com/checkbox')
#
# text = browser.element('.text-center').locate().text
#
# print(text)
#
# browser.quit()
from pprint import pprint

from faker import Faker
fake = Faker()

# users = [{
#     'First Name': fake.first_name(),
#     'Last Name': fake.last_name(),
#     'Email': fake.email(),
#     'Age': fake.random_int(1, 99),
#     'Salary': fake.random_int(100, 20000),
#     'Department': fake.random_element([
#         'QA', 'Developer', 'Marketing',
#         'Legal', 'Insurance', 'Compliance'])
# }for _ in range(15)]
i = 0
while i < 5:
    print(i)
    i += 1