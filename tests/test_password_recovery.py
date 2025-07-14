import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data import TEST_EMAIL

@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        with allure.step("Переход на страницу входа"):
            main_page.click_login_button()

        with allure.step("Переход на страницу восстановления пароля"):
            login_page.click_forgot_password_link()

        with allure.step("Проверка перехода на страницу восстановления пароля"):
            assert forgot_password_page.is_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_restore_password(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        with allure.step("Переходим на страницу входа"):
            main_page.click_login_button()

        with allure.step("Переходим на страницу восстановления пароля"):
            login_page.click_forgot_password_link()

        with allure.step("Вводим email и отправляем запрос"):
            forgot_password_page.enter_email(TEST_EMAIL)
            forgot_password_page.click_restore_button()

        with allure.step("Проверяем переход на страницу сброса пароля"):
            assert reset_password_page.is_code_input_visible(), "Не удалось перейти на страницу сброса пароля"

    @allure.title("Активация поля пароля при клике на иконку")
    def test_password_field_activation(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        with allure.step("Переход на страницу входа"):
            main_page.click_login_button()

        with allure.step("Переход на страницу восстановления пароля"):
            login_page.click_forgot_password_link()

        with allure.step("Ввод email и отправка запроса"):
            forgot_password_page.enter_email(TEST_EMAIL)
            forgot_password_page.click_restore_button()

        with allure.step("Клик по иконке показать/скрыть пароль"):
            reset_password_page.click_show_password_button()

        with allure.step("Проверка активности поля пароля"):
            assert reset_password_page.is_password_input_active(), "Поле пароля не стало активным"