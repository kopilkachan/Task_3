from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_js(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))  
        self.driver.execute_script("arguments[0].click();", element)

    def write(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def on_displayed(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
        
    def wait_close(self, locator):
        self.wait.until_not(EC.visibility_of_element_located(locator))

    def take_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def drag_drop(self, locator_from, locator_to):
        source = self.wait.until(EC.presence_of_element_located(locator_from))
        target = self.wait.until(EC.presence_of_element_located(locator_to))
        self.driver.execute_script("""
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function (key, value) {
                        this.data[key] = value;
                    },
                    getData: function (key) {
                        return this.data[key];
                    }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                if (element.dispatchEvent) {
                    element.dispatchEvent(event);
                } else if (element.fireEvent) {
                    element.fireEvent("on" + event.type, event);
                }
            }
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(arguments[0], dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(arguments[1], dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(arguments[0], dragEndEvent, dragStartEvent.dataTransfer);
        """, source, target)

    def get_num_locators(self, locator):
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]
        
    def wait_for_url_to_be(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))

    def get_current_url(self):
        return self.driver.current_url
    