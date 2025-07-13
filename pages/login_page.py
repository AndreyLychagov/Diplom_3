from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
