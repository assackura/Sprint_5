from selenium.webdriver.common.by import By

class BurgersLocators:

    SIGN_IN_ACCOUNT_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")
    INPUT_NAME_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[1]//input")
    INPUT_EMAIL_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[2]//input")
    INPUT_PASSWORD_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input[@name='Пароль']")
    BUTTON_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Зарегистрироваться']")
    ERROR_TEXT_PASSWORD = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//p[text()='Некорректный пароль']")
    BUTTON_SIGNIN_ON_PAGE_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Войти']")
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[1]//input")
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input[@name='Пароль']")
    CHECKOUT_BTN = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket']//button[text()='Оформить заказ']")
    H1_ASSEMBLE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a")
    AUTH_LINK_IN_REGISTER_PAGE = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Войти']")
    FORGOT_PWD_LINK = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")