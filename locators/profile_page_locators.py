from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
