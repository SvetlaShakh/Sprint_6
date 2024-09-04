import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    url_home_page = 'https://qa-scooter.praktikum-services.ru/'
    url_dzen_main = 'https://dzen.ru/?yredirect=true'
    logo_scooter = [By.XPATH, ".//img[@alt = 'Scooter']/.."]
    logo_yandex = [By.XPATH, ".//img[@alt = 'Yandex']/.."]

    def __init__(self, driver):
        self.driver = driver

    def click_on_button(self, button):
        self.driver.find_element(*button).click()

    @allure.step('Открыть главную страницу "Яндекс.Самокат')
    def open_home_page(self):
        self.driver.get(self.url_home_page)

    @allure.step('Удалить куки')
    def delete_cookie(self):
        self.driver.delete_all_cookies()

    def scroll_to_element_of_page(self, element_of_page):
        element = self.driver.find_element(*element_of_page)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_visibility_of_element(self, element):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(element))

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(url))

    def send_key_to_field(self, element, key):
        self.driver.find_element(*element).send_keys(key)

    def get_text_of_element(self, element):
        return self.driver.find_element(*element).text

    @allure.step('Получить текущий URL страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step("Перейти в следуещее окно")
    def switch_next_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Перейти в предыдущее окно")
    def switch_previous_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
