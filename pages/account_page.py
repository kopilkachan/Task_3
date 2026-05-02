from locators.account_page_locators import AccountPageLocators
from locators.home_page_locators import HomePageLocators 
from pages.base_page import BasePage
import allure 
from data import URL


class AccountPage(BasePage):

    @allure.step('Открыть страницу входа')
    def open_login_page(self):
        self.open_page(URL.LOGIN_PAGE)

    @allure.step('Открыть страницу восстановления пароля')
    def open_forgot_pass_page(self):
        self.open_page(URL.FORGOT_PASS)

    @allure.step('Кликнуть по кнопке "Восстановить пароль')
    def click_recover_pass(self):
        self.click_js(AccountPageLocators.RECOVER_PASSWORD)

    @allure.step('Ввести email')
    def set_email(self, EMAIL):
        self.write(AccountPageLocators.EMAIL, EMAIL)

    @allure.step('Кликнуть по кнопке "Восстановить пароль')
    def click_recover_pass_button(self, URL):
        self.click_js(AccountPageLocators.RECOVER_BUTTON)
        self.wait_for_url_to_be(URL)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_eye_pass(self):
        self.click_js(AccountPageLocators.EYE_PASS)

    @allure.step('Проверить, что поле активно')
    def check_field(self):
        return self.on_displayed(AccountPageLocators.ACTIVE_FIELD)

    @allure.step('Общий шаг до страницы сброса пароля')
    def go_to_reset_pass_page(self, email):
        self.open_page(URL.FORGOT_PASS)
        self.write(AccountPageLocators.EMAIL, email)
        self.click(AccountPageLocators.RECOVER_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_order(self):
        self.wait_close(HomePageLocators.OVERLAY)
        self.click(AccountPageLocators.HISTORY_ORDERS)

    @allure.step('Получить номер последнего заказа"')
    def set_last_order_num(self):
        return self.take_text(AccountPageLocators.LAST_ORDER)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit(self, URL):
        self.click_js(AccountPageLocators.EXIT_ACCOUNT)
        self.wait_for_url_to_be(URL)

    @allure.step('Общий шаг ввода логопаса и вход')
    def login_test_user(self, email, password):
        self.click(HomePageLocators.PERSONAL_ACCOUNT)
        self.write(AccountPageLocators.EMAIL, email)
        self.write(AccountPageLocators.PASSWORD, password)
        self.click_js(AccountPageLocators.LOGIN_BUTTON)
        self.wait_for_url_to_be(URL.BASE_URL)
        