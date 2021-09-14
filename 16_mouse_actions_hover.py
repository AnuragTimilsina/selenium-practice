from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usr_mgnt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
usr = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usr_mgnt).move_to_element(usr).click().perform()

driver.quit()
