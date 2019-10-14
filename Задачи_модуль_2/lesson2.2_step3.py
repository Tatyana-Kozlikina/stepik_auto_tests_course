from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(a,b):
    result = int(a) + int(b)
    return str(result)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_css_selector("h2 #num1").text
    b = browser.find_element_by_css_selector("h2 #num2").text

    c=calc(a, b)
    
    d=Select(browser.find_element_by_css_selector("select#dropdown"))
    e=d.select_by_visible_text(c)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()

