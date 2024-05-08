# Sprint_5

Проект состоит из:
 - Файл с фикстурами - conftest.py
 - Файл с данными пользователей (текущего и рандомного) - data.py
 - Файл локаторов - locators.py, 
 - Файл с сылками использумемыми в тесте - url_s.py, 
 - Файл gitignor

**Описание проекта:**
- Файл "test_registratoin.py":
    - Проверка успешной регистрации
    - Проверка появления сообщения при не корректном вводе
- Файл "test_login.py":
  - Проверка входа по кнопке «Войти в аккаунт» на главной
  - Проверка входа через кнопку «Личный кабинет»
  - Проверка входа через кнопку в форме регистрации
  - Проверка входа через кнопку в форме восстановления пароля
- Файл "test_transfer_in_personal_account.py" - Проверка перехода по клику на «Личный кабинет»
- Файл "test_transfer_from_personal_account_to_constructor.py":
  - Проверка перехода по клику на "Конструктор"
  - Проверка перехода по клику на логотип Stellar Burgers
- Файл "test_exit_from_account.py" - Проверка выхода по кнопке «Выйти» в личном кабинете
- Файл "test_constructor.py"- Проверен переход по разеделам "Булки", "Соусы" и "Начинки"