from selenium import webdriver
import time

link1="http://suninjuly.github.io/registration1.html"

link2="http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)

    input1=browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("Ivan@mail.ru")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    print(f"Результат теста страницы:'{welcome_text}")

finally:
    time.sleep(30)
    browser.quit()

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("Ivan@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
