from url_s import MAIN_PAGE_URL, LOGIN_PAGE_URL
from locators import LocatorsHeaderNav
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransferInPersonalAccount:
    def test_transfer_from_main_to_lk(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsHeaderNav.ACCOUNT_LINK))
        driver.find_element(*LocatorsHeaderNav.ACCOUNT_LINK).click()
        assert driver.current_url == LOGIN_PAGE_URL
