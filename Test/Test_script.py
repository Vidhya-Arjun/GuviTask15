from selenium.webdriver.common.by import By

from POM.Login import Login
from utils.Excel_Reader import Excel_Reader


def test_Login(browser_start):
    driver = browser_start
    login = Login(driver)
    login.OpenUrl("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    test_data = Excel_Reader.get_data("C:\\Users\\vidhy\\PycharmProjects\\GuviTask15\\TestData\\Test_data.xlsx","Test_data")
    print(test_data)
    for row in test_data:
        UserName = row[1]
        Password = row[2]
        login.send_user_name(UserName)
        login.send_password(Password)
        login.login_click()

    assert driver.current_url== "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index" ,"test failed,user unable to login"