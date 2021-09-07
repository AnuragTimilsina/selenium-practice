from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")

#Assume opening the url takes some time
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#print(driver.title)

driver.implicitly_wait(3) # 3 seconds pause for all the driver elements!!! Can be only declared once!!!

assert "साइन इन गर्नुहोस् - Google खाताहरु" in driver.title

driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("evadrop11@gmail.com")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

driver.find_element_by_name("password").send_keys("Evadrop@1729")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

