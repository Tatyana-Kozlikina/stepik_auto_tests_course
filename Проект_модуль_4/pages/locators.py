from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET=(By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-add-to-basket")
    MASSAGE_ADD_TO_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1)>div")
    NAME_BOOK_IN_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(1)>.alertinner >strong")
    NAME_BOOK=(By.CSS_SELECTOR,".col-sm-6.product_main h1")
    MESSAGE_PRICE_BASKET=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3)>div>p")
    BASKET_PRICE=(By.CSS_SELECTOR,"#messages>.alert:nth-child(3) >div >p >strong")
    BOOK_PRICE=(By.CSS_SELECTOR,".col-sm-6.product_main p")
