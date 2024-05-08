from url_s import MAIN_PAGE_URL
from locators import LocatorsMainPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_tab_on_bread(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.CONSTRUCTOR_TITLE))
        assert 'type_current' in driver.find_element(*LocatorsMainPage.BREAD_TAB).get_attribute('class')

    def test_tab_on_sauces(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.CONSTRUCTOR_TITLE))
        driver.find_element(*LocatorsMainPage.SAUCES_TAB).click()
        assert 'type_current' in driver.find_element(*LocatorsMainPage.SAUCES_TAB).get_attribute('class')

    def test_tab_on_topping(self, driver):
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LocatorsMainPage.CONSTRUCTOR_TITLE))
        driver.find_element(*LocatorsMainPage.TOPPING_TAB).click()
        assert 'type_current' in driver.find_element(*LocatorsMainPage.TOPPING_TAB).get_attribute('class')
