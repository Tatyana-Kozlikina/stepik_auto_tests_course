from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("label #input_value").text
    y = calc(x_element)

    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)

    button2 = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()

