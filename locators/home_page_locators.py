from selenium.webdriver.common.by import By 


class HomePageLocators:

    PERSONAL_ACCOUNT = (By.XPATH, ".//*[text()='Личный Кабинет']")
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    ORDERS_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    R2_D3_BUN = (By.XPATH, ".//img[@alt ='Флюоресцентная булка R2-D3']")
    H2_INGREDIENT_CARD = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
    CONSTRUCTOR_MODAL = (By.XPATH, ".//span[text() ='Перетяните булочку сюда (верх)']")
    COUNTER_R2_D3 = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[2]")
    COUNTER_R2_D3_2 = (By.XPATH, "//p[text()='2']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUM = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
    