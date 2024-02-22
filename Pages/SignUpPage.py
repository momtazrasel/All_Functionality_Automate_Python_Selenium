from Locators.DemoBlazeLocators import SignUpLocator
from Pages.HomePage import HomePage


class SignUpPage(HomePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = SignUpLocator()

    def sign_up(self):
        # self.verify_text("Sign up", *self.locator.signUpTab)
        # self.click_element(*self.locator.signUpTab)
        self.is_element_displayed(*self.locator.toolsQA)
        # self.assert_text_present("Sign Up", *self.locator.signUpTab)

