from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[src='images/chest.png']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector("input#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("input#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
















