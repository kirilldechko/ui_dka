import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    """Класс для работы со страницей экологически чистых товаров"""
    page_url = "/collections/eco-friendly.html"

    @allure.feature("Переход на страницу товара")
    def go_to_commodity_page(self):
        search_commodity = self.find_elem(loc.commodity_path)
        search_commodity.click()
        commodity_text_to_compare = self.find_elem(loc.commodity_text_to_compare_path).text
        assert commodity_text_to_compare == loc.commodity_text

    @allure.feature("Выбрать размер товара")
    def change_commodity_size(self):
        size_button = self.find_elem(loc.size_button)
        size_button.click()
        selected_size = self.find_elem(loc.selected_size).text
        assert selected_size == str(loc.commodity_size)

    @allure.feature("Выбрать цвет товара")
    def change_commodity_color(self):
        color_button = self.find_elem(loc.color_button)
        color_button.click()
        selected_color = self.find_elem(loc.selected_color).text
        assert selected_color == loc.commodity_color

    @allure.feature("Добавить товар в корзину, проверить товар в корзине")
    def add_to_cart(self):
        find_add_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                               (loc.add_button))
        find_add_button.click()
        check_cart = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                          (loc.added_item_in_cart)).text
        assert check_cart == str(loc.commodity_value)
