from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import utilities.common_urls
from base.base_page import Base


class Checkout(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_header = '//*[@id="sales"]//div[1]/h3'
    expected_checkout_header = 'Корзина'
    product_name_checkout = 'a[class*="ProductItem_product-title"]'
    product_price_checkout = 'div[data-qa="actual_price"]'
    delivery_block = 'div[data-qa="pick_up_common_pane"]'
    shops_button = 'div[class*="Delivery_delivery-types"] > div:nth-child(1)'
    modal_header = 'div[class*="styles_modal-header__T_9GB"]'
    shop_address_in_delivery_block = 'div[class*="ShopInfo_shop-delivery"] > div'
    select_another_shop_button = 'button[data-qa="select_pickup_btn"]'
    address_field = 'div[class*="DeliveryHeader"] > div > input'
    desired_shop_name = 'ТРЦ Атмосфера'
    found_shop_name = 'div[class*="ReactVirtualized__Grid"] > div:nth-child(1) > div> div > div > span[data-qa="trc_name"]'
    found_shop_in_list_select_button = 'button[data-qa="pick_up_button"]'
    confirm_order_button = 'button[data-qa="create_order_btn"]'
    no_prepayment_button = 'div[data-qa="btn-type-cash"]'

    # Getters
    def get_checkout_header(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.checkout_header))).text

    def get_product_name_checkout(self):
        return self.get_element(self.product_name_checkout).text

    def get_product_price_checkout(self):
        product_price_checkout = self.get_element(self.product_price_checkout).text
        return self.get_converted_price(product_price_checkout)

    def get_shop_name_in_delivery_block(self):
        return self.get_element(self.shop_address_in_delivery_block).text.splitlines()[2].split(',')[0]

    def get_shop_block_len(self):
        block_len = len(self.driver.find_elements(By.CSS_SELECTOR, self.delivery_block))
        return block_len

    # Actions

    def click_shops_button(self):
        button = self.get_element(self.shops_button)
        ActionChains(self.driver).move_to_element(button).click(button).perform()
        print(f'Shops button clicked')

    def enter_desired_shop_name(self):
        self.get_element(self.address_field).send_keys(self.desired_shop_name)
        print('Shop name entered')
        self.check_text(self.found_shop_name, self.desired_shop_name)
        print('Check that shop has been found')

    def click_select_shop_in_list_button(self):
        button = self.get_element(self.found_shop_in_list_select_button)
        ActionChains(self.driver).move_to_element(button).perform()
        button.click()
        print('Select shop in list button clicked')

    def click_select_another_shop_button(self):
        self.get_element(self.select_another_shop_button).click()
        print('Shops button clicked')

    def click_no_prepayment_button(self):
        self.get_element(self.no_prepayment_button).click()
        print('No prepayment option selected')

    def click_confirm_order_button(self):
        self.get_element(self.confirm_order_button).click()
        print('Order confirmed')

    # Methods
    def check_page(self):
        self.assert_url(utilities.common_urls.checkout_url)
        self.assert_text(self.expected_checkout_header, self.get_checkout_header())

    def check_product_checkout(self, product_name_from_catalog, product_price_from_catalog):
        self.assert_text(product_name_from_catalog, self.get_product_name_checkout())
        self.assert_price(product_price_from_catalog, self.get_product_price_checkout())

    def select_shop(self):
        if self.get_shop_block_len() > 0 and self.get_shop_name_in_delivery_block() == self.desired_shop_name:
            print('Shop has been selected before')
        elif self.get_shop_block_len() > 0 and self.get_shop_name_in_delivery_block() != self.desired_shop_name:
            print(self.desired_shop_name, self.get_shop_name_in_delivery_block())
            self.click_select_another_shop_button()
            self.enter_desired_shop_name()
            self.click_select_shop_in_list_button()
        elif self.get_shop_block_len() == 0:
            self.click_shops_button()
            self.enter_desired_shop_name()
            self.click_select_shop_in_list_button()

    def select_payment_method_and_confirm_order(self):
        self.click_no_prepayment_button()
        # self.click_confirm_order_button()
