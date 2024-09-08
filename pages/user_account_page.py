import random
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import user_account_locators as ual


class NewUserPage(BasePage):  # этот класс наследуется из BasePage
    """Класс для работы со страницей регистрации нового пользователя"""
    page_url = "/customer/account/"

    @allure.step("Проверить сообщение о создании нового пользователя")
    def check_success_report(self, report_text):
        success_report = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                              (ual.success_report_elem_path))
        assert success_report.text == report_text
