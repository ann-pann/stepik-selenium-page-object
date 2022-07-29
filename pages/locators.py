from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")
    LOGIN_LINK_INVALID = (By.XPATH, "//*[@id='login_link_inc']")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//*[contains(@class,'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//*[contains(@class,'product_main')]/h1")
    BASKET_MESSAGE_PRODUCT_NAME = (By.XPATH, "//*[@id = 'messages']/div[1]/*/strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@class = 'price_color']")
    BASKET_MESSAGE_PRODUCT_PRICE = (By.XPATH, "//*[@id = 'messages']/div[3]/*/*/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-success')]")
