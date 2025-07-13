from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    HEADER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    INGREDIENT_SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    INGREDIENT_TOPPING = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa7f']")
    INGREDIENT_BUN_COUNTER = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//div[contains(@class, 'counter_counter')]")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_ID_TITLE = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='идентификатор заказа']")
    MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')]")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")


