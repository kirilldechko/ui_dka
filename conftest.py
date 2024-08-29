from selenium import webdriver
import pytest

"""Фикстура для открытия браузера, общая в каждом тесте"""


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver
