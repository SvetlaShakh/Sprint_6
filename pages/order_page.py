from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):

    input_first_name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    input_last_name = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    input_adress = [By.XPATH, ".//input[contains(@placeholder, 'Адрес:')]"]
    input_subway = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    subway_selected_pr_mira = [By.XPATH, ".//div[text()='Проспект Мира']/parent::button"]
    subway_selected_1905 = [By.XPATH, ".//div[text()='Улица 1905 года']/parent::button"]
    input_phone = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
    input_when_to_deliver = [By.XPATH, ".//input[contains(@placeholder, 'Когда привезти самокат')]"]
    day_today = [By.XPATH, ".//div[contains(@class, 'today')]"]
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

    def send_first_name(self, first_name):
        self.driver.find_element(*self.input_first_name).send_keys(first_name)

    def send_last_name(self, last_name):
        self.driver.find_element(*self.input_last_name).send_keys(last_name)

    def send_adress(self, adress):
        self.driver.find_element(*self.input_adress).send_keys(adress)

    def send_subway(self, subway):
        self.click_on_button(self.input_subway)
        self.driver.find_element(By.XPATH, ".//div[text()='{}']/parent::button".format(subway)).click()

    def send_phone(self, phone):
        self.driver.find_element(*self.input_phone).send_keys(phone)

    def send_when_to_deliver(self, day_order):
        self.click_on_button(self.input_when_to_deliver)
        today = self.driver.find_element(*self.day_today).text
        if day_order == 'tomorrow':
            last_day_in_month = self.driver.find_element(*self.last_day_in_month).text
            if int(today) == int(last_day_in_month):
                self.click_on_button(self.button_next_month)
                self.driver.find_element(By.XPATH, ".//div[text() = '1']").click()
            else:
                tomorrow = int(today) + 1
                self.driver.find_element(By.XPATH, ".//div[text() = '{}']".format(tomorrow)).click()
        elif day_order == 'next_month':
            self.click_on_button(self.button_next_month)
            last_day_in_month = self.driver.find_element(*self.last_day_in_month).text
            if int(today) > int(last_day_in_month):
                self.driver.find_element(By.XPATH, ".//div[not (contains(@class,'outside-month'))][text() = '{}']"
                                         .format(last_day_in_month)).click()
            else:
                self.driver.find_element(By.XPATH, ".//div[text() = '{}']".format(today)).click()

    def send_time_to_rent(self, time_to_rent):
        self.click_on_button(self.input_time_to_rent)
        self.driver.find_element(By.XPATH, ".//div[contains(text(), '{}')]".format(time_to_rent)).click()

    def send_comment(self, comment):
        self.driver.find_element(*self.input_comment).send_keys(comment)
