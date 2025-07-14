from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_personal_account_button(self):
        self.safe_click_with_modal_handling(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON,
            MainPageLocators.MODAL_OVERLAY
        )

    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def is_order_button_visible(self):
        return self.is_visible(MainPageLocators.ORDER_BUTTON)

    def is_header_title_visible(self):
        return self.is_visible(MainPageLocators.HEADER_TITLE)

    def is_ingredient_details_visible(self):
        return self.is_visible(MainPageLocators.MODAL_TITLE)

    def get_counter_value(self):
        return self.get_element_text_or_default(MainPageLocators.INGREDIENT_BUN_COUNTER)

    def click_order_button(self):
        self.safe_click(MainPageLocators.ORDER_BUTTON)

    def drag_bun_to_constructor(self):
        source = self.find_element(MainPageLocators.INGREDIENT_BUN)
        target = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_AREA)

        if self.is_firefox():
            self.drag_and_drop_js(source, target)
        else:
            self.drag_and_drop(source, target)

        self.wait_for_condition(
            lambda d: self.get_counter_value() > 0,
            timeout=5,
            message="Счетчик ингредиента не увеличился"
        )

    def open_ingredient_details(self, ingredient_type="bun"):
        if ingredient_type == "bun":
            locator = MainPageLocators.INGREDIENT_BUN
        elif ingredient_type == "sauce":
            locator = MainPageLocators.INGREDIENT_SAUCE
        else:
            locator = MainPageLocators.INGREDIENT_TOPPING

        self.scroll_to_element(locator)
        self.click(locator)
        self.wait_for_element_visible(MainPageLocators.MODAL_TITLE, timeout=5)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisible(MainPageLocators.MODAL, timeout=5)

    def safely_close_modal(self):
        close_button = self.wait_for_element_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click_via_actions(close_button)
        self.wait_for_element_invisible(MainPageLocators.MODAL)

    def wait_for_real_order_number(self, timeout=15):
        def is_valid_order_number(text):
            return text != "9999" and text.isdigit()

        return self.wait_for_text_condition(
            MainPageLocators.ORDER_NUMBER,
            is_valid_order_number,
            timeout=timeout,
            message="Номер заказа не обновился с заглушки 9999"
        )

    def safely_click_order_feed_button(self):
        self.safe_click_with_modal_handling(
            MainPageLocators.ORDER_FEED_BUTTON,
            MainPageLocators.MODAL_OVERLAY
        )

    def is_login_button_visible(self):
        return self.is_visible(MainPageLocators.LOGIN_BUTTON)

    def is_ingredient_modal_closed(self):
        return not self.is_visible(MainPageLocators.MODAL)

    def is_order_modal_opened(self):
        return self.is_visible(MainPageLocators.ORDER_ID_TITLE)
