from selenium.webdriver.common.by import By


class AllLocator:
    signUpTab = (By.XPATH, "(//a[normalize-space()='Sign up'])[1]")
    toolsQA = (By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
    textBox = (By.XPATH, "(//li[@id='item-0'])[1]")


class TextElement:
    textBox = (By.XPATH, "(//li[@id='item-0'])[1]")
