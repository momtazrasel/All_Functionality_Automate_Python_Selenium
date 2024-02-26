from selenium.webdriver.common.by import By


class AllLocator(object):
    signUpTab = (By.XPATH, "(//a[normalize-space()='Sign up'])[1]")
    toolsQA = (By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
    textBox = (By.XPATH, "(//div[@class = 'card mt-4 top-card'])[1]")


class TextElement(object):
    textBox = (By.XPATH, "(//div[@class = 'card mt-4 top-card'])[1]")
