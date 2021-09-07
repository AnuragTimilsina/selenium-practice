from selenium import webdriver

# from selenium.webdriver.common.keys import keys

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://www.google.com/")

print(driver.title) # getting the title from the page

print(driver.current_url) # returns the URL of the page

print(driver.page_source) # HTML code for the page

driver.close()