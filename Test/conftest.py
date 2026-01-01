import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_start():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()