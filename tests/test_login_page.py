import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from locators import BurgersLocators

class TestLoginPage:

    def test_login_from_btn_signin_account(self, driver_chrome):
        driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        driver_chrome.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
        driver_chrome.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
        driver_chrome.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert driver_chrome.find_element(*BurgersLocators.H1_ASSEMBLE_BURGER).is_displayed()

    def test_login_from_personal_area(self, driver_chrome):
        driver_chrome.find_element(*BurgersLocators.PERSONAL_AREA_LINK).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        driver_chrome.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
        driver_chrome.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
        driver_chrome.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert driver_chrome.find_element(*BurgersLocators.H1_ASSEMBLE_BURGER).is_displayed()

    def test_login_from_link_in_page_register(self, register_page_driver):
        register_page_driver.find_element(*BurgersLocators.AUTH_LINK_IN_REGISTER_PAGE).click()
        WebDriverWait(register_page_driver, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        register_page_driver.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
        register_page_driver.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
        register_page_driver.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
        WebDriverWait(register_page_driver, DataBurgers.TIME_WAIT).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert register_page_driver.find_element(*BurgersLocators.H1_ASSEMBLE_BURGER).is_displayed()

    def test_login_from_link_in_page_forgot_pwd(self, driver_chrome):
        driver_chrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        driver_chrome.find_element(*BurgersLocators.FORGOT_PWD_LINK).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("forgot-password"))
        driver_chrome.find_element(*BurgersLocators.AUTH_LINK_IN_REGISTER_PAGE).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        driver_chrome.find_element(*BurgersLocators.INPUT_PASSWORD_LOGIN).send_keys(DataBurgers.USER_PASSWORD)
        driver_chrome.find_element(*BurgersLocators.INPUT_EMAIL_LOGIN).send_keys(DataBurgers.USER_LOGIN)
        driver_chrome.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, ".//h1[text()='Соберите бургер']")))
        assert driver_chrome.find_element(*BurgersLocators.H1_ASSEMBLE_BURGER).is_displayed()




