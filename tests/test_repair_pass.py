import allure
from pages.account_page import LoginPage
from data import URL, LogoPass

class TestRepairPass:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_forgot_password_page_with_recover_pass(self, browser):
        login = LoginPage(browser)
        login.open_login_page()
        login.click_recover_pass()
        assert browser.current_url == URL.FORGOT_PASS
 
    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_set_pass_and_clickable_repair(self, browser):
        login = LoginPage(browser)
        login.open_forgot_pass_page()
        login.set_email(LogoPass.EMAIL)
        login.click_recover_pass_button(URL.RESET_PAGE)
        assert browser.current_url == URL.RESET_PAGE

    @allure.title('Проверка кнопки показать/окрыть пароль')
    def test_activity_field_click_eye(self, browser):
        login = LoginPage(browser)
        login.open_forgot_pass_page()
        login.set_email(LogoPass.EMAIL)
        login.click_recover_pass_button(URL.RESET_PAGE)
        login.click_eye_pass()
        assert login.check_field() == True
        