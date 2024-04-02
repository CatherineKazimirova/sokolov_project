from selenium.webdriver.support.wait import WebDriverWait
import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)
