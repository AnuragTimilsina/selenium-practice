# We are learning:
# 1. verify selected radio buttons (isSelected())
# 2. Click operation

from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Before click: ", status)

driver.find_element_by_id("RESULT_RadioButton-7_0").click()

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("After click: ", status)

# Similar operations to check boxes

driver.find_element_by_id("RESULT_CheckBox-9_0").click()
driver.find_element_by_id("RESULT_CheckBox-9_6").click()

status = driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected()
print(status)

