from telnetlib import EC

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class PageObjectManager:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_text(self, expected_text, *locator):
        actual_txt = self.driver.find_element(*locator).text
        assert actual_txt == expected_text, \
            f"Expected '{expected_text}' but found '{actual_txt}' for signup button text."

    def send_keys(self, *locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def assert_element_displayed(self, *locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.find_element(*locator).is_displayed()
            )
            # print(f"Element with locator '{locator}' is displayed.")
        except TimeoutException:
            self.fail(f"Element with locator '{locator}' is not displayed.")

    def scroll_down(self, num_times=1):
        actions = ActionChains(self)
        for _ in range(num_times):
            actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()


