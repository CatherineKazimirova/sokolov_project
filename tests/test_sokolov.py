import time
import utilities.common_urls
from pages.authorization import Authorization
from pages.catalog_page import Catalog
from pages.checkout_page import Checkout
from pages.city_change import CityChange
from pages.order_page import OrderPage
from pages.product_card_page import ProductCard
from pages.thank_you_page import ThankYouPage


def test_authorization(set_up):
    driver = set_up
    driver.get(utilities.common_urls.base_url)
    driver.maximize_window()
    Authorization(driver).auth_with_email()
    Authorization(driver).check_auth()


def test_clear_checkout(set_up):
    driver = set_up
    Checkout(driver).clear_basket()


def test_change_city(set_up):
    driver = set_up
    CityChange(driver).change_city()


def test_order_to_sokolov_shop_no_prepayment(set_up):
    driver = set_up
    Catalog(driver).go_to_jewelry_catalog()
    Catalog(driver).select_jewelry_type()
    Catalog(driver).apply_filter_by_price_from()
    Catalog(driver).apply_filter_by_price_to()
    Catalog(driver).select_metal()
    Catalog(driver).select_insert()
    Catalog(driver).select_insert_color()
    Catalog(driver).select_quantity_of_inserts()
    Catalog(driver).select_delivery_time()
    Catalog(driver).click_first_product()
    product_name_catalog = Catalog(driver).get_item_name()
    product_url_catalog = Catalog(driver).get_item_link_catalog()
    product_price_catalog = Catalog(driver).get_item_price_catalog()
    Catalog(driver).click_first_product_in_list()

    ProductCard(driver).check_product_card(product_url_catalog, product_name_catalog, product_price_catalog)
    ProductCard(driver).add_to_basket(product_name_catalog, product_price_catalog)

    Checkout(driver).check_page_basket()
    Checkout(driver).check_product_checkout(product_name_catalog, product_price_catalog)
    Checkout(driver).select_shop()
    Checkout(driver).select_payment_method_and_confirm_order()

    ThankYouPage(driver).check_thank_you_page()
    ThankYouPage(driver).go_to_order_page()


def test_cancel_order(set_up):
    driver = set_up
    OrderPage(driver).check_order_page()
    OrderPage(driver).cancel_order()
    OrderPage(driver).check_status()
    time.sleep(1)
