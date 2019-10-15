import pytest
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import Locators
from .pages.locators import BasePageLocators
from .pages.basket_page import BasketPage

link="http://selenium1py.pythonanywhere.com/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page_main = MainPage(browser, link)
    page_main.open()
    page_base = BasePage(browser, link)
    page_base.click_element(*Locators.VIEW_BASKET)
    page_basket = BasketPage(browser, link)
    page_basket.should_be_empty_basket()

@pytest.mark.skip
def test_guest_should_see_login_link_on_main_page(browser):
    page_main=MainPage(browser,link)
    page_main.open()
    page_base=BasePage(browser,link)
    page_base.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_main_page(browser):
    page_main = MainPage(browser, link)
    page_main.open()
    page_base = BasePage(browser, link)
    page_base.go_to_login_page()
    page_login=LoginPage(browser,browser.current_url)
    page_login.should_be_login_page()