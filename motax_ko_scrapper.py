# CSV: "//*[@id="highcharts-0hyktyw-112"]/div[2]/ul/li[6]"

# DROP DOWN: //*[@id="highcharts-0hyktyw-112"]/svg/g[7]/g/path

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("http://smog.spatialapps.net/apps/airqualitynp/")

driver.maximize_window() #Maximize the page

element = driver.find_element_by_xpath("//*[@id="highcharts-0hyktyw-112"]/div[2]/ul/li[6]")

actions = ActionChains(driver)

actions.click(element).perform()