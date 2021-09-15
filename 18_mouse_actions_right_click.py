from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window() #Maximize the page

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions = ActionChains(driver)

actions.context_click(button).perform() # Right click action

