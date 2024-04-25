from base.base_page import Base
import utilities.common_urls


class ThankYouPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        """Сравнение url и заголовка страницы Спасибо за заказ с ожидаемыми"""
        self.check_page(self.order_created_header, self.order_created_expected_header, utilities.common_urls.thank_you_url)

    def go_to_order_page(self):
        """Переход на страницу созданного заказа, переключение на вкладку со страницей"""
        self.click_order_page_button()
        self.driver.switch_to.window(self.driver.window_handles[1])
