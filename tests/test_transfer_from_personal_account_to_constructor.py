from url_s import MAIN_PAGE_URL, LOGIN_PAGE_URL
from locators import LocatorsMainPage, LocatorsHeaderNav
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransferFromLkToConstructor:
    def test_transfer_from_lk_by_constructor_link(self, driver):
        driver.get(LOGIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.CONSTRUCTOR_LINK))
        driver.find_element(*LocatorsHeaderNav.CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.LOGIN_BUTTON_MAIN_PAGE))
        assert driver.current_url == MAIN_PAGE_URL

    def test_transfer_from_lk_by_logo(self, driver):
        driver.get(LOGIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.LOGO_LINK))
        driver.find_element(*LocatorsHeaderNav.LOGO_LINK).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.LOGIN_BUTTON_MAIN_PAGE))
        assert driver.current_url == MAIN_PAGE_URL
