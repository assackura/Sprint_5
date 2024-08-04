import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from helpers import Help
from locators import BurgersLocators
from links import LinksBurgers

class TestStellarBurgerRegisterPage:

    @pytest.mark.parametrize('name,email,password', [['Woody', Help.generate_email(), Help.generate_password()], ['Scooby', Help.generate_email(), Help.generate_password()], ['Chilly', Help.generate_email(), Help.generate_password()]])
    def test_register_page_correct_login_password(self, register_page_driver, name, email, password):
        register_page_driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER).send_keys(password)
        register_page_driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER).send_keys(email)
        register_page_driver.find_element(*BurgersLocators.INPUT_NAME_REGISTER).send_keys(name)
        register_page_driver.find_element(*BurgersLocators.BUTTON_REGISTER).click()
        WebDriverWait(register_page_driver, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
            (BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN)))
        assert register_page_driver.current_url == LinksBurgers.LOGIN_URL

    def test_show_error_for_not_correct_password(self, register_page_driver):
        register_page_driver.find_element(*BurgersLocators.INPUT_PASSWORD_REGISTER).send_keys("1")
        register_page_driver.find_element(*BurgersLocators.INPUT_EMAIL_REGISTER).send_keys("1")
        text_element = register_page_driver.find_element(*BurgersLocators.ERROR_TEXT_PASSWORD).text
        assert text_element == 'Некорректный пароль'


