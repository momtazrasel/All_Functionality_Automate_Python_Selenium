from Locators.Locators import AllLocator, TextElement
from Pages.PageObjectManager import PageObjectManager


class HomePage(PageObjectManager):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AllLocator()
        self.locator = TextElement()

    def home_page(self):
        # self.verify_text("Sign up", *self.locator.signUpTab)
        # self.click_element(*self.locator.signUpTab)
        self.assert_element_displayed(*self.locator.toolsQA)
        self.click_element(*self.locator.textBox)
        # self.scroll_down()
        # self.assert_text_present("Sign Up", *self.locator.signUpTab)

