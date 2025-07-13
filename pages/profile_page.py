from .base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    def click_order_history_link(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    def click_logout_button(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def is_save_button_visible(self):
        return self.is_visible(ProfilePageLocators.SAVE_BUTTON)

    def is_order_history_page(self):
        current_url = self.get_current_url()
        return "account/order-history" in current_url