from selenium.webdriver.common.by import By 


class AccountPageLocators:

    RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
    EMAIL = (By.XPATH, ".//input[@type='text']")
    PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    ACTIVE_FIELD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    EYE_PASS = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    HISTORY_ORDERS = (By.XPATH, ".//a[text()='История заказов']")
    EXIT_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")
    LAST_ORDER = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    R2_D3_IN_HISTORY = (By.XPATH, ".//h2[text()='Флюоресцентный бургер']")