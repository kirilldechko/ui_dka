from time import sleep

import allure
from selenium.webdriver import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import data_tests

import pages.data_tests
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    """Класс для работы со страницей распродажи"""
    page_url = "/sale.html"

    @allure.feature("Проверить название вкладки Sale")
    def check_sale_tab(self):
        search_tab = self.find_elem(loc.sale_tab_xpath)
        assert search_tab.text == data_tests.page_title

    @allure.feature("Проверить функцию поиска товара")
    def check_search_field(self):
        search_field = self.find_elem(loc.search_field_xpath)
        search_field.send_keys(data_tests.search_data)
        search_field.send_keys(Keys.ENTER)
        search_result = self.find_elem(loc.search_result_xpath)
        assert search_result.text == data_tests.search_page_title

    @allure.feature("Переход на страницу товара")
    def go_to_commodity_page(self):
        search_commodity = self.find_elem(loc.commodity_path)
        search_commodity.click()
        commodity_text_to_compare = self.find_elem(loc.commodity_text_to_compare_path).text
        assert commodity_text_to_compare == data_tests.search_data

    @allure.feature("Переход на домашнюю страницу")
    def test_home_page(self):
        search_home_button = self.find_elem(loc.home_button_xpath)
        search_home_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             (loc.home_page_title_path))
        home_page_title_text = self.driver.title
        assert home_page_title_text == data_tests.home_page_title
