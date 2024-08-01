import pytest

from selenium import webdriver
from data import DataBurgers

@pytest.fixture(scope='function')
def driverChrome():
    driver_chrome = webdriver.Chrome()
    driver_chrome.get(DataBurgers.MAIN_URL)
    yield driver_chrome

    driver_chrome.quit()
