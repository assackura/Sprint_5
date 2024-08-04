import pytest

from selenium import webdriver
from data import DataBurgers
from locators import BurgersLocators
from links import LinksBurgers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def driver_chrome():
    dc = webdriver.Chrome()
    dc.get(LinksBurgers.MAIN_URL)
    yield dc

    dc.quit()

@pytest.fixture(scope='function')
def register_page_driver(driver_chrome):
    driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN)))
    driver_chrome.find_element(*BurgersLocators.REGISTER_LINK).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (BurgersLocators.BUTTON_REGISTER)))
    return driver_chrome

@pytest.fixture(scope='function')
def signin_main_driver(driver_chrome):
    driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN)))
    driver_chrome.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
    driver_chrome.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
    driver_chrome.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (BurgersLocators.CHECKOUT_BTN)))
    driver_chrome.get(LinksBurgers.MAIN_URL)
    return driver_chrome

@pytest.fixture(scope='function')
def goto_personal_area(signin_main_driver):
    signin_main_driver.find_element(*BurgersLocators.PERSONAL_AREA_LINK).click()
    WebDriverWait(signin_main_driver, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (BurgersLocators.SAVE_BTN_IN_PERSONAL_AREA)))
    return signin_main_driver
