import pytest
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

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="some bug")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    page_product=ProductPage(browser,link)
    page_product.open()
    page_product.click_button(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.solve_quiz_and_get_code()
    page_product.should_be_in_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.click_button(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page_product = ProductPage(browser, link)
    page_product.open()
    page_product.click_button(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
    page_product.should_disappear_success_message()