from base.base_page import Base


class CityChange(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    city_button = 'div[data-tooltip-id="city-helper"]'
    city_name = 'span[class*="CitySelectButton_city"]'
    desired_city = 'li[data-city="Санкт-Петербург"]'

    # Getters
    def get_city_name(self):
        """Получение названия выбираемого города из модального окна Выберите город"""
        return self.get_element(self.desired_city).text

    # Actions
    def click_city_button(self):
        self.get_element(self.city_button).click()
        print('City button clicked')

    def click_city_name(self):
        self.get_element(self.desired_city).click()
        print('City name clicked')

    # Methods
    def change_city(self):
        """Изменение города на желаемый. Нажатие на кнопку с названием города в хедере, сохранение названия
        желаемого города, выбор желаемого города, сравнение сохраненного названия с названием выбранного
        города в хедере"""
        self.click_city_button()
        city = self.get_city_name()
        self.click_city_name()
        self.check_text(self.city_name, city)
