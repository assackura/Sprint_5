from selenium.webdriver.common.by import By

class BurgersLocators:

    SIGN_IN_ACCOUNT_BTN = (By.XPATH, ".//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт"
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']") #Ссылка на страницу "Зарегистрироваться"
    INPUT_NAME_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[1]//input") #Поле для ввода имени при регистрации
    INPUT_EMAIL_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[2]//input") #Поле для ввода email при регистрации
    INPUT_PASSWORD_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input[@name='Пароль']") #Поле для ввода пароля при регистрации
    BUTTON_REGISTER = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Зарегистрироваться']") #Кнопка зарегистрироваться
    ERROR_TEXT_PASSWORD = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//p[text()='Некорректный пароль']") #Поле с ошибкой неверного пароля при регистрации
    BUTTON_SIGNIN_ON_PAGE_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Войти']") #Кнопка "Войти"
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]/fieldset[1]//input") #Поле для ввода email на странице login
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//input[@name='Пароль']") #Поле для ввода пароля на странице login
    CHECKOUT_BTN = (By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button[text()='Оформить заказ']") #кнопка "Оформить заказ"
    H1_ASSEMBLE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']") #Заголовок на главное странице "Соберите бургер"
    PERSONAL_AREA_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']/parent::a") #Ссылка на "личный кабинет"
    AUTH_LINK_IN_REGISTER_PAGE = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Войти']") #Ссылка на страницу авторизации на странице регистрации
    FORGOT_PWD_LINK = (By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']") #Ссылка на страницу "Восстановить пароль"
    SAVE_BTN_IN_PERSONAL_AREA = (By.XPATH, ".//div[contains(@class, 'Profile_buttonBox')]/button[text()='Сохранить']") #Кнопка "Сохранить" в личном кабинете
    LINK_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a") #Логотип бургерной
    LOGOUT_BTN_PESONAL_AREA = (By.XPATH, ".//ul[contains(@class, 'Account_list')]//button[text()='Выход']") #Кнопка "Выход" в личном кабинете
    BUNS_LINK = (By.XPATH, ".//span[text()='Булки']/parent::div") #Раздел "Булки" в конструкторе
    SAUCES_LINK = (By.XPATH, ".//span[text()='Соусы']/parent::div") #Раздел "Соусы" в конструкторе
    FILLINGS_LINK = (By.XPATH, ".//span[text()='Начинки']/parent::div") #Раздел "Начинки" в конструкторе
    BUTTON_RESTORE = (By.XPATH, ".//form[contains(@class, 'Auth_form')]//button[text()='Восстановить']")  # Кнопка "Восстановить"
    ING_MAIN_PAGE_MEAT = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient') and text()='Мясо бессмертных моллюсков Protostomia']") #Ингридиент в конструкторе
    ING_MAIN_PAGE_BUNS = (By.XPATH, ".//p[contains(@class, 'BurgerIngredient_ingredient') and text()='Флюоресцентная булка R2-D3']") #Ингридиент в конструкторе