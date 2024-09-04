import allure
from selenium.webdriver import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import data_tests
from pages.locators import sale_page_locators as sp_loc
from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    """Класс для работы со страницей распродажи"""
    page_url = "/sale.html"

    @allure.step("Проверить название вкладки Sale")
    def check_sale_tab(self, page_name):
        self.check_elem_name_text(page_name, sp_loc.sale_tab_xpath)

    @allure.step("Проверить функцию поиска товара")
    def check_search_field(self, search_data):
        search_field = self.find_elem(sp_loc.search_field_xpath)
        search_field.send_keys(search_data)
        search_field.send_keys(Keys.ENTER)
        search_result = self.find_elem(loc.search_result_xpath)
        assert search_result.text == f"Search results for: '{search_data}'"

    @allure.step("Переход на страницу товара")
    def go_to_commodity_page(self, commodity_name):
        select_commodity = self.find_elem(loc.commodity_path)
        select_commodity.click()
        self.check_elem_name_text(commodity_name, loc.commodity_text_to_compare_path)

    @allure.step("Переход на домашнюю страницу")
    def test_home_page(self, page_title):
        search_home_button = self.find_elem(loc.home_button_xpath)
        search_home_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             (loc.home_page_title_path))
        home_page_title_text = self.driver.title
        assert home_page_title_text == page_title
