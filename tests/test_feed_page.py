import allure
from pages.feed_page import FeedPage
from pages.home_page import HomePage
from pages.account_page import AccountPage
from data import URL


class TestFeed:

    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_click_order_open_details(self, browser):
        home = HomePage(browser)
        feed = FeedPage(browser)
        home.open_feed_orders()
        feed.click_order()

        assert feed.is_visible_ins() == True

    @allure.title('Проверка наличия заказов из "Истории заказов" в "Ленте заказов"')
    def test_check_order_in_feed_and_history(self, browser, create_user):
        home = HomePage(browser)
        acc = AccountPage(browser)
        feed = FeedPage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.drag_drop_ingredient()
        home.click_order_button()
        home.exit_order()
        home.click_account(URL.PERSONAL_ACCOUNT)
        acc.click_history_order()
        num1 = acc.set_last_order_num()
        feed.open_page(URL.ORDERS_FEED)
        nums_three = feed.get_first_three_orders()

        assert num1 in nums_three

    @allure.title('Проверка счетчика "Выполнено за всё время"')
    def test_count_all_orders(self, browser, create_user):
        home = HomePage(browser)
        acc = AccountPage(browser)
        feed = FeedPage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        feed.open_page(URL.ORDERS_FEED)
        num1 = feed.get_all_count_orders()
        home.click_constructor()
        home.drag_drop_ingredient()
        home.click_order_button()
        home.exit_order()
        home.click_feed_orders()
        num2 = feed.get_all_count_orders()

        assert int(num1) < int(num2)

    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    def test_count_all_today_orders(self, browser, create_user):
        home = HomePage(browser)
        acc = AccountPage(browser)
        feed = FeedPage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        feed.open_page(URL.ORDERS_FEED)
        num1 = feed.get_today_count_orders()
        home.click_constructor()
        home.drag_drop_ingredient()
        home.click_order_button()
        home.exit_order()
        home.click_feed_orders()
        num2 = feed.get_today_count_orders()

        assert int(num1) < int(num2)

    @allure.title('Проверка появление заказа в "В работе"')
    def test_ordrer_in_work_orders(self, browser, create_user):
        home = HomePage(browser)
        acc = AccountPage(browser)
        feed = FeedPage(browser)
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.drag_drop_ingredient()
        home.click_order_button()
        home.exit_order()
        home.click_account(URL.PERSONAL_ACCOUNT)
        acc.click_history_order()
        num1 = acc.set_last_order_num()
        num1 = feed.refact_order_num(num1)
        feed.open_page(URL.ORDERS_FEED)
        num2 = feed.get_first_three_orders_in_work()
        
        assert num1 in num2
    