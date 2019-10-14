from selenium import webdriver
import time
import math

link="https://www.degreesymbol.net/"

try:
    browser=webdriwer.Chrome()
    browser.get(link)
    need_link=browser.find_element_by_link_text("224592")
    need_link.click()

finally:
    time.sleep(30)
    browser.quit()
