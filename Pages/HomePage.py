from Locators.Locators import TextElement
from Locators.Locators import AllLocator
from Pages.PageObjectManager import PageObjectManager


class HomePage(PageObjectManager):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = AllLocator()
        self.locator = TextElement()

    def home_page(self):
        # self.verify_text("Sign up", *self.locator.signUpTab)
        # self.click_element(*self.locator.signUpTab)
        self.assert_element_displayed(*self.locators.toolsQA)
        self.click_element(*self.locator.textBox)
        # self.scroll_down()
        # self.assert_text_present("Sign Up", *self.locator.signUpTab)

