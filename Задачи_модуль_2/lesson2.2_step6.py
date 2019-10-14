from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element=browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    y = calc(x_element)

    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)

    browser.find_element_by_css_selector("input#robotCheckbox").click()

    button=browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);",button)

    browser.find_element_by_css_selector("input#robotsRule").click()

    button.click()

finally:
    time.sleep(30)
    browser.quit()

