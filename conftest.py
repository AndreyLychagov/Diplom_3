import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

main_url = "https://stellarburgers.nomoreparties.site/"


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")  # Раскомментировать для CI
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")  # Раскомментировать для CI
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(main_url)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from pages.profile_page import ProfilePage

    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)

    # Переход на страницу логина
    main_page.click_personal_account_button()

    # Ввод тестовых данных
    login_page.enter_email("aspirine@mail.ru")
    login_page.enter_password("test121")
    login_page.click_login_button()

    # Проверка успешного входа
    assert main_page.is_order_button_visible(), "Вход не выполнен"

@pytest.fixture
def test_email():
    return "test@example.com"
