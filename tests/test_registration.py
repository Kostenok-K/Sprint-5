from data import UserData
from url_s import REGISTRATION_URL, LOGIN_PAGE_URL
from locators import LocatorsReg, LocatorsLoginPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration_successful(self, driver):
        driver.get(REGISTRATION_URL)
        driver.find_element(*LocatorsReg.NAME_FIELD).send_keys(UserData.random_user.get('name'))
        driver.find_element(*LocatorsReg.EMAIL_FIELD).send_keys(UserData.random_user.get('email'))
        driver.find_element(*LocatorsReg.PASSWORD_FIELD).send_keys(UserData.random_user.get('password'))
        driver.find_element(*LocatorsReg.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsLoginPage.ENTER_TITLE))

        assert driver.current_url == LOGIN_PAGE_URL

    def test_registration_password_error(self, driver):
        driver.get(REGISTRATION_URL)
        driver.find_element(*LocatorsReg.NAME_FIELD).send_keys(UserData.random_user.get('name'))
        driver.find_element(*LocatorsReg.EMAIL_FIELD).send_keys(UserData.random_user.get('email'))
        driver.find_element(*LocatorsReg.PASSWORD_FIELD).send_keys(" ")
        driver.find_element(*LocatorsReg.REG_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsReg.ERROR_MESSAGE))
        error_message = driver.find_element(*LocatorsReg.ERROR_MESSAGE).text
        assert error_message == "Некорректный пароль"
