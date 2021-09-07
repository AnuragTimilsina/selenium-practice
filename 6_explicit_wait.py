from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element_by_xpath("//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a/span").click()

driver.find_element_by_xpath("//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").send_keys("NYC")

time.sleep(3)

driver.find_elements_by_xpath("//*[@id='app-layer-location-field-leg1-destination-ta-dialog']/div[2]/div/div[1]/section/div/input").send_keys("SFO")

driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

# Explicit waits:
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stops-0']")))

element.click()
time.sleep(3)

driver.quit()

