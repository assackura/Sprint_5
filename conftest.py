import pytest

from selenium import webdriver
from data import DataBurgers
from locators import BurgersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

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

@pytest.fixture(scope='function')
def signin_main_driver(driver_chrome):
    driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
    driver_chrome.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
    driver_chrome.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
    driver_chrome.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
    WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button[text()='Оформить заказ']")))
    driver_chrome.get(DataBurgers.MAIN_URL)
    return driver_chrome

@pytest.fixture(scope='function')
def goto_personal_area(signin_main_driver):
    signin_main_driver.find_element(*BurgersLocators.PERSONAL_AREA_LINK).click()
    WebDriverWait(signin_main_driver, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, ".//li[contains(@class, 'Account_listItem')]/a[contains(@class, 'Account_link')]")))
    return signin_main_driver
