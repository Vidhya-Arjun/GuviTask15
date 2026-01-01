from POM.Login import Login


def test_Login(browser_start):
        driver = browser_start
        login = Login(driver)
        login.OpenUrl("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login.send_user_name("Admin")
        login.send_password("admin123")
        login.login_click()
