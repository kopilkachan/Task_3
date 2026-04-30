import allure
from pages.home_page import HomePage
from data import URL, Answer
from pages.account_page import AccountPage

class TestHomePage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_constructor_open_home_page(self, browser):
        home = HomePage(browser)
        home.open_feed_orders()
        home.click_constructor()
        assert browser.current_url == URL.BASE_URL

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_feed_open_feed_page(self, browser):
        home = HomePage(browser)
        home.click_feed_orders()
        assert browser.current_url == URL.ORDERS_FEED

    @allure.title('Клик на ингредиент вызвает всплывающее окно с деталями')
    def test_click_ing_open_modal_window(self, browser):
        home = HomePage(browser)
        home.click_bun()
        assert home.is_visible_descr() == True

    @allure.title('Клик на крестик закрывает всплывающее окно с деталями')
    def test_click_close_button_on_modal_window(self, browser):
        home = HomePage(browser)
        home.click_bun()
        home.exit_descr()
        home.is_close_descr()
        assert home.is_visible_descr() == False

    @allure.title('Проверка каунтера ингридиента')
    def test_take_ing_plus_count(self, browser):
        home = HomePage(browser)
        before = home.check_count()
        home.drag_drop_ingredient()
        home.check_count_after()
        after = home.check_count_after()
        assert int(before) < int(after)

    @allure.title('Проверка возможности оформить заказ залогиненным юзером')
    def test_can_create_order_login_user(self, browser, create_user):
        home = HomePage(browser)
        acc = AccountPage(browser)
        
        email = create_user["user_data"]["email"]
        password = create_user["user_data"]["password"]
        acc.login_test_user(email, password)
        home.click_order_button()
        assert home.check_num_order() == Answer.SUC_ORDER
    
       