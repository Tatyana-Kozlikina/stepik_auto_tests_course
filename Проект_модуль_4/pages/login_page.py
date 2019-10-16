from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self,email,password):
        input_email=self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        input_password2.send_keys(password)
        button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        actual_link=self.browser.current_url
        assert "login" in actual_link, "Неверный url"
		
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), \
            "Отсутствует форма регистрации нового пользователя"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), \
            "Отсутствует форма 'Вход' "
