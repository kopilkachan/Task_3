import allure
from pages.account_page import AccountPage
from pages.home_page import HomePage
from data import URL

class TestAccount:

    @allure.title('Проверка перехода переход по клику на «Личный кабинет»')
    def test_click_account_open_account_page(self, browser, create_user):
        acc = AccountPage(browser)
        home = HomePage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.click_account(URL.PERSONAL_ACCOUNT)
        assert browser.current_url == URL.PERSONAL_ACCOUNT

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_click_history_orders_open_page(self, browser, create_user):
        acc = AccountPage(browser)
        home = HomePage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.click_account(URL.PERSONAL_ACCOUNT)
        acc.click_history_order()
        assert browser.current_url == URL.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_click_exit_to_login_page(self, browser, create_user):
        acc = AccountPage(browser)
        home = HomePage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.click_account(URL.PERSONAL_ACCOUNT)
        acc.click_exit(URL.LOGIN_PAGE)
        assert browser.current_url == URL.LOGIN_PAGE