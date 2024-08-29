from pages.create_account import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage
from selenium import webdriver
import pytest


@pytest.fixture()  # Фикстура для открытия браузера
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()  # инициализируем создание аккаунта и возвращаем этот объект доступным для тестов
def create_account_page(driver):
    return CreateAccount(driver)


@pytest.fixture()  # инициализируем страницу товаров
def eco_friendly_page(driver):
    return EcoFriendly(driver)


@pytest.fixture()  # инициализируем страницу распродажи
def sale_page(driver):
    return SalePage(driver)
