from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain.application/plain")
profile.set_preference("browser.download.manager.showWhenStarting", False)
#profile.set_preference("browser.download.dir", "D:\memes")

driver = webdriver.Firefox(executable_path="geckodriver.exe", firefox_profile=profile)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

