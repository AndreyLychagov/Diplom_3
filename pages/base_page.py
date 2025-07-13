from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site/"

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False

    def scroll_to_element(self, element_or_locator):
        if isinstance(element_or_locator, tuple):
            element = self.find_element(element_or_locator)
        else:
            element = element_or_locator
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def drag_and_drop(self, source, target):
        self.scroll_to_element(source)
        self.scroll_to_element(target)

        actions = ActionChains(self.driver)
        actions.move_to_element(source)
        actions.click_and_hold()
        actions.pause(0.3)
        actions.move_to_element(target)
        actions.pause(0.3)
        actions.release()
        actions.perform()

    def drag_and_drop_js(self, source, target):
        js_script = """
            function simulateDragDrop(sourceNode, targetNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop',
                    DRAG_OVER: 'dragover'
                };

                function createCustomEvent(type) {
                    var event = new CustomEvent("CustomEvent");
                    event.initCustomEvent(type, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(type, val) {
                            this.data[type] = val;
                        },
                        getData: function(type) {
                            return this.data[type];
                        }
                    };
                    return event;
                }

                function dispatchEvent(node, type, event) {
                    if (node.dispatchEvent) {
                        return node.dispatchEvent(event);
                    }
                    if (node.fireEvent) {
                        return node.fireEvent("on" + type, event);
                    }
                }

                var event = createCustomEvent(EVENT_TYPES.DRAG_START);
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);

                var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                dropEvent.dataTransfer = event.dataTransfer;
                dispatchEvent(targetNode, EVENT_TYPES.DROP, dropEvent);

                var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                dragEndEvent.dataTransfer = event.dataTransfer;
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
            }

            simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_script, source, target)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не стал видимым за {timeout} сек"
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не стал кликабельным за {timeout} сек"
        )

    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator),
            message=f"Элемент {locator} не исчез за {timeout} сек"
        )

    def click_via_actions(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    def wait_for_text_change(self, locator, initial_text, timeout=15):
        def is_text_changed(driver):
            return driver.find_element(*locator).text != initial_text

        self.wait_for_condition(is_text_changed, timeout)

    def wait_for_condition(self, condition, timeout=10, message=""):
        return WebDriverWait(self.driver, timeout).until(
            condition,
            message=message
        )

    def safe_click(self, locator, timeout=10):
        button = self.wait_for_element_clickable(locator, timeout)
        if "firefox" in self.driver.capabilities.get("browserName", "").lower():
            self.driver.execute_script("arguments[0].click();", button)
        else:
            button.click()

    def is_firefox(self):
        return "firefox" in self.driver.capabilities.get("browserName", "").lower()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def wait_for_element_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден на странице за {timeout} сек"
        )

    def get_current_url(self):
        return self.driver.current_url

    def safe_click_with_modal_handling(self, locator, modal_overlay_locator=None, timeout=10):
        try:
            self.click(locator, timeout)
        except ElementClickInterceptedException:
            if modal_overlay_locator:
                self.wait_for_element_invisible(modal_overlay_locator, timeout)
            button = self.wait_for_element_clickable(locator, timeout)
            self.click_via_actions(button)

    def get_element_text_or_default(self, locator, default=0, timeout=3):
        try:
            return int(self.find_element(locator, timeout).text or default)
        except:
            return default

    def wait_for_text_condition(self, locator, condition_func, timeout=10, message=""):
        """
        Ждет, пока текст элемента будет удовлетворять условию condition_func
        :param condition_func: Функция, принимающая текст элемента и возвращающая bool
        """

        def _inner(driver):
            try:
                element = self.find_element(locator)
                current_text = element.text.strip()
                return condition_func(current_text)
            except:
                return False

        self.wait_for_condition(_inner, timeout=timeout, message=message)
        return self.find_element(locator).text.strip()