from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link="http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_on_main_page(browser):
    page_main=MainPage(browser,link)
    page_main.open()
    page_base=BasePage(browser,link)
    page_base.should_be_login_link()

def test_guest_can_go_to_login_page_from_main_page(browser):
    page_main = MainPage(browser, link)
    page_main.open()
    page_base = BasePage(browser, link)
    page_base.go_to_login_page()
    page_login=LoginPage(browser,browser.current_url)
    page_login.should_be_login_page()