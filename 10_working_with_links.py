from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://en.wikipedia.org/wiki/Nepal")

links = driver.find_elements(By.TAG_NAME, "a")

print("Total links: ", len(links))

# reading all links:

for link in links:
    print(link.text, "\n")

# Clicking on the link:

# driver.find_element(By.LINK_TEXT, "Nepali").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Nep").click()
