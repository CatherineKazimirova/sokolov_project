import time
import allure
import utilities.common_urls
from pages.authorization import Authorization
from pages.catalog_page import Catalog
from pages.checkout_page import Checkout
from pages.city_change import CityChange
from pages.order_page import OrderPage
from pages.product_card_page import ProductCard
from pages.thank_you_page import ThankYouPage
import pytest


@pytest.mark.order(1)
@allure.description("Authorization")
def test_authorization(set_up):
    """Открытие сайта"""
    driver = set_up
    driver.get(utilities.common_urls.base_url)
    driver.maximize_window()
    """Авторизация по е-мейл"""
    Authorization(driver).auth_with_email()
    """Переход в профиль и проверка, что пользователь авторизован"""
    Authorization(driver).check_auth()


@pytest.mark.order(2)
@allure.description("Clear checkout")
def test_clear_checkout(set_up):
    """Очистка корзины перед выполнением сценария"""
    driver = set_up
    Checkout(driver).clear_basket()


@pytest.mark.order(3)
@allure.description("Change city")
def test_change_city(set_up):
    """Изменение города"""
    driver = set_up
    CityChange(driver).change_city()


@pytest.mark.order(4)
@allure.description("Create self pickup order to SOKOLOV shop, no prepayment")
def test_order_to_sokolov_shop_no_prepayment(set_up):
    """Переход в каталог украшений"""
    driver = set_up
    Catalog(driver).go_to_jewelry_catalog()
    """Фильтр по типу украшений"""
    Catalog(driver).select_jewelry_type()
    """Фильтр по цене"""
    Catalog(driver).apply_filter_by_price_from()
    Catalog(driver).apply_filter_by_price_to()
    """Фильтр по металлу, вставкам, цене вставок, количеству вставок и типу доставки"""
    Catalog(driver).select_metal()
    Catalog(driver).select_insert()
    Catalog(driver).select_insert_color()
    Catalog(driver).select_quantity_of_inserts()
    Catalog(driver).select_delivery_time()
    """Сохранение в переменные названия первого товара в выдаче, его цены и ссылки на КТ"""
    product_name_catalog = Catalog(driver).get_item_name()
    product_url_catalog = Catalog(driver).get_item_link_catalog()
    product_price_catalog = Catalog(driver).get_item_price_catalog()
    """Переход в КТ первого товара в выдаче"""
    Catalog(driver).click_first_product()

    """Сравнение ссылки на КТ, названия и цены с ссылкой, названием и ценой из каталога"""
    ProductCard(driver).check_product_card(product_url_catalog, product_name_catalog, product_price_catalog)
    """Добавление товара в корзину и сравнение названия и цены с названием и ценой из каталога"""
    ProductCard(driver).add_to_basket(product_name_catalog, product_price_catalog)

    """Проверка заголовка и url страницы чекаута"""
    Checkout(driver).check_page_checkout()
    """Сравнение названия и цены в чекауте с названием и ценой из каталога"""
    Checkout(driver).check_product_checkout(product_name_catalog, product_price_catalog)
    """Выбор магазина"""
    Checkout(driver).select_shop()
    """Выбор способа оплаты и подтверждение заказа"""
    Checkout(driver).select_payment_method_and_confirm_order()

    """Проверка заголовка и url страницы"""
    ThankYouPage(driver).check_thank_you_page()
    """Переход на страницу созданного заказа"""
    ThankYouPage(driver).go_to_order_page()


@pytest.mark.order(5)
@allure.description("Cancel order")
def test_cancel_order(set_up):
    """Проверка заголовка и url страницы заказа"""
    driver = set_up
    OrderPage(driver).check_order_page()
    """Проверка заголовка и url страницы заказа"""
    OrderPage(driver).cancel_order()
    """Проверка статуса заказа"""
    OrderPage(driver).check_status()
    time.sleep(1)
