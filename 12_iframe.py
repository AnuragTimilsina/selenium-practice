from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame") # First Frame
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") # Second Frame
driver.find_elements_by_link_text("WebDriver").click()

driver.switch_to.default_content() # switching back to main page from frame
