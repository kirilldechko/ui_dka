import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import commoditi_page_locators as loc


class CommodityPage(BasePage):
    page_url = "/ana-running-short.html"

    @allure.step("Проверка наименования товара на странице товара")
    def check_commodity_name(self, commodity_name):
        search_commodity_name = self.find_elem(loc.commodity_name_loc)
        print(search_commodity_name.text)
        self.check_elem_name_text(commodity_name, search_commodity_name.text)

