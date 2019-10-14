from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1= browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Pupkin")

    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("Pupkin@mail.ru")

    attach = browser.find_element_by_css_selector("input#file")
    
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir,'test.txt')
    attach.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(30)
    browser.quit()

