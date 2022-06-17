from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADD_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ADD_TO_CART_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PRICE = (By.XPATH, '//div[contains(@class, "basket-mini")]/text()[2]')
    BASKET_LINK = (By.XPATH, '//span[@class="btn-group"]/a[contains(@href, "basket")]')


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
