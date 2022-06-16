import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_cart_button()
        self.add_to_cart_and_get_code()
        self.product_name_and_product_cost_should_be_equal()

    def should_be_add_to_cart_button(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET), "No 'Add to basket' button"

    def add_to_cart_and_get_code(self):
        # реализуйте проверку, что есть форма логина
        cart = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        cart.click()
        self.solve_quiz_and_get_code()

    def product_name_and_product_cost_should_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.ADD_TO_CART_PRODUCT_NAME).text, 'Product names do not match.'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.ADD_TO_CART_PRODUCT_PRICE).text, 'Product prices do not match.'



