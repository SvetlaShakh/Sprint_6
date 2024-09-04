import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    button_cookie = [By.CLASS_NAME, 'App_CookieButton__3cvqF']
    finish_button_order = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]
    header_button_order = [By.XPATH, ".//div[@class='Header_Header__214zg']//button[text()='Заказать']"]
    title_questions = [By.XPATH, ".//div[text()='Вопросы о важном']"]
    button_question_how_much = [By.XPATH, ".//div[contains(text(), 'Сколько это стоит?')]"]
    answer_panel_how_much = [By.XPATH, ".//div[contains(text(), 'Сколько это стоит?')]"
                                       "/../../div[@class='accordion__panel']/p"]
    button_question_several_scooters = [By.XPATH, ".//div[contains(text(), 'сразу несколько самокатов')]"]
    answer_panel_several_scooters = [By.XPATH, ".//div[contains(text(), 'сразу несколько самокатов')]/../../"
                                               "div[@class='accordion__panel']/p"]
    button_question_time_rent = [By.XPATH, ".//div[contains(text(), 'время аренды')]"]
    answer_panel_time_rent = [By.XPATH, ".//div[contains(text(), 'время аренды')]/../../"
                                        "div[@class='accordion__panel']/p"]
    button_question_scooter_on_today = [By.XPATH, ".//div[contains(text(), 'самокат прямо на сегодня')]"]
    answer_panel_scooter_on_today = [By.XPATH, ".//div[contains(text(), 'самокат прямо на сегодня')]/../../"
                                               "div[@class='accordion__panel']/p"]
    button_question_extend_order = [By.XPATH, ".//div[contains(text(), 'продлить заказ')]"]
    answer_panel_extend_order = [By.XPATH, ".//div[contains(text(), 'продлить заказ')]/../../"
                                           "div[@class='accordion__panel']/p"]
    button_question_scooter_charger = [By.XPATH, ".//div[contains(text(), 'зарядку вместе с самокатом')]"]
    answer_panel_scooter_charger = [By.XPATH, ".//div[contains(text(), 'зарядку вместе с самокатом')]/../../"
                                              "div[@class='accordion__panel']/p"]
    button_question_cancel_order = [By.XPATH, ".//div[contains(text(), 'отменить заказ')]"]
    answer_panel_cancel_order = [By.XPATH, ".//div[contains(text(), 'отменить заказ')]/../../"
                                           "div[@class='accordion__panel']/p"]
    button_question_beyond_mkad = [By.XPATH, ".//div[contains(text(), 'за МКАДом')]"]
    answer_panel_beyond_mkad = [By.XPATH, ".//div[contains(text(), 'за МКАДом')]/../../"
                                          "div[@class='accordion__panel']/p"]

    @allure.step('Прокрутить страницу до блока с вопросами')
    def scroll_to_questions(self):
        element_of_page = self.title_questions
        self.scroll_to_element_of_page(element_of_page)

    @allure.step('Принять куки')
    def click_on_button_cookie(self):
        self.click_on_button(self.button_cookie)

    @allure.step('Кликнуть по кнопке "Заказать"')
    def click_on_order_button(self, button):
        self.click_on_button(button)

    @allure.step('Кликнуть по полю с вопросом')
    def click_question_button(self, question_button):
        self.wait_for_visibility_of_element(question_button)
        self.click_on_button(question_button)

    @allure.step('Получить текст панели ответа')
    def get_text_answer(self, panel):
        self.wait_for_visibility_of_element(panel)
        return self.get_text_of_element(panel)

    @allure.step('Кликнуть по лого "Самокат"')
    def click_on_logo_scooter(self):
        self.click_on_button(BasePage.logo_scooter)

    @allure.step('Кликнуть по лого "Яндекс"')
    def click_on_logo_yandex(self):
        self.click_on_button(BasePage.logo_yandex)
