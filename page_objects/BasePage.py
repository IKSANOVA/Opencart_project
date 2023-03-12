from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser        

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError("Не найден элемент по локатору: {}".format(locator))


    @allure.step("Поиск элемента {locator}")
    def _element(self, locator: tuple):
        try:
            return self._verify_element_presence(locator)
        except TimeoutException as e:
            allure.attach(body = self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise AssertionError(e.msg)
            self.logger.error(f"Element {locator} not found")
            raise AssertionError(f"Element {locator} can't be found")


    def _simple_click_element(self, element):
        element.click()
    
    @allure.step("Поиск элемента {locator}")
    def _check_title(self, locator):
        return WebDriverWait(self.browser, 5).until(EC.title_is(locator))


    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).move_to_element(element).click().perform()
        


    def _elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найден элемент по локатору {locator}",
        )
        
        
    def _count(self, locator, count):
        element = self._elements(locator)       
        if len(element) != count:
            raise AssertionError(f"{count} != {len(element)}")
