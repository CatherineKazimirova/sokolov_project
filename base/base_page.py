import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import datetime
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    # Actions
    def get_element(self, locator):
        """Получение элемента по CSS селектору"""
        try:
            return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f' {locator} not found!')

    def action_chains_click(self, locator):
        """Переход к элементу с помощью ActionChains и нажатие на элемент"""
        try:
            button = self.get_element(locator)
            ActionChains(self.driver).move_to_element(button).perform()
            print(f'Moved to element {locator}')
            ActionChains(self.driver).click(button).perform()
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f' {locator} not found!')

    def check_visibility(self, locator):
        """Проверка исчезновения элемента"""
        try:
            self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, locator)))
            print(f'Element {locator} disappeared')
        except TimeoutException:
            self.get_screenshot()
            raise AssertionError(f'Problem with visibility of locator {locator}')

    def assert_url(self, expected_url):
        """Проверка строгого соответствия полученного и ожидаемого url"""
        try:
            page_url = self.driver.current_url
            self.wait.until(EC.url_to_be(expected_url))
            assert expected_url == page_url
            print(f'URL checked {page_url}, correct')
        except AssertionError:
            self.get_screenshot()
            print(f'URL is not correct. Current URL: {page_url}')

    def assert_part_of_url(self, expected_url):
        """Поиск в полученном url части url и сравнение по частичному совпадению"""
        try:
            page_url = self.driver.current_url
            self.wait.until(EC.url_contains(expected_url))
            assert expected_url in page_url
            print(f'URL checked - contains expected part: {expected_url}')
        except AssertionError:
            self.get_screenshot()
            print(f'URL is not correct. Current URL: {page_url}')

    def assert_text(self, expected_text, current_text):
        """Проверка строгого соответствия полученного и ожидаемого текстов"""
        try:
            assert current_text == expected_text
            print(f'Text ({current_text}) checked, correct')
        except AssertionError:
            self.get_screenshot()
            print(f'Text ({current_text}) in element is not correct')

    def assert_part_of_text(self, expected_text, current_text):
        """Поиск в полученном тексте части текста и сравнение по частичному совпадению"""
        try:
            assert expected_text in current_text
            print(f'Text ({expected_text}) found in the element text, correct')
        except AssertionError:
            self.get_screenshot()
            print(f'Text ({expected_text}) not found in the element. Current text: {current_text}')

    def check_text(self, locator, expected_text):
        """Сравнение ожидаемого текста и текста, содержащегося в элементе"""
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), expected_text))
            print(f'Text ({expected_text}) in the element checked, correct')
        except TimeoutException:
            self.get_screenshot()
            print(f'Element {locator} not found!')
        except AssertionError:
            self.get_screenshot()
            print(f'Text in the element {locator} is not correct')

    def assert_price(self, expected_price, current_price):
        """Сравнение полученной и ожидаемой цен на товар"""
        try:
            assert current_price == expected_price
            print(f'Price ({current_price}) checked, correct')
        except AssertionError:
            self.get_screenshot()
            print(f'Price {current_price} is not correct')

    def check_name_and_price(self, expected_text, current_text, expected_price, current_price):
        """Фукнция для проверки и названия товара, и цены"""
        self.assert_text(expected_text, current_text)
        self.assert_price(expected_price, current_price)

    def check_page(self, locator, expected_text, expected_url):
        """Проверка текста (заголовка) и url, если эти элементы статичны"""
        self.check_text(locator, expected_text)
        self.assert_url(expected_url)

    def get_converted_price(self, price):
        """Преобразование цены типа '40 000 ₽' в целочисленное значение"""
        return int(re.sub('[A-Za-z:₽ ]', '', price))

    def get_len(self, locator):
        """Поиск элементов с одинаковым CSS селектором и подсчет количества"""
        return len(self.driver.find_elements(By.CSS_SELECTOR, locator))

    def get_screenshot(self):
        """Сохранение скриншота с указанием даты до секунд"""
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
        screenshot_name = 'screenshot' + current_date + '.png'
        self.driver.save_screenshot('screenshots/' + screenshot_name)
