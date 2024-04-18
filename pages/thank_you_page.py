from base.base_page import Base


class ThankYouPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_created_header = 'div[class*="Order_order"] > h1'
    order_created_expected_header = 'Заказ оформлен'
    order_price = 'div[class*="Order_order-title"]'
    order_details_button = 'button[class*="OrderList_order-link"]'

    # Getters


    # Actions



    # Methods

