from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_correct_name_in_basket_message()
        self.should_be_correct_price_in_basket_message()

    def should_be_correct_name_in_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, f"Product name in header {product_name} doesn't match with name" \
                                                     f"in  message {message_product_name}"

    def should_be_correct_price_in_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_product_price = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE).text
        assert product_price == message_product_price, f"Product price in header {product_price} doesn't match with " \
                                                       f"price in message {message_product_price} "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message didn't disappear on time"
