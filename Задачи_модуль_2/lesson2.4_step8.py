from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price= WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'),"$100"))

    browser.find_element_by_css_selector("button#book").click()

    x_element=browser.find_element(By.CSS_SELECTOR,"span#input_value").text
    y = calc(x_element)

    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)

    browser.find_element_by_css_selector("button#solve").click()

finally:
    time.sleep(30)
    browser.quit()
