from selenium.webdriver.common.by import By

sale_tab_xpath = (By.XPATH, "//span[text()='Sale']")
search_field_xpath = (By.XPATH, "//input[@id ='search']")
search_result_xpath = (By.XPATH, "//span[@data-ui-id ='page-title-wrapper']")
commodity_path = (By.XPATH, "//a[contains(@href, 'tees-men.') and text()='Tees']")
commodity_text_to_compare_path = (By.XPATH, "//span [contains(@class, 'base') and text()='Tees']")
home_button_xpath = (By.XPATH, "//a[@title='Go to Home Page']")
home_page_title_path = (By.XPATH, "//title[text()='Home Page']")
