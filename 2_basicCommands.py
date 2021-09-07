from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) # returns the title of the page
print(driver.current_url) # returns the URL of the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

# driver.close() # Only closes the tab it opens first!!!

driver.quit() # Quits all the tabs the bot opens!!!



