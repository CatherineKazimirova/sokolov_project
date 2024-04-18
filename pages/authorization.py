from base.base_page import Base
import utilities.userdata
import utilities.common_urls

class Authorization(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    header_login_or_profile_button = 'button[data-qa="header_user_login_btn"]'
    enter_with_email_button = 'button[class*="AuthControl_auth"]'
    email_field = 'div[class*="LoginMail_email-input"] > div[class*="Input_input-group"] > input:nth-child(1)'
    password_field = 'input[type="password"]'
    login_with_email_button = 'div[class*="styles_modal-body"] > div > div > button[class*="Button_button"]'

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

    def click_profile_button(self):
        self.get_element(self.header_login_or_profile_button).click()
        print('Check user profile - login successful')

    # Methods
    def auth_from_header(self):
        self.click_header_login_button()
        self.click_email_button()
        self.enter_email()
        self.enter_password()
        self.click_login_with_email_button()
        self.click_profile_button()
        self.assert_url(utilities.common_urls.profile_url)

