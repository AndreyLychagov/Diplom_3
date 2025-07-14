from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active')]//input[@type='text']")
    CODE_INPUT = (By.XPATH, "//label[contains(text(), 'Введите код из письма')]")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
