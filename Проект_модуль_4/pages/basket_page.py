from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_message_empty_basket()
        self.should_not_be_product()

    def should_be_message_empty_basket(self):
        assert self.is_text_element_present(*BasketPageLocators.MESSAGE_VIEW_BASKET), \
            "Отсутствует сообщение 'Ваша корзина пуста'"

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "В корзине есть книги, а должно быть пусто"