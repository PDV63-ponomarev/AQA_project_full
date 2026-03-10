from selene import browser

browser.open('https://demoqa.com/checkbox')

text = browser.element('.text-center').locate().text

print(text)

browser.quit()
