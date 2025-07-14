from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def enter_email(self, email):
        self.input_text(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)

    def is_forgot_password_page(self):
        return self.is_visible(ForgotPasswordLocators.PAGE_TITLE)
