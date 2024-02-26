from TestPages.BasePage import BaseClass
from Pages.HomePage import HomePage


class HomePageTest(BaseClass):
    def test_home_page(self):
        test = HomePage(self.driver)
        test.home_page()
