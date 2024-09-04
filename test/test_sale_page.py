from time import sleep

import allure
from pages.data_tests import sale_page_data as sale_data
from pages.locators import sale_page_locators as sp_loc


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to sale page")
def test_sale_tab_name(sale_page):
    """Проверка названия вкладки распродажи"""
    sale_page.open_page()
    sale_page.check_sale_tab(sale_data.page_name)


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Checking search field by sale page")
def test_search_field(sale_page):
    """Проверка результата поиска товара"""
    sale_page.open_page()
    sale_page.check_search_field(sale_data.search_data)


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to commodity page")
def test_go_to_commodity_page(sale_page):
    """Переход на страницу товара"""
    sale_page.open_page()
    sale_page.go_to_commodity_page(sale_data.commodity_name)


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to home page")
def test_go_to_home_page(sale_page):
    """Переход на домашнюю страницу"""
    sale_page.open_page()
    sale_page.test_home_page(sale_data.page_title)
