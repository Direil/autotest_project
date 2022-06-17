import time
import pytest
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def has_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared"

    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        cart.click()

    def product_name_and_product_cost_should_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(
                   *ProductPageLocators.ADD_TO_CART_PRODUCT_NAME).text, 'Product names do not match.'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(
                   *ProductPageLocators.ADD_TO_CART_PRODUCT_PRICE).text, 'Product prices do not match.'



