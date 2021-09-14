from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("table.html")

rows = len(driver.find_element_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)
print(cols)

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text()
        print(value)