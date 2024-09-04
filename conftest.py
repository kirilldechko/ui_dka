from pages.create_account import CreateAccount
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import SalePage
from selenium import webdriver
from pages.user_account_page import NewUserPage
from pages.commodity_page import CommodityPage


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


@pytest.fixture()  # инициализируем страницу распродажи
def new_user_page(driver):
    return NewUserPage(driver)


@pytest.fixture()  # инициализируем страницу товара
def commodity_page(driver):
    return CommodityPage(driver)
