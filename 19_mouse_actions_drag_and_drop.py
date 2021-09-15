from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source = driver.find_element_by_xpath("//*[@id='box3']")
target = driver.find_element_by_xpath("//*[@id='box103']")

actions = ActionChains(driver)

actions.drag_and_drop(source, target).perform() # Drag and drop


