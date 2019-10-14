from selenium.webdriver.common.by import By
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
def test_is_element_button_present(browser):
    browser.get(link)
    button=bool(browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button,"Страница товара не содержит кнопку добавления в корзину"
    print(button)
