import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from pages.locators import commoditi_page_locators as cp_loc
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    """Класс для работы со страницей экологически чистых товаров"""
    page_url = "/collections/eco-friendly.html"

    @allure.step("Переход на страницу товара")
    def go_to_commodity_page(self, commodity_name):
        search_commodity = self.find_elem(loc.commodity_path(commodity_name))
        search_commodity.click()
        self.check_elem_name_text(commodity_name, cp_loc.commodity_name_loc)

    @allure.step("Переход на вкладку товара")
    def go_on_commodity_page(self, commodity_name):
        self.find_elem(loc.commodity_path(commodity_name))

    @allure.step("Выбрать размер товара")
    def select_commodity_size(self, size, commodity_name):
        size_button = self.find_elem(loc.size_button(size, commodity_name))
        size_button.click()
        selected_size_path = loc.selected_size(size, commodity_name)
        self.check_elem_name_text(size, selected_size_path)

    @allure.step("Выбрать цвет товара")
    def change_commodity_color(self, color, commodity_name):
        color_button = self.find_elem(loc.color_button(color, commodity_name))
        color_button.click()
        selected_color_elem = self.find_elem(loc.selected_color(color, commodity_name))
        assert selected_color_elem.get_attribute('aria-label') == color

    @allure.step("Проверить количество товара в корзине")
    def add_to_cart(self, commodity_name, commodity_value):
        search_commodity = self.find_elem(loc.commodity_path(commodity_name))
        actions = ActionChains(self.driver)  # для наведения мыши на элемент инициализируем ActionChains
        actions.move_to_element(search_commodity).perform()  # наводим мышь на элемент
        find_add_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located
                                                               (loc.add_button))
        find_add_button.click()
        check_cart = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located
                                                          (loc.added_item_in_cart)).text
        assert check_cart == commodity_value
