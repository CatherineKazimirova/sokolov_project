from base.base_page import Base


class Order(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_profile_partial_title = 'h1[data-qa="main_order_number"]'
    order_profile_expected_partial_title = 'Заказ №'
    order_profile_product_name = 'div[data-qa="product_title"]'
    order_profile_product_price = 'span[data-qa="actual_price"]'
    order_profile_cancel_order_button = 'button[data-qa="cancel_order_btn"]'
    cancel_reason_button = 'ul[class*="CancelOrder_reasons"] > li:nth-child(1) input[type="radio"]'
    confirm_order_cancel_button = 'div[class*="CancelOrder_modal"] > button'
    double_confirm_order_cancel_button = 'div[class*="CancelOrder_confirm-buttons"] > button:nth-child(1)'
    expected_status = 'Отменён'
    profile_order_status = 'div[class*="OrdersStatus"]'

    # Getters

    # Actions

    # Methods

