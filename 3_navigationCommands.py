from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("http://www.google.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.quit()

