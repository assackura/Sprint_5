import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from helpers import Help
from locators import BurgersLocators

class TestStellarBurgerRegisterPage:

    @pytest.mark.parametrize('name,email,password', [['Woody', Help.generate_email(), Help.generate_password()], ['Scooby', Help.generate_email(), Help.generate_password()], ['Chilly', Help.generate_email(), Help.generate_password()]])
    def test_register_page_correct_login_password(self, register_page_driver, name, email, password):
        register_page_driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER).send_keys(password)
        register_page_driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER).send_keys(email)
        register_page_driver.find_element(*BurgersLocators.INPUT_NAME_REGISTER).send_keys(name)
        register_page_driver.find_element(*BurgersLocators.BUTTON_REGISTER).click()
        WebDriverWait(register_page_driver, DataBurgers.TIME_WAIT).until(expected_conditions.url_contains("login"))

        assert register_page_driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_show_error_for_not_correct_password(self, register_page_driver):
        register_page_driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER).send_keys("1")
        register_page_driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER).send_keys("1")
        text_element = register_page_driver.find_element(*BurgersLocators.ERROR_TEXT_PASSWORD).text
        assert text_element == 'Некорректный пароль'


