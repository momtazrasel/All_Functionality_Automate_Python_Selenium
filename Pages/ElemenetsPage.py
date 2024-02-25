from Locators.Locators import AllLocator
from Pages.PageObjectManager import PageObjectManager


class AllElements(PageObjectManager):
    def __init__(self, driver):
        self.driver = driver
        self.locator = AllLocator()

    def text_box_element(self):
        self.click_element(*self.locator.textBox)

