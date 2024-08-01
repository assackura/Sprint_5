import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from helpers import Help
from locators import BurgersLocators

class TestStellarBurgerRegisterPage:

    @pytest.mark.parametrize('name,email,password', [['Woody', Help.generate_email(), '123456'], ['Scooby', Help.generate_email(), 'dfkjhdfkg'], ['Chilly', Help.generate_email(), 'Dhh123$##DSAY@~%f2']])
    def test_register_page_correct_login_password(self, driverChrome, name, email, password):
        driverChrome.find_element(*BurgersLocators.SIGN_IN_ACCOUNT_BTN).click()
        WebDriverWait(driverChrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))
        driverChrome.find_element(*BurgersLocators.REGISTER_LINK).click()
        WebDriverWait(driverChrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("register"))
        driverChrome.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER).send_keys(password)
        driverChrome.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER).send_keys(email)
        driverChrome.find_element(*BurgersLocators.INPUT_NAME_REGISTER).send_keys(name)
        driverChrome.find_element(*BurgersLocators.BUTTON_REGISTER).click()
        WebDriverWait(driverChrome, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))

        assert driverChrome.current_url == 'https://stellarburgers.nomoreparties.site/login'

