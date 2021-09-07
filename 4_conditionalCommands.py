from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="geckodriver.exe")

# driver.get("https://phptravels.com/demo/")
#
# driver.find_element_by_xpath("/html/body/header/div/nav/a[6]").click()
#
# print(login)

driver.get("https://phptravels.org/index.php?rp=/login")

email = driver.find_element_by_xpath("//*[@id='inputPassword']")

print(email.is_displayed()) # Return true false based of element status
print(email.is_enabled())

pass_wd = driver.find_element_by_xpath("//*[@id='inputPassword']")
print(pass_wd.is_displayed())
print(pass_wd.is_enabled())

email.send_keys("testing@email.com")
pass_wd.send_keys("testing@123")

driver.find_element_by_xpath("//*[@id='login']").click()

"""
is_selected() method is used to verify
whether some radio buttons or checkbox is selected or not!
"""