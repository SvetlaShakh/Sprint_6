import allure
import pytest

from selenium import webdriver
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestOrderScooter:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    order_data = [[HomePage.finish_button_order, 'Георг', 'Гофман', 'пр Мира 26', 'Проспект Мира',
                   '89998887766', 'next_month', 'трое', OrderPage.checkbox_black, 'Посадить дуб'],
                  [HomePage.header_button_order, 'МарияСофияМария', 'ИвановаПетроваИванова',
                   'улица Большая Дмитровская дом 2', 'Улица 1905 года', '+79998887766', 'tomorrow', 'сутки',
                   OrderPage.checkbox_grey, '']]

    @allure.title('Проверка флоу позитивного сценария')
    @allure.description('Заполнить форму заказа самоката, получить подтверждение о заказе, перейти на главную страницу '
                        'по клику на лого "Самокат", перейти на главную страницу Дзен по клику на лого "Яндекс"')
    @pytest.mark.parametrize('order_button, first_name, last_name, adress, subway, phone, day_order, time_to_rent, '
                             'collor, comment', order_data)
    def test_order_scooter(self, order_button, first_name, last_name, adress, subway, phone, day_order, time_to_rent,
                           collor, comment):
        self.driver.get(BasePage.url_home_page)
        home_page = HomePage(self.driver)
        home_page.click_on_button(HomePage.button_cookie)
        home_page.click_on_button(order_button)
        order_page = OrderPage(self.driver)
        order_page.send_first_name(first_name)
        order_page.send_last_name(last_name)
        order_page.send_adress(adress)
        order_page.send_subway(subway)
        order_page.send_phone(phone)
        order_page.click_on_button(OrderPage.button_further)
        order_page.send_when_to_deliver(day_order)
        order_page.send_time_to_rent(time_to_rent)
        order_page.click_on_button(collor)
        order_page.send_comment(comment)
        order_page.click_on_button(OrderPage.button_order_in_form)
        order_page.click_on_button(OrderPage.button_yes_in_form)
        text_window = self.driver.find_element(*OrderPage.text_successful_order).text
        assert 'Заказ оформлен' in text_window, f'Текст в окне - {text_window}, ожидаемый текст - Заказ оформлен'

        order_page.click_on_button(OrderPage.button_status_in_form)
        order_page.click_on_button(BasePage.logo_scooter)
        assert self.driver.current_url == BasePage.url_home_page

        order_page.click_on_button(BasePage.logo_yandex)
        self.driver.delete_all_cookies()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(BasePage.url_dzen_main))
        assert self.driver.current_url == BasePage.url_dzen_main
        self.driver.switch_to.window(self.driver.window_handles[0])

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
