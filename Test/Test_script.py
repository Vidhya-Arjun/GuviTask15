import time

from selenium.webdriver.common.by import By
import pytest
from POM.Login import Login
from utils.Excel_Reader import read_data,write_excel_data


@pytest.mark.parametrize("row, username, password",read_data())
def test_Login(browser_start,row,username,password):
    driver = browser_start
    login = Login(driver)
    login.OpenUrl("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    login.send_user_name(username)
    login.send_password(password)
    login.login_click()
    time.sleep(3)

    print(username,password)
    try:
        assert "dashboard" in driver.current_url
        write_excel_data(row,"PASS")
    except AssertionError:
        write_excel_data(row,"FAIL")
        raise
