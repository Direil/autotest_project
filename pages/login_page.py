from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current URL does not contain 'login'"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'No login form'

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'No register form'

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        user_email.send_keys(email)
        user_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        user_password1.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_CONFIRM)
        user_password2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.click()
