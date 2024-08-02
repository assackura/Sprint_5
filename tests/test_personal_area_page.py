import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from locators import BurgersLocators


class TestPersonalArea:

    def test_click_logo_from_personal_area(self, goto_personal_area):
        goto_personal_area.find_element(*BurgersLocators.LINK_LOGO).click()
        WebDriverWait(goto_personal_area, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button[text()='Оформить заказ']")))
        order_btn = goto_personal_area.find_element(*BurgersLocators.CHECKOUT_BTN)
        assert order_btn.is_displayed()

    def test_logout_btn_from_personal_area(self, goto_personal_area):
        goto_personal_area.find_element(*BurgersLocators.LOGOUT_BTN_PESONAL_AREA).click()
        WebDriverWait(goto_personal_area, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//form[contains(@class, 'Auth_form')]/button[text()='Войти']")))
        sign_in_btn = goto_personal_area.find_element(*BurgersLocators.BUTTON_SIGNIN_ON_PAGE_LOGIN)
        assert sign_in_btn.is_displayed()

