import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Переход в ленту заказов"):
            main_page.click_order_feed_button()
            order_feed_page.wait_for_feed_loaded()

        with allure.step("Клик по иконке заказа"):
            order_feed_page.click_order_icon()

        with allure.step("Проверка отображения состава заказа в модальном окне"):
            assert order_feed_page.is_order_details_modal_visible(), "Раздел 'Состав' в модальном окне не отобразился"

    @allure.title("Заказ пользователя отображается на странице ленты заказов")
    def test_user_order_in_feed(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создание нового заказа"):
            main_page.drag_bun_to_constructor()
            main_page.click_order_button()
            order_number = main_page.wait_for_real_order_number()
            main_page.safely_close_modal()

        with allure.step("Переход в ленту заказов"):
            main_page.click_order_feed_button()
            order_feed_page.wait_for_feed_loaded()

        with allure.step("Проверка отображения заказа в ленте"):
            displayed_numbers = order_feed_page.get_displayed_order_numbers()
            assert order_number in displayed_numbers, \
                f"Заказ {order_number} не найден в ленте. Отображаются: {displayed_numbers}"

    @allure.title("При создании заказа счетчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increase(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получение начального значения счетчика"):
            main_page.safely_click_order_feed_button()
            order_feed_page.wait_for_feed_loaded()
            initial_count = order_feed_page.get_total_orders()

        with allure.step("Создание нового заказа"):
            main_page.click_constructor_button()
            main_page.drag_bun_to_constructor()
            main_page.click_order_button()
            main_page.wait_for_real_order_number()
            main_page.safely_close_modal()

        with allure.step("Проверка увеличения счетчика"):
            main_page.click_order_feed_button()
            order_feed_page.wait_for_total_increase(initial_count)
            new_count = order_feed_page.get_total_orders()
            assert new_count > initial_count, \
                f"Ожидалось, что счетчик увеличится. Было: {initial_count}, стало: {new_count}"

    @allure.title("При создании заказа счетчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increase(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получение начального значения счетчика"):
            main_page.safely_click_order_feed_button()
            order_feed_page.wait_for_feed_loaded()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Создание нового заказа"):
            main_page.click_constructor_button()
            main_page.drag_bun_to_constructor()
            main_page.click_order_button()
            main_page.wait_for_real_order_number()
            main_page.safely_close_modal()

        with allure.step("Проверка увеличения счетчика"):
            main_page.safely_click_order_feed_button()
            order_feed_page.wait_for_today_increase(initial_today)
            new_today = order_feed_page.get_today_orders_count()
            assert new_today > initial_today, \
                f"Ожидалось, что счетчик 'Сегодня' увеличится. Было: {initial_today}, стало: {new_today}"

    @allure.title("Номер заказа появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создание заказа и получение его номера"):
            main_page.drag_bun_to_constructor()
            main_page.click_order_button()
            order_number = main_page.wait_for_real_order_number().lstrip('0')
            main_page.safely_close_modal()

        with allure.step("Переход в ленту заказов"):
            main_page.safely_click_order_feed_button()
            order_feed_page.wait_for_feed_loaded()

        with allure.step("Проверка раздела 'В работе'"):
            orders_in_progress = order_feed_page.get_orders_in_progress()
            assert order_number in orders_in_progress, \
                f"Заказ {order_number} не найден в разделе 'В работе'. Текущие заказы: {orders_in_progress}"