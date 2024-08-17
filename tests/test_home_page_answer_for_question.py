import allure
import pytest

from selenium import webdriver
from pages.home_page import HomePage
from pages.base_page import BasePage


class TestHomePage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    question_answer = [[HomePage.button_question_how_much, HomePage.answer_panel_how_much,
                        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                       [HomePage.button_question_several_scooters, HomePage.answer_panel_several_scooters,
                        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                        'можете просто сделать несколько заказов — один за другим.'],
                       [HomePage.button_question_time_rent, HomePage.answer_panel_time_rent,
                        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                        'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                        'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                       [HomePage.button_question_scooter_on_today, HomePage.answer_panel_scooter_on_today,
                        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                       [HomePage.button_question_extend_order, HomePage.answer_panel_extend_order,
                        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                        'по красивому номеру 1010.'],
                       [HomePage.button_question_scooter_charger, HomePage.answer_panel_scooter_charger,
                        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                        'кататься без передышек и во сне. Зарядка не понадобится.'],
                       [HomePage.button_question_cancel_order, HomePage.answer_panel_cancel_order,
                        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                        'Все же свои.'],
                       [HomePage.button_question_beyond_mkad, HomePage.answer_panel_beyond_mkad,
                        'Да, обязательно. Всем самокатов! И Москве, и Московской области.']]

    @allure.title('Проверка блока "Вопросы о важном" на главной старице')
    @allure.description('Проверка соответствия открывающегося текста ответа на вопрос из списка')
    @pytest.mark.parametrize('question_button, panel, text_in_panel', question_answer)
    def test_click_on_button_text_answer_panel(self, question_button, panel, text_in_panel):
        self.driver.get(BasePage.url_home_page)
        home_page = HomePage(self.driver)
        home_page.click_on_button(HomePage.button_cookie)
        home_page.scroll_to_questions()
        home_page.click_question_button(question_button)
        text_answer = home_page.get_text_answer(panel)
        assert text_answer == text_in_panel
        self.driver.delete_all_cookies()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
