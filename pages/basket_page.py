from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "The basket should be empty"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "No 'your basket is empty' text"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "The basket should not be empty"
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "There should be not 'your basket is empty' text"


