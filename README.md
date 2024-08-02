# Sprint_5
<h1>Тестирование сайта бургерной https://stellarburgers.nomoreparties.site/ </h1>

<h2>test/test_login_page.py</h2>

1) **test_login_from_btn_signin_account**<br>
        *Тест проверяет ввход по кнопке "Войти в аккаунт"*
2) **test_login_from_personal_area**<br>
        *Тест проверяет вход по кнопке "Личный кабинет"*
3) **test_login_from_link_in_page_register**<br>
        *Тест проверяет вход по ссылке на странице регистрации*
4) **test_login_from_link_in_page_forgot_pwd**<br>
        *Тест проверяет вход по ссылке на странице "Восстановить пароль"*

<h2>test/test_main_page.py</h2>

1) **test_link_personal_area**<br>
        *Тест проверяет работоспособность ссылки/кнопки "Личный кабинет"*
2) **test_buns_on_main_page**<br>
        *Тест проверяет кнопку "Булки" в конструкторе*
3) **test_sauces_on_main_page**<br>
        *Тест проверяет кнопку "Соусы" в конструкторе*
4) **test_fillings_on_main_page**<br>
        *Тест проверяет кнопку "Начинки" в конструкторе*

<h2>test/test_personal_area_page.py</h2>

1) **test_click_logo_from_personal_area**<br>
        *Тест проверяет работоспособность логотипа со страницы "Личный кабинет"*
2) **test_logout_btn_from_personal_area**<br>
        *Тест проверяет кнопку "Выход" в личном кабинете*

<h2>test/test_register_page.py</h2>

1) **test_register_page_correct_login_password**<br>
        *Тест проверяет корректность регистрации с генерацией логинов и паролей*
2) **test_show_error_for_not_correct_password**<br>
        *Тест проверяет наличие ошибки, если ввести меньше 6 символов в поле пароль*

<h2>conftest.py</h2>
    *Фикстуры для тестов*

<h2>data.py</h2>
    *Константы используемые в тестах*

<h2>helpers.py</h2>
    *Вспомогательные функции, в данном случае только генераторы email и паролей*

<h2>locators.py</h2>
    *Используемые в тестах локаторы*