import random
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from pages import data_tests as dt


class CreateAccount(BasePage):  # этот класс наследуется из BasePage
    """Класс для работы со страницей регистрации нового пользователя"""
    page_url = "/customer/account/create/"

    @allure.feature("Проверить название формы регистрации")
    def check_header_title(self, text=dt.page_form_name):
        search_form_field = self.find_elem(loc.page_form_path)
        assert search_form_field.text == text

    @allure.feature("Заполнить поле 'Имя'")
    def fill_in_the_first_name_field(self, name=dt.first_name):
        search_first_name_fild = self.find_elem(loc.first_name_x_path)
        search_first_name_fild.send_keys(dt.first_name)
        assert search_first_name_fild.get_attribute("value") == name

    @allure.feature("Заполнить поле 'Фамилия'")
    def fill_in_the_last_name_field(self, second_name=dt.last_name):
        search_last_name_fild = self.find_elem(loc.last_name_x_path)
        search_last_name_fild.send_keys(dt.last_name)
        assert search_last_name_fild.get_attribute("value") == second_name

    @allure.feature("Заполнить поле 'Email'")
    def fill_in_the_email_field(self, email=dt.test_email):
        search_email_fild = self.find_elem(loc.email_field_path)
        search_email_fild.send_keys(dt.test_email)
        assert search_email_fild.get_attribute("value") == email

    @allure.feature("Заполнить поле 'Пароль'")
    def fill_in_the_password_field(self, passw_d=dt.password):
        search_pass_field = self.find_elem(loc.password_field_path)
        search_pass_field.send_keys(dt.password)
        assert search_pass_field.get_attribute("value") == passw_d

    @allure.feature("Заполнить поле 'Подтвердите пароль'")
    def fill_in_the_confirm_password_field(self, passw_d=dt.password):
        search_confirm_pass_field = self.find_elem(loc.confirm_password_field_path)
        search_confirm_pass_field.send_keys(dt.password)
        assert search_confirm_pass_field.get_attribute("value") == passw_d

    @allure.feature("Нажать кнопку 'Зарегистрироваться'")
    def click_on_registration_button(self):
        search_registration_button = self.find_elem(loc.registration_button_path)
        search_registration_button.click()

    @allure.feature("Проверить создание нового пользователя")
    def check_success_report(self):
        success_report = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                              (loc.success_report_elem_path))
        assert success_report.text == dt.success_report_text

    @allure.feature("Проверка обязательности полей формы")
    def check_required_fields(self):
        search_name_fild = self.find_elem(random.choice(loc.requirement_fields))
        assert search_name_fild.get_attribute("aria-required") == "true"
