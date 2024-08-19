import allure
import pytest

from selenium import webdriver
from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.order_page import OrderPage


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
    @pytest.mark.parametrize('order_button, first_name, last_name, address, subway, phone, day_order, time_to_rent, '
                             'color, comment', order_data)
    def test_order_scooter(self, order_button, first_name, last_name, address, subway, phone, day_order, time_to_rent,
                           color, comment):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_on_button_cookie()
        home_page.click_on_order_button(order_button)
        order_page = OrderPage(self.driver)
        order_page.send_first_name(first_name)
        order_page.send_last_name(last_name)
        order_page.send_address(address)
        order_page.send_subway(subway)
        order_page.send_phone(phone)
        order_page.click_on_button_further()
        order_page.send_when_to_deliver(day_order)
        order_page.send_time_to_rent(time_to_rent)
        order_page.click_on_button_color(color)
        order_page.send_comment(comment)
        order_page.click_on_button_order_in_form()
        order_page.click_on_button_yes_in_form()
        text_window = order_page.get_text_of_title()
        assert 'Заказ оформлен' in text_window, f'Текст в окне - {text_window}, ожидаемый текст - Заказ оформлен'

        order_page.click_on_button_status_in_form()
        home_page.click_on_logo_scooter()
        current_url = home_page.get_url()
        assert current_url == BasePage.url_home_page, \
            f'Текущий URL - {current_url}, ожидаемый URL - {BasePage.url_home_page}'

        home_page.click_on_logo_yandex()
        home_page.delete_cookie()
        home_page.switch_next_window()
        home_page.wait_for_url(BasePage.url_dzen_main)
        redirect_url = home_page.get_url()
        home_page.switch_previous_window()
        assert redirect_url == BasePage.url_dzen_main

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
