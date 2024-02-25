from Pages.BasePage import BaseClass
from Pages.ElemenetsPage import AllElements


class AllElementsTest(BaseClass):
    def text_box_element(self):
        test = AllElements(self.driver)
        test.text_box_element()

