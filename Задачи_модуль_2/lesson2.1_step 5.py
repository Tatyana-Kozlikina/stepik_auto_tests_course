from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 
link=" http://suninjuly.github.io/math.html"

try:
	browser=webdriver.Chrome()
	browser.get(link)
		
	x_element = browser.find_element_by_Css_selector("label #input_value")
	
	x = x_element.text
	y = calc(x)
	input=browser.find_element_by_()
	input.send_keys(y)
	
	option1=browser.find_element_by_Css_selector("[for='robotCheckbox']")
	option1.click()
	
	option2=browser.find_element_by_Css_selector("[for='robotsRule']")
	option2.click()
	
	button=browser.find_element_by_Css_selector("button.btn")
	button.click()
	
finally:
	time.sleep(30)
	browser.quit()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
