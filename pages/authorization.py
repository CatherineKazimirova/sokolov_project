import time
from base.base_page import Base
import utilities.userdata
import utilities.common_urls
from utilities.logger import Logger
import allure


class Authorization(Base):

    # Locators

    header_login_or_profile_button = 'button[data-qa="header_user_login_btn"]'
    phone_field = 'input[type="tel"]'
    send_or_confirm_code_button = 'button[data-qa="send_code"]'
    code_field = 'input[data-qa="auth_code"]'
    enter_with_email_button = 'button[class*="AuthControl_auth"]'
    email_field = 'div[class*="LoginMail_email-input"] > div[class*="Input_input-group"] > input:nth-child(1)'
    password_field = 'input[type="password"]'
    login_with_email_button = 'div[class*="styles_modal-body"] > div > div > button[class*="Button_button"]'
    modal_auth = 'div[class*="styles_modal_small"]'
    send_code_error = 'span[class*="Input_input-error"]'
    send_code_loader = 'div[class*="Loader_loader"]'

    # Getter

    def get_error_block_len(self):
        """Проверка наличия ошибки 'Отправка СМС доступна через 60 секунд после последней отправки' в модальном
        окне Вход. Len 0 - ошибки нет, len > 0 - ошибка есть"""
        return self.get_len(self.send_code_error)

    # Actions

    def click_header_login_button(self):
        self.get_element(self.header_login_or_profile_button).click()
        print('Login button clicked')

    def click_email_button(self):
        self.get_element(self.enter_with_email_button).click()
        print('Enter with email button clicked')

    def enter_email(self):
        self.get_element(self.email_field).send_keys(utilities.userdata.email)
        print('User email entered')

    def enter_password(self):
        self.get_element(self.password_field).send_keys(utilities.userdata.password)
        print('User password entered')

    def click_login_with_email_button(self):
        self.get_element(self.login_with_email_button).click()
        print('Login with email button clicked')

    def click_phone_field(self):
        self.get_element(self.phone_field).click()
        print('Click in phone field')

    def enter_phone(self):
        self.get_element(self.phone_field).send_keys(utilities.userdata.phone_number)
        print('User phone entered')

    def click_send_code_button(self):
        self.get_element(self.send_or_confirm_code_button).click()
        print('Send code button clicked')

    def click_code_field(self):
        self.get_element(self.code_field).click()
        print('Click in code field')

    def enter_code(self):
        self.get_element(self.code_field).send_keys(utilities.userdata.permanent_code)
        print('Permanent code entered')

    def click_confirm_code_button(self):
        self.get_element(self.send_or_confirm_code_button).click()
        print('Confirm code button clicked')

    def click_profile_button(self):
        self.get_element(self.header_login_or_profile_button).click()
        print('Profile button clicked')

    # Methods
    def auth_with_email(self):
        with allure.step("Authorization with email"):
            Logger.add_start_step("auth_with_email")
            """Авторизация по паролю и е-мейлу. Нажатие на кнопку профиля/логина в хедере, нажатие на кнопку Войти по
            e-mail, ввод е-мейла и пароля, подтверждение е-мейла и пароля"""
            self.click_header_login_button()
            self.click_email_button()
            self.enter_email()
            self.enter_password()
            self.click_login_with_email_button()
            Logger.add_end_step(self.driver.current_url, "auth_with_email")

    def enter_and_confrim_code(self):
        """Авторизация по смс-коду. Клик в поле ввода смс-кода, ввод кода, подтверждение кода, проверка
        скрытия окна авторизации"""
        self.click_code_field()
        self.enter_code()
        self.click_confirm_code_button()
        self.check_visibility(self.modal_auth)

    def auth_with_phone(self):
        with allure.step("Authorization with phone"):
            Logger.add_start_step("auth_with_phone")
            """Авторизация по смс-коду для пользователя из белого списка: отключена капча и присвоен постоянный
            смс-код. Происходит открытие модального окна Вход через хедер, ввод номера телефона и нажатие на
            кнопку отправки кода. Проверяется присутствие ошибки 'Отправка СМС доступна через 60 секунд...'.
            Если ошибка есть, то через 60 секунд код отправляется еще раз и вызывается функция авторизации.
            Если ошибки нет, то функция авторизации по смс-коду вызывается сразу"""
            self.click_header_login_button()
            self.click_phone_field()
            self.enter_phone()
            self.click_send_code_button()
            self.check_visibility(self.send_code_loader)
            if self.get_error_block_len() == 0:
                self.enter_and_confrim_code()
            elif self.get_error_block_len() > 0:
                time.sleep(60)
                self.click_send_code_button()
                self.enter_and_confrim_code()
            Logger.add_end_step(self.driver.current_url, "auth_with_phone")

    def check_auth(self):
        with allure.step("Authorization check"):
            Logger.add_start_step("check_auth")
            """Нажатие на кнопку профиля в хедере, переход на страницу профиля и проверка url профиля"""
            self.click_profile_button()
            self.assert_url(utilities.common_urls.profile_url)
            print('Check user profile - login successful')
            Logger.add_end_step(self.driver.current_url, "check_auth")
