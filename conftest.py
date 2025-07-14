import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from urls import MAIN_URL
from data import VALID_LOGIN_EMAIL, VALID_LOGIN_PASSWORD


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
    driver.get(MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)

    # Переход на страницу логина
    main_page.click_personal_account_button()

    # Ввод тестовых данных
    login_page.enter_email(VALID_LOGIN_EMAIL)
    login_page.enter_password(VALID_LOGIN_PASSWORD)
    login_page.click_login_button()