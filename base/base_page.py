import re
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import datetime
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    # Actions
    def get_element(self, locator):
        """Returns an element"""
        try:
            return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f' {locator} not found!')

    def assert_url(self, expected_url):
        """Compares exact URLs"""
        try:
            page_url = self.driver.current_url
            self.wait.until(EC.url_to_be(expected_url))
            assert expected_url == page_url
            print(f'URL {page_url} is correct')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'URL is not correct. Current URL: {page_url}')

    def assert_part_of_url(self, expected_url):
        """Checks URLs partially"""
        try:
            page_url = self.driver.current_url
            self.wait.until(EC.url_contains(expected_url))
            assert expected_url in page_url
            print(f'URL checked - contains expected part: {expected_url}')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'URL is not correct. Current URL: {page_url}')

    def assert_text(self, expected_text, current_text):
        """Compares text returned from element with expected text"""
        try:
            assert current_text == expected_text
            print(f'Name/title/text ({current_text}) compared, correct')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'Name/title/text {current_text} is not correct')

    def check_text(self, locator, expected_text):
        """Compares text in element with expected text"""
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), expected_text))
            print(f'Name/title/text ({expected_text}) compared, correct')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'Element{locator} not found!')

    def assert_price(self, expected_price, current_price):
        """Compares a number returned from element with expected number"""
        try:
            assert current_price == expected_price
            print(f'Prices ({current_price}) compared, correct')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'Price {current_price} is not correct')

    def get_converted_price(self, price):
        """Convert a price (str) like '40 000 ₽' to int"""
        return int(re.sub('[A-Za-z:₽ ]', '', price))

    def get_screenshot(self):
        """Saves screenshots with date to the nearest second"""
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
        screenshot_name = 'screenshot' + current_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Bread\\PycharmProjects\\sokolov_project\\screenshots\\' + screenshot_name)
