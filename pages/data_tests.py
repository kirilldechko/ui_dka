from faker import Faker

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
test_email = fake.email()
password = fake.password(length=8)
page_form_name = "Create New Customer Account"
success_report_text = "Thank you for registering with Main Website Store."
page_title = "Sale"
search_data = "Tees"
search_page_title = f"Search results for: '{search_data}'"
home_page_title = "Home Page"
