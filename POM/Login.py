from POM.BaseCode import BaseCode
from selenium.webdriver.common.by import By

class Login(BaseCode):
    username = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    login = (By.XPATH,"//button[contains(normalize-space(),'Login')]")
    def __init__(self,driver):
        super().__init__(driver)
    def send_user_name(self,value):
        element = self.locate_element(self.username)
        element.clear()
        element.send_keys(value)
    def send_password(self,value):
        element = self.locate_element(self.password)
        element.clear()
        element.send_keys(value)
    def login_click(self):
        self.click_action(self.login)
    def OpenUrl(self,url):
        self.driver.get(url)