from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseCode():


    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,timeout)
    def locate_and_sendkeys(self,locator,value):
         element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
         element.send_keys(value)
    def click_action(self,locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        element.click()