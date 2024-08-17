from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
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

    def scroll_to_questions(self):
        element = self.driver.find_element(*self.title_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question_button(self, question_button):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(question_button))
        self.click_on_button(question_button)

    def get_text_answer(self, panel):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(panel))
        return self.driver.find_element(*panel).text
