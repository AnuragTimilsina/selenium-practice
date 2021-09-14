from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(3)

# driver.switch_to_alert().accept() # closes alert window using OK button

driver.switch_to_alert().dismiss() # closes alert using cancel button

time.sleep(5)

driver.close()