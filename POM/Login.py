from POM.BaseCode import BaseCode
from selenium.webdriver.common.by import By

class Login(BaseCode):
    username = (By.XPATH,"//input[@class='username']")
    password = (By.XPATH,"//input[@class='password']")
    login = (By.XPATH,"//button[contains(normalize-space(),'Login')]")
    def __init__(self,driver):
        super().__init__(driver)
    def send_user_name(self,value):
        self.locate_and_sendkeys(self.username,value)
    def send_password(self,value):
        self.locate_and_sendkeys(self.password,value)
    def login_click(self,login):
        self.click_action(login)
    def OpenUrl(self,url):
        self.driver.get(url)