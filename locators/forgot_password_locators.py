from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PAGE_TITLE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")