import allure


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to sale page")
def test_go_to_sale_page(sale_page):
    """Переход на страницу распродажи"""
    sale_page.open_page()
    sale_page.check_sale_tab()


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Checking search field by sale page")
def test_search_field(sale_page):
    """Поиск товара"""
    sale_page.open_page()
    sale_page.check_search_field()


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to commodity page")
def test_go_to_commodity_page(sale_page):
    """Переход на страницу товара"""
    sale_page.open_page()
    sale_page.go_to_commodity_page()


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to home page")
def test_go_to_home_page(sale_page):
    """Переход на главную страницу"""
    sale_page.open_page()
    sale_page.test_home_page()
