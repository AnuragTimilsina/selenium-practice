# WE will be doing:
# 1. Select one option
# 2. Capture options from drop down
# 3. Count how many options present

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drop_down = Select(driver.find_element_by_id("RESULT_RadioButton-9"))

# Select by visible text:
drop_down.select_by_visible_text("Morning")

# Select by index:
drop_down.select_by_index(1)

# Select by value:
drop_down.select_by_value("Radio-2")

# Count number of options
print(len(drop_down.options))

# Capture all the options and print them as optput:

all_options = drop_down.options

for option in all_options:
    print(option.text)