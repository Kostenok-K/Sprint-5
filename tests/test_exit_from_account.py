from url_s import LOGIN_PAGE_URL
from locators import LocatorsMainPage, LocatorsLoginPage, LocatorsHeaderNav, LocatorsAccountProfile
from data import UserData
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExitFromLk:
    def test_exit_from_lk(self, driver):
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(*LocatorsLoginPage.EMAIL_FIELD).send_keys(UserData.current_user.get('email'))
        driver.find_element(*LocatorsLoginPage.PASSWORD_FIELD).send_keys(UserData.current_user.get('password'))
        driver.find_element(*LocatorsLoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.SUBMIT_BUTTON))
        driver.find_element(*LocatorsHeaderNav.ACCOUNT_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsAccountProfile.LOGOUT_BUTTON))
        driver.find_element(*LocatorsAccountProfile.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsLoginPage.LOGIN_BUTTON))
        assert driver.current_url == LOGIN_PAGE_URL
