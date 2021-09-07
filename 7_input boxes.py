from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Now we are learning:
'''
    1. How to find how many input boxes are present in the web page.
    2. How to provide value into the text box. 
    3. How to get the status.
'''

# 1. How to find how many input boxes are present in the web page.

input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')

print(len(input_boxes))

# 3. How to get the status.

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Is displayed: ", status) #True/False

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("IS enabled: ", status)

# 2. How to provide value into the text box.

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("Death")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("God")




