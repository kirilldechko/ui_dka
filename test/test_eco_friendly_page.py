import allure
from pages.data_tests import eco_freandly_data as ef_data


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Go to commodity page")
def test_go_to_commodity_page(eco_friendly_page):
    """Переход на страницу товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page(ef_data.commodity_name)


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Select commodity size")
def test_select_size(eco_friendly_page):
    """Выбрать размер товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.select_commodity_size(ef_data.commodity_size, ef_data.commodity_name)


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Change commodity colore")
def test_select_color(eco_friendly_page):
    """Изменить цвет товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.change_commodity_color(ef_data.commodity_color, ef_data.commodity_name)


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Put commodity to cart")
def test_add_to_cart(eco_friendly_page):
    """Положить товар в корзину и проверить корзину"""
    eco_friendly_page.open_page()
    eco_friendly_page.select_commodity_size(ef_data.commodity_size, ef_data.commodity_name)
    eco_friendly_page.change_commodity_color(ef_data.commodity_color, ef_data.commodity_name)
    eco_friendly_page.go_on_commodity_page(ef_data.commodity_name)
    eco_friendly_page.add_to_cart(ef_data.commodity_name, ef_data.commodity_value)

