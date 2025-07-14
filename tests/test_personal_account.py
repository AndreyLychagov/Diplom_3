import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title("Переход в личный кабинет")
    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Переход в личный кабинет"):
            main_page.click_personal_account_button()

        with allure.step("Проверка перехода в личный кабинет"):
            assert profile_page.is_save_button_visible(), "Не удалось перейти в личный кабинет"

    @allure.title("Переход в историю заказов")
    def test_go_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)
        main_page = MainPage(driver)

        with allure.step("Переход в личный кабинет"):
            main_page.click_personal_account_button()

        with allure.step("Переход в историю заказов"):
            profile_page.click_order_history_link()

        with allure.step("Проверка URL страницы истории заказов"):
            assert profile_page.is_order_history_page(), "Не удалось перейти в историю заказов"

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Переход в личный кабинет"):
            main_page.click_personal_account_button()

        with allure.step("Выход из аккаунта"):
            profile_page.click_logout_button()

        with allure.step("Проверка отображения кнопки 'Войти'"):
            assert main_page.is_login_button_visible(), "Выход из аккаунта не выполнен"