from Locators.Locators import SignUpLocator, AllLocator
from Pages.PageObjectManager import PageObjectManager


class HomePage(PageObjectManager):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AllLocator()

    def home_page(self):
        # self.verify_text("Sign up", *self.locator.signUpTab)
        # self.click_element(*self.locator.signUpTab)
        self.assert_element_displayed(*self.locator.toolsQA)
        self.scroll_down()
        # self.assert_text_present("Sign Up", *self.locator.signUpTab)

