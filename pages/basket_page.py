import time

from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasketPage(BasePage):
    def are_basket_elements_located(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_basket_empty_text_located(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_empty_basket(self):
        assert not self.are_basket_elements_located(*BasketPageLocators.EMPTY_BASKET), "The basket should be empty"
        assert self.are_basket_elements_located(*BasketPageLocators.EMPTY_BASKET_TEXT), "No 'your basket is empty' text"

    def should_not_be_empty_basket(self):
        assert self.are_basket_elements_located(*BasketPageLocators.EMPTY_BASKET), "The basket should be full, but it is empty"
        assert not self.are_basket_elements_located(*BasketPageLocators.EMPTY_BASKET_TEXT), "There should be not 'your basket is empty' text"


