from .base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def is_feed_header_visible(self):
        return self.is_visible(OrderFeedLocators.FEED_HEADER)

    def wait_for_feed_loaded(self, timeout=15):
        self.wait_for_element_visible(OrderFeedLocators.FEED_HEADER, timeout)
        self.wait_for_element_present(OrderFeedLocators.ORDER_ITEM, timeout)

        if self.is_firefox():
            self.wait_for_condition(
                lambda d: len(self.find_elements(OrderFeedLocators.ORDER_ITEM)) > 0,
                timeout=5
            )

    def is_order_details_modal_visible(self):
        return self.is_visible(OrderFeedLocators.ORDER_DETAILS_COMPOSITION_TITLE, timeout=15)

    def get_displayed_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.ORDER_NUMBERS_IN_FEED)
        return [self._normalize_order_number(element.text) for element in elements]

    def _normalize_order_number(self, order_text):
        number = order_text.replace("#", "").strip()
        return number.lstrip('0') or '0'

    def wait_for_total_increase(self, initial_value, timeout=15):
        self.wait_for_condition(
            lambda d: self.get_total_orders() > initial_value,
            timeout=timeout,
            message=f"Счетчик не увеличился за {timeout} секунд"
        )

    def get_total_orders(self):
        return int(self.find_element(OrderFeedLocators.TOTAL_ORDERS).text)

    def get_today_orders_count(self):
        return int(self.find_element(OrderFeedLocators.TODAY_ORDERS_COUNT).text)

    def wait_for_today_increase(self, initial_value, timeout=15):
        self.wait_for_condition(
            lambda d: self.get_today_orders_count() > initial_value,
            timeout=timeout,
            message=f"Счетчик за сегодня не увеличился за {timeout} секунд"
        )

    def get_orders_in_progress(self, timeout=10):
        self.wait_for_element_visible(OrderFeedLocators.ORDERS_IN_PROGRESS, timeout)
        elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [element.text.lstrip('0') for element in elements]

    def click_order_icon(self):
        self.click(OrderFeedLocators.ORDER_ITEM_ICON)