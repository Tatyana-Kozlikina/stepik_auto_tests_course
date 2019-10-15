from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

def test_product_can_to_add_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page_product=ProductPage(browser,link)
    page_product.open()
    page_product.click_button(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.solve_quiz_and_get_code()
    page_product.should_be_in_basket()

