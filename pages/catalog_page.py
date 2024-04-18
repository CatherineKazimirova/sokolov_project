import time

import utilities.common_urls
from base.base_page import Base
from selenium.webdriver.common.keys import Keys


class Catalog(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    header_catalog_button = 'button[data-qa="header_catalog_nav_open_btn"]'
    catalog_all_categories_banner = 'a[data-qa="all_of_this_category"]'
    jewelry_catalog_expected_header = 'Ювелирные украшения1'
    earrings_button = 'div[data-link-href*="earrings"]'
    jewelry_type_catalog_expected_header = 'Серьги'
    price_from_field = 'input[data-qa="min_price"]'
    price_to_field = 'input[data-qa="max_price"]'
    price_from = '1000'
    price_to = '6000'
    silver_checkbox = '#silver'
    show_all_inserts_button = 'div[data-qa="filter_section_insert"] button[class*="ButtonDeprecated_sklv-button"]'
    fianit_checkbox = '#fianit'
    inserts_colors_button = 'div[data-qa="filter_section_color"]'
    show_all_inserts_colors = 'div[data-qa="filter_section_color"] button[class*="ButtonDeprecated_sklv-button"]'
    pink_color_checkbox = '#pink'
    quantity_of_inserts_button = 'div[data-qa="filter_section_count_insert"]'
    two_inserts_checkbox = '#two-stones'
    pickup_delivery_type_button = 'input[value="pickup"]'
    first_product_in_list = 'div[data-qa="product-list"] > a:nth-child(1)'
    first_product_in_list_name = 'div[data-qa="product-list"] > a:nth-child(1) div[data-qa="product_title"]'
    first_product_in_list_url = 'div[data-qa="product-list"] > a:nth-child(1)'
    first_product_in_list_price = 'div[data-qa="product-list"] > a:nth-child(1) span[data-qa="actual_pirce"]'
    catalog_header = 'h1[itemprop="name"]'

    # Getters
    def get_item_name(self):
        return self.get_element(self.first_product_in_list_name).text

    def get_item_link_catalog(self):
        return self.get_element(self.first_product_in_list_url).get_attribute('href')

    def get_item_price_catalog(self):
        current_price = self.get_element(self.first_product_in_list_price).text.splitlines()[0]
        return self.get_converted_price(current_price)

    def get_current_catalog_header(self):
        return self.get_element(self.catalog_header).text

    # Actions

    def click_header_catalog_button(self):
        self.get_element(self.header_catalog_button).click()
        print('Catalog button clicked')

    def click_all_categories_banner(self):
        self.get_element(self.catalog_all_categories_banner).click()
        print('All categories banner clicked')

    def click_on_jewelry_type(self):
        self.get_element(self.earrings_button).click()
        print('Jewelry type selected')

    def clear_price_from_field(self):
        self.get_element(self.price_from_field).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def enter_price_from(self):
        self.get_element(self.price_from_field).send_keys(self.price_from, Keys.RETURN)

    def clear_price_to_field(self):
        self.get_element(self.price_to_field).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

    def enter_price_to(self):
        self.get_element(self.price_to_field).send_keys(self.price_to, Keys.RETURN)

    def click_metal_checkbox(self):
        self.get_element(self.silver_checkbox).click()
        print('Metal selected')

    def click_show_all_inserts_button(self):
        self.get_element(self.show_all_inserts_button).click()
        print('Show all inserts button clicked')

    def click_insert_checkbox(self):
        self.get_element(self.fianit_checkbox).click()
        print('Insert selected')

    def click_inserts_color_button(self):
        self.get_element(self.inserts_colors_button).click()
        print('Inserts color button clicked')

    def click_show_all_inserts_color_button(self):
        self.get_element(self.show_all_inserts_colors).click()
        print('Inserts color button clicked')

    def click_insert_color_checkbox(self):
        self.get_element(self.pink_color_checkbox).click()
        print('Insert color selected')

    def click_quantity_of_inserts_button(self):
        self.get_element(self.quantity_of_inserts_button).click()
        print('Inserts color button clicked')

    def click_inserts_quantity_checkbox(self):
        self.get_element(self.two_inserts_checkbox).click()
        print('Inserts quantity selected')

    def click_pickup_in_shop_button(self):
        self.get_element(self.pickup_delivery_type_button).click()
        print('Pickup delivery type selected')

    def click_first_product_in_list(self):
        self.get_element(self.first_product_in_list).click()
        print('First product in list clicked')

    # Methods
    def go_to_jewelry_catalog(self):
        self.click_header_catalog_button()
        self.click_all_categories_banner()
        self.check_text(self.catalog_header, self.jewelry_catalog_expected_header)
        self.assert_url(utilities.common_urls.jewelry_catalog_url)

    def select_jewelry_type(self):
        self.click_on_jewelry_type()
        self.check_text(self.catalog_header, self.jewelry_type_catalog_expected_header)
        self.assert_url(utilities.common_urls.jewelry_type_catalog_url)

    def apply_filter_by_price(self):
        self.clear_price_from_field()
        self.enter_price_from()
        self.clear_price_to_field()
        self.enter_price_to()

    def select_metal(self):
        self.click_metal_checkbox()

    def select_insert(self):
        self.click_show_all_inserts_button()
        self.click_insert_checkbox()

    def select_insert_color(self):
        self.click_inserts_color_button()
        self.click_show_all_inserts_color_button()
        self.click_insert_color_checkbox()

    def select_quantity_of_inserts(self):
        self.click_quantity_of_inserts_button()
        self.click_inserts_quantity_checkbox()

    def select_delivery_time(self):
        self.click_pickup_in_shop_button()

    def click_first_product(self):
        self.driver.refresh()
        self.click_first_product_in_list()
