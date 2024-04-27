import allure
from base.base_page import Base
from utilities.logger import Logger


class ProductCard(Base):

    # Locators
    product_name_card = 'h1[class*="ProductTitle_title"]'
    product_price_card = 'div[class*="ProductPrice_sklv-price__new"]'
    add_to_basket_from_card_button = 'button[class*="Product_btn-basket"]'
    modal_basket_header = 'div[class*="styles_header"] > div'
    modal_basket_expected_header = 'Товар добавлен в корзину'
    product_name_basket_modal = 'div[class*=styles_name]'
    product_price_basket_modal = 'div[class*="styles_basket"] div[class*="ProductPrice_sklv-price__new"]'
    confirm_order_in_basket_button = 'div[class*="styles_btn-container"] button[class*="Button_primary"]'

    # Getters
    def get_product_name_card(self):
        """Получение названия товара из карточки товара"""
        return self.get_element(self.product_name_card).text.splitlines()[0]

    def get_product_price_card(self):
        """Получение цены на товар из карточки товара и преобразование полученной строки в целое число"""
        product_price = self.get_element(self.product_price_card).text.splitlines()[0]
        return self.get_converted_price(product_price)

    def get_product_name_modal_basket(self):
        return self.get_element(self.product_name_basket_modal).text

    def get_product_price_modal_basket(self):
        """Получение цены на товар из модального окна корзины и преобразование полученной строки в целое число"""
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
        with allure.step("Check product card"):
            Logger.add_start_step("check_product_card")
            """Сравнение url карточки товара, названия и цены со значениями, полученными из каталога"""
            self.check_name_and_price(product_name_from_catalog, self.get_product_name_card(), product_price_from_catalog, self.get_product_price_card())
            self.assert_url(product_url_from_catalog)
            Logger.add_end_step(self.driver.current_url, "check_product_card")

    def add_to_basket(self, product_name_from_catalog, product_price_from_catalog):
        with allure.step("Add to basket"):
            Logger.add_start_step("add_to_basket")
            """Нажатие на кнопку добавления товара в корзину, проверка открытия модального окна (проверка заголовка)
            сравнение цены товара и названия товара, полученных из каталога"""
            self.click_add_to_basket_button()
            self.check_text(self.modal_basket_header, self.modal_basket_expected_header)
            self.check_name_and_price(product_name_from_catalog, self.get_product_name_modal_basket(), product_price_from_catalog, self.get_product_price_modal_basket())
            self.click_confirm_order_in_basket_button()
            Logger.add_end_step(self.driver.current_url, "add_to_basket")
