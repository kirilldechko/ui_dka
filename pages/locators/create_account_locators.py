from selenium.webdriver.common.by import By

first_name_x_path = (By.XPATH, "//*[@title='First Name' and @id='firstname']")
last_name_x_path = (By.XPATH, "//*[@title='Last Name' and @id='lastname']")
page_form_path = (By.XPATH, "//*[@data-ui-id='page-title-wrapper' and text()='Create New Customer Account']")
email_field_path = (By.XPATH, "//*[@id='email_address']")
password_field_path = (By.XPATH, "//*[@id ='password']")
confirm_password_field_path = (By.XPATH, "//*[@id = 'password-confirmation']")
registration_button_path = (By.XPATH, "//*[@class='action submit primary' and @title='Create an Account']")

