import allure

from pages.base_page import BasePage
from pages.locators import commodity_page_locators as loc


class CommodityPage(BasePage):
    page_url = "/ana-running-short.html"

    @allure.step("Проверка наименования товара на странице товара")
    def check_commodity_name(self, commodity_name):
        search_commodity_name = self.find_elem(loc.commodity_name_loc)
        self.check_elem_by_text(commodity_name, search_commodity_name.text)

