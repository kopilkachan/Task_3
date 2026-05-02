from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage
import allure 


class FeedPage(BasePage):

    @allure.step('Кликнуть по заказу')
    def click_order(self):
        self.click(FeedPageLocators.FIRST_ORDER)

    @allure.step('Проверить видимость окна деталей заказа')
    def is_visible_ins(self):
        return self.on_displayed(FeedPageLocators.MODAL_ORDER_WINDOW_OPEN)
    
    @allure.step('Получить номера первых трех заказов')
    def get_first_three_orders(self):
        return self.get_num_locators(FeedPageLocators.THREE_ORDERS_IN_FEED)
    
    @allure.step('Получить количество заказов из "Выполнено за все время"')
    def get_all_count_orders(self):
        return self.take_text(FeedPageLocators.ALL_ORDERS_SUM)
    
    @allure.step('Получить количество заказов из "Выполнено за сегодня"')
    def get_today_count_orders(self):
        return self.take_text(FeedPageLocators.ALL_TODAY_ORDERS_SUM)
    
    @allure.step('Получить номера первых трех в работе')
    def get_first_three_orders_in_work(self):
        return self.get_num_locators(FeedPageLocators.IN_WORK_LIST)
    
    @allure.step('Привести номер заказа к формату из блока "В работе"')
    def refact_order_num(self, num):
        return num.lstrip('#')
