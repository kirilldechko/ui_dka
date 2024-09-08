from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """Базовый класс для всех страниц"""
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None

    def __init__(self, driver: WebDriver):  # драйвер имеет тип WebDriver
        self.driver = driver

    def open_page(self):  # Функция для открытия страницы
        self.driver.get(f'{self.base_url}{self.page_url}')

    def find_elem(self, locator: tuple):
        return self.driver.find_element(*locator)  # функция поиска элемента по локатору

    def find_all_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)  # функция поиска элементов

    def check_elem_name_value(self, elem_name, elem_path):  # проверка данных введенных в поле
        search_fild = self.find_elem(elem_path)
        assert search_fild.get_attribute("value") == elem_name

    def check_elem_by_text(self, compare_elem_1, compare_elem_2):  # проверка данных введенных в поле
        assert compare_elem_1 == compare_elem_2

    def check_header_title(self, elem_name, elem_path):  # проверка названия страницы
        search_fild = self.find_elem(elem_path)
        assert search_fild.text == elem_name
