from base.base_page import Base
import utilities.common_urls


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_page_header = 'h1[data-qa="main_order_number"]'
    order_page_expected_partial_header = 'Заказ №'
    cancel_order_button = 'button[data-qa="cancel_order_btn"]'
    cancel_reason_radiobutton = 'ul[class*="CancelOrder_reasons"] input[value="131"]'
    cancel_reason_field = 'textarea[name="message"]'
    cancel_reason_text = 'тестовый заказ'
    confirm_cancel_order_button = 'div[class*="CancelOrder_modal"] > button'
    double_confirm_order_cancel_button = 'div[class*="CancelOrder_confirm-buttons"] > button:nth-child(1)'
    cancel_order_modal = 'div[class*="styles_modal_small"]'
    expected_status = 'Отменён'
    profile_order_status = 'div[class*="OrdersStatus"]'

    # Getters

    def get_order_page_header(self):
        """Получение заголовка страницы заказа"""
        return self.get_element(self.order_page_header).text

    # Actions
    def click_cancel_order_button(self):
        self.get_element(self.cancel_order_button).click()
        print('Cancel order button clicked')

    def select_cancel_reason_radiobutton(self):
        self.action_chains_click(self.cancel_reason_radiobutton)
        print('Cancel reason selected')

    def enter_cancel_reason(self):
        self.get_element(self.cancel_reason_field).send_keys(self.cancel_reason_text)
        print('Cancel reason entered')

    def click_confirm_cancel_order_button(self):
        self.get_element(self.confirm_cancel_order_button).click()
        print('Another cancel order button clicked')

    def click_double_confirm_order_cancel_button(self):
        self.get_element(self.double_confirm_order_cancel_button).click()
        print('Confirm cancel order again, the third cancel button clicked')
        self.check_visibility(self.cancel_order_modal)

    # Methods
    def check_order_page(self):
        """"Ожидание загрузки заголовка, поиск части ожидаемого url  и заголовка в текущих url и заголовке
        и проверка, что части найдены"""
        self.get_element(self.order_page_header)
        self.assert_part_of_text(self.order_page_expected_partial_header, self.get_order_page_header())
        self.assert_part_of_url(utilities.common_urls.orders_url)

    def cancel_order(self):
        """Нажатие на кнопку отмены заказа, ввод и подтверждение причины отмены, отмена заказа"""
        self.click_cancel_order_button()
        self.select_cancel_reason_radiobutton()
        self.enter_cancel_reason()
        self.click_confirm_cancel_order_button()
        self.click_double_confirm_order_cancel_button()

    def check_status(self):
        """Проверка статуса заказа"""
        self.check_text(self.profile_order_status, self.expected_status)
        print(f'Order status checked: {self.get_element(self.profile_order_status).text}')
