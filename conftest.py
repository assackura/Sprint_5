import pytest

from selenium import webdriver
from data import DataBurgers
from locators import BurgersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope='function')
def driver_chrome():
    dc = webdriver.Chrome()
    dc.get(DataBurgers.MAIN_URL)
    yield dc

    dc.quit()

@pytest.fixture(scope='function')
def register_page_driver(driver_chrome):
    driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
    driver_chrome.find_element(*BurgersLocators.REGISTER_LINK).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("register"))
    return driver_chrome
