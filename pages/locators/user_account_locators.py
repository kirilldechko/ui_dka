from selenium.webdriver.common.by import By

success_report_elem_path = (By.XPATH, "//*[@data-bind='html: $parent.prepareMessageForHtml(message.text)']"
                                      "[contains(text(), 'Thank you for registering')]")