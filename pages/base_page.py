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
