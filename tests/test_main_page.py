import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import DataBurgers
from locators import BurgersLocators


class TestMainPage:

    def test_link_personal_area(self, signin_main_driver):
        signin_main_driver.find_element(*BurgersLocators.PERSONAL_AREA_LINK).click()
        WebDriverWait(signin_main_driver, DataBurgers.TIME_WAIT).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, ".//li[contains(@class, 'Account_listItem')]/a[contains(@class, 'Account_link')]")))
        save_btn = signin_main_driver.find_element(*BurgersLocators.SAVE_BTN_IN_PERSONAL_AREA)
        assert save_btn.is_displayed()

    def test_buns_on_main_page(self, driver_chrome):
        driver_chrome.find_element(*BurgersLocators.FILLINGS_LINK).click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.visibility_of_element_located((
            By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient') and text()='Мясо бессмертных моллюсков Protostomia']"
        )))
        div_buns_class = driver_chrome.find_element(*BurgersLocators.BUNS_LINK)
        div_buns_class.click()
        WebDriverWait(driver_chrome, DataBurgers.TIME_WAIT).until(expected_conditions.visibility_of_element_located((
            By.XPATH,
            ".//p[contains(@class, 'BurgerIngredient_ingredient') and text()='Флюоресцентная булка R2-D3']"
        )))
        assert "current" in div_buns_class.get_attribute("class")

    def test_sauces_on_main_page(self, driver_chrome):
        div_sauces_class = driver_chrome.find_element(*BurgersLocators.SAUCES_LINK)
        div_sauces_class.click()
        assert "current" in div_sauces_class.get_attribute("class")

    def test_fillings_on_main_page(self, driver_chrome):
        div_fillings_class = driver_chrome.find_element(*BurgersLocators.FILLINGS_LINK)
        div_fillings_class.click()
        assert "current" in div_fillings_class.get_attribute("class")
