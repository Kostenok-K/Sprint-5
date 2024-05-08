from selenium.webdriver.common.by import By


class LocatorsReg:
    NAME_FIELD = (By.XPATH, "(//form//input)[1]")
    # Страница регистрации, форма регистрации поле ввода Имя
    EMAIL_FIELD = (By.XPATH, "(//form//input)[2]")
    # Страница регистрации, форма регистрации поле ввода E-mail
    PASSWORD_FIELD = (By.XPATH, "(//form//input)[3]")
    # Страница регистрации, форма регистрации поле ввода Password
    REG_BUTTON = (By.XPATH, "//form//button")
    # Страница регистрации, форма регистрации кнопка Зарегистрироваться
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    # Страница регистрации, ссылка Войти
    ERROR_MESSAGE = (By.XPATH, "//form//p[contains (@class, 'input__error')]")
    # Страница регистрации, сообщение об ошибки


class LocatorsMainPage:
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, ".//main//button")
    # Главная кнопка Войти в аккаунт
    SUBMIT_BUTTON = (By.XPATH, ".//main//button[text()='Оформить заказ']")
    # Главная кнока Оформить заказ
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1")
    # Главная заголовок Соберите бургер
    BREAD_TAB = (By.XPATH, "(//section[contains(@class, 'BurgerIngredients')]//div[contains(@class, 'noselect')])[1]")
    # Главная, таб Булки
    SAUCES_TAB = (By.XPATH, "(//section[contains(@class, 'BurgerIngredients')]//div[contains(@class, 'noselect')])[2]")
    # Главная, таб Соусы
    TOPPING_TAB = (By.XPATH, "(//section[contains(@class, 'BurgerIngredients')]//div[contains(@class, 'noselect')])[3]")
    # Главная, таб Начинки


class LocatorsLoginPage:
    LOGIN_BUTTON = (By.XPATH, "//form//button")
    # Страниа входа, кнопка Войти
    EMAIL_FIELD = (By.XPATH, "//form//input[@type='text']")
    # Страница входа, поле ввода E-mail
    PASSWORD_FIELD = (By.XPATH, "//form//input[@type='password']")
    # Страница входа, поле ввода Password
    ENTER_TITLE = (By.XPATH, "//h2[text()='Вход']")
    # Страница входа, заголовок Вход


class LocatorsHeaderNav:
    CONSTRUCTOR_LINK = (By.XPATH, "//nav//a[contains(@class, 'AppHeader') and @href='/']")
    # Хедер ссылка под Контруктор
    LOGO_LINK = (By.XPATH, "//nav//div[contains(@class, 'logo')]//a")
    # Хедер ссылка под Лого
    ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")
    # Хедер ссылка под Личный Кабинет


class LocatorsAccountProfile:
    LOGOUT_BUTTON = (By.XPATH, "//nav//button")
    #  Страница ЛК, кнопка Выход
