from base.base_page import Base


class ProductCard(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_name_card = 'h1[class*="ProductTitle_title"]'
    product_price_card = 'div[class*="ProductPrice_sklv-price__new"]'
    add_to_basket_from_card_button = 'button[class*="Product_btn-basket"]'
    product_name_basket_modal = 'div[class*=styles_name]'
    product_price_basket_modal = 'div[class*="styles_basket"] div[class*="ProductPrice_sklv-price__new"]'
    confirm_order_in_basket_button = 'div[class*="styles_btn-container"] button[class*="Button_primary"]'

    # Getters
    def get_product_name_card(self):
        return self.get_element(self.product_name_card).text.splitlines()[0]

    def get_product_price_card(self):
        product_price = self.get_element(self.product_price_card).text.splitlines()[0]
        return self.get_converted_price(product_price)

    def get_product_name_modal_basket(self):
        return self.get_element(self.product_name_basket_modal).text

    def get_product_price_modal_basket(self):
        product_price_basket = self.get_element(self.product_price_basket_modal).text
        return self.get_converted_price(product_price_basket)

    # Actions

    def click_add_to_basket_button(self):
        self.get_element(self.add_to_basket_from_card_button).click()
        print('Add to basket button clicked')

    def click_confirm_order_in_basket_button(self):
        self.get_element(self.confirm_order_in_basket_button).click()
        print('Product confirmed in basket, checkout')

    # Methods
    def check_product_card(self, product_url_from_catalog, product_name_from_catalog, product_price_from_catalog):
        self.assert_text(product_name_from_catalog, self.get_product_name_card())
        self.assert_price(product_price_from_catalog, self.get_product_price_card())
        self.assert_url(product_url_from_catalog)

    def add_to_basket(self, product_name_from_catalog, product_price_from_catalog):
        self.click_add_to_basket_button()
        self.assert_text(product_name_from_catalog, self.get_product_name_modal_basket())
        self.assert_price(product_price_from_catalog, self.get_product_price_modal_basket())
        self.click_confirm_order_in_basket_button()
