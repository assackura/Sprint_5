from selenium.webdriver.common.by import By

class BurgersLocators:

    SIGN_IN_ACCOUNT_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    INPUT_NAME_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[1]//input")
    INPUT_EMAIL_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[2]//input")
    INPUT_PASSWORD_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input[@name='Пароль']")
    BUTTON_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Зарегистрироваться']")