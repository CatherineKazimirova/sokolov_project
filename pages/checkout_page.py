import allure
import utilities.common_urls
from base.base_page import Base
from utilities.logger import Logger


class Checkout(Base):

    # Locators
    checkout_header = 'div[class*="Rout_block"] > h3'
    expected_checkout_header = 'Корзина'
    product_name_checkout = 'a[class*="ProductItem_product-title"]'
    product_price_checkout = 'div[data-qa="actual_price"]'
    delivery_block = 'div[data-qa="pick_up_common_pane"]'
    shops_button = 'div[class*="Delivery_delivery-types"] > div:nth-child(1) > svg > path'
    modal_shops_list = 'div[class*="styles_modal_fullscreen"]'
    shop_address_in_delivery_block = 'div[class*="ShopInfo_shop-delivery"] > div'
    select_another_shop_button = 'button[data-qa="select_pickup_btn"]'
    address_field = 'div[class*="DeliveryHeader"] > div > input'
    desired_shop_name = 'ТРЦ Атмосфера'
    found_shop_name = 'div[class*="ReactVirtualized__Grid"] > div:nth-child(1) > div> div > div > span[data-qa="trc_name"]'
    found_shop_in_list_select_button = 'button[data-qa="pick_up_button"]'
    confirm_order_button = 'button[data-qa="create_order_btn"]'
    no_prepayment_button = 'div[data-qa="btn-type-cash"]'
    checkout_button = 'button[data-qa="header_to_basket_btn"]'
    product_block = 'div[class*="ProductItem_product-info__title"]'
    delete_product_button = 'div[class*="ProductList_checkout-products"] > div:nth-child(1) button[data-qa="delete_item_from_cart"]'
    delete_product_loader = 'div[class*="ProductList_checkout-products"] > div:nth-child(1) div[class*="loader--size-small"]'
    header_link = 'div[class*="logo"]'
    checkout_loader = 'div[class*="loader--size-medium"]'

    # Getters

    def get_product_price_checkout(self):
        """Получение цены на товар из чекаута и преобразование полученной строки в целое число"""
        product_price_checkout = self.get_element(self.product_price_checkout).text
        return self.get_converted_price(product_price_checkout)

    def get_product_name_checkout(self):
        """Получение названия товара из чекаута"""
        return self.get_element(self.product_name_checkout).text

    def get_shop_name_in_delivery_block(self):
        """Получение названия ТЦ, где находится магазин, из блока доставки"""
        return self.get_element(self.shop_address_in_delivery_block).text

    def get_shop_block_len(self):
        """Проверка, был ли выбран способ доставки ранее (до выполнения текущего заказа).
        len 1 - блок доставки есть, 0 - блока нет"""
        return self.get_len(self.delivery_block)

    def get_products_block_len(self):
        """Проверка наличия товаров в чекауте до выполнения текущего заказа. Len 0 - корзина пуста,
        > 0 товары есть в корзине"""
        return self.get_len(self.product_block)

    # Actions

    def click_shops_button(self):
        self.action_chains_click(self.shops_button)
        print('Shops button clicked')

    def enter_desired_shop_name(self):
        self.get_element(self.address_field).send_keys(self.desired_shop_name)
        print('Shop name entered')
        self.check_text(self.found_shop_name, self.desired_shop_name)
        print('Desired shop name found')

    def click_select_shop_in_list_button(self):
        self.action_chains_click(self.found_shop_in_list_select_button)
        print('Select shop in list button clicked')

    def click_select_another_shop_button(self):
        self.get_element(self.select_another_shop_button).click()
        print('Shops button clicked')

    def click_no_prepayment_button(self):
        self.action_chains_click(self.no_prepayment_button)
        print('No prepayment option selected')

    def click_confirm_order_button(self):
        self.action_chains_click(self.confirm_order_button)
        print('Confirm order button clicked')

    def click_delete_product_button(self):
        self.get_element(self.delete_product_button).click()
        print('Product deleted')

    def click_header_link(self):
        self.get_element(self.header_link).click()
        print('Return to main page')

    # Methods
    def clear_basket(self):
        with allure.step("Clear basket"):
            Logger.add_start_step("clear_basket")
            """Проверка наличия в чекауте товаров и удаление, если они есть. Проверка загрузки хедера, затем
            ожидание прогрузки страницы чекаут и проверка длины блока товаров. Если длина == 0 - переход
            на главную. Если товаров > 0 - удаление всех товаров по очереди и переход на главную страницу."""
            self.get_element(self.checkout_button).click()
            self.get_element(self.header_link)
            self.check_visibility(self.checkout_loader)
            products = self.get_products_block_len()
            if products > 0:
                for i in range(products):
                    self.click_delete_product_button()
                    self.check_visibility(self.delete_product_loader)
                print('Checkout cleared')
                self.click_header_link()
            elif products == 0:
                print('Checkout has already been cleared')
                self.click_header_link()
            Logger.add_end_step(self.driver.current_url, "clear_basket")

    def check_page_checkout(self):
        with allure.step("Check page checkout"):
            Logger.add_start_step("check_page_basket")
            """Переход в чекаут, сравнение текущих url и заголовка с ожидаемыми"""
            self.check_page(self.checkout_header, self.expected_checkout_header, utilities.common_urls.checkout_url)
            Logger.add_end_step(self.driver.current_url, "check_page_basket")

    def check_product_checkout(self, product_name_from_catalog, product_price_from_catalog):
        with allure.step("Check product checkout"):
            Logger.add_start_step("check_product_checkout")
            """Сравнение названия и цены со значениями, полученными из каталога"""
            self.check_name_and_price(product_name_from_catalog, self.get_product_name_checkout(),
                                      product_price_from_catalog, self.get_product_price_checkout())
            Logger.add_end_step(self.driver.current_url, "check_product_checkout")

    def select_shop_and_check(self):
        """Выбор магазина в модальном окне Самовывоз: ввод названия ТЦ, в котором находится магазин,
        нажатие на кнопку Заберу отсюда в блоке найденного магазина, проверка, пока окно Самовывоз не закроется,
        сравнение названия ТЦ с адресом в блоке доставки по частичному совпадению"""
        self.enter_desired_shop_name()
        self.click_select_shop_in_list_button()
        self.check_visibility(self.modal_shops_list)
        self.driver.refresh()
        self.assert_part_of_text(self.desired_shop_name, self.get_shop_name_in_delivery_block())
        print(f'Shop {self.desired_shop_name} selected')

    def select_shop(self):
        with allure.step("Select shop"):
            Logger.add_start_step("select_shop")
            """Выбор магазина в зависимости от того, был ли он выбран при предыдущих заказах: если блок доставки
            отсутствует - ранее пользователь в этом городе делал заказы в магазин; если блок доставки присутствует
            и название ТЦ не равно желаемому (desired_shop_name), вызывается функция выбора магазина (в желаемом ТЦ);
            если название ТЦ совпадает с желаемым, то вызывается фукнция подтверждения способа оплаты и заказа"""
            if self.get_shop_block_len() > 0 and self.desired_shop_name in self.get_shop_name_in_delivery_block():
                print('Shop has already been selected before')
            elif self.get_shop_block_len() > 0 and self.desired_shop_name not in self.get_shop_name_in_delivery_block():
                self.click_select_another_shop_button()
                self.select_shop_and_check()
            elif self.get_shop_block_len() == 0:
                self.click_shops_button()
                self.select_shop_and_check()
            Logger.add_end_step(self.driver.current_url, "select_shop")

    def select_payment_method_and_confirm_order(self):
        with allure.step("Authorization check"):
            Logger.add_start_step("select_payment_method_and_confirm_order")
            """Нажатие на кнопку Оплата при получении и подтверждение оформления заказа"""
            self.click_no_prepayment_button()
            self.driver.refresh()
            self.click_confirm_order_button()
            Logger.add_end_step(self.driver.current_url, "select_payment_method_and_confirm_order")
