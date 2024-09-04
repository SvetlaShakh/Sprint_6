import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    input_first_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_address = [By.XPATH, ".//input[contains(@placeholder, 'Адрес:')]"]
    input_subway = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    subway_selected_pr_mira = [By.XPATH, ".//div[text()='Проспект Мира']/parent::button"]
    subway_selected_1905 = [By.XPATH, ".//div[text()='Улица 1905 года']/parent::button"]
    input_phone = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
    input_when_to_deliver = [By.XPATH, ".//input[contains(@placeholder, 'Когда привезти самокат')]"]
    day_today = [By.XPATH, ".//div[contains(@class, 'today')]"]
    first_day_in_month = [By.XPATH, ".//div[text() = '1']"]
    last_day_in_month = [By.XPATH, ".//div[@class='react-datepicker__week'][last()]/"
                                   "div[not (contains(@class,'outside-month'))][last()]"]
    button_next_month = [By.XPATH, ".//button[text() = 'Next Month']"]
    input_time_to_rent = [By.XPATH, ".//div[contains(text(), 'Срок аренды')]"]
    checkbox_black = [By.XPATH, ".//label[@for = 'black']/input"]
    checkbox_grey = [By.XPATH, ".//label[@for = 'grey']/input"]
    input_comment = [By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]"]
    button_further = [By.XPATH, ".//button[text()='Далее']"]
    button_order_in_form = [By.XPATH, ".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']"]
    button_yes_in_form = [By.XPATH, ".//button[text()='Да']"]
    button_status_in_form = [By.XPATH, ".//button[contains(text(),'статус')]"]
    text_successful_order = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]

    @staticmethod
    def find_day_of_month(day):
        day_locator = [By.XPATH, ".//div[text() = '{}']".format(day)]
        return day_locator

    @staticmethod
    def find_station(subway):
        station_locator = [By.XPATH, ".//div[text()='{}']/parent::button".format(subway)]
        return station_locator

    @allure.step('Заполнить поле "Имя"')
    def send_first_name(self, first_name):
        element = self.input_first_name
        self.send_key_to_field(element, first_name)

    @allure.step('Заполнить поле "Фамилия"')
    def send_last_name(self, last_name):
        element = self.input_last_name
        self.send_key_to_field(element, last_name)

    @allure.step('Заполнить поле "Адрес"')
    def send_address(self, address):
        element = self.input_address
        self.send_key_to_field(element, address)

    @allure.step('Заполнить поле "Станция метро"')
    def send_subway(self, subway):
        self.click_on_button(self.input_subway)
        station = self.find_station(subway)
        self.click_on_button(station)

    @allure.step('Заполнить поле "Телефон"')
    def send_phone(self, phone):
        element = self.input_phone
        self.send_key_to_field(element, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_on_button_further(self):
        self.click_on_button(self.button_further)

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def send_when_to_deliver(self, day_order):
        self.click_on_button(self.input_when_to_deliver)
        today = self.get_text_of_element(self.day_today)
        if day_order == 'tomorrow':
            last_day_in_month = self.get_text_of_element(self.last_day_in_month)
            if int(today) == int(last_day_in_month):
                self.click_on_button(self.button_next_month)
                self.click_on_button(self.first_day_in_month)
            else:
                tomorrow = int(today) + 1
                day_tomorrow = self.find_day_of_month(tomorrow)
                self.click_on_button(day_tomorrow)
        elif day_order == 'next_month':
            self.click_on_button(self.button_next_month)
            last_day_in_month = self.get_text_of_element(self.last_day_in_month)
            if int(today) > int(last_day_in_month):
                self.click_on_button(self.last_day_in_month)
            else:
                day_number = self.find_day_of_month(today)
                self.click_on_button(day_number)

    @allure.step('Заполнить поле "Срок аренды"')
    def send_time_to_rent(self, time_to_rent):
        self.click_on_button(self.input_time_to_rent)
        self.driver.find_element(By.XPATH, ".//div[contains(text(), '{}')]".format(time_to_rent)).click()

    @allure.step('Нажать чекбокс с цветом самоката')
    def click_on_button_color(self, color):
        self.click_on_button(color)

    @allure.step('Заполнить поле "Комментарий"')
    def send_comment(self, comment):
        element = self.input_comment
        self.send_key_to_field(element, comment)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_on_button_order_in_form(self):
        self.click_on_button(OrderPage.button_order_in_form)

    @allure.step('Кликнуть на кнопку "Да"')
    def click_on_button_yes_in_form(self):
        self.click_on_button(OrderPage.button_yes_in_form)

    @allure.step('Получить название всплывающего окна')
    def get_text_of_title(self):
        return self.get_text_of_element(self.text_successful_order)

    @allure.step('Кликнуть на кнопку "Посмотреть статус"')
    def click_on_button_status_in_form(self):
        self.click_on_button(self.button_status_in_form)
