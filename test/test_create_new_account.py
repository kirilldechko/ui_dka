import allure


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Check title on registration page")
def test_registration_page_name(create_account_page):
    """Тест проверки названия страницы регистрации"""
    create_account_page.open_page()
    create_account_page.check_header_title()  # по умолчанию проверка на "Create New Customer Account"


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Checking mandatory fields on a form")
def test_field_requirement(create_account_page):
    """Тест проверки обязательности полей регистрации"""
    create_account_page.open_page()
    create_account_page.check_required_fields()


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Create new customer account.")
def test_create_new_customer(create_account_page):
    """Тест регистрации нового пользователя"""
    create_account_page.open_page()
    create_account_page.fill_in_the_first_name_field()
    create_account_page.fill_in_the_last_name_field()
    create_account_page.fill_in_the_email_field()
    create_account_page.fill_in_the_password_field()
    create_account_page.fill_in_the_confirm_password_field()
    create_account_page.click_on_registration_button()
    create_account_page.check_success_report()


