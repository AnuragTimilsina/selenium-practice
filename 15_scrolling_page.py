from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# Scrolling by pixels
#driver.execute_script("window.scrollBy(0,10000)", "")

# Scrolling by id
flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[23]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll till the end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
