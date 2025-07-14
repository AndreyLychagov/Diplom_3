import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.click_order_feed_button()

        with allure.step("Переход обратно в конструктор"):
            main_page.click_constructor_button()

        with allure.step("Проверка, что перешли обратно в конструктор"):
            assert main_page.is_header_title_visible(), "Не удалось вернуться в конструктор"

    @allure.title("Переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.click_order_feed_button()

        with allure.step("Проверка, что перешли в ленту заказов"):
            assert order_feed_page.is_feed_header_visible(), "Не удалось перейти в ленту заказов"

    @allure.title("Открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)

        with allure.step("Клик по ингредиенту"):
            main_page.open_ingredient_details("bun")

        with allure.step("Проверка, что открылись детали ингридиента"):
            assert main_page.is_ingredient_details_visible(), "Модальное окно с деталями ингредиента не открылось"

    @allure.title("Закрытие модального окна")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открытие модального окна"):
            main_page.open_ingredient_details("bun")
            assert main_page.is_ingredient_details_visible(), "Модальное окно не открылось"

        with allure.step("Закрытие модального окна"):
            main_page.close_ingredient_modal()

        with allure.step("Проверка, что модальное окно закрылось"):
            assert main_page.is_ingredient_modal_closed(), "Модальное окно не закрылось"

    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)

        initial_count = main_page.get_counter_value()

        with allure.step("Перетаскиваем булку в конструктор"):
            main_page.drag_bun_to_constructor()

        new_count = main_page.get_counter_value()

        with allure.step("Проверка, что счетчик увеличился"):
            assert new_count > initial_count


    @allure.title("Оформление заказа авторизованным пользователем")
    def test_place_order(self, driver, login):
        main_page = MainPage(driver)

        with allure.step("Добавление булки и оформление заказа"):
            main_page.drag_bun_to_constructor()
            main_page.click_order_button()

        with allure.step("Проверка номера заказа"):
            assert main_page.is_order_modal_opened(), "Модальное окно заказа не появилось"