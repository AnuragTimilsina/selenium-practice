from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://www.facebook.com/")
driver.save_screenshot("C:\screenshot\login.png")

driver.get_screenshot_as_file("C:\screenshot\login.png")