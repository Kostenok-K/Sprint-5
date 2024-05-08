from url_s import MAIN_PAGE_URL, REGISTRATION_URL, RECOVERY_PAGE_URL
from locators import LocatorsMainPage, LocatorsLoginPage, LocatorsReg, LocatorsHeaderNav
from data import UserData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_using_button_on_main_page(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.LOGIN_BUTTON_MAIN_PAGE))
        driver.find_element(*LocatorsMainPage.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*LocatorsLoginPage.EMAIL_FIELD).send_keys(UserData.current_user.get('email'))
        driver.find_element(*LocatorsLoginPage.PASSWORD_FIELD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.SUBMIT_BUTTON))
        assert driver.find_element(*LocatorsMainPage.SUBMIT_BUTTON).text == 'Оформить заказ'

    def test_login_using_button_lk(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.ACCOUNT_LINK))
        driver.find_element(*LocatorsHeaderNav.ACCOUNT_LINK).click()
        driver.find_element(*LocatorsLoginPage.EMAIL_FIELD).send_keys(UserData.current_user.get('email'))
        driver.find_element(*LocatorsLoginPage.PASSWORD_FIELD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.SUBMIT_BUTTON))
        assert driver.find_element(*LocatorsMainPage.SUBMIT_BUTTON).text == 'Оформить заказ'

    def test_login_from_registrarion_form(self, driver):
        driver.get(REGISTRATION_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsReg.LOGIN_LINK))
        driver.find_element(*LocatorsReg.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.ACCOUNT_LINK))
        driver.find_element(*LocatorsLoginPage.EMAIL_FIELD).send_keys(UserData.current_user.get('email'))
        driver.find_element(*LocatorsLoginPage.PASSWORD_FIELD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.SUBMIT_BUTTON))
        assert driver.find_element(*LocatorsMainPage.SUBMIT_BUTTON).text == 'Оформить заказ'

    def test_login_from_recovery_form(self, driver):
        driver.get(RECOVERY_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsReg.LOGIN_LINK))
        driver.find_element(*LocatorsReg.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.ACCOUNT_LINK))
        driver.find_element(*LocatorsLoginPage.EMAIL_FIELD).send_keys(UserData.current_user.get('email'))
        driver.find_element(*LocatorsLoginPage.PASSWORD_FIELD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.SUBMIT_BUTTON))
        assert driver.find_element(*LocatorsMainPage.SUBMIT_BUTTON).text == 'Оформить заказ'
