from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//*[@id='login_link']")
    LOGIN_LINK_INVALID = (By.XPATH, "//*[@id='login_link_inc']")
    BASKET_LINK = (By.XPATH, "//*[@class='btn-group']/*[contains(@href,'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")
    REGISTER_FORM_EMAIL_FIELD = (By.XPATH, "//*[@id='register_form']//input[@type='email']")
    REGISTER_FORM_PASSWORD_FIELD = (By.XPATH, "//*[@name='registration-password1']")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.XPATH, "//*[@name='registration-password2']")
    REGISTER_FORM_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//*[contains(@class,'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//*[contains(@class,'product_main')]/h1")
    BASKET_MESSAGE_PRODUCT_NAME = (By.XPATH, "//*[@id = 'messages']/div[1]//strong")
    PRODUCT_PRICE = (By.XPATH, "//*[@class = 'price_color']")
    BASKET_MESSAGE_PRODUCT_PRICE = (By.XPATH, "//*[@id = 'messages']/div[3]//strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(@class,'alert-success')]")


class BasketPageLocators:
    PRODUCTS_FORM = (By.XPATH, "//form[@class = 'basket_summary']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id = 'content_inner']/p")
