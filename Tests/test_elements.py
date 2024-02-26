from TestPages.BasePage import BaseClass
from Pages.ElemenetsPage import AllElements


class ElementsTest(BaseClass):
    def elementTest(self):
        test = AllElements(self.driver)
        test.text_box_element()