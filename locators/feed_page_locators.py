from selenium.webdriver.common.by import By 


class FeedPageLocators:
        
    FIRST_ORDER = (By.XPATH, "(.//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]")
    MODAL_ORDER_WINDOW_OPEN = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    THREE_ORDERS_IN_FEED = (By.XPATH, "(//p[@class='text text_type_digits-default'])[position() <= 3]")
    ALL_ORDERS_SUM = (By.XPATH, ".//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class,'OrderFeed_number__2MbrQ')]")
    ALL_TODAY_ORDERS_SUM = (By.XPATH, ".//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class,'OrderFeed_number__2MbrQ')]")
    IN_WORK_LIST = (By.XPATH, ".//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2'][position() <= 3]")