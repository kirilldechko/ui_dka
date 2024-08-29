import allure


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Go to commodity page")
def test_go_to_commodity_page(eco_friendly_page):
    """Переход на страницу товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page()


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Change commodity size")
def test_select_size(eco_friendly_page):
    """Изменить размер товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page()
    eco_friendly_page.change_commodity_size()


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Change commodity colore")
def test_select_color(eco_friendly_page):
    """Изменить цвет товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page()
    eco_friendly_page.change_commodity_color()


@allure.feature("Сommodity page")
@allure.story("Сommodity page")
@allure.title("Put commodity to cart")
def test_add_to_cart(eco_friendly_page):
    """Положить товар в корзину"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page()
    eco_friendly_page.change_commodity_size()
    eco_friendly_page.change_commodity_color()
    eco_friendly_page.add_to_cart()
