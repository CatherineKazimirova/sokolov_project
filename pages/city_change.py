from base.base_page import Base


class CityChange(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    city_button = 'div[data-tooltip-id="city-helper"]'
    city_name = 'span[class*="CitySelectButton_city"]'
    select_city_name = 'li[data-city="Санкт-Петербург"]'

    # Getters
    def get_city_name(self):
        return self.get_element(self.select_city_name).text

    # Actions
    def click_city_button(self):
        self.get_element(self.city_button).click()
        print('City button clicked')

    def click_city_name(self):
        city = self.get_city_name()
        self.get_element(self.select_city_name).click()
        print('City name clicked')
        self.check_text(self.city_name, city)
        print('Check that the city has been selected')

    # Methods
    def change_city(self):
        self.click_city_button()
        self.click_city_name()
