from selenium.webdriver.common.by import By


class BasePage:

    url_home_page = 'https://qa-scooter.praktikum-services.ru/'
    url_dzen_main = 'https://dzen.ru/?yredirect=true'
    logo_scooter = [By.XPATH, ".//img[@alt = 'Scooter']/.."]
    logo_yandex = [By.XPATH, ".//img[@alt = 'Yandex']/.."]

    def __init__(self, driver):
        self.driver = driver

    def click_on_button(self, button):
        self.driver.find_element(*button).click()
