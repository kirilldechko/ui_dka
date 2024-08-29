from selenium.webdriver.common.by import By

commodity_text = 'Fiona Fitness Short'
commodity_size = 28
commodity_color = 'Black'
commodity_value = 1
commodity_path = (By.XPATH, f"//div[@class='product-item-info']//a[@class='product-item-link' and contains(text(),"
                            f" '{commodity_text}')]")
add_button = (By.XPATH, "//*[@id='product-addtocart-button']")
color_button = (By.XPATH, f"//div[@class='swatch-option color' and @option-label= '{commodity_color}']")
size_button = (By.XPATH, f"//div[@class='swatch-option text' and text()='{commodity_size}']")
commodity_text_to_compare_path = (By.XPATH, f"//*[@itemprop='name' and text()='{commodity_text}']")
selected_size = (By.XPATH, f"//span[@class='swatch-attribute-selected-option' and text()='{commodity_size}']")
selected_color = (By.XPATH, f"//span[@class='swatch-attribute-selected-option' and text()='{commodity_color}']")
added_item_in_cart = (By.XPATH, f"//span[@class='counter-number' and text()='{commodity_value}']")
