from locators.home_page_locators import HomePageLocators 
from pages.base_page import BasePage
import allure 
from data import URL


class HomePage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_account(self, URL):
        self.click_js(HomePageLocators.PERSONAL_ACCOUNT)
        self.wait_for_url_to_be(URL)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_orders(self):
        self.click_js(HomePageLocators.ORDERS_FEED)

    @allure.step('Открыть страницу ленты заказов"')
    def open_feed_orders(self):
        self.open_page(URL.ORDERS_FEED)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor(self):
        self.click_js(HomePageLocators.CONSTRUCTOR)

    @allure.step('Клик ингредиенту булка r2-d3')
    def click_bun(self):
        self.click(HomePageLocators.R2_D3_BUN)
    
    @allure.step('Появилось модальное окно описания ингредиента')
    def is_visible_descr(self):
        return self.on_displayed(HomePageLocators.H2_INGREDIENT_CARD)
    
    allure.step('Ожидание закрытия модального окна')
    def is_close_descr(self):
        return self.wait_close(HomePageLocators.H2_INGREDIENT_CARD)

    @allure.step('Закрыть окно описания')
    def exit_descr(self):
        self.click(HomePageLocators.CLOSE_BUTTON)   

    @allure.step('Перетянуть ингредиент в окно сборки')
    def drag_drop_ingredient(self):
        self.drag_drop(HomePageLocators.R2_D3_BUN, HomePageLocators.CONSTRUCTOR_MODAL)

    @allure.step('Посмотреть счетчик ингридиента до использования продукта')
    def check_count(self):
        return self.take_text(HomePageLocators.COUNTER_R2_D3)
    
    @allure.step('Посмотреть счетчик ингридиента после использования продукта')
    def check_count_after(self):
        self.on_displayed(HomePageLocators.COUNTER_R2_D3_2)
        return self.take_text(HomePageLocators.COUNTER_R2_D3_2)

    @allure.step('Получить счетчик ингредиента')
    def click_order_button(self):
        self.click(HomePageLocators.ORDER_BUTTON)
    
    @allure.step('Получить номер заказа')
    def check_num_order(self):
        return self.take_text(HomePageLocators.ORDER_NUM)
    
    @allure.step('Закрыть окно оформленного')
    def exit_order(self):
        self.wait_close(HomePageLocators.OVERLAY)
        self.click_js(HomePageLocators.CLOSE_BUTTON)
    