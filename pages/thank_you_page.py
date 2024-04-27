import allure
from base.base_page import Base
import utilities.common_urls
from utilities.logger import Logger


class ThankYouPage(Base):

    # Locators
    order_created_header = 'div[class*="Order_order"] > h1'
    order_created_expected_header = 'Заказ оформлен'
    order_price = 'div[class*="Order_order-title"]'
    order_details_button = 'button[class*="OrderList_order-link"]'

    # Actions
    def click_order_page_button(self):
        self.get_element(self.order_details_button).click()
        print('Order details button clicked, go to order page')

    # Methods
    def check_thank_you_page(self):
        with allure.step("Check thank you page"):
            Logger.add_start_step("check_thank_you_page")
            """Сравнение url и заголовка страницы Спасибо за заказ с ожидаемыми"""
            self.check_page(self.order_created_header, self.order_created_expected_header, utilities.common_urls.thank_you_url)
            Logger.add_end_step(self.driver.current_url, "check_thank_you_page")

    def go_to_order_page(self):
        with allure.step("Go to order page"):
            Logger.add_start_step("go_to_order_page")
            """Переход на страницу созданного заказа, переключение на вкладку со страницей"""
            self.click_order_page_button()
            self.driver.switch_to.window(self.driver.window_handles[1])
            Logger.add_end_step(self.driver.current_url, "go_to_order_page")
