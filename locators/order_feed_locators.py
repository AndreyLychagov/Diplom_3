from selenium.webdriver.common.by import By

class OrderFeedLocators:
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_ITEM = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem']")
    ORDER_ITEM_ICON = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem'] svg")
    ORDER_DETAILS_COMPOSITION_TITLE = (By.XPATH, "//p[@class='text text_type_main-medium mb-8' and text()='Cостав']")
    ORDER_NUMBERS_IN_FEED = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")
